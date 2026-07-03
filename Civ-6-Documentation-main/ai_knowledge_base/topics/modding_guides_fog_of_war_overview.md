---
title: "Fog of War Overview"
category: "Modding Guides"
summary: "The Civ6 Fog of War system determines how parts of the map that have never been visible and/or are not currently visible get rendered.  By default, Civ6 uses a maplike style to render things that a..."
keywords: ["overview","modding","guides","artdef","texture","control"]
---

# Fog of War Overview

The Civ6 Fog of War system determines how parts of the map that have never been visible and/or are not currently visible get rendered.  By default, Civ6 uses a map-like style to render things that are in the "mid-fog",
which is terrain that you have explored but do not currently have vision on.

This document provides an overview of how to modify the appearance of the Fog of War in Civ6.

Note:  The sepia-tone mid-fog is a shader, and cannot be modified by end users.

The below applies to creating a new Fog of War ArtDef.  Select the "FOWConfig" Art Definition Template for Fog of War ArtDefs.

### FOWConfig Collection

The FOWConfig Collection always and only contains one value - "Default".  Elements with any other name will not be read.  A collection without a "Default" element will not influence Fog of War in the game.

### The "Default" FOWConfig Element

This element has numerous parameters.  In addition, it has children collections that allow further specification.

Name:

- Must be set to "Default".

MidFog:

- MidFog_RiverParchment -> Texture to combine with the river in fog of war.

- TerrainHatchColor -> Controls the color at the MidFog/FullFog boundary.

- TerrainHatchRotation -> Changes the direction of the terrain hatch.

- MidFog_CoastStripeThickness -> Thickness of the coast outline in mid-fog.  The outline expands in-land as it grows larger.  The default value is 0.04.

- MidFog_CoastStripeColor -> Color of the coast outline in mid-fog.

- TerrainHatchTileRate -> Controls the smoothness of the hatch pattern.  Lower values are smoother, higher values are rougher.  The default value is 50.

- MidFog_WaterParchmentTiling -> Scales the Water Parchment texture.  The default value is 200.  The higher the value, the more space the texture takes up in the world.

- MidFog_ShallowWaveJitter -> Doesn't appear to do anything. ###

- MidFog_OceanWaveJitter -> Appears to effect the randomness of where ocean waves are placed in mid-fog.

- MidFog_DeepWaterParchment -> Changes the texture that is used to render deep-water (ocean) in mid-fog.

- MidFog_ShallowWaterParchmet -> Changes the texture that is used to render shallow-water (lakes and coast) in mid-fog.

- MidFog_WaterParchmentRotation -> Rotates the water parchment.

- MidFog_CoastalWavesExtrudeDistance -> Determines how far out the coastal wave texture gets drawn into the hex in mid-fog.

- MidFog_CoastalWavesTiling -> Changes the scale of the waves that are rendered.  The default value is 270.  A higher value makes the waves larger, a smaller value makes them smaller.

- MidFog_CoastalWaves -> Changes the texture that is used to render waves on top of coast.

- MidFog_FlowLineColor -> Doesn't appear to do anything. ###

- MidFog_FlowLineThickness -> Doesn't appear to do anything. ###

- MidFog_FlowLineOpacity -> Doesn't appear to do anything. ###

- MidFog_FlowLineHeightBias -> Doesn't appear to do anything. ###

- MidFog_FlowLineOffset -> Doesn't appear to do anything. ###

FullFog:

- FullFog_LineOpacityTiling -> Doesn't appear to do anything. ###

- FullFog_ParchmentTiling -> Changes the frequency that the parchment tiles.  Smaller numbers increase frequency.  The default value is 600.

- FullFog_Parchment -> Changes the texture that is used for the parchment.

- FullFog_LineOpacityNoise -> Changes the texture that is used for the LineOpacityNoise.

- FullFog_LineOpacity -> Doesn't appear to do anything. ###

- FullFog_LineColor -> Doesn't appear to do anything. ###

- FullFog_ParchmentRotation -> Rotates the parchment tiles (the squares in full-fog).

- FullFog_DecoJitter -> Appears to effect the randomness of where Deco sprites are placed.

- FullFog_LineThicknessY -> Doesn't appear to do anything. ###

- FullFog_LineIntervalY -> Doesn't appear to do anything. ###

- FullFog_LineIntervalX -> Doesn't appear to do anything. ###

- FullFog_LineThicknessX -> Doesn't appear to do anything. ###

Value:

- BackgroundColor -> Doesn't appear to do anything. ###

FogBorder:

- FogBorderUVScale -> Determines the UV Scale sampling from the Noise Texture at fog borders.  Values range from 0.0 to 1.0.  The default value is 0.0045.  Values higher than 0.01 make the edge incredibly noisy.

- FogBorderNoiseIntensity -> The noise intensity at fog borders.  Values range from 0.0 to 1.0.  Lower values cause fog to encroach on visible tiles more heavily.

- FogBorderColor -> Determines the color of the border between no-fog and mid-fig/full-fog.

Models:

- Models_HatchTileRate -> Effects the density of the hatch rate.  The default value is 50.  Lower values create a smoother appearance, while higher values make the hatch sharper.  Values between 40 and 70 tend to produce the best results.

- Models_HatchRotation -> Rotates the "hatch" on models in Fog of War.

- Models_HatchColor -> Determines the color of the vertical hatch that appears vertically on Fog of War models and resources.

- Models_StrokeColor -> Determines the color of the model outline in Fog of War.

- Models_StrokeOpacity -> Determines the visibility of the stroke that outlines models in Fog of War.

- Models_StrokeThickness -> Determines the thickness of the model outline.

- Models_Parchment -> The parchment texture that is used to be mixed with the parchment weight.

- Models_ParchmentWeight -> Controls how heavily the parchment texture influences the base color texture.

CompassLines: -- Appear as diagnal lines that bisect the FullFog parchment.

- CompassLine_Texture -> Controls the texture that is used to render compass lines.

- CompassLine_Width -> Controls how wide the compass lines are.

- CompassLine_SeparationAngle -> Controls how close together or separated the compass lines are.

- Children:

<ul>
<li>OceanWaveSets
<ul>
<li>LargeWaves
<ul>
<li>Rarity -> Determines the frequency of LargeWaves in the total set of OceanWaves.

- Sprites [Collection] -> Each entry has a name, a texture assigned to it, and a scale factor.

</li>
- MediumWaves

<li>Rarity -> Determines the frequency of MediumWaves in the total set of OceanWaves.

- Sprites [Collection] -> Each entry has a name, a texture assigned to it, and a scale factor.

</li>
- SmallWaves

<li>Rarity -> Determines the frequency of SmallWaves in the total set of OceanWaves.

- Sprites [Collection] -> Each entry has a name, a texture assigned to it, and a scale factor.

</li>
</ul>
</li>
- FullFogDecotSets

<li>Rarity -> Determines how frequently a Deco sprite will be placed on the full-fog map parchment.

- Sprites [Collection] -> Each entry has a name, a texture assigned to it, and a scale factor.

</li>
- ShallowWaveSets

<li>Rarity -> Determines the frequency of Waves in the total set of ShallowWaveSets.

- Sprites [Collection] -> Each entry has a name, a texture assigned to it, and a scale factor.

</li>
- MapBorders

<li>Rarity -> Determines the frequency of MapBorders in the total set of MapBorders.

- Sprites [Collection] -> Each entry has a name, a texture assigned to it, and a scale factor.

</li>
- HatchTextures [Collection] -> Maps a name to a Hatch texture.

- ModelHatchTextures [Collection] -> Maps a name to a Model Hatch texture.

</ul>
</li>
</ul>