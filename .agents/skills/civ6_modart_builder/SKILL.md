---
name: civ6_modart_builder
description: Generate and manage Civilization VI Mod.Art.xml dependency metadata and .artdef references. Trigger this skill when the user asks to compile, build, or update mod art metadata, dependency tables, or .artdef/XLP bindings.
---

# Civilization VI ModArt & Dependency Builder

This skill enables you to compile and generate the crucial `Mod.Art.xml` configuration which Civilization VI uses to link database items with 3D art definitions, textures, and package XLPs.

## Files in this Skill

- **[build_modart.py](file:///d:/Civilization_VI_mod/Civ-6-Documentation-main/.agents/skills/civ6_modart_builder/scripts/build_modart.py)**: Python script to scan `Artdefs` and `XLPs` directories and output the asset consumer tree.

## Usage

You can invoke the ModArt builder using Python on the user's system:

```bash
& "C:\Program Files\NVIDIA Corporation\Nsight Compute 2025.4.0\host\target-windows-x64\python\bin\python.exe" "d:\Civilization_VI_mod\Civ-6-Documentation-main\.agents\skills\civ6_modart_builder\scripts\build_modart.py" --project-dir "/path/to/mod/project" --mod-name "<Name>" --mod-id "<GUID>"
```

### Options

- `--project-dir`: **(Required)** Path to mod project containing `Artdefs` and/or `XLPs` folders.
- `--mod-name`: **(Required)** The name of the mod as defined in the `.civ6proj` or `.modinfo` file.
- `--mod-id`: **(Required)** The UUID/GUID GUID key of the mod.

### What it does

The script:
1. Scans `Artdefs/` for `.artdef` files and extracts their internal `<m_TemplateName>` tags.
2. Scans `XLPs/` for `.xlp` files and extracts their `<m_ClassName>` and `<m_PackageName>` tags.
3. Automatically computes the required `loadsLibraries` dependencies for each art consumer.
4. Generates a fully formatted `Mod.Art.xml` in the root of the specified project directory.
