---
title: "MappingToGameCore"
category: "Content Creation Basics"
summary: "Mapping GameCore IDs to ArtDef Entries GameCore uses database IDs row numbers to reference features, resources, improvements, districts, buildings, and units.  So when the player builds something G..."
keywords: ["mappingtogamecore","content","creation","basics","artdef","xml","reference"]
---

# MappingToGameCore

Mapping GameCore IDs to ArtDef Entries

GameCore uses database IDs (row numbers) to reference features, resources, improvements, districts, buildings, and units. So when the player builds something GameCore asks the engine to draw "improvement 14." Depending on the version of the game, which DLCs, expansion packs, or mods are loaded, "improvement 14" can refer to different assets. The engine provides a **translation layer**, commonly referred to as Xref, which translates "improvement 14" into a specific ArtDef entry. A missing entry in the translation layer will cause the asset to not show up (and trigger a red data error), even if a corresponding ArtDef entry exists on the engine side.

GameCore Database IDs

The GameCore database that contains all features, resources, improvement, districts, buildings, and units is created from XML files located in //civ6/main/Civ6/game/assets/Gameplay/Data/… The XML files correspond each to an asset category:

- Buildings.xml,

- Districts.xml,

- Features.xml,

- Improvements.xml,

- Resources.xml,

- Terrains.xml, and

- Units.xml.

You should never edit these files, but by looking at the entries in the <Types> element you can see what "things" GameCore can ask for in each category. **Each of these entries must correspond to an entry in the Xref ArtDef!**

Xref ArtDefs

The engine's translation layer is implemented via ArtDef files in //civ6/main/Civ6/game/ArtDefs/… You will find an Xref ArtDef file for each one of the GameCore database XMLs:

- Buildings.artdef,

- Districts.artdef,

- Features.artdef,

- Improvements.artdef,

- Resources.artdef,

- Terrains.artdef, and

- Units.artdef.

Each of the ArtDef files contains a single collection with entries named exactly like the <Types> element entries in the GameCore XMLs. Any misspellings or missing entries will cause the engine to not find the entry GameCore requested and not render it.

An entry in the Xref ArtDef contains multiple parameters, usually Audio and StrategicView (WorldView will be added later). These parameters are names of entries in other ArtDef files - in the case of the StrategicView it's StrategicView.artdef.

**It is up to the art department to ensure that all GameCore database IDs are represented in their respective Xref ArtDef files and that the ArtDef entries are referencing valid names of type-specific ArtDef entries!**

For example, if Features.xml contains FEATURE_FLOODPLAINS, then Features.artdef must contain an entry called FEATURE_FLOODPLAINS whose StrategicView parameter references the Floodplains entry within StrategicView.artdef.