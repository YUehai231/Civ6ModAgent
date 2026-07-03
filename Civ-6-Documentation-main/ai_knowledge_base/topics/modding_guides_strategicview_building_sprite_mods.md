---
title: "StrategicView Building Sprite Mods"
category: "Modding Guides"
summary: "See: Texture System Mods#Modding%5CTexture%20System%20Mods.  Replace %XLPCLASS% with StrategicViewSprite."
keywords: ["strategicview","building","sprite","mods","modding","guides","artdef","xlp","texture"]
---

# StrategicView Building Sprite Mods

### Creating the Texture and adding it to the XLP

See: [Texture System Mods](#Modding%5CTexture%20System%20Mods).  Replace %XLP_CLASS% with `StrategicView_Sprite`.
See: [Add and Update Libraries in Mod Art File](#Modding%5CAdd%20and%20Update%20Libraries%20in%20Mod%20Art%20File).  Replace %LIBRARY_NAME% with `StrategicView_Sprite`

We have multiple different building states for each building sprite.

Visibility States:

- Revealed

- Visible

Building State:

- Normal (constructed)

- Pillaged

- Under Construction

### Creating the ArtDef and Referencing the Sprites

1. - Go to File -> New -> ArtDef

- Change the **Art Definition Template** to `StrategicView`.

### Adding the Building Entries

1. - Select the **BuildingEntries** item in the Tree, right-click, and press *Add Element*.  Do this once for each construction state.

- Change the name of the newly created elements to the name of the building and its construction state.

- Under the **Visible_XLPEntry** field, click the dropdown, and then click the *Browse* button.

- Find the newly created entry in the XLP browser.

- Select the entry and press the *OK* button.

- Under the **Revealed_XLPEntry** field, click the dropdown, and then click the *Browse* button.

- Find the newly created entry in the XLP browser.

- Select the entry and press the *OK* button.

### Adding the Buildings

1. - Select the **Buildings** item in the Tree, right-click, and press *Add Element*.  Do this once for each construction state.

- Name the new entries based on the building and construction state that it will be in.

- For each new entry, select the BuildingChain (which determines which district this building belongs in), the PositionSet (which determines how the game places the entries), and the placement rules (where in the Position Set does this particular entry live).

- Expand the tree node for each of the newly created buildings.

- Select **Entries**, right-click, and press *Add Element*.

- Select the new entry.  Choose a new name for it, and then select the appropriate ArtDefEntry that you added in the above section.

Please remember to save your work.

### Adding the ArtDef to the Game

See: [Add and Update Consumers in Mod Art File][cons].  Replace %CONSUMER_NAME% with `StrategicView_Sprite`

### Seeing art in the game

See: [Cooking Art Files](#Modding%5CCooking%20Art%20Files)