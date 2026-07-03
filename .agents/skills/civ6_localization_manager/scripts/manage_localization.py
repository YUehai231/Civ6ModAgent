import os
import sys
import argparse
import re
import xml.etree.ElementTree as ET

LOC_PATTERN = r'(?<=[\'"])(LOC_[a-zA-Z0-9_]+)(?=[\'"])'

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

def guess_text(tag):
    # e.g. LOC_UNIT_SCOIA_TAEL_NAME -> Unit Scoia Tael Name -> Scoia Tael
    clean = tag[4:].replace("_", " ").title()
    prefixes = ["Unit ", "Leader ", "Civ ", "Civilization ", "Building ", "Improvement ", "District ", "Trait "]
    for p in prefixes:
        if clean.startswith(p):
            clean = clean[len(p):]
    if clean.endswith(" Name"):
        clean = clean[:-5]
    elif clean.endswith(" Description"):
        clean = clean[:-12] + " Description"
    return clean

def main():
    parser = argparse.ArgumentParser(description="Civilization VI Localized Text Manager")
    parser.add_argument("--project-dir", required=True, help="Path to project directory containing mod files")
    parser.add_argument("--language", default="en_US", help="Default language code (e.g. en_US, zh_CN)")
    parser.add_argument("--out-filename", default="LocalizedText.xml", help="Filename of the localized text XML file")
    
    args = parser.parse_args()
    
    project_dir = os.path.abspath(args.project_dir)
    out_path = os.path.join(project_dir, args.out_filename)
    
    # 1. Scan files
    tags_found = set()
    for root, dirs, files in os.walk(project_dir):
        for fname in files:
            # Skip the output file itself
            if fname.lower() == args.out_filename.lower():
                continue
            
            fpath = os.path.join(root, fname)
            if fpath.endswith((".xml", ".sql")):
                try:
                    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                        for match in re.findall(LOC_PATTERN, content):
                            tags_found.add(match)
                except Exception as e:
                    print(f"Error reading {fname}: {e}", file=sys.stderr)
                    
    print(f"Scanned project and found {len(tags_found)} unique LOC_ tags.")
    
    # 2. Read existing translations
    translations = {}
    if os.path.exists(out_path):
        try:
            tree = ET.parse(out_path)
            xml_root = tree.getroot()
            localized_text = xml_root.find("LocalizedText")
            if localized_text is not None:
                for row in localized_text.findall("Row"):
                    tag = row.attrib.get("Tag")
                    lang = row.attrib.get("Language")
                    text_node = row.find("Text")
                    text_val = text_node.text if text_node is not None else ""
                    
                    if tag and lang:
                        if tag not in translations:
                            translations[tag] = {}
                        translations[tag][lang] = text_val
            print(f"Loaded {len(translations)} existing translations from {args.out_filename}")
        except Exception as e:
            print(f"Warning: Failed to parse existing {args.out_filename}: {e}", file=sys.stderr)
            
    # 3. Synchronize tags
    new_count = 0
    for tag in sorted(tags_found):
        if tag not in translations:
            translations[tag] = {}
        if args.language not in translations[tag]:
            guessed = guess_text(tag)
            translations[tag][args.language] = guessed
            new_count += 1
            
    # 4. Generate new XML
    new_root = ET.Element("GameData")
    new_loc = ET.SubElement(new_root, "LocalizedText")
    
    # Sort keys for clean output
    for tag in sorted(translations.keys()):
        for lang, val in sorted(translations[tag].items()):
            row = ET.SubElement(new_loc, "Row", {"Tag": tag, "Language": lang})
            text_node = ET.SubElement(row, "Text")
            text_node.text = val
            
    indent(new_root)
    new_tree = ET.ElementTree(new_root)
    new_tree.write(out_path, encoding="utf-8", xml_declaration=True)
    
    print(f"Sync complete: {new_count} new tags added. Total tags in localized database: {len(translations)}")
    print(f"Updated localization file: {out_path}")

if __name__ == "__main__":
    main()
