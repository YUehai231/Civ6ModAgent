---
title: "CheckBox"
category: "Forge UI Controls"
summary: "<CheckBox> Friday, February 21, 2014 4:58 PM The check box control consists of a normal button with an overlaid CheckTexture and a text button label which can be clicked.  The size and position con..."
keywords: ["checkbox","forge","controls","texture","control"]
---

# CheckBox

<CheckBox>

Friday, February 21, 2014

4:58 PM

The check box control consists of a normal button with an overlaid **CheckTexture** and a text button label which can be clicked.

The size and position control the check box and the text button is positioned relative to the check box.

All attributes are passed through to the inherent TextButton control which itself builds from the inherent Text control. As such the attributes listed below are either common to be set or unique to checkboxes but there are additional attribute that can be set (e.g., “Font”, “NormalColor”, etc…)

| **Attribute** | **Details** |
| --- | --- |
| **BoxOnLeft** | Replaces “**TextAnchor**”, if true places the box on the left of the text button, instead of to the right. |
| **ButtonSize** | **Required** Size of the check button itself. |
| **ButtonTexture** | **Required** Texture to use for the button |
| **CheckColor** | A color to tint the checked image. |
| **CheckOffset** | Coordinate for positioning the check over the button. |
| **CheckSize** | Size of the check texture. |
| **CheckTexture** | Texture to use as the check mark. |
| **CheckTextureOffset** | Offset into the check texture. |
| **IsChecked** | Flag indicating the box should start checked |
| **String** | Set the label |
| **TextAnchor** | DEPRECATED Anchor flag for the TextButton |
| **TextButtonData** | All of the tags used for the TextButton control are used here to describe the text button portion of the check box |
| **TextOffset** | Offset of the TextButton portion from the check button |
| **UnCheckColor** | A color to tint the image used in the uncheck state |
| **UnCheckOffset** | Same as CheckOffset but for the UnCheckTexture |
| **UnCheckSize** | Same as CheckSize but for the UnCheckTexture |
| **UnCheckTexture** | A texture to show on top of the button when unchecked |
| **UnCheckTextureOffset** | Same as CheckTextureOffset but for the UnCheckTexture |
| **UseSelectedTextures** | The button of the checkbox has "selected" states (for normal, over, and down) which should be used when checked. |