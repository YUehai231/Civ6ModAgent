---
name: civ6_localization_manager
description: Scan project XML/SQL files and synchronize localized text tags (LOC_). Trigger this skill when the user asks to manage, update, extract, or translate text, descriptions, and labels inside a mod.
---

# Civilization VI Localized Text Manager

This skill scans the project workspace XML and SQL database files, automatically extracts all localized text keys starting with `LOC_`, and synchronizes them with the project's translation catalog.

## Files in this Skill

- **[manage_localization.py](file:///d:/Civilization_VI_mod/Civ-6-Documentation-main/.agents/skills/civ6_localization_manager/scripts/manage_localization.py)**: Python script to scan mod files, compile translation dicts, and update `LocalizedText.xml`.

## Usage

You can invoke the localization manager using Python on the user's system:

```bash
& "C:\Program Files\NVIDIA Corporation\Nsight Compute 2025.4.0\host\target-windows-x64\python\bin\python.exe" "d:\Civilization_VI_mod\Civ-6-Documentation-main\.agents\skills\civ6_localization_manager\scripts\manage_localization.py" --project-dir "/path/to/project" --language "en_US"
```

### Options

- `--project-dir`: **(Required)** Path to project directory containing XML/SQL mod files.
- `--language`: **(Default: en_US)** Language code to register new tags under (e.g. `en_US`, `zh_CN`, `ru_RU`).
- `--out-filename`: **(Default: LocalizedText.xml)** Filename for the output localized text catalog.

### Features

1. **Auto-Scanning**: Reads all database XML and SQL scripts, parsing out quoted strings starting with `LOC_`.
2. **Key Preservation**: Preserves any existing tags and their translation text already defined in `LocalizedText.xml`.
3. **Smart Guessing**: For any newly added keys, the script automatically parses the key name to guess a clean English label (e.g., `LOC_UNIT_SCOIA_TAEL_NAME` -> `Scoia Tael`).
