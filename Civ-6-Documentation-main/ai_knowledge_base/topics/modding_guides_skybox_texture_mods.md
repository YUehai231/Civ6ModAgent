---
title: "SkyBox Texture Mods"
category: "Modding Guides"
summary: "See: Texture System Mods#Modding%5CTexture%20System%20Mods.  Replace %XLPCLASS% with SkyBoxTexture."
keywords: ["skybox","texture","mods","modding","guides","artdef","xlp"]
---

# SkyBox Texture Mods

### Creating the Texture and adding it to the XLP

See: [Texture System Mods](#Modding%5CTexture%20System%20Mods).  Replace %XLP_CLASS% with `SkyBoxTexture`.
See: [Add and Update Libraries in Mod Art File](#Modding%5CAdd%20and%20Update%20Libraries%20in%20Mod%20Art%20File).  Replace %LIBRARY_NAME% with `SkyBoxTexture`

### Creating the ArtDef and Referencing the Sprites

1. - Go to File -> New -> ArtDef

- Change the **Art Definition Template** to `SkyBox`.

### Selecting the new SkyBox Textures

In the SkyBox collection, create a new element named "SkyPlane".  If there is already a "SkyPlane" element, modify its SkyBoxTexture value, setting it to the newly created SkyBox Texture.

### Adding the ArtDef to the Game

See: [Add and Update Consumers in Mod Art File](#Modding%5CAdd%20and%20Update%20Consumers%20in%20Mod%20Art%20File).  Replace %CONSUMER_NAME% with `SkyBox`

### Seeing art in the game

See: [Cooking Art Files](#Modding%5CCooking%20Art%20Files)