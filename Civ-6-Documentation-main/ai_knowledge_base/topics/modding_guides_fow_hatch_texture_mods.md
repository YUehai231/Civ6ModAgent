---
title: "FoW Hatch Texture Mods"
category: "Modding Guides"
summary: "See: Texture System Mods#Modding%5CTexture%20System%20Mods.  Replace %XLPCLASS% with FOWTexture."
keywords: ["hatch","texture","mods","modding","guides","artdef","xlp"]
---

# FoW Hatch Texture Mods

### Creating the Texture and adding it to the XLP

See: [Texture System Mods](#Modding%5CTexture%20System%20Mods).  Replace %XLP_CLASS% with `FOWTexture`.
See: [Add and Update Libraries in Mod Art File](#Modding%5CAdd%20and%20Update%20Libraries%20in%20Mod%20Art%20File).  Replace %LIBRARY_NAME% with `FOWTexture`

Hatch textures are typically FOWGreyscale textures, not FOW textures.

### Creating the ArtDef and Referencing the Sprites

1. - Go to File -> New -> ArtDef

- Change the **Art Definition Template** to `FOWConfig`.

### Selecting the new Hatch Textures

Hatch textures are used to hatch models and terrain in Fog of War.  They are added in a list under Default -> HatchTextures and Default -> ModelHatchTextures.

After creating adding a hatch texture to the FOWTexture XLP, you can add it to the HatchTextures collection.

### Adding the ArtDef to the Game

See: [Add and Update Consumers in Mod Art File](#Modding%5CAdd%20and%20Update%20Consumers%20in%20Mod%20Art%20File).  Replace %CONSUMER_NAME% with `FOW`

### Seeing art in the game

See: [Cooking Art Files](#Modding%5CCooking%20Art%20Files)