---
title: "2D Leader Background Mods"
category: "Modding Guides"
summary: "See: Texture System Mods#Modding%5CTexture%20System%20Mods.  Replace %XLPCLASS% with LeaderFallback."
keywords: ["leader","background","mods","modding","guides","artdef","blp","xlp","animation","texture"]
---

# 2D Leader Background Mods

### Creating the Texture and adding it to the XLP

See: [Texture System Mods](#Modding%5CTexture%20System%20Mods).  Replace %XLP_CLASS% with `LeaderFallback`.
See: [Add and Update Libraries in Mod Art File](#Modding%5CAdd%20and%20Update%20Libraries%20in%20Mod%20Art%20File).  Replace %LIBRARY_NAME% with `LeaderFallback`

### Creating the ArtDef and Referencing the Texture

1. - Go to File -> New -> ArtDef

- Change the **Art Definition Template** to LeaderFallback.

- Select the **Leaders** item in the Tree, right-click, and press *Add Element*.

- Change the name of the newly created element to the name of the leader.

- Select the **Animations** item in the Tree, right-click, and press *Add Element*.

- Change the **Name** to `DEFAULT`.

- Under the **BLP Entry** column, select the field, click the dropdown, and then click the *Browse* button.

- Find the newly created entry in the XLP browser.

- Select the entry and press the *OK* button.

- Save the ArtDef.

See: [Add and Update Consumers in Mod Art File](#Modding%5CAdd%20and%20Update%20Consumers%20in%20Mod%20Art%20File).  Replace %CONSUMER_NAME% with `LeaderFallback`

### Seeing art in the game

See: [Cooking Art Files](#Modding%5CCooking%20Art%20Files)