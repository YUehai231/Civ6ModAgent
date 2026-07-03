---
title: "World Builder"
category: "Content Creation Basics"
summary: "scrollexternal\attachments\image201866155519806c77b8608b72aed5a3181a425630c744adee755cf1dbce003a6f7396c1ec69. png.."
keywords: ["world","builder","content","creation","basics","xml","screen"]
---

# World Builder

![_scroll_external\attachments\image2018-6-6_15-55-19-806c77b8608b72aed5a3181a425630c744adee755cf1dbce003a6f7396c1ec69.png](../World Builder/media/image1.png)

How to use the Tiled Importer for World Builder 

1. - Open Tiled Editor and open up a new map (File -> New -> New Map)

![_scroll_external\attachments\image2018-6-5_16-27-20-f6115e54a7ccc71bb38e8cd13e510d433cd1aedb83c32634e556ed062241c8b6.png](../World Builder/media/image2.png)

1. - Choose a Hexagonal map, for tile layer format, choose CSV and render order right down

- Under map size, you may set any dimensions you like, but staying close to existing Civ map dimensions is probably best.

<ol style="list-style-type: lower-alpha">
- Duel: 44 tiles wide by 26 tiles high

- Tiny: 60 tiles wide by 38 tiles high

- Small: 74 tiles wide by 46 tiles high

- Standard: 84 tiles wide by 54 tiles high

- Large: 96 tiles wide by 60 tiles high

- Huge: 106 tiles wide by 66 tiles high

- Under Tile size, choose Width: 32px Height: 64px

</ol>

![_scroll_external\attachments\image2018-7-23_16-16-44-82ef751efb1b4df764abe1866e95a73100f63a42b25a6c6199416028b606bae1.png](../World Builder/media/image3.png)

1. - Use Tiled's File→Open function to load the tilesets for each layer you're going to use.  They are currently in Examples/WorldBuilder Tiled Importing.

- Under Map -> Properties: 

- Hexagonal (Staggered)

- Tile Width: 32

- Tile Height 64

- Stagger Axis: Y

- Stagger Index: Even

- Tile Layer Format: XML

- Tile Render Order: "Right Down" or "Right Up" will work.  The importer can tell which is which and flip the map accordingly.

![_scroll_external\attachments\image2018-6-6_15-50-53-5f28629fc6414da6b74787a778576bcc441ac991562fd17962236e30002ccde3.png](../World Builder/media/image4.png)

1. - Layers can be a mix of tile layers and object layers.  Object layers are necessary for some types because they allow you to define per-tile parameters that are passed to the importer.

- In order from the top to the bottom of the layer list, the layers must be: Rivers, Buildings, Districts, Cities, Continents, Improvements, Resources, Features, and Terrain.

<ol style="list-style-type: lower-alpha">
- Terrain must be a tile layer and you should always define all of the tiles on the terrain layer.  The Bucket Fill tool can be useful to set the whole map to a base type.

- You don't have to have all layers in a given map for it to import successfully, but all of the layers below the highest one you have must exist.  For instance, if you want to place improvements on terrain, you must still have resources and features layers.  Just don't place anything on them.

- Features can be a tile layer or an object layer.  Unused hexes do not need to be filled in.

- Resources should be an object layer.  After you place each resource, click the "+" at the bottom of the Properties column and add a custom property "number" of type "int".  Then set the value to represent the amount of that resource present in that hex.

- Improvements should be an object layer.  As with resources, add a custom property named "player" of type "int".  This value sets which civ the improvement will belong to.

- Continents should be a tile layer currently.  The tiles for them represent, in order: Africa, Amasia, America, Antarctica, Arctica, Asia, AsiaAmerica, Atlantica, Atlantis, Australia, Avalonia, Azania, Baltica, Cimmeria, Columbia, Congo Craton, EurAmerica, Europe, Gondwana, Kalaharia, Kazakhstania, Kernorland, Kumari Kandam, LaurAsia, Laurentia, Lemuria, Mu, Nena, North America, Novopangea, Nuna, Oceana, Pangaea, Pangaea Ultima, Pannotia, Rodinia, Siberia, South America, Australis, Ur, Vaalbara, Vendia, and Zelandia.

- Cities can be a tile layer or an object layer.  In both cases, the tiles are 1-16 representing up to 16 players in a game.  TIle 1 here is the same as "player 0" in the Improvements layer, 2 is the same as "1", and so on.
<ol style="list-style-type: lower-roman">
2. If you make this an object layer, you can add a custom parameter named "spawn" of type Bool.  This will show as a checkbox in the list of parameters, and if you check it, this will be the spawn point for the player rather than generating a city on the spot.

- Districts should be an object layer with a "player" custom parameter

- Buildings should be an object layer with a "player" custom parameter.

- Rivers should be an object layer with a custom parameter named "direction" of type String.  Valid values are "NE", "E", "SE", "SW", 'W", or "NW".  TODO: what does this parameter mean?

- To set up parameters:

1. - Click here:

![_scroll_external\attachments\image2018-7-26_16-21-29-681b577720210f3bf085ba8de004e7208e374b2613575a829b618b1ae9e13ce2.png](../World Builder/media/image5.png)

- Which brings up this: ![_scroll_external\attachments\image2018-7-26_16-23-59-11d86b1413e07a024a686f73c2aa8609783f9c190f05bd7434e499ecf18d49fb.png](../World Builder/media/image6.png)

- Enter the name in the text field and set the type with the drop-down ![_scroll_external\attachments\image2018-7-26_16-27-27-d2e0ec31bbffe7d88f9c2b88188a2743a6468510816c4c46a7f7ecb0d0804860.png](../World Builder/media/image7.png)

- The new parameter will appear in the left-hand column as shown where you may set the value.Buildings should be an object layer with a "player" custom parameter.

</ol></li>
- Each layer must only use tiles from one tileset.  If you use more than one the behavior of the importer is not guaranteed to be correct.

- Save file as tmx.

- In Civ VI->Additional Content->World Builder choose "Import Map".

1. - ![_scroll_external\attachments\image2018-6-25_9-58-38-ce921c1f7b19efb11e6e68a5606dece4cfe609f3b9b2f36990d4f251114e0817.png](../World Builder/media/image8.png)

- The "Advanced Setup" screen will appear, minus the map size options.   Pick the number of players for your map and the specific teams if you want them to be particular civs, as well as any rules changes.

- Click the "Import Map" button and the Civ file browser will appear, with extra buttons for full drive navigation to anywhere on your computer.  Choose a map and WorldBuilder will load with the selected map.

- When you're finished viewing/fine-tuning in WorldBuilder, press Esc to bring up the menu and click the "Save Game" button to save a game with your map.

</ol>