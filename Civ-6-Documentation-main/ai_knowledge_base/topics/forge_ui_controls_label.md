---
title: "Label"
category: "Forge UI Controls"
summary: "<Label> Friday, February 21, 2014 2:42 PM The internal “TextControl” which is used to display text.  Its size will automatically be calculated to the bounds of the text string, and should not be se..."
keywords: ["label","forge","controls","lua","xml","control"]
---

# Label

**<Label>**

Friday, February 21, 2014

2:42 PM

The internal “TextControl” which is used to display text. Its **size** will automatically be calculated to the bounds of the text string, and should not be set manually.

| **Attribute** | **Details** |
| --- | --- |
| **Align** | How to align the lines of text: "**left**" "**center**" "**right**" - *Note: text will align based on the width of the longest text string (in the case of a paragraph) or based on the width of its parent control. |
| **Color0** | Has same meaning as the base control’s “**Color**”. (Currently if you specify both in the same tag, Color0 will override Color) |
| **Color1** | DEPRECATED: See *EffectColor* |
| **Color2** | DEPRECATED: See GradientColor |
| **ColorSet** | The name of the color set to use. |
| **EffectColor** | (optional) The secondary color used for FontStyles such as “**Stroke**”, “**Glow**”, and “**Shadow**”. |
| **Font** | The name of the font to use for this control. |
| **FontSize** | The point size of the font to use. |
| **FontStyle** | The name of the font style to use. Valid styles are: "**Shadow**", "**Glow**", "**Stroke**" |
| **GradientColor** | (optional) Gradient color to use at the bottom of the font. |
| **LeadingOffset** | Leading offset from line to line. |
| **ReduceWidth** | Shrink the FontSize until the string fits within this width. *NOT IMPLEMENTED* |
| **Rotation** | Number of degrees to rotate the text. Rotation pivot is from the left-bottom of the first glyph. |
| **SmallCaps** | Size of font to use for the capitalization |
| **SmallCapsLeading** | Amount of leading to add to the non-small caps letters. |
| **SmallCapsType** | How to apply small caps, either: "**EveryWord**" (default) or "**FirstOnly**" |
| **String** | Control text. |
| **TruncateWidth** | The width (in pixels) to cut the string off. |
| **WrapWidth** | The width (in pixels) to start wrapping to the next line. |

**Example: Gradient Text**

*Game_ColorAtlas.xml:*

<ColorSet Name="ResCultureLabelCS" Color0="190,89,189,255" Color1="0,0,0,100" Color2="255,214,255,255" />

Where..

| Color0 | Top gradient |
| --- | --- |
| Color1 | Color of shadow, stroke, or glow |
| Color2 | Bottom gradient |

*SomeTechCivicToggle.xml*

<Label Offset="32,6" Style="FontNormal14" FontStyle="Glow" ColorSet="ResCultureLabelCS" />

Produces:

![C:\E3AD9F25\673868D8-982B-4885-B090-A5DC822099F8_files\image001.png](../Forge UI\Controls\Label/media/image1.png)

**Example: Small Caps**

<Label FontSize="20" String="NATIVE SMALL CAPS SUPPORT" Offset="10,10" Color="green" SmallCaps="28" SmallCapsLeading="6" SmallCapsType="EveryWord" />

![cid:image002.png@01D06594.25B3CD10](../Forge UI\Controls\Label/media/image2.png)

**Example: WrapWidth**

| ![Machine generated alternative text: I’m excited for the new super troopers movie. I’m excited for the new super troopers movie. I’m excited for the new super troopers movie. I’m excited for the new super troopers movie. I’m excited for the new super troopers movie. I’m excited for the new super troopers movie.](../Forge UI\Controls\Label/media/image3.png) | <Box Size="200,50" Color="99,88,77"> <Label String="I'm excited for the new super troopers movie." Size="parent,100" debug="1" /> </Box> <Box Size="200,50" Color="99,88,77" Offset="0,60"> <Label String="I'm excited for the new super troopers movie." Size="200,100" debug="1" /> </Box> <Box Size="200,50" Color="99,88,77" Offset="0,120"> <Label String="I'm excited for the new super troopers movie." debug="1" /> </Box> <Box Size="200,50" Color="99,88,77" Offset="0,180"> <Label String="I'm excited for the new super troopers movie." WrapWidth="200" debug="1" /> </Box> <Box Size="200,50" Color="99,88,77" Offset="0,240"> <Label String="I'm excited for the new super troopers movie." WrapWidth="parent" debug="1" /> </Box> <Box Size="200,50" Color="99,88,77" Offset="0,300"> <Label String="I'm excited for the new super troopers movie." Size="parent,100" WrapWidth="parent" debug="1" /> </Box> |
| --- | --- |

**LUA Functions**

| **Function** | **Returns** | **Arguments** | **Description** |
| --- | --- | --- | --- |
| **SetColor** | **n/a** | **uint ABGR, (uint layer)** **ABGR**, is a single ABGR to represent the alpha, blue, green, and red values as a single HEX value. (0xAABBGGRR) **layer**, (optional) a value 0 to 2 representing which "layer" of color to change. 0 is the main color of the glyphs, 1 is the effect color (shadow, glow, etc…) and 2 is a layer that isn't used… yet. |  |
| **SetColorByName** | **n/a** | **name**, The name of a color set in the color atlas | Sets the label to use all of the controls in the existing colorset. (Overrides the base implementation which only grabs the first color in the color set). |