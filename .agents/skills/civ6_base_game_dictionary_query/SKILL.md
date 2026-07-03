---
name: civ6_base_game_dictionary_query
description: Query the official base Civilization VI gameplay database for units, buildings, technologies, civics, leaders, civilizations, and modifiers.
---

# Civ 6 Base Game Dictionary Query Skill

Use this skill when you need to find official base-game elements, statistics, modifier names, table schema columns, or database values during Civilization VI modding.

## Knowledge Base Location

* **SQLite Database**: `D:\Civilization_VI_mod\Knowledge\BaseGameplay\Civ6GameplayBase.sqlite`
* **JSON Dictionary**: `D:\Civilization_VI_mod\Knowledge\BaseGameplay\gameplay_dictionary.json`
* **CLI Query Helper**: `D:\Civilization_VI_mod\Knowledge\BaseGameplay\query_helper.py`

## Instructions

When the user asks to look up a gameplay type, modifier, building, unit, technology, civic, leader, or civilization, use the python query helper tool.

### Command syntax:
Run the helper tool using the system python interpreter (`D:\anaconda\python.exe`):

1. **Keyword Search** (searches across Units, Buildings, Technologies, Civics, Leaders, Civilizations, Modifiers, Types):
   ```powershell
   & "D:\anaconda\python.exe" "D:\Civilization_VI_mod\Knowledge\BaseGameplay\query_helper.py" -s "Keyword"
   ```

2. **Custom SQL SELECT Query** (returns a formatted ASCII table):
   ```powershell
   & "D:\anaconda\python.exe" "D:\Civilization_VI_mod\Knowledge\BaseGameplay\query_helper.py" -q "SELECT Column1, Column2 FROM TableName WHERE Condition LIMIT N"
   ```

3. **Get JSON Results** (ideal for parsing in your agent code):
   ```powershell
   & "D:\anaconda\python.exe" "D:\Civilization_VI_mod\Knowledge\BaseGameplay\query_helper.py" -q "SELECT * FROM Units WHERE UnitType = 'UNIT_SETTLER'" --json
   ```

## Example Queries

* List all columns in the Units table:
  `PRAGMA table_info('Units')`
* Find modifiers related to culture yields:
  `SELECT ModifierId, ModifierType FROM Modifiers WHERE ModifierId LIKE '%culture%' OR ModifierType LIKE '%culture%' LIMIT 10`
* Find arguments of a specific modifier:
  `SELECT Name, Value FROM ModifierArguments WHERE ModifierId = 'STANDARD_DIPLOMACY_ALERT_MODIFIER'`
