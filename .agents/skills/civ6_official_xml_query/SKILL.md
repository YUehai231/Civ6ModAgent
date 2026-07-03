---
name: civ6_official_xml_query
description: Access official Civilization VI base game and DLC XML gameplay and config files for read-only queries (cannot modify or write).
---

# Civ 6 Official XML Query Skill

Use this skill when you need to inspect or search Civilization VI official XML files (from base game assets and DLCs) for gameplay tables, schema definitions, defaults, or modifiers.

> [!IMPORTANT]
> This skill is strictly **READ-ONLY**. Under no circumstances should you attempt to modify or write to the official XML gameplay files.

## Query Helper Script Location

* **Python Query Helper**: `d:\Civilization_VI_mod\Civ-6-Documentation-main\.agents\skills\civ6_official_xml_query\scripts\query_official_xml.py`
* **Python Interpreter**: `D:\anaconda\python.exe`

## Instructions

When you need to look up official definitions, statistics, XML layouts, or structure of the base game or DLC files:

### 1. Keyword Regex Search (Grep mode)
Search across all XML gameplay and configuration files:
```powershell
& "D:\anaconda\python.exe" "d:\Civilization_VI_mod\Civ-6-Documentation-main\.agents\skills\civ6_official_xml_query\scripts\query_official_xml.py" -s "MODIFIER_PLAYER_CITIES_ADJUST_RESOURCE_HARVEST_YIELD"
```

To limit searching to specific files (e.g., only files containing `Units` in their name):
```powershell
& "D:\anaconda\python.exe" "d:\Civilization_VI_mod\Civ-6-Documentation-main\.agents\skills\civ6_official_xml_query\scripts\query_official_xml.py" -s "UNIT_SETTLER" -f "*Units*"
```

### 2. XPath Element Query
Query structural elements using XPath. ElementTree supports a subset of XPath including tags, attributes, and wildcard child searches:

Find a specific UnitType Row in the XMLs:
```powershell
& "D:\anaconda\python.exe" "d:\Civilization_VI_mod\Civ-6-Documentation-main\.agents\skills\civ6_official_xml_query\scripts\query_official_xml.py" -x ".//Row[@UnitType='UNIT_SETTLER']"
```

Find all Rows under a specific table:
```powershell
& "D:\anaconda\python.exe" "d:\Civilization_VI_mod\Civ-6-Documentation-main\.agents\skills\civ6_official_xml_query\scripts\query_official_xml.py" -x "Types/Row" -f "*Units.xml"
```

### 3. List Scanned Official XML Files
Show a list of all official XML gameplay data and configuration files scanned by this tool:
```powershell
& "D:\anaconda\python.exe" "d:\Civilization_VI_mod\Civ-6-Documentation-main\.agents\skills\civ6_official_xml_query\scripts\query_official_xml.py" -l
```

### 4. Output JSON for Agent Parsing
Use the `-j` or `--json` flag to return structured JSON results instead of text:
```powershell
& "D:\anaconda\python.exe" "d:\Civilization_VI_mod\Civ-6-Documentation-main\.agents\skills\civ6_official_xml_query\scripts\query_official_xml.py" -x ".//Row[@UnitType='UNIT_SETTLER']" -j
```
