---
title: "TextureBar"
category: "Forge UI Controls"
summary: "<TextureBar> Friday, February 21, 2014 3:12 PM Progress bar control made of a texture.  XML Attribute Type Details Color String The red, green, blue and optional alpha values to apply to the meter ..."
keywords: ["texturebar","forge","controls","lua","xml","animation","texture","control"]
---

# TextureBar

**<TextureBar>**

Friday, February 21, 2014

3:12 PM

Progress bar control made of a texture.

**XML**

| **Attribute** | **Type** | **Details** |
| --- | --- | --- |
| Color | String | The red, green, blue and (optional) alpha values to apply to the meter texture. (Default is white with full alpha e.g., "255,255,255,255); |
| Direction | String | In which way does the bar fill: **"Up" "Down" "Left" "Right"** |
| Percent | Number | Start value of the bar, by default this is 0. |
| Sampler | String | Linear |
| ShadowColor | Number | "R,G,B" Color 'tint' for the drop shadow version of the texture. Greyscale values work best (ie: 112, 112, 112) |
| Speed | Number | (default: "**0**") What speed to animate the fill. If 0, no animation; immediately set percentage. |
| Texture | String | Filename of the texture to use for the bar. |
| TextureOffset | String | -"X,Y" value in pixels to offset the Texture |

**LUA Functions**

| **Function** | **Returns** | **Arguments** |
| --- | --- | --- |
| **SetPercent** | **n/a** | **float**, 0.0 - 1.0 percent of the texture bar that is displayed (filled) |
| **SetShadowPercent** | **n/a** | **float**, 0.0-1.0 percent of texture used as a 'drop shadow' |
| **SetAnimationSpeed** | **n/a** | **float**, 0 to animation speed where 0 is none |