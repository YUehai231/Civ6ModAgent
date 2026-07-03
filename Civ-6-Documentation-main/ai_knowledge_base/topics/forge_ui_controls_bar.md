---
title: "Bar"
category: "Forge UI Controls"
summary: "<Bar> Friday, February 21, 2014 3:05 PM Progress bar control made of a solid color.  For a bitmapped version see: <TextureBar> XML Attribute Type Details FGColor String The red, green, blue and opt..."
keywords: ["forge","controls","lua","xml","animation","texture","control"]
---

# Bar

**<Bar>**

Friday, February 21, 2014

3:05 PM

Progress bar control made of a solid color. For a bitmapped version see: *<TextureBar>*

**XML**

| **Attribute** | **Type** | **Details** |
| --- | --- | --- |
| FGColor | String | The red, green, blue and (optional) alpha values to apply to the meter texture. (Default is white with full alpha e.g., "255,255,255,255); |
| BGColor | String |  |
| Direction | String | In which way does the bar fill: **"Up" "Down" "Left" "Right"** |
| Percent | Number | Start value of the bar, by default this is 0. |
| Speed | Number | (default: "**0**") What speed to animate the fill. If 0, no animation; immediately set percentage. |

**LUA Functions**

| **Function** | **Returns** | **Arguments** |
| --- | --- | --- |
| **SetPercent** | **n/a** | **float**, 0.0 - 1.0 percent of the texture bar that is displayed (filled) |
| **SetShadowPercent** | **n/a** | **float**, 0.0-1.0 percent of texture used as a 'drop shadow' |
| **SetAnimationSpeed** | **n/a** | **float**, 0 to animation speed where 0 is none |