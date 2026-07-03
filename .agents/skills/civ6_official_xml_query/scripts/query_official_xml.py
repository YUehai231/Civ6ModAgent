#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Civ 6 Official XML Query Helper
This script allows read-only query of Civilization VI base game and DLC XML files
using simple text grep or XPath queries.
"""

import os
import sys
import glob
import json
import argparse
import xml.etree.ElementTree as ET
import re

# Official directories
BASE_DIR = r"E:\SteamLibrary\steamapps\common\Sid Meier's Civilization VI\Base\Assets\Gameplay\Data"
DLC_DIR = r"E:\SteamLibrary\steamapps\common\Sid Meier's Civilization VI\DLC"

def get_xml_files(base_only=False, dlc_only=False, file_filter=None):
    files = []
    
    # 1. Base Game XML Files
    if not dlc_only:
        if os.path.exists(BASE_DIR):
            for root, _, filenames in os.walk(BASE_DIR):
                for f in filenames:
                    if f.lower().endswith('.xml'):
                        files.append(os.path.join(root, f))
                        
    # 2. DLC XML Files
    if not base_only:
        if os.path.exists(DLC_DIR):
            for root, dirs, filenames in os.walk(DLC_DIR):
                # We want to scan XML files inside DLC directories
                # To keep it relevant to gameplay/config, we check if the path has 'data' or 'config'
                # or we can scan all xml files but ignore UI, ArtDefs, Text to avoid noise.
                lower_root = root.lower()
                if "artdefs" in lower_root or "ui" in lower_root or "text" in lower_root or "binaries" in lower_root:
                    continue
                for f in filenames:
                    if f.lower().endswith('.xml'):
                        files.append(os.path.join(root, f))
                        
    # Apply file filter if provided (glob style)
    if file_filter:
        filtered_files = []
        filter_pat = file_filter.lower().replace('*', '.*') + '$'
        # If it doesn't have wildcards, make it match anywhere in the file path
        if '*' not in file_filter:
            filter_pat = '.*' + re.escape(file_filter.lower()) + '.*'
        
        rx = re.compile(filter_pat)
        for f in files:
            rel_path = get_relative_path(f).lower()
            if rx.match(rel_path) or rx.match(os.path.basename(f).lower()):
                filtered_files.append(f)
        return filtered_files
        
    return files

def get_relative_path(path):
    # Try to make path relative to Civ 6 root for cleaner output
    civ6_root = r"E:\SteamLibrary\steamapps\common\Sid Meier's Civilization VI"
    if path.startswith(civ6_root):
        return os.path.relpath(path, civ6_root)
    return path

def run_grep_search(files, pattern, case_sensitive=False, format_json=False):
    results = []
    flags = 0 if case_sensitive else re.IGNORECASE
    try:
        rx = re.compile(pattern, flags)
    except Exception as e:
        print(f"Error: Invalid regular expression pattern: {e}", file=sys.stderr)
        sys.exit(1)
        
    for filepath in files:
        try:
            with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
                for line_idx, line in enumerate(f, 1):
                    if rx.search(line):
                        clean_line = line.strip()
                        rel_path = get_relative_path(filepath)
                        results.append({
                            "file": rel_path,
                            "line": line_idx,
                            "content": clean_line
                        })
        except Exception as e:
            # Skip unreadable files silently, or print if not json
            if not format_json:
                print(f"Warning: Could not read {filepath}: {e}", file=sys.stderr)
                
    if format_json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        if not results:
            print("No matches found.")
            return
        for r in results:
            print(f"[{r['file']}:{r['line']}] {r['content']}")

def run_xpath_search(files, xpath_expr, format_json=False):
    results = []
    
    # Pre-compile the XPath if possible, but ElementTree does it on the fly.
    # Note: ElementTree's xpath support requires relative queries or // queries.
    # If the user queries absolute paths starting with /, we strip it to make it relative.
    if xpath_expr.startswith('/'):
        # For ElementTree, we don't have absolute xpath /GameInfo/Types/Row.
        # We can rewrite /GameInfo/Types/Row to GameInfo/Types/Row or .//Types/Row.
        # Let's adjust xpath expression slightly if it starts with '/'
        clean_xpath = xpath_expr.lstrip('/')
    else:
        clean_xpath = xpath_expr
        
    for filepath in files:
        try:
            tree = ET.parse(filepath)
            root = tree.getroot()
            
            # ElementTree search starts from the root element.
            # If xpath is simple like 'Types/Row', it matches from root.
            # If xpath is './/Row', it matches anywhere.
            # Let's handle different cases:
            matches = []
            
            # First, check if root matches the query tag (if query is just the root tag name)
            if root.tag == clean_xpath or clean_xpath == '.':
                matches.append(root)
            else:
                matches = root.findall(clean_xpath)
                
            for elem in matches:
                # Get elements relative path within XML if possible
                # Represent element as string
                elem_str = ET.tostring(elem, encoding='utf-8').decode('utf-8').strip()
                # Truncate very long elements for text output to avoid bloat
                if not format_json and len(elem_str) > 500:
                    elem_str = elem_str[:500] + "... (truncated)"
                    
                rel_path = get_relative_path(filepath)
                results.append({
                    "file": rel_path,
                    "tag": elem.tag,
                    "attrib": elem.attrib,
                    "text": elem.text.strip() if elem.text else "",
                    "xml": ET.tostring(elem, encoding='utf-8').decode('utf-8').strip()
                })
        except ET.ParseError:
            # Skip invalid XML files silently (some config files might not be standard XML)
            pass
        except Exception as e:
            if not format_json:
                print(f"Warning: Error parsing {filepath}: {e}", file=sys.stderr)
                
    if format_json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        if not results:
            print("No matches found.")
            return
        
        # Group by file for clean display
        by_file = {}
        for r in results:
            by_file.setdefault(r["file"], []).append(r["xml"])
            
        for filepath, xmls in by_file.items():
            print(f"\n=== Matches in {filepath} ===")
            for x in xmls:
                # Indent xml lines for readability
                indented = "\n".join("  " + line for line in x.splitlines())
                print(indented)

def list_files(files, format_json=False):
    results = [get_relative_path(f) for f in files]
    if format_json:
        print(json.dumps(results, indent=2))
    else:
        print(f"Found {len(results)} official XML gameplay/config files:")
        for r in sorted(results):
            print(f" - {r}")

def main():
    parser = argparse.ArgumentParser(description="Query Civ 6 official XML gameplay and DLC files.")
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-s", "--search", help="Perform regex search in XML file contents (grep mode).")
    group.add_argument("-x", "--xpath", help="Perform XPath search (e.g. './/Row[@UnitType=\"UNIT_SETTLER\"]' or 'Types/Row').")
    group.add_argument("-l", "--list", action="store_true", help="List all official XML files being scanned.")
    
    parser.add_argument("-f", "--file", help="Glob pattern to filter XML files by name (e.g. '*Units*' or 'Expansion1*').")
    parser.add_argument("-j", "--json", action="store_true", help="Format output as JSON.")
    parser.add_argument("-c", "--case-sensitive", action="store_true", help="Make grep search case-sensitive.")
    
    group_scope = parser.add_mutually_exclusive_group()
    group_scope.add_argument("--base-only", action="store_true", help="Search only in base game gameplay assets.")
    group_scope.add_argument("--dlc-only", action="store_true", help="Search only in DLC assets.")
    
    args = parser.parse_args()
    
    files = get_xml_files(base_only=args.base_only, dlc_only=args.dlc_only, file_filter=args.file)
    
    if args.list:
        list_files(files, format_json=args.json)
    elif args.search:
        run_grep_search(files, args.search, case_sensitive=args.case_sensitive, format_json=args.json)
    elif args.xpath:
        run_xpath_search(files, args.xpath, format_json=args.json)

if __name__ == "__main__":
    main()
