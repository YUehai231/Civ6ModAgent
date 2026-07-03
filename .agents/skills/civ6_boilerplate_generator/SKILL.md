---
name: civ6_boilerplate_generator
description: Generate Civilization VI XML database boilerplate structures for new units, leaders, civilizations, or improvements. Trigger this skill when the user asks to create, initialize, or generate a new unit, leader, civ, or building database config.
---

# Civilization VI Database Boilerplate Generator

This skill enables you to generate standard, game-ready XML database boilerplate structures for new gameplay entities like units, leaders, civilizations, and improvements.

## Files in this Skill

- **[generate_boilerplate.py](file:///d:/Civilization_VI_mod/Civ-6-Documentation-main/.agents/skills/civ6_boilerplate_generator/scripts/generate_boilerplate.py)**: Python script to output XML structures for Units, Leaders, Civilizations, and Improvements.

## Usage

You can invoke the boilerplate generator using Python on the user's system:

```bash
& "C:\Program Files\NVIDIA Corporation\Nsight Compute 2025.4.0\host\target-windows-x64\python\bin\python.exe" "d:\Civilization_VI_mod\Civ-6-Documentation-main\.agents\skills\civ6_boilerplate_generator\scripts\generate_boilerplate.py" --type <Type> --name <Name> --out-dir "/path/to/output"
```

### Options

- `--type`: **(Required)** Choice of: `Unit`, `Leader`, `Civilization`, `Improvement`.
- `--name`: **(Required)** Database ID name (e.g. `GERALT`, `WITCHER_CIV`, `SCOIA_TAEL`, `TAVERN`).
- `--out-dir`: Output directory for generated XML files (defaults to `.`).
- `--params`: Optional JSON string to override default attributes (e.g. combat strength, upgrade paths, prereqs).
- `--params-file`: Optional JSON file path to override default attributes.

### Examples of `--params` overrides

#### Custom Unit Setup:
```json
{
  "Combat": 45,
  "RangedCombat": 50,
  "Range": 2,
  "Moves": 3,
  "Cost": 120,
  "UpgradeUnit": "UNIT_CROSSBOWMAN",
  "ReplacesUnit": "UNIT_ARCHER"
}
```

#### Custom Civilization Setup:
```json
{
  "CitizenNamesMale": ["LOC_CITIZEN_GERALT", "LOC_CITIZEN_VESEMIR"],
  "CitizenNamesFemale": ["LOC_CITIZEN_YENNEFER", "LOC_CITIZEN_CIRI"]
}
```
