---
name: civ6_building_creator
description: Generate Civilization VI custom building XML files (Gameplay, Icons, Text) and ArtDef models based on a base template building. Trigger this skill when the user asks to create or generate a new building that is based on or modifies an existing building.
---

# Civ 6 Custom Building Creator Skill

Use this skill when you need to create a new custom Civilization VI building that borrows properties, icons, and 3D visual models from an existing template building in the game database.

It automatically extracts attributes and metadata from official game files (`Buildings.xml`, `Icons_Buildings.xml`, and `Buildings.artdef`) and generates 4 game-ready files:
1. `[Project_name]_Gameplay.xml` (Stats, yields, pre-requisites)
2. `[Project_name]_Icons.xml` (Icon and FOW icon definitions)
3. `[Project_name]_Text.xml` (Localized names and descriptions in English and Simplified Chinese)
4. `[Project_name].artdef` (3D model reference)

## Query Helper Script Location

* **Python Creator Script**: `d:\Civilization_VI_mod\Civ-6-Documentation-main\.agents\skills\civ6_building_creator\scripts\create_building.py`
* **Python Interpreter**: `D:\anaconda\python.exe`

## Game Path Configuration (.env)

The script automatically searches for a `.env` file in the workspace root, its parent directories, or the script's directory. 
To specify where your Civilization VI game is installed, create a `.env` file containing:
```env
CIV6_PATH=E:\SteamLibrary\steamapps\common\Sid Meier's Civilization VI
```
An example file `.env.example` is provided in the skill directory.

## Instructions

When the user requests to create a custom building (e.g. `BUILDING_MONUMENT_ALTER` based on `BUILDING_MONUMENT`), run the Python automation script.

### CLI Command Syntax
```powershell
& "D:\anaconda\python.exe" "d:\Civilization_VI_mod\Civ-6-Documentation-main\.agents\skills\civ6_building_creator\scripts\create_building.py" `
  -p "<ProjectName>" `
  -b "<NewBuildingName>" `
  -t "<TemplateBuildingName>" `
  --name-en "<EnglishName>" `
  --name-zh "<ChineseName>" `
  --desc-en "<EnglishDescription>" `
  --desc-zh "<ChineseDescription>" `
  -o "<OutputDirectory>"
```

### Options
* `-p`, `--project`: **(Required)** Project name (e.g. `QinShiHuangAlter`, `Witcher`). Used as file prefix.
* `-b`, `--building`: **(Required)** Database ID for the new building (e.g. `BUILDING_MONUMENT_ALTER`).
* `-t`, `--template`: **(Required)** Official building database ID to copy properties from (e.g. `BUILDING_MONUMENT`, `BUILDING_LIBRARY`).
* `--name-en`: **(Required)** English display name.
* `--name-zh`: **(Required)** Chinese display name.
* `--desc-en`: English description text.
* `--desc-zh`: Chinese description text.
* `-o`, `--out-dir`: Output directory for generated files (defaults to `.`).
* `-g`, `--game-path`: Civ 6 base directory (looks up from `.env` or defaults to `E:\SteamLibrary\steamapps\common\Sid Meier's Civilization VI`).
* `--replaces`: If set, adds a database row making the new building replace the template building (civilization unique building).
* **Attribute Overrides**:
  * `--cost <int>`: Override production cost.
  * `--maintenance <int>`: Override gold maintenance.
  * `--district <string>`: Override required district (e.g., `DISTRICT_CAMPUS`).
  * `--tech <string>`: Override required technology (e.g., `TECH_WRITING`).
  * `--civic <string>`: Override required civic (e.g., `CIVIC_DRAMA_POETRY`).
  * `--yields <string>`: Override yield changes (e.g., `YIELD_CULTURE:2,YIELD_SCIENCE:1`).
  * `--housing <int>`: Override housing provided.

### Example
To generate files for a building `BUILDING_MONUMENT_ALTER` based on `BUILDING_MONUMENT` for project `QinShiHuangAlter` with custom yields of 3 Culture and 1 Science, and a cost of 60:
```powershell
& "D:\anaconda\python.exe" "d:\Civilization_VI_mod\Civ-6-Documentation-main\.agents\skills\civ6_building_creator\scripts\create_building.py" `
  -p "QinShiHuangAlter" `
  -b "BUILDING_MONUMENT_ALTER" `
  -t "BUILDING_MONUMENT" `
  --name-en "Altered Monument" `
  --name-zh "改良纪念碑" `
  --desc-en "An altered monument that provides science." `
  --desc-zh "提供科技值加成的改良纪念碑。" `
  --cost 60 `
  --yields "YIELD_CULTURE:3,YIELD_SCIENCE:1" `
  -o "D:\Civilization_VI_mod\Civ-6-Documentation-main\output"
```
This generates:
- `output/QinShiHuangAlter_Gameplay.xml`
- `output/QinShiHuangAlter_Icons.xml`
- `output/QinShiHuangAlter_Text.xml`
- `output/QinShiHuangAlter.artdef`
