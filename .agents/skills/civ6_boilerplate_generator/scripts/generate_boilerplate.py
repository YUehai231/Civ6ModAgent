import os
import sys
import argparse
import json
import xml.etree.ElementTree as ET

# Indent utility for XML pretty printing
def indent(elem, level=0):
    i = "\n" + level*"    "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "    "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def build_unit(name, params):
    name = name.upper()
    if not name.startswith("UNIT_"):
        name = "UNIT_" + name

    xml_root = ET.Element("GameData")
    
    # Types
    types = ET.SubElement(xml_root, "Types")
    ET.SubElement(types, "Row", {"Type": name, "Kind": "KIND_UNIT"})
    
    # Units
    units = ET.SubElement(xml_root, "Units")
    unit_row = {
        "UnitType": name,
        "Name": f"LOC_{name}_NAME",
        "Description": f"LOC_{name}_DESCRIPTION",
        "BaseSightRange": str(params.get("BaseSightRange", 2)),
        "Combat": str(params.get("Combat", 20)),
        "RangedCombat": str(params.get("RangedCombat", 0)),
        "Range": str(params.get("Range", 0)),
        "Moves": str(params.get("Moves", 2)),
        "Cost": str(params.get("Cost", 80)),
        "Domain": params.get("Domain", "DOMAIN_LAND"),
        "FormationClass": params.get("FormationClass", "FORMATION_CLASS_LAND_COMBAT"),
        "PromotionClass": params.get("PromotionClass", "PROMOTION_CLASS_MELEE"),
        "AdvisorType": params.get("AdvisorType", "ADVISOR_MILITARY"),
        "PurchaseYield": params.get("PurchaseYield", "YIELD_GOLD")
    }
    # Prereqs if set
    if "PrereqTech" in params:
        unit_row["PrereqTech"] = params["PrereqTech"]
    if "PrereqCivic" in params:
        unit_row["PrereqCivic"] = params["PrereqCivic"]
        
    ET.SubElement(units, "Row", unit_row)
    
    # UnitUpgrades
    if "UpgradeUnit" in params:
        upgrades = ET.SubElement(xml_root, "UnitUpgrades")
        ET.SubElement(upgrades, "Row", {"Unit": name, "UpgradeUnit": params["UpgradeUnit"].upper()})
        
    # UnitReplaces
    if "ReplacesUnit" in params:
        replaces = ET.SubElement(xml_root, "UnitReplaces")
        ET.SubElement(replaces, "Row", {"CivUniqueUnitType": name, "ReplacesUnitType": params["ReplacesUnit"].upper()})
        
    # UnitAiInfos
    ai_infos = ET.SubElement(xml_root, "UnitAiInfos")
    default_ais = params.get("AiTypes", ["UNITAI_COMBAT", "UNITAI_EXPLORE"])
    for ai in default_ais:
        ET.SubElement(ai_infos, "Row", {"UnitType": name, "AiType": ai})
        
    # TypeTags
    tags = ET.SubElement(xml_root, "TypeTags")
    default_tags = params.get("Tags", ["CLASS_ALL_COMBAT_UNITS", "CLASS_MELEE"])
    for tag in default_tags:
        ET.SubElement(tags, "Row", {"Type": name, "Tag": tag})
        
    return xml_root

def build_leader(name, params):
    name = name.upper()
    if not name.startswith("LEADER_"):
        name = "LEADER_" + name
        
    xml_root = ET.Element("GameData")
    
    # Types
    types = ET.SubElement(xml_root, "Types")
    ET.SubElement(types, "Row", {"Type": name, "Kind": "KIND_LEADER"})
    
    trait_name = f"TRAIT_{name.replace('LEADER_', '')}_ABILITY"
    ET.SubElement(types, "Row", {"Type": trait_name, "Kind": "KIND_TRAIT"})
    
    # Leaders
    leaders = ET.SubElement(xml_root, "Leaders")
    ET.SubElement(leaders, "Row", {
        "LeaderType": name,
        "Name": f"LOC_{name}_NAME",
        "Description": f"LOC_{name}_DESCRIPTION",
        "InheritFrom": params.get("InheritFrom", "LEADER_DEFAULT"),
        "Sex": params.get("Sex", "Male")
    })
    
    # Traits
    traits = ET.SubElement(xml_root, "Traits")
    ET.SubElement(traits, "Row", {
        "TraitType": trait_name,
        "Name": f"LOC_{trait_name}_NAME",
        "Description": f"LOC_{trait_name}_DESCRIPTION"
    })
    
    # LeaderTraits
    leader_traits = ET.SubElement(xml_root, "LeaderTraits")
    ET.SubElement(leader_traits, "Row", {"LeaderType": name, "TraitType": trait_name})
    
    # HistoricalAgendas
    agenda = params.get("Agenda", f"AGENDA_{name.replace('LEADER_', '')}")
    agendas = ET.SubElement(xml_root, "HistoricalAgendas")
    ET.SubElement(agendas, "Row", {"LeaderType": name, "AgendaType": agenda})
    
    return xml_root

def build_civ(name, params):
    name = name.upper()
    if not name.startswith("CIVILIZATION_"):
        name = "CIVILIZATION_" + name
        
    xml_root = ET.Element("GameData")
    
    # Types
    types = ET.SubElement(xml_root, "Types")
    ET.SubElement(types, "Row", {"Type": name, "Kind": "KIND_CIVILIZATION"})
    
    trait_name = f"TRAIT_{name.replace('CIVILIZATION_', '')}_ABILITY"
    ET.SubElement(types, "Row", {"Type": trait_name, "Kind": "KIND_TRAIT"})
    
    # Civilizations
    civs = ET.SubElement(xml_root, "Civilizations")
    ET.SubElement(civs, "Row", {
        "CivilizationType": name,
        "Name": f"LOC_{name}_NAME",
        "Description": f"LOC_{name}_DESCRIPTION",
        "Adjective": f"LOC_{name}_ADJECTIVE",
        "StartingCivicCode": params.get("StartingCivicCode", "CIVIC_CODE_OF_LAWS"),
        "StartingTechCode": params.get("StartingTechCode", "TECH_AGRICULTURE"),
        "Ethnicity": params.get("Ethnicity", "ETHNICITY_EURO")
    })
    
    # Traits
    traits = ET.SubElement(xml_root, "Traits")
    ET.SubElement(traits, "Row", {
        "TraitType": trait_name,
        "Name": f"LOC_{trait_name}_NAME",
        "Description": f"LOC_{trait_name}_DESCRIPTION"
    })
    
    # CivilizationTraits
    civ_traits = ET.SubElement(xml_root, "CivilizationTraits")
    ET.SubElement(civ_traits, "Row", {"CivilizationType": name, "TraitType": trait_name})
    
    # CitizenNames
    citizens = ET.SubElement(xml_root, "CivilizationCitizenNames")
    male_names = params.get("CitizenNamesMale", ["LOC_CITIZEN_CUSTOM_MALE_1", "LOC_CITIZEN_CUSTOM_MALE_2"])
    female_names = params.get("CitizenNamesFemale", ["LOC_CITIZEN_CUSTOM_FEMALE_1", "LOC_CITIZEN_CUSTOM_FEMALE_2"])
    
    for cname in male_names:
        ET.SubElement(citizens, "Row", {"CivilizationType": name, "CitizenName": cname, "Female": "0"})
    for cname in female_names:
        ET.SubElement(citizens, "Row", {"CivilizationType": name, "CitizenName": cname, "Female": "1"})
        
    return xml_root

def build_improvement(name, params):
    name = name.upper()
    if not name.startswith("IMPROVEMENT_"):
        name = "IMPROVEMENT_" + name
        
    xml_root = ET.Element("GameData")
    
    # Types
    types = ET.SubElement(xml_root, "Types")
    ET.SubElement(types, "Row", {"Type": name, "Kind": "KIND_IMPROVEMENT"})
    
    # Improvements
    imps = ET.SubElement(xml_root, "Improvements")
    ET.SubElement(imps, "Row", {
        "ImprovementType": name,
        "Name": f"LOC_{name}_NAME",
        "Description": f"LOC_{name}_DESCRIPTION",
        "Icon": f"ICON_{name}",
        "PrereqTech": params.get("PrereqTech", "TECH_MINING"),
        "PlunderType": params.get("PlunderType", "PLUNDER_GOLD"),
        "PlunderAmount": str(params.get("PlunderAmount", 25)),
        "Buildable": "1",
        "Domain": "DOMAIN_LAND"
    })
    
    # Improvement_YieldChanges
    yields = ET.SubElement(xml_root, "Improvement_YieldChanges")
    default_yields = params.get("YieldChanges", {"YIELD_PRODUCTION": 1, "YIELD_GOLD": 1})
    for ytype, val in default_yields.items():
        ET.SubElement(yields, "Row", {"ImprovementType": name, "YieldType": ytype, "YieldChange": str(val)})
        
    return xml_root

def main():
    parser = argparse.ArgumentParser(description="Civilization VI Database Boilerplate Code Generator")
    parser.add_argument("--type", required=True, choices=["Unit", "Leader", "Civilization", "Improvement"], help="Boilerplate template type")
    parser.add_argument("--name", required=True, help="Internal Database Name (e.g. GERALT, SCOIA_TAEL)")
    parser.add_argument("--out-dir", default=".", help="Output directory for generated XML")
    parser.add_argument("--params", help="Optional JSON string of custom configuration parameters")
    parser.add_argument("--params-file", help="Optional path to a JSON configuration file")
    
    args = parser.parse_args()
    
    # Parse custom params
    params = {}
    if args.params_file:
        try:
            with open(args.params_file, "r", encoding="utf-8") as f:
                params = json.load(f)
        except Exception as e:
            print(f"Error reading params file: {e}", file=sys.stderr)
            sys.exit(1)
    elif args.params:
        try:
            params = json.loads(args.params)
        except Exception as e:
            print(f"Error parsing params JSON string: {e}", file=sys.stderr)
            sys.exit(1)
            
    # Build tree
    if args.type == "Unit":
        root = build_unit(args.name, params)
    elif args.type == "Leader":
        root = build_leader(args.name, params)
    elif args.type == "Civilization":
        root = build_civ(args.name, params)
    elif args.type == "Improvement":
        root = build_improvement(args.name, params)
    else:
        print("Invalid type specified", file=sys.stderr)
        sys.exit(1)
        
    # Output file path
    clean_name = args.name.upper().replace("UNIT_", "").replace("LEADER_", "").replace("CIVILIZATION_", "").replace("IMPROVEMENT_", "")
    out_filename = f"{args.type}_{clean_name}.xml"
    out_path = os.path.join(args.out_dir, out_filename)
    
    indent(root)
    tree = ET.ElementTree(root)
    os.makedirs(args.out_dir, exist_ok=True)
    tree.write(out_path, encoding="utf-8", xml_declaration=True)
    print(f"Successfully generated boilerplate XML: {out_path}")

if __name__ == "__main__":
    main()
