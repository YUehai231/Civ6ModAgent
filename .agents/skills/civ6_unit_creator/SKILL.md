---
name: civ6_unit_creator
description: Generate Civilization VI custom unit XML files (Gameplay, Icons, Text) and ArtDef models based on a base template unit. Trigger this skill when the user asks to create or generate a new unit that is based on or modifies an existing unit.
---

# Civ 6 Custom Unit Creator Skill

Use this skill when you need to create a new custom Civilization VI unit that borrows properties, icons, and 3D visual models from an existing template unit in the game database.

It automatically extracts attributes and metadata from official game files (`Units.xml`, `Icons_Units.xml`, `Icons_UnitPortraits.xml`, and `Units.artdef`) and generates 4 game-ready files:
1. `[Project_name]_Gameplay.xml` (Stats, combat attributes, AI tags)
2. `[Project_name]_Icons.xml` (Unit and portrait icons, including ethnic-specific portraits)
3. `[Project_name]_Text.xml` (Localized names and descriptions in English and Simplified Chinese)
4. `[Project_name].artdef` (3D model reference)

## Query Helper Script Location

* **Python Creator Script**: `d:\Civilization_VI_mod\Civ-6-Documentation-main\.agents\skills\civ6_unit_creator\scripts\create_unit.py`
* **Python Interpreter**: `D:\anaconda\python.exe`

## Game Path Configuration (.env)

The script automatically searches for a `.env` file in the workspace root, its parent directories, or the script's directory. 
To specify where your Civilization VI game is installed, create a `.env` file containing:
```env
CIV6_PATH=E:\SteamLibrary\steamapps\common\Sid Meier's Civilization VI
```
An example file `.env.example` is provided in the skill directory.

## Instructions

When the user requests to create a custom unit (e.g. `UNIT_PEON` based on `UNIT_BUILDER`), run the Python automation script.

### CLI Command Syntax
```powershell
& "D:\anaconda\python.exe" "d:\Civilization_VI_mod\Civ-6-Documentation-main\.agents\skills\civ6_unit_creator\scripts\create_unit.py" `
  -p "<ProjectName>" `
  -u "<NewUnitName>" `
  -t "<TemplateUnitName>" `
  --name-en "<EnglishName>" `
  --name-zh "<ChineseName>" `
  --desc-en "<EnglishDescription>" `
  --desc-zh "<ChineseDescription>" `
  -o "<OutputDirectory>"
```

### Options
* `-p`, `--project`: **(Required)** Project name (e.g. `QinShiHuangAlter`, `Witcher`). Used as file prefix.
* `-u`, `--unit`: **(Required)** Database ID for the new unit (e.g. `UNIT_PEON`, `UNIT_WITCHER`).
* `-t`, `--template`: **(Required)** Official unit database ID to copy properties from (e.g. `UNIT_BUILDER`, `UNIT_ARCHER`).
* `--name-en`: **(Required)** English display name.
* `--name-zh`: **(Required)** Chinese display name.
* `--desc-en`: English description text.
* `--desc-zh`: Chinese description text.
* `-o`, `--out-dir`: Output directory for generated files (defaults to `.`).
* `-g`, `--game-path`: Civ 6 base directory (looks up from `.env` or defaults to `E:\SteamLibrary\steamapps\common\Sid Meier's Civilization VI`).
* `--replaces`: If set, adds a database row making the new unit replace the template unit (civilization unique unit).
* **Attribute Overrides**:
  * `--combat <int>`: Override combat strength.
  * `--ranged-combat <int>`: Override ranged combat strength.
  * `--range <int>`: Override range.
  * `--moves <int>`: Override movement points.
  * `--cost <int>`: Override cost.
  * `--sight <int>`: Override sight range.

### Example
To generate files for a unit `UNIT_PEON` based on `UNIT_BUILDER` for project `QinShiHuangAlter` with a custom cost of 50 and moves of 3:
```powershell
& "D:\anaconda\python.exe" "d:\Civilization_VI_mod\Civ-6-Documentation-main\.agents\skills\civ6_unit_creator\scripts\create_unit.py" `
  -p "QinShiHuangAlter" `
  -u "UNIT_PEON" `
  -t "UNIT_BUILDER" `
  --name-en "Peon" `
  --name-zh "后勤兵" `
  --desc-en "A simple peon." `
  --desc-zh "一个简单的后勤兵。" `
  --cost 50 `
  --moves 3 `
  -o "D:\Civilization_VI_mod\Civ-6-Documentation-main\output"
```
This generates:
- `output/QinShiHuangAlter_Gameplay.xml`
- `output/QinShiHuangAlter_Icons.xml`
- `output/QinShiHuangAlter_Text.xml`
- `output/QinShiHuangAlter.artdef`
