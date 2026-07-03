---
title: "TextButton"
category: "Forge UI Controls"
summary: "<TextButton> Friday, February 21, 2014 4:49 PM Button control which is text only.  The color and style can be specified for each button state."
keywords: ["textbutton","forge","controls","xml","screen","control"]
---

# TextButton

**<TextButton>**

Friday, February 21, 2014

4:49 PM

Button control which is text only. The color and style can be specified for each button state.

**XML**

| **Attribute** | **Details** |
| --- | --- |
| **Style** | The style of the button to use in the normal state. This style is not applied to the text button in its other states! |
| **MouseOverStyle** | Style to use for MouseOver |
| **ButtonDownStyle** | The style to use for when the button is “pressed” Down |
| **DisabledStyle** | The style to use for Disabled. |
| **Font** | Name of the font to use for this control. |
| **FontSize** | Point size of the font to use. |
| **FontStyle** | Style (“**stroke**”, “**shadow**”, “**glow**”) of the font to use in its normal state. |
| **String** | Text to use as the button |
| **ButtonDownColor** | **DEPRECATED:** The ColorSet to use when in the “pressed” Down state. |
| **DisabledColor** | **DEPRECATED:** The ColorSet to use when Disabled |
| **MouseOverColor** | **DEPRECATED**: ColorSet to use for MouseOver |
| **NormalColor** | **DEPRECATED:** ColorSet to use normally |

**Example**

<!-- defined in styles.xml -->

<TestNormal Font="HelveticaNeue.ttf" FontSize="22" Color0="255,0,0,255" Color1="0,99,99,200" FontStyle="Stroke" />

<TestOver Font="HelveticaNeue.ttf" FontSize="26" Color0="255,255,0,255" Color1="9,9,200,255" FontStyle="Shadow" />

<TestDown Font="HelveticaNeue.ttf" FontSize="18" Color0="255,255,0,255" Color1="255,0,0,255" FontStyle="Stroke" />

<TestDisabled Font="HelveticaNeue.ttf" FontSize="26" Color0="90,90,90,190" Color1="0,0,0,255" FontStyle="Normal" />

<!-- used in specific screen's .xml -->

<TextButton ID="test" Anchor="C,B" Offset="0,0" String="This is a test!"

Style="TestNormal"

MouseOverStyle="TestOver"

ButtonDownStyle="TestDown"

DisabledStyle="TestDisabled" />