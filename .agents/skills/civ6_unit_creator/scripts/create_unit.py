#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Civ 6 Custom Unit Creator Automation Script
Generates Gameplay, Icons, Text, and ArtDef files for a new Unit based on a template Unit.
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

def generate_gameplay(civ6_path, project_name, unit_name, template_name, replaces, out_dir, overrides=None):
    units_xml_path = os.path.join(civ6_path, "Base", "Assets", "Gameplay", "Data", "Units.xml")
    if not os.path.exists(units_xml_path):
        print(f"Error: Game units file not found at {units_xml_path}", file=sys.stderr)
        sys.exit(1)
        
    tree = ET.parse(units_xml_path)
    root = tree.getroot()
    
    # 1. Extract template Row from <Units>
    units_table = root.find("Units")
    template_unit_row = None
    if units_table is not None:
        for row in units_table.findall("Row"):
            if row.attrib.get("UnitType") == template_name:
                template_unit_row = copy.deepcopy(row)
                break
                
    if template_unit_row is None:
        print(f"Error: Template unit {template_name} not found in Units.xml", file=sys.stderr)
        sys.exit(1)
        
    # Modify template unit row attributes
    template_unit_row.attrib["UnitType"] = unit_name
    template_unit_row.attrib["Name"] = f"LOC_{unit_name}_NAME"
    template_unit_row.attrib["Description"] = f"LOC_{unit_name}_DESCRIPTION"
    
    # Apply custom overrides
    if overrides:
        for k, v in overrides.items():
            if v is not None:
                template_unit_row.attrib[k] = str(v)
                
    # 2. Extract <UnitAiInfos>
    ai_table = root.find("UnitAiInfos")
    new_ai_rows = []
    if ai_table is not None:
        for row in ai_table.findall("Row"):
            if row.attrib.get("UnitType") == template_name:
                new_row = copy.deepcopy(row)
                new_row.attrib["UnitType"] = unit_name
                new_ai_rows.append(new_row)
                
    # 3. Extract <TypeTags>
    tags_table = root.find("TypeTags")
    new_tag_rows = []
    if tags_table is not None:
        for row in tags_table.findall("Row"):
            if row.attrib.get("Type") == template_name:
                new_row = copy.deepcopy(row)
                new_row.attrib["Type"] = unit_name
                new_tag_rows.append(new_row)
                
    # 4. Extract <UnitUpgrades>
    upgrades_table = root.find("UnitUpgrades")
    new_upgrade_rows = []
    if upgrades_table is not None:
        for row in upgrades_table.findall("Row"):
            if row.attrib.get("Unit") == template_name:
                new_row = copy.deepcopy(row)
                new_row.attrib["Unit"] = unit_name
                new_upgrade_rows.append(new_row)

    # Assemble new Gameplay XML
    new_root = ET.Element("GameInfo")
    
    # Types
    types = ET.SubElement(new_root, "Types")
    ET.SubElement(types, "Row", {"Type": unit_name, "Kind": "KIND_UNIT"})
    
    # Units
    units_sec = ET.SubElement(new_root, "Units")
    units_sec.append(template_unit_row)
    
    # UnitAiInfos
    if new_ai_rows:
        ai_sec = ET.SubElement(new_root, "UnitAiInfos")
        for row in new_ai_rows:
            ai_sec.append(row)
            
    # TypeTags
    if new_tag_rows:
        tags_sec = ET.SubElement(new_root, "TypeTags")
        for row in new_tag_rows:
            tags_sec.append(row)
            
    # UnitUpgrades
    if new_upgrade_rows:
        upgrades_sec = ET.SubElement(new_root, "UnitUpgrades")
        for row in new_upgrade_rows:
            upgrades_sec.append(row)
            
    # UnitReplaces
    if replaces:
        replaces_sec = ET.SubElement(new_root, "UnitReplaces")
        ET.SubElement(replaces_sec, "Row", {"CivUniqueUnitType": unit_name, "ReplacesUnitType": template_name})
        
    indent(new_root)
    out_path = os.path.join(out_dir, f"{project_name}_Gameplay.xml")
    new_tree = ET.ElementTree(new_root)
    new_tree.write(out_path, encoding="utf-8", xml_declaration=True)
    print(f"Generated: {out_path}")

def generate_icons(civ6_path, project_name, unit_name, template_name, out_dir):
    # Parse Icons_Units.xml
    icons_units_path = os.path.join(civ6_path, "Base", "Assets", "UI", "Icons", "Icons_Units.xml")
    unit_atlas, unit_index = "ICON_ATLAS_UNITS", "1"
    if os.path.exists(icons_units_path):
        try:
            tree = ET.parse(icons_units_path)
            root = tree.getroot()
            defs = root.find("IconDefinitions")
            if defs is not None:
                for row in defs.findall("Row"):
                    if row.attrib.get("Name") == f"ICON_{template_name}":
                        unit_atlas = row.attrib.get("Atlas")
                        unit_index = row.attrib.get("Index")
                        break
        except Exception:
            pass
            
    # Parse Icons_UnitPortraits.xml
    icons_portraits_path = os.path.join(civ6_path, "Base", "Assets", "UI", "Icons", "Icons_UnitPortraits.xml")
    portrait_atlas, portrait_index = "ICON_ATLAS_UNIT_PORTRAITS", "1"
    ethnic_portraits = {}
    ethnic_prefixes = ["ICON_ETHNICITY_ASIAN_", "ICON_ETHNICITY_MEDIT_", "ICON_ETHNICITY_SOUTHAM_", "ICON_ETHNICITY_AFRICAN_"]
    
    if os.path.exists(icons_portraits_path):
        try:
            tree = ET.parse(icons_portraits_path)
            root = tree.getroot()
            defs = root.find("IconDefinitions")
            if defs is not None:
                for row in defs.findall("Row"):
                    name = row.attrib.get("Name")
                    if name == f"ICON_{template_name}_PORTRAIT":
                        portrait_atlas = row.attrib.get("Atlas")
                        portrait_index = row.attrib.get("Index")
                    else:
                        for prefix in ethnic_prefixes:
                            if name == f"{prefix}{template_name}_PORTRAIT":
                                ethnic_portraits[prefix] = {
                                    "Atlas": row.attrib.get("Atlas"),
                                    "Index": row.attrib.get("Index")
                                }
        except Exception:
            pass

    # Build new Icons XML
    new_root = ET.Element("GameData")
    defs_sec = ET.SubElement(new_root, "IconDefinitions")
    
    # 1. Main Icon
    ET.SubElement(defs_sec, "Row", {"Name": f"ICON_{unit_name}", "Atlas": unit_atlas, "Index": unit_index})
    # 2. Main Portrait
    ET.SubElement(defs_sec, "Row", {"Name": f"ICON_{unit_name}_PORTRAIT", "Atlas": portrait_atlas, "Index": portrait_index})
    
    # 3. Ethnic Portraits
    ethnic_mapping = [
        ("ICON_ETHNICITY_ASIAN_", "ICON_ATLAS_ASIAN_UNIT_PORTRAITS"),
        ("ICON_ETHNICITY_MEDIT_", "ICON_ATLAS_MEDITERRANEAN_UNIT_PORTRAITS"),
        ("ICON_ETHNICITY_SOUTHAM_", "ICON_ATLAS_SOUTH_AMERICAN_UNIT_PORTRAITS"),
        ("ICON_ETHNICITY_AFRICAN_", "ICON_ATLAS_AFRICAN_UNIT_PORTRAITS")
    ]
    for prefix, default_atlas in ethnic_mapping:
        info = ethnic_portraits.get(prefix)
        atlas = info["Atlas"] if info else default_atlas
        idx = info["Index"] if info else portrait_index
        ET.SubElement(defs_sec, "Row", {"Name": f"{prefix}{unit_name}_PORTRAIT", "Atlas": atlas, "Index": idx})
        
    indent(new_root)
    out_path = os.path.join(out_dir, f"{project_name}_Icons.xml")
    new_tree = ET.ElementTree(new_root)
    new_tree.write(out_path, encoding="utf-8", xml_declaration=True)
    print(f"Generated: {out_path}")

def generate_text(project_name, unit_name, name_en, name_zh, desc_en, desc_zh, out_dir):
    new_root = ET.Element("GameData")
    text_sec = ET.SubElement(new_root, "LocalizedText")
    
    # Name En & Zh
    ET.SubElement(text_sec, "Row", {"Tag": f"LOC_{unit_name}_NAME", "Language": "en_US"}).append(ET.Element("Text"))
    text_sec[-1].find("Text").text = name_en
    ET.SubElement(text_sec, "Row", {"Tag": f"LOC_{unit_name}_NAME", "Language": "zh_Hans_CN"}).append(ET.Element("Text"))
    text_sec[-1].find("Text").text = name_zh
    
    # Description En & Zh
    ET.SubElement(text_sec, "Row", {"Tag": f"LOC_{unit_name}_DESCRIPTION", "Language": "en_US"}).append(ET.Element("Text"))
    text_sec[-1].find("Text").text = desc_en
    ET.SubElement(text_sec, "Row", {"Tag": f"LOC_{unit_name}_DESCRIPTION", "Language": "zh_Hans_CN"}).append(ET.Element("Text"))
    text_sec[-1].find("Text").text = desc_zh
    
    indent(new_root)
    out_path = os.path.join(out_dir, f"{project_name}_Text.xml")
    new_tree = ET.ElementTree(new_root)
    new_tree.write(out_path, encoding="utf-8", xml_declaration=True)
    print(f"Generated: {out_path}")

def generate_artdef(civ6_path, project_name, unit_name, template_name, out_dir):
    artdef_path = os.path.join(civ6_path, "Base", "ArtDefs", "Units.artdef")
    if not os.path.exists(artdef_path):
        print(f"Error: Units.artdef not found at {artdef_path}", file=sys.stderr)
        sys.exit(1)
        
    tree = ET.parse(artdef_path)
    root = tree.getroot()
    
    # Find Units collection
    units_collection = None
    root_collections = root.find("m_RootCollections")
    if root_collections is not None:
        for coll in root_collections.findall("Element"):
            coll_name = coll.find("m_CollectionName")
            if coll_name is not None and coll_name.attrib.get("text") == "Units":
                units_collection = coll
                break
                
    if units_collection is None:
        print("Error: Units collection not found in official ArtDef", file=sys.stderr)
        sys.exit(1)
        
    # Find template element
    template_element = None
    for elem in units_collection.findall("Element"):
        name_elem = elem.find("m_Name")
        if name_elem is not None and name_elem.attrib.get("text") == template_name:
            template_element = copy.deepcopy(elem)
            break
            
    if template_element is None:
        print(f"Error: Template model for {template_name} not found in Units.artdef", file=sys.stderr)
        sys.exit(1)
        
    # Get fields and child collections
    copied_fields = template_element.find("m_Fields")
    copied_child_colls = template_element.find("m_ChildCollections")
    
    # Assemble the new ArtDef tree
    new_root = ET.Element("AssetObjects..ArtDefSet")
    
    m_version = ET.SubElement(new_root, "m_Version")
    ET.SubElement(m_version, "major").text = "4"
    ET.SubElement(m_version, "minor").text = "0"
    ET.SubElement(m_version, "build").text = "253"
    ET.SubElement(m_version, "revision").text = "293"
    
    ET.SubElement(new_root, "m_TemplateName", {"text": "Units"})
    
    new_root_colls = ET.SubElement(new_root, "m_RootCollections")
    
    # Units collection
    new_units_coll = ET.SubElement(new_root_colls, "Element")
    ET.SubElement(new_units_coll, "m_CollectionName", {"text": "Units"})
    ET.SubElement(new_units_coll, "m_ReplaceMergedCollectionElements").text = "false"
    
    # New Unit element
    new_unit_elem = ET.SubElement(new_units_coll, "Element")
    new_unit_elem.append(copied_fields)
    new_unit_elem.append(copied_child_colls)
    ET.SubElement(new_unit_elem, "m_Name", {"text": unit_name})
    ET.SubElement(new_unit_elem, "m_AppendMergedParameterCollections").text = "false"
    
    # Empty collections
    empty_colls = [
        "UnitMovementTypes", "UnitFormationTypes", "MemberCombat", "UnitCombat",
        "CombatAttack", "UnitFormationLayoutTypes", "CombatFormation", "UnitDomainTypes",
        "UnitAttachmentBins", "UnitMemberTypes", "UnitTintTypes", "UnitGlobals"
    ]
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
    parser = argparse.ArgumentParser(description="Create custom Civ 6 Unit files based on a template Unit.")
    parser.add_argument("-p", "--project", required=True, help="Project name (e.g. QinShiHuangAlter)")
    parser.add_argument("-u", "--unit", required=True, help="Database Unit ID (e.g. UNIT_PEON)")
    parser.add_argument("-t", "--template", required=True, help="Template Unit ID (e.g. UNIT_BUILDER)")
    parser.add_argument("--name-en", required=True, help="English display name")
    parser.add_argument("--name-zh", required=True, help="Chinese display name")
    parser.add_argument("--desc-en", default="", help="English description")
    parser.add_argument("--desc-zh", default="", help="Chinese description")
    parser.add_argument("-o", "--out-dir", default=".", help="Output directory")
    parser.add_argument("-g", "--game-path", help="Civ 6 base install directory")
    parser.add_argument("--replaces", action="store_true", help="Make this unit replace the template unit")
    
    # Specific Unit attribute overrides
    parser.add_argument("--combat", type=int, help="Override combat strength")
    parser.add_argument("--ranged-combat", type=int, help="Override ranged combat strength")
    parser.add_argument("--range", type=int, help="Override range")
    parser.add_argument("--moves", type=int, help="Override movement points")
    parser.add_argument("--cost", type=int, help="Override cost")
    parser.add_argument("--sight", type=int, help="Override sight range")
    
    args = parser.parse_args()
    
    civ6_path = load_civ6_path(args.game_path)
    print(f"Civilization VI game folder path: {civ6_path}")
    
    # Normalize unit name prefix
    unit_name = args.unit.upper()
    if not unit_name.startswith("UNIT_"):
        unit_name = "UNIT_" + unit_name
        
    template_name = args.template.upper()
    if not template_name.startswith("UNIT_"):
        template_name = "UNIT_" + template_name
        
    os.makedirs(args.out_dir, exist_ok=True)
    
    overrides = {
        "Combat": args.combat,
        "RangedCombat": args.ranged_combat,
        "Range": args.range,
        "BaseMoves": args.moves,
        "Cost": args.cost,
        "BaseSightRange": args.sight
    }
    
    # Generate the 4 files
    generate_gameplay(civ6_path, args.project, unit_name, template_name, args.replaces, args.out_dir, overrides)
    generate_icons(civ6_path, args.project, unit_name, template_name, args.out_dir)
    generate_text(args.project, unit_name, args.name_en, args.name_zh, args.desc_en, args.desc_zh, args.out_dir)
    generate_artdef(civ6_path, args.project, unit_name, template_name, args.out_dir)
    
    print("\nUnit creation workflow complete! All 4 files generated successfully.")

if __name__ == "__main__":
    main()
