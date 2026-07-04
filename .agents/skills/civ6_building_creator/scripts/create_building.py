#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Civ 6 Custom Building Creator Automation Script
Generates Gameplay, Icons, Text, and ArtDef files for a new Building based on a template Building.
"""

import os
import sys
import argparse
import copy
import xml.etree.ElementTree as ET

# Indent utility for XML pretty printing
def indent(elem, level=0):
    i = "\n" + level*"    "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "    "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for sub_elem in elem:
            indent(sub_elem, level+1)
        if not sub_elem.tail or not sub_elem.tail.strip():
            sub_elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def load_civ6_path(custom_path=None):
    if custom_path:
        return custom_path
    # Try loading from .env in standard locations
    for env_path in ['.env', '../.env', '../../.env']:
        if os.path.exists(env_path):
            try:
                with open(env_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        if '=' in line:
                            k, v = line.strip().split('=', 1)
                            if k.strip() in ['CIV6_PATH', 'CIV6_DIR', 'GAME_PATH']:
                                return v.strip().strip('"').strip("'")
            except Exception:
                pass
    # Fallback to verified default path
    return r"E:\SteamLibrary\steamapps\common\Sid Meier's Civilization VI"

def parse_yields(yields_str):
    # Parses string like "YIELD_CULTURE:2,YIELD_SCIENCE:1"
    yields = {}
    if not yields_str:
        return yields
    for item in yields_str.split(','):
        if ':' in item:
            k, v = item.split(':', 1)
            try:
                yields[k.strip().upper()] = int(v.strip())
            except ValueError:
                pass
    return yields

def generate_gameplay(civ6_path, project_name, building_name, template_name, replaces, out_dir, overrides=None, custom_yields=None):
    buildings_xml_path = os.path.join(civ6_path, "Base", "Assets", "Gameplay", "Data", "Buildings.xml")
    if not os.path.exists(buildings_xml_path):
        print(f"Error: Game buildings file not found at {buildings_xml_path}", file=sys.stderr)
        sys.exit(1)
        
    tree = ET.parse(buildings_xml_path)
    root = tree.getroot()
    
    # 1. Extract template Row from <Buildings>
    buildings_table = root.find("Buildings")
    template_row = None
    if buildings_table is not None:
        for row in buildings_table.findall("Row"):
            if row.attrib.get("BuildingType") == template_name:
                template_row = copy.deepcopy(row)
                break
                
    if template_row is None:
        print(f"Error: Template building {template_name} not found in Buildings.xml", file=sys.stderr)
        sys.exit(1)
        
    # Modify template building row attributes
    template_row.attrib["BuildingType"] = building_name
    template_row.attrib["Name"] = f"LOC_{building_name}_NAME"
    template_row.attrib["Description"] = f"LOC_{building_name}_DESCRIPTION"
    
    # Apply custom overrides
    if overrides:
        for k, v in overrides.items():
            if v is not None:
                template_row.attrib[k] = str(v)
                
    # 2. Extract <Building_YieldChanges>
    yields_table = root.find("Building_YieldChanges")
    new_yield_rows = []
    
    if custom_yields:
        # Generate custom yields
        for ytype, val in custom_yields.items():
            new_row = ET.Element("Row", {
                "BuildingType": building_name,
                "YieldType": ytype,
                "YieldChange": str(val)
            })
            new_yield_rows.append(new_row)
    else:
        # Copy from template
        if yields_table is not None:
            for row in yields_table.findall("Row"):
                if row.attrib.get("BuildingType") == template_name:
                    new_row = copy.deepcopy(row)
                    new_row.attrib["BuildingType"] = building_name
                    new_yield_rows.append(new_row)
                    
    # 3. Extract <BuildingModifiers>
    modifiers_table = root.find("BuildingModifiers")
    new_modifier_rows = []
    if modifiers_table is not None:
        for row in modifiers_table.findall("Row"):
            if row.attrib.get("BuildingType") == template_name:
                new_row = copy.deepcopy(row)
                new_row.attrib["BuildingType"] = building_name
                new_modifier_rows.append(new_row)

    # 4. Extract other building-related tables dynamically (e.g. Building_GreatPersonPoints)
    dynamic_tables = {}
    for child in root:
        table_name = child.tag
        if table_name in ["Types", "Buildings", "BuildingModifiers", "Building_YieldChanges"]:
            continue
            
        rows_to_copy = []
        for row in child.findall("Row"):
            if row.attrib.get("BuildingType") == template_name:
                new_row = copy.deepcopy(row)
                new_row.attrib["BuildingType"] = building_name
                rows_to_copy.append(new_row)
                
        if rows_to_copy:
            dynamic_tables[table_name] = rows_to_copy

    # Assemble new Gameplay XML
    new_root = ET.Element("GameInfo")
    
    # Types
    types = ET.SubElement(new_root, "Types")
    ET.SubElement(types, "Row", {"Type": building_name, "Kind": "KIND_BUILDING"})
    
    # Buildings
    buildings_sec = ET.SubElement(new_root, "Buildings")
    buildings_sec.append(template_row)
    
    # Building_YieldChanges
    if new_yield_rows:
        yields_sec = ET.SubElement(new_root, "Building_YieldChanges")
        for row in new_yield_rows:
            yields_sec.append(row)
            
    # BuildingModifiers
    if new_modifier_rows:
        modifiers_sec = ET.SubElement(new_root, "BuildingModifiers")
        for row in new_modifier_rows:
            modifiers_sec.append(row)
            
    # BuildingReplaces
    if replaces:
        replaces_sec = ET.SubElement(new_root, "BuildingReplaces")
        ET.SubElement(replaces_sec, "Row", {"CivUniqueBuildingType": building_name, "ReplacesBuildingType": template_name})
            
    # Dynamic tables (e.g. Building_GreatPersonPoints)
    for table_name, rows in dynamic_tables.items():
        sec = ET.SubElement(new_root, table_name)
        for row in rows:
            sec.append(row)
            
    indent(new_root)
    out_path = os.path.join(out_dir, f"{project_name}_Gameplay.xml")
    new_tree = ET.ElementTree(new_root)
    new_tree.write(out_path, encoding="utf-8", xml_declaration=True)
    print(f"Generated: {out_path}")

def generate_icons(civ6_path, project_name, building_name, template_name, out_dir):
    # Parse Icons_Buildings.xml
    icons_path = os.path.join(civ6_path, "Base", "Assets", "UI", "Icons", "Icons_Buildings.xml")
    building_atlas, building_index = "ICON_ATLAS_BUILDINGS", "0"
    fow_atlas, fow_index = "ICON_ATLAS_BUILDINGS_FOW", "0"
    
    if os.path.exists(icons_path):
        try:
            tree = ET.parse(icons_path)
            root = tree.getroot()
            defs = root.find("IconDefinitions")
            if defs is not None:
                for row in defs.findall("Row"):
                    name = row.attrib.get("Name")
                    if name == f"ICON_{template_name}":
                        building_atlas = row.attrib.get("Atlas")
                        building_index = row.attrib.get("Index")
                    elif name == f"ICON_{template_name}_FOW":
                        fow_atlas = row.attrib.get("Atlas")
                        fow_index = row.attrib.get("Index")
        except Exception:
            pass

    # Build new Icons XML
    new_root = ET.Element("GameData")
    defs_sec = ET.SubElement(new_root, "IconDefinitions")
    
    # Regular Icon
    ET.SubElement(defs_sec, "Row", {"Name": f"ICON_{building_name}", "Atlas": building_atlas, "Index": building_index})
    # FOW Icon
    ET.SubElement(defs_sec, "Row", {"Name": f"ICON_{building_name}_FOW", "Atlas": fow_atlas, "Index": fow_index})
        
    indent(new_root)
    out_path = os.path.join(out_dir, f"{project_name}_Icons.xml")
    new_tree = ET.ElementTree(new_root)
    new_tree.write(out_path, encoding="utf-8", xml_declaration=True)
    print(f"Generated: {out_path}")

def generate_text(project_name, building_name, name_en, name_zh, desc_en, desc_zh, out_dir):
    new_root = ET.Element("GameData")
    text_sec = ET.SubElement(new_root, "LocalizedText")
    
    # Name En & Zh
    ET.SubElement(text_sec, "Row", {"Tag": f"LOC_{building_name}_NAME", "Language": "en_US"}).append(ET.Element("Text"))
    text_sec[-1].find("Text").text = name_en
    ET.SubElement(text_sec, "Row", {"Tag": f"LOC_{building_name}_NAME", "Language": "zh_Hans_CN"}).append(ET.Element("Text"))
    text_sec[-1].find("Text").text = name_zh
    
    # Description En & Zh
    ET.SubElement(text_sec, "Row", {"Tag": f"LOC_{building_name}_DESCRIPTION", "Language": "en_US"}).append(ET.Element("Text"))
    text_sec[-1].find("Text").text = desc_en
    ET.SubElement(text_sec, "Row", {"Tag": f"LOC_{building_name}_DESCRIPTION", "Language": "zh_Hans_CN"}).append(ET.Element("Text"))
    text_sec[-1].find("Text").text = desc_zh
    
    indent(new_root)
    out_path = os.path.join(out_dir, f"{project_name}_Text.xml")
    new_tree = ET.ElementTree(new_root)
    new_tree.write(out_path, encoding="utf-8", xml_declaration=True)
    print(f"Generated: {out_path}")

def generate_artdef(civ6_path, project_name, building_name, template_name, out_dir):
    artdef_path = os.path.join(civ6_path, "Base", "ArtDefs", "Buildings.artdef")
    if not os.path.exists(artdef_path):
        print(f"Error: Buildings.artdef not found at {artdef_path}", file=sys.stderr)
        sys.exit(1)
        
    tree = ET.parse(artdef_path)
    root = tree.getroot()
    
    # Find Building collection
    building_collection = None
    root_collections = root.find("m_RootCollections")
    if root_collections is not None:
        for coll in root_collections.findall("Element"):
            coll_name = coll.find("m_CollectionName")
            if coll_name is not None and coll_name.attrib.get("text") == "Building":
                building_collection = coll
                break
                
    if building_collection is None:
        print("Error: Building collection not found in official ArtDef", file=sys.stderr)
        sys.exit(1)
        
    # Find template element
    template_element = None
    for elem in building_collection.findall("Element"):
        name_elem = elem.find("m_Name")
        if name_elem is not None and name_elem.attrib.get("text") == template_name:
            template_element = copy.deepcopy(elem)
            break
            
    if template_element is None:
        print(f"Error: Template model for {template_name} not found in Buildings.artdef", file=sys.stderr)
        sys.exit(1)
        
    # Get fields and child collections
    copied_fields = template_element.find("m_Fields")
    copied_child_colls = template_element.find("m_ChildCollections")
    
    # Assemble the new ArtDef tree
    new_root = ET.Element("AssetObjects..ArtDefSet")
    
    m_version = ET.SubElement(new_root, "m_Version")
    ET.SubElement(m_version, "major").text = "4"
    ET.SubElement(m_version, "minor").text = "0"
    ET.SubElement(m_version, "build").text = "378"
    ET.SubElement(m_version, "revision").text = "919"
    
    ET.SubElement(new_root, "m_TemplateName", {"text": "Buildings"})
    
    new_root_colls = ET.SubElement(new_root, "m_RootCollections")
    
    # Building collection
    new_building_coll = ET.SubElement(new_root_colls, "Element")
    ET.SubElement(new_building_coll, "m_CollectionName", {"text": "Building"})
    ET.SubElement(new_building_coll, "m_ReplaceMergedCollectionElements").text = "false"
    
    # New Building element
    new_building_elem = ET.SubElement(new_building_coll, "Element")
    new_building_elem.append(copied_fields)
    new_building_elem.append(copied_child_colls)
    ET.SubElement(new_building_elem, "m_Name", {"text": building_name})
    ET.SubElement(new_building_elem, "m_AppendMergedParameterCollections").text = "false"
    
    # Empty collections
    empty_colls = ["BuildStates", "BuildingChains"]
    for coll_name in empty_colls:
        coll_elem = ET.SubElement(new_root_colls, "Element")
        ET.SubElement(coll_elem, "m_CollectionName", {"text": coll_name})
        ET.SubElement(coll_elem, "m_ReplaceMergedCollectionElements").text = "false"
        
    indent(new_root)
    out_path = os.path.join(out_dir, f"{project_name}.artdef")
    new_tree = ET.ElementTree(new_root)
    new_tree.write(out_path, encoding="utf-8", xml_declaration=True)
    print(f"Generated: {out_path}")

def main():
    parser = argparse.ArgumentParser(description="Create custom Civ 6 Building files based on a template Building.")
    parser.add_argument("-p", "--project", required=True, help="Project name (e.g. QinShiHuangAlter)")
    parser.add_argument("-b", "--building", required=True, help="Database Building ID (e.g. BUILDING_MONUMENT_ALTER)")
    parser.add_argument("-t", "--template", required=True, help="Template Building ID (e.g. BUILDING_MONUMENT)")
    parser.add_argument("--name-en", required=True, help="English display name")
    parser.add_argument("--name-zh", required=True, help="Chinese display name")
    parser.add_argument("--desc-en", default="", help="English description")
    parser.add_argument("--desc-zh", default="", help="Chinese description")
    parser.add_argument("-o", "--out-dir", default=".", help="Output directory")
    parser.add_argument("-g", "--game-path", help="Civ 6 base install directory")
    
    # Specific Building attribute overrides
    parser.add_argument("--cost", type=int, help="Override cost")
    parser.add_argument("--maintenance", type=int, help="Override maintenance")
    parser.add_argument("--district", help="Override PrereqDistrict")
    parser.add_argument("--tech", help="Override PrereqTech")
    parser.add_argument("--civic", help="Override PrereqCivic")
    parser.add_argument("--yields", help="Yield changes (e.g. YIELD_CULTURE:2,YIELD_SCIENCE:1)")
    parser.add_argument("--housing", type=int, help="Override housing")
    parser.add_argument("--replaces", action="store_true", help="Make this building replace the template building")
    
    args = parser.parse_args()
    
    civ6_path = load_civ6_path(args.game_path)
    print(f"Civilization VI game folder path: {civ6_path}")
    
    # Normalize building name prefix
    building_name = args.building.upper()
    if not building_name.startswith("BUILDING_"):
        building_name = "BUILDING_" + building_name
        
    template_name = args.template.upper()
    if not template_name.startswith("BUILDING_"):
        template_name = "BUILDING_" + template_name
        
    os.makedirs(args.out_dir, exist_ok=True)
    
    overrides = {
        "Cost": args.cost,
        "Maintenance": args.maintenance,
        "PrereqDistrict": args.district,
        "PrereqTech": args.tech,
        "PrereqCivic": args.civic,
        "Housing": args.housing
    }
    
    custom_yields = parse_yields(args.yields)
    
    # Generate the 4 files
    generate_gameplay(civ6_path, args.project, building_name, template_name, args.replaces, args.out_dir, overrides, custom_yields)
    generate_icons(civ6_path, args.project, building_name, template_name, args.out_dir)
    generate_text(args.project, building_name, args.name_en, args.name_zh, args.desc_en, args.desc_zh, args.out_dir)
    generate_artdef(civ6_path, args.project, building_name, template_name, args.out_dir)
    
    print("\nBuilding creation workflow complete! All 4 files generated successfully.")

if __name__ == "__main__":
    main()
