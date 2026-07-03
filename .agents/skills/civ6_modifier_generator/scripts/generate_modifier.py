import os
import sys
import argparse
import json
import xml.etree.ElementTree as ET

# Helper to import lib_modifier_data dynamically
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.abspath(os.path.join(script_dir, "..", "resources")))

try:
    import lib_modifier_data as lib_mod
except ImportError as e:
    print(f"Error importing lib_modifier_data: {e}", file=sys.stderr)
    sys.exit(1)

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

def main():
    parser = argparse.ArgumentParser(description="Civilization VI Modifier & Requirement Generator")
    parser.add_argument("--modifier-id", required=True, help="Custom Modifier ID (e.g. MODIFIER_GERALT_COMBAT)")
    parser.add_argument("--modifier-type", required=True, help="Base ModifierType (e.g. MODIFIER_UNIT_ADJUST_COMBAT_STRENGTH)")
    parser.add_argument("--owner-type", choices=["Trait", "Building", "District", "Belief", "Policy", "Project", "Civic", "Technology", "UnitAbility"], help="Owner entity type to bind modifier to")
    parser.add_argument("--owner-id", help="Owner Entity ID (e.g. TRAIT_LEADER_GERALT_ABILITY, BUILDING_TAVERN)")
    parser.add_argument("--args", help="JSON string of modifier arguments (e.g. '{\"Amount\": 5}')")
    parser.add_argument("--subject-reqset", help="Subject Requirement Set ID to apply to this modifier")
    parser.add_argument("--owner-reqset", help="Owner Requirement Set ID to apply to this modifier")
    parser.add_argument("--out-dir", default=".", help="Output directory for generated XML")

    args = parser.parse_args()

    # Validate ModifierType
    mod_type = args.modifier_type.upper()
    if mod_type not in lib_mod.Modifiers:
        print(f"Warning: ModifierType '{mod_type}' is not recognized in the standard database. Proceeding anyway...", file=sys.stderr)
    else:
        info = lib_mod.Modifiers[mod_type]
        print(f"Validated ModifierType: {mod_type} (Collection: {info.get('CollectionType')})")

    xml_root = ET.Element("GameData")

    # Modifiers Table
    modifiers_node = ET.SubElement(xml_root, "Modifiers")
    mod_row = {
        "ModifierId": args.modifier_id.upper(),
        "ModifierType": mod_type
    }
    if args.subject_reqset:
        mod_row["SubjectRequirementSetId"] = args.subject_reqset.upper()
    if args.owner_reqset:
        mod_row["OwnerRequirementSetId"] = args.owner_reqset.upper()
    ET.SubElement(modifiers_node, "Row", mod_row)

    # ModifierArguments Table
    if args.args:
        try:
            mod_args = json.loads(args.args)
        except Exception as e:
            print(f"Error parsing args JSON string: {e}", file=sys.stderr)
            sys.exit(1)

        args_node = ET.SubElement(xml_root, "ModifierArguments")
        for arg_name, arg_val in mod_args.items():
            ET.SubElement(args_node, "Row", {
                "ModifierId": args.modifier_id.upper(),
                "Name": str(arg_name),
                "Value": str(arg_val)
            })

    # Owner Binding Table (e.g. TraitModifiers, BuildingModifiers, etc.)
    if args.owner_type and args.owner_id:
        # Match table name
        type_to_table = {
            "Trait": ("TraitModifiers", "TraitType"),
            "Building": ("BuildingModifiers", "BuildingType"),
            "District": ("DistrictModifiers", "DistrictType"),
            "Belief": ("BeliefModifiers", "BeliefType"),
            "Policy": ("PolicyModifiers", "PolicyType"),
            "Project": ("ProjectModifiers", "ProjectType"),
            "Civic": ("CivicModifiers", "CivicType"),
            "Technology": ("TechnologyModifiers", "TechnologyType"),
            "UnitAbility": ("UnitAbilityModifiers", "UnitAbilityType")
        }
        
        table_name, col_name = type_to_table[args.owner_type]
        binding_node = ET.SubElement(xml_root, table_name)
        ET.SubElement(binding_node, "Row", {
            col_name: args.owner_id.upper(),
            "ModifierId": args.modifier_id.upper()
        })

    # Save to file
    out_filename = f"Modifier_{args.modifier_id.upper()}.xml"
    out_path = os.path.join(args.out_dir, out_filename)
    
    indent(xml_root)
    tree = ET.ElementTree(xml_root)
    os.makedirs(args.out_dir, exist_ok=True)
    tree.write(out_path, encoding="utf-8", xml_declaration=True)
    print(f"Successfully generated modifier XML: {out_path}")

if __name__ == "__main__":
    main()
