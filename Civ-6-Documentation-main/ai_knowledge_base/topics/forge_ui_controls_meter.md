---
title: "Meter"
category: "Forge UI Controls"
summary: "<Meter> Friday, February 21, 2014 4:17 PM Rotational progress meter.  XML Attribute Type Details Color String The red, green, blue and optional alpha values to apply to the meter texture."
keywords: ["meter","forge","controls","lua","xml","animation","texture","control"]
---

# Meter

**<Meter>**

Friday, February 21, 2014

4:17 PM

Rotational progress meter.

**XML**

| **Attribute** | **Type** | **Details** |
| --- | --- | --- |
| Color | String | The red, green, blue and (optional) alpha values to apply to the meter texture. (Default is white with full alpha e.g., "255,255,255,255); |
| CounterClockwise | Bool | If true will have the meter run counter-clockwise . |
| Follow | Bool | If true the texture will rotate and "follow" whatever percentage the mask has currently revealed. Essentially revealing more of itself as the mask moves. |
| HasShadow | Bool | If true a second version of the texture will be used that sits under the main texture. |
| Percent | Number | Start value of the meter, by default this is 0. |
| ShadowAlpha | Number | Alpha value to apply to the "shadow" version |
| Speed | Number | How fast the meter should animate. If 0 (the default) no animation is used, it instantly |
| Texture | String | The texture to use for the meter (and optional "shadow") of the meter. |

**LUA Functions**

| **Function** | **Returns** | **Arguments** |
| --- | --- | --- |
| **SetAnimationSpeed** | **n/a** | **float**, 0 to animation speed where 0 is none |
| **SetCounterClockwise** | **n/a** | **bool** if true, meter runs counterclockwise; if false runs the meter clockwise |
| **SetFollow** | **n/a** | **Bool** if true, the texture will follow the rotation of the revealed mask. If false, the texture is stationary as the mask rotates around, revealing more of it. |
| **SetPercent** | **n/a** | **float**, 0.0 - 1.0 percent of the texture that is displayed (filled) |
| **SetPercents** | **n/a** | **float** 0.0-1.0**, float** 0.0-1.0 Sets both the main percent and "shadow" percent |
| **SetShadowColor** | **n/a** | **uint**, ABGR value that sets the color of the 'shadow' |
| **SetShadowPercent** | **n/a** | **float**, 0.0-1.0 percent of texture used as a 'shadow' |

**Examples**

![Machine generated alternative text: ](../Forge UI\Controls\Meter/media/image1.png)

<Meter Size="256,256" Texture="TestImage.dds" Percent="0.65" />

![Machine generated alternative text: .](../Forge UI\Controls\Meter/media/image2.png)

<Meter Size="256,256" Texture="TestImage.dds" Percent="0.65" **CounterClockwise="1"** />

![Machine generated alternative text: ](../Forge UI\Controls\Meter/media/image3.png)

<Meter Size="256,256" Texture="TestImage.dds" Percent="0.62" **Follow="1"** />

![Machine generated alternative text: ](../Forge UI\Controls\Meter/media/image4.png)

<Meter Size="256,256" Texture="TestImage.dds" Percent="0.62" **CounterClockwise="1"** **Follow="1"** />

![Machine generated alternative text: ](../Forge UI\Controls\Meter/media/image5.png)

<Meter Size="256,256" Texture="TestImage.dds" Percent="0.1" **HasShadow="1"** />