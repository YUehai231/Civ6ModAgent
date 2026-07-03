---
title: "FoW Parchment Texture Mods"
category: "Modding Guides"
summary: "See: Texture System Mods#Modding%5CTexture%20System%20Mods.  Replace %XLPCLASS% with FOWTexture."
keywords: ["parchment","texture","mods","modding","guides","artdef","xlp"]
---

# FoW Parchment Texture Mods

### Creating the Texture and adding it to the XLP

See: [Texture System Mods](#Modding%5CTexture%20System%20Mods).  Replace %XLP_CLASS% with `FOWTexture`.
See: [Add and Update Libraries in Mod Art File](#Modding%5CAdd%20and%20Update%20Libraries%20in%20Mod%20Art%20File).  Replace %LIBRARY_NAME% with `FOWTexture`

Parchments textures are typically FOW textures.

### Creating the ArtDef and Referencing the Sprites

1. - Go to File -> New -> ArtDef

- Change the **Art Definition Template** to `FOWConfig`.

### Selecting the new Parchment Textures

Parchment textures are used by the `Default` element in the `FOWConfig` ArtDef Element.  In Fog of War, separate textures are used for the mid-fog river, ocean, shallow waters,
as well as the shallow waves.  Additional textures are used for the compass lines, the full-fog parchment, and the model parchment.

### Adding the ArtDef to the Game

See: [Add and Update Consumers in Mod Art File](#Modding%5CAdd%20and%20Update%20Consumers%20in%20Mod%20Art%20File).  Replace %CONSUMER_NAME% with `FOW`

### Seeing art in the game

See: [Cooking Art Files](#Modding%5CCooking%20Art%20Files)