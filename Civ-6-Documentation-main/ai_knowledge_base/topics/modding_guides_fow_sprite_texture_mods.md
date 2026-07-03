---
title: "FoW Sprite Texture Mods"
category: "Modding Guides"
summary: "See: Texture System Mods#Modding%5CTexture%20System%20Mods.  Replace %XLPCLASS% with FOWSprite."
keywords: ["sprite","texture","mods","modding","guides","artdef","xlp"]
---

# FoW Sprite Texture Mods

### Creating the Texture and adding it to the XLP

See: [Texture System Mods](#Modding%5CTexture%20System%20Mods).  Replace %XLP_CLASS% with `FOWSprite`.
See: [Add and Update Libraries in Mod Art File](#Modding%5CAdd%20and%20Update%20Libraries%20in%20Mod%20Art%20File).  Replace %LIBRARY_NAME% with `FOWSprite`

Sprite textures belong to the FOWSprite texture class.

### Creating the ArtDef and Referencing the Sprites

1. - Go to File -> New -> ArtDef

- Change the **Art Definition Template** to `FOWConfig`.

### Selecting the new Sprite Textures

Sprite textures are used to draw on top of the mid-fog and full-fog sections of the map.  The sea-dragons and other fantasy creatures, the wave sprites in shallow
and deep water, and the map borders are all FOWSprites.

There are four collections that accept sprite textures -> OceanWaveSets, FullFogDecoSets, ShallowWaveSets, and MapBorders.  Each of these collections have a child
element that contains a rarity and a collection of sprites.  Once your textures exist in the FOWSprite XLPs, they can be added to the appropriate Sprites collection.

### Adding the ArtDef to the Game

See: [Add and Update Consumers in Mod Art File](#Modding%5CAdd%20and%20Update%20Consumers%20in%20Mod%20Art%20File).  Replace %CONSUMER_NAME% with `FOW`

### Seeing art in the game

See: [Cooking Art Files](#Modding%5CCooking%20Art%20Files)