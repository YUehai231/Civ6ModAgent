---
title: "TerrainOverview"
category: "Content Creation Basics"
summary: "Terrain Overview Madrid Exported on Jun 30, 2017 The Strategic View uses a modified version of offset blending to render most of its terrainbased elements i. e."
keywords: ["terrainoverview","content","creation","basics","blp","texture"]
---

# TerrainOverview

Terrain Overview

Madrid

Exported on Jun 30, 2017

The Strategic View uses a modified version of *offset blending* to render most of its terrain-based elements (i.e. terrain blending and the rendering of rivers, coastlines, the hex grid, and culture borders). Offset blending uses a *blend grid* to position all render elements. The blend grid is separate hex grid that is offset from the game grid by half a hex on both the Cartesian X and Y axes. In addition, where the game grid’s odd rows are offset along the positive Cartesian X axis, the blend grid’s odd rows are offset along the negative Cartesian Y axis. (Compare the game and blend grid’s plot [0, 1] in Figure 1.)

Figure 1 Figure 1: The game hex grid (black) and the blend hex grid (grey).

![Figure 1: The game hex grid (black) and the blend hex grid (grey).](../TerrainOverview/media/image1.png)

Each blend hex overlaps three game hexes and conversely each game hex contains parts of three different blend hexes. (Game hex [1, 1] consists of blend hexes [1, 2], [2, 2], and [2, 1] in Figure 1.) The animated GIF in Figure 2 depicts the relationship between the blend hexes and the game hexes.

Figure 2 Figure 2: The relationship between the game grid and the blend grid.

![Figure 2: The relationship between the game grid and the blend grid.](../TerrainOverview/media/image2.png)

Because of this both sides of the edge between game hexes are contained within a single blend hex. This ensures that the blends between different terrain textures will always line up perfectly. The only drawback is that the blends from different blend textures have to line up at three of the hex’s six points (2, 6, and 10 o’clock).

In order to render the terrain system needs six textures:

1. - the Terrain Blend Texture,

- the Terrain Diffuse Texture covering the lower-right (red) part of the blend hex,

- the Terrain Diffuse Texture covering the lower-left (green) part of the blend hex,

- the Terrain Diffuse Texture covering the top (blue) part of the blend hex,

- the Coastline / Riverbank Texture, and

- the Culture Border / Hex Grid Texture.

Unless noted otherwise the textures are all 256x256 uncompressed DDS files (8.8.8.8. ARGB 32 bpp | unsigned).

<h1 id="terrain-blend-texture">Terrain Blend Texture</h1>
The Terrain Blend Texture determines where each of the three Terrain Diffuse Textures gets rendered. The texture uses the red channel to place Terrain Diffuse Texture 1, the green channel to place Terrain Diffuse Texture 2, and the blue channel to place Terrain Diffuse Texture 3. The alpha channel is used to render the actual hex shape and prevent the rendering quads from visibly overlapping.

An example texture using straight lines to separate the three diffuse textures can be seen in Figure 3. A more advanced blending texture can be seen in Figure 4.)

![/download/attachments/166105140/image2017-6-14_10-33-35.png?version=1&modificationDate=1497450815060&api=v2](../TerrainOverview/media/image3.png)![/download/attachments/166105140/image2017-6-14_10-34-0.png?version=1&modificationDate=1497450840313&api=v2](../TerrainOverview/media/image4.png)

| **Channels** | **Description** |
| --- | --- |
| R | Bottom-right (red) terrain diffuse texture will be drawn here. |
| G | Bottom-left (green) terrain diffuse texture will be drawn here. |
| B | Top (blue) terrain diffuse texture will be drawn here. |
| A | Hex shape visibility to prevent quad overlap. |

<h1 id="terrain-diffuse-textures">Terrain Diffuse Textures</h1>
The three Terrain Diffuse Textures provide color information for the different terrain types. Ideally they are hex-tileable, i.e. each of the six hex edges matches its opposite edge perfectly.

![/download/attachments/166105140/image2017-6-14_10-47-35.png?version=1&modificationDate=1497451655923&api=v2](../TerrainOverview/media/image5.png)![/download/attachments/166105140/image2017-6-14_10-47-50.png?version=1&modificationDate=1497451670440&api=v2](../TerrainOverview/media/image6.png)

| **Channels** | **Description** |
| --- | --- |
| R, G , B | Diffuse color information for the terrain type. |
| A | No information |

<h1 id="the-coastline-riverbank-texture">The Coastline / Riverbank Texture</h1>
The Coastline / Riverbank Texture stores the luminance information for the lines that represent the coastlines and the riverbanks as well as the placement information for the coastal outline / river water. Since the color will be superimposed on top of the terrain blending the location within the texture needs to only roughly follow the terrain blend.

The luminance information is expressed in nine (9) different layers stored in three (3) separate permutation textures:

1. - right inside coastline / riverbank (stored in the first texture’s red channel),

- right outside coastline / riverbank (stored in the first texture’s green channel),

- left inside coastline / riverbank (stored in the second texture’s red channel),

- left outside coastline / riverbank (stored in the second texture’s green channel),

- top inside coastline / riverbank (stored in the third texture’s red channel),

- top outside coastline / riverbank (stored in the third texture’s green channel),

- left-corner dot coastline / riverbank (stored in the first texture’s blue channel),

- right-corner dot coastline / riverbank (stored in the second texture’s blue channel), and

- bottom-corner dot coastline / riverbank (stored in the third texture’s blue channel).

The direction (right / left) describes which way the coastlines / riverbanks are turning – right means turning towards 2 o’clock, left means turning towards 10 o’clock. Inside / outside describes where the coastline / riverbank is placed in relationship to its respective terrain blend – inside means the coastline / riverbank overlaps the terrain blend, outside means it overlaps the remaining two terrain blends. The dot is required to connect combinations of coastlines / riverbanks that extend into neighboring blend hexes, e.g. two left inside coastlines / riverbanks arranged diagonally. The dots can most likely be authored once and reused.

![/download/attachments/166105140/image2017-6-14_10-50-46.png?version=1&modificationDate=1497451846160&api=v2](../TerrainOverview/media/image7.png)![/download/attachments/166105140/image2017-6-14_10-51-18.png?version=1&modificationDate=1497451878663&api=v2](../TerrainOverview/media/image8.png)![/download/attachments/166105140/image2017-6-14_10-51-53.png?version=1&modificationDate=1497451913287&api=v2](../TerrainOverview/media/image9.png)

In addition to the luminance information for the coastline / riverbank lines the Coastline / Riverbank Texture stores placement information for the coastal outline / river water in the alpha channel of each of the three textures.

![/download/attachments/166105140/image2017-6-14_10-52-52.png?version=1&modificationDate=1497451972350&api=v2](../TerrainOverview/media/image10.png)![/download/attachments/166105140/image2017-6-14_10-53-26.png?version=1&modificationDate=1497452006633&api=v2](../TerrainOverview/media/image11.png)![/download/attachments/166105140/image2017-6-14_10-53-55.png?version=1&modificationDate=1497452035463&api=v2](../TerrainOverview/media/image12.png)

Rivers can start in one of six directions within a blend hex (see Figure 13). Special variations of the Coastline / Riverbank Texture provide the luminance information for these cases and just like the dots can most likely be authored once and reused.

Figure 3 Figure 13: River source flow directions.

![Figure 13: River source flow directions.](../TerrainOverview/media/image13.png)

Unfortunately since the coastal outline needs to be wider than the river water area, the coastline textures and river textures cannot be shared.

| **Channels** | **Description** |
| --- | --- |
| R | Inside coastline / riverbank luminance information. |
| G | Outside coastline / riverbank luminance information. |
| B | Dot coastline / riverbank luminance information. |
| A | Coastal outline / river water placement. |

<h1 id="culture-border-hex-grid-texture">Culture Border / Hex Grid Texture</h1>
The Culture Border / Hex Grid Texture stores the luminance (or possibly gradient lookup) information for culture borders as well as the hex grid luminance information. Since the color will be superimposed on top of the terrain blending or the coastlines / riverbanks the location within the texture needs to exactly match one of the previous two textures.

The luminance / gradient lookup information is expressed in nine (9) different layers stored in three (3) separate permutation textures:

1. - right inside culture border (stored in the first texture’s red channel),

- right outside culture border (stored in the first texture’s green channel),

- left inside culture border (stored in the second texture’s red channel),

- left outside culture border (stored in the second texture’s green channel),

- top inside culture border (stored in the third texture’s red channel),

- top outside culture border (stored in the third texture’s green channel),

- left-corner dot culture border (stored in the first texture’s blue channel),

- right-corner dot culture border (stored in the second texture’s blue channel), and

- bottom-corner dot culture border (stored in the third texture’s blue channel).

The direction (right / left) describes which way culture border is turning – right means turning towards 2 o’clock, left means turning towards 10 o’clock. Inside / outside describes where the culture border is placed in relationship to its respective terrain blend – inside means the culture border overlaps the terrain blend, outside means it overlaps the remaining two terrain blends. The dot is required to connect combinations of culture borders that extend into neighboring blend hexes, e.g. two left inside culture borders arranged diagonally. The dots can most likely be authored once and reused.

![/download/attachments/166105140/image2017-6-14_11-0-29.png?version=1&modificationDate=1497452429657&api=v2](../TerrainOverview/media/image14.png)![/download/attachments/166105140/image2017-6-14_11-1-4.png?version=1&modificationDate=1497452464283&api=v2](../TerrainOverview/media/image15.png)![/download/attachments/166105140/image2017-6-14_11-1-32.png?version=1&modificationDate=1497452492237&api=v2](../TerrainOverview/media/image16.png)

In addition to the luminance / gradient lookup information for the culture border the Culture Border / Hex Grid Texture stores the hex grid luminance information in the alpha channel of each of the three textures.

Figure 4 Figure 17: Hex grid luminance information.

![Figure 17: Hex grid luminance information.](../TerrainOverview/media/image17.png)

The Culture Border / Hex Grid Texture is tightly coupled to either the terrain blend shapes of the Terrain Blend Texture or the coastline / riverbank shapes of the Coastline / Riverbank Texture and cannot therefore be associated with both of them at the same time.

| **Channels** | **Description** |
| --- | --- |
| R | Inside culture border luminance / gradient lookup information. |
| G | Outside culture border luminance / gradient lookup information. |
| B | Dot culture border luminance / gradient lookup information. |
| A | Hex grid luminance information. |

<h1 id="authoring-and-runtime">Authoring and Runtime</h1>
(For a detailed walk-through of how to author the terrain blend textures see the Base game's Art OneNote, StrategicView, Generating Terrain Blends.)

Each terrain blend (with or without corresponding coastline / riverbank) is authored in a single PSD file with many layers. The export process takes care of encoding the layers in different texture channels and assigns them to textures. The cooker then creates all possible permutations of coastlines, riverbanks, and culture borders and stores all of them as separate entries in the BLP. At runtime the engine simply selects the appropriate BLP entry based on the procedurally generated terrain.

In the table below the Group column specifies which layers have to present for a terrain blend PSD to be valid:

- Base represents a terrain blend that can be applied to any blend tile that has no river banks, sources or coastlines present.

- Channel must include all Base layers in addition to its own and represents a terrain blend that can be applied to a tile that has either coastlines or river banks, but no sources, in addition to any blend tiles that Base can be applied to.

- Source must include all Base and Channel layers in addition to its own and represents the full terrain blend that can be applied to any blend tile, including one with river sources.

| Group | Layer |
| --- | --- |
| Base | TerrainBlend |
|  | CultureBorder_Right |
|  | CultureBorder_Left |
|  | CultureBorder_Top |
|  | RiverbankCorners_CultureBorder_RightBottom |
|  | RiverbankCorners_CultureBorder_RightTop |
|  | RiverbankCorners_CultureBorder_RightTopAndBottom |
|  | RiverbankCorners_CultureBorder_LeftBottom |
|  | RiverbankCorners_CultureBorder_LeftTop |
|  | RiverbankCorners_CultureBorder_LeftTopAndBottom |
|  | RiverbankCorners_CultureBorder_TopLeft |
|  | RiverbankCorners_CultureBorder_TopRight |
|  | RiverbankCorners_CultureBorder_TopRightAndLeft |
| Channel | RiverbankChannelRight_ChannelBottomThin |
|  | RiverbankChannelRight_ChannelBottomThin_CultureBorder_Left |
|  | RiverbankChannelRight_ChannelBottomThin_CultureBorder_Right |
|  | RiverbankChannelRight_ChannelBottomThin_CultureBorder_Top |
|  | RiverbankChannelRight_ChannelBottomFat |
|  | RiverbankChannelLeft_ChannelBottomThin |
|  | RiverbankChannelLeft_ChannelBottomThin_CultureBorder_Left |
|  | RiverbankChannelLeft_ChannelBottomThin_CultureBorder_Right |
|  | RiverbankChannelLeft_ChannelBottomThin_CultureBorder_Top |
|  | RiverbankChannelLeft_ChannelBottomFat |
|  | RiverbankChannelRight_ChannelLeft |
|  | RiverbankChannelRight_ChannelLeft_CultureBorder_Left |
|  | RiverbankChannelRight_ChannelLeft_CultureBorder_Right |
|  | RiverbankChannelRight_ChannelLeft_CultureBorder_Top |
| Source | RiverbankSourceRight |
|  | RiverbankSourceRight_CultureBorder_Right |
|  | RiverbankSourceRight_CultureBorder_Top |
|  | RiverbankSourceRight_ChannelBottomThin |
|  | RiverbankSourceRight_ChannelBottomThin_CultureBorder_Right |
|  | RiverbankSourceRight_ChannelBottomThin_CultureBorder_Top |
|  | RiverbankSourceRight_ChannelBottomFat |
|  | RiverbankSourceRight_ChannelLeft_ChannelBottomThin |
|  | RiverbankSourceRight_ChannelLeft_ChannelBottomThin_CultureBorder_Top |
|  | RiverbankSourceRight_ChannelLeft_ChannelBottomFat |
|  | RiverbankSourceRight_ChannelLeft |
|  | RiverbankSourceRight_ChannelLeft_CultureBorder_Right |
|  | RiverbankSourceRight_SourceLeft_ChannelBottomThin |
|  | RiverbankSourceRight_SourceLeft_ChannelBottomThin_CultureBorder_Left |
|  | RiverbankSourceRight_SourceLeft_ChannelBottomThin_CultureBorder_Top |
|  | RiverbankSourceRight_SourceLeft_ChannelBottomFat |
|  | RiverbankSourceRight_SourceBottom_ChannelLeft |
|  | RiverbankSourceRight_SourceBottom_ChannelLeft_CultureBorder_Left |
|  | RiverbankSourceRight_SourceBottom_ChannelLeft_CultureBorder_Right |
|  | RiverbankSourceLeft |
|  | RiverbankSourceLeft_CultureBorder_Left |
|  | RiverbankSourceLeft_CultureBorder_Top |
|  | RiverbankSourceLeft_ChannelRight_ChannelBottomThin |
|  | RiverbankSourceLeft_ChannelRight_ChannelBottomThin_CultureBorder_Top |
|  | RiverbankSourceLeft_ChannelRight_ChannelBottomFat |
|  | RiverbankSourceLeft_ChannelBottomThin |
|  | RiverbankSourceLeft_ChannelBottomThin_CultureBorder_Top |
|  | RiverbankSourceLeft_ChannelBottomFat |
|  | RiverbankSourceLeft_ChannelRight |
|  | RiverbankSourceLeft_ChannelRight_CultureBorder_Left |
|  | RiverbankSourceLeft_SourceBottom_ChannelRight |
|  | RiverbankSourceLeft_SourceBottom_ChannelRight_CultureBorder_Left |
|  | RiverbankSourceLeft_SourceBottom_ChannelRight_CultureBorder_Right |
|  | RiverbankSourceBottom_Thin |
|  | RiverbankSourceBottom_Thin_CultureBorder_Left |
|  | RiverbankSourceBottom_Thin_CultureBorder_Right |
|  | RiverbankSourceBottom_Fat |
|  | RiverbankSourceBottom_ChannelRight |
|  | RiverbankSourceBottom_ChannelRight_CultureBorder_Left |
|  | RiverbankSourceBottom_ChannelLeft |
|  | RiverbankSourceBottom_ChannelLeft_CultureBorder_Right |
|  | RiverbankSourceBottom_ChannelRight_ChannelLeft |
|  | RiverbankSourceRight_SourceLeft_SourceBottom |

Additionally, the following four textures are part of a separate terrain blend corners PSD, because they do not depend on the individual terrain blends:

| Corners | CultureBorderCorners_All |
| --- | --- |
|  | RiverbankCorners_All |
|  | RiverbankWaterCorners_All |
|  | RiverbankCorners_CultureBorder_All |