---
name: civ6_modifier_generator
description: Generate Civilization VI XML database modifier structures. Trigger this skill when the user asks to create or configure modifiers, modifier arguments, requirement sets, or requirements for leaders, civilizations, units, buildings, etc.
---

# Civilization VI Modifier & Requirement Generator

This skill enables you to generate standard, game-ready XML database modifier definitions and their corresponding entity attachments (e.g. `TraitModifiers`, `BuildingModifiers`) with validation.

## Files in this Skill

- **[generate_modifier.py](file:///d:/Civilization_VI_mod/Civ-6-Documentation-main/.agents/skills/civ6_modifier_generator/scripts/generate_modifier.py)**: Python script to generate XML structures for custom modifiers and arguments.
- **[lib_modifier_data.py](file:///d:/Civilization_VI_mod/Civ-6-Documentation-main/.agents/skills/civ6_modifier_generator/resources/lib_modifier_data.py)**: Dictionaries of base game modifier types, collection types, and properties used for validation.

## Usage

You can invoke the modifier generator using Python on the user's system:

```bash
& "C:\Program Files\NVIDIA Corporation\Nsight Compute 2025.4.0\host\target-windows-x64\python\bin\python.exe" "d:\Civilization_VI_mod\Civ-6-Documentation-main\.agents\skills\civ6_modifier_generator\scripts\generate_modifier.py" --modifier-id <ModifierId> --modifier-type <ModifierType> --args <ArgsJSON> --out-dir "/path/to/output"
```

### Options

- `--modifier-id`: **(Required)** Custom Modifier ID (e.g. `MODIFIER_GERALT_GOLD_BONUS`).
- `--modifier-type`: **(Required)** Base ModifierType (e.g. `MODIFIER_PLAYER_CITIES_ADJUST_CITY_YIELD_CHANGE`).
- `--args`: JSON string representing modifier arguments (e.g. `'{"YieldType": "YIELD_GOLD", "Amount": 5}'`).
- `--owner-type`: Choice of: `Trait`, `Building`, `District`, `Belief`, `Policy`, `Project`, `Civic`, `Technology`, `UnitAbility`. Adds matching binding rows.
- `--owner-id`: Owner entity database ID (e.g. `TRAIT_LEADER_GERALT_ABILITY`, `BUILDING_TAVERN`).
- `--subject-reqset`: Subject Requirement Set ID to restrict when this modifier applies.
- `--owner-reqset`: Owner Requirement Set ID to restrict who can trigger this modifier.
- `--out-dir`: Output directory for generated XML files (defaults to `.`).

### Example

To generate a modifier that grants a building a trait bonus:
```bash
& "C:\Program Files\NVIDIA Corporation\Nsight Compute 2025.4.0\host\target-windows-x64\python\bin\python.exe" "d:\Civilization_VI_mod\Civ-6-Documentation-main\.agents\skills\civ6_modifier_generator\scripts\generate_modifier.py" --modifier-id "MODIFIER_GERALT_TAVERN_PRODUCTION" --modifier-type "MODIFIER_BUILDING_YIELD_CHANGE" --owner-type "Building" --owner-id "BUILDING_TAVERN" --args '{"YieldType": "YIELD_PRODUCTION", "Amount": 2}' --out-dir "."
```
This generates `Modifier_MODIFIER_GERALT_TAVERN_PRODUCTION.xml`.
