---
title: "GridButton"
category: "Forge UI Controls"
summary: "<GridButton> Friday, February 21, 2014 2:33 PM A Button control which uses a Grid to allow the size to be flexible, and may contain an optional text field.  Grid specific data is specified by a sub..."
keywords: ["gridbutton","forge","controls","lua","xml","texture","control"]
---

# GridButton

<GridButton>

Friday, February 21, 2014

2:33 PM

A Button control which uses a **Grid** to allow the size to be flexible, and may contain an optional text field. Grid specific data is specified by a sub-control called **<GridData>** which contains all of the normal control data for a GridControl. For state changes, we offset into the texture by the **StateOffsetIncrement** value in the GridData.

**Child Tags**

**<GridData>** - Sub control with the details of the grid to use. See *<Grid>* for details.

**XML**

| **Attribute** | **Details** |
| --- | --- |
| **Color** | What color to set the grid vertices to use. |
| **ColorSet** | Color set to utilize. |
| **Font** | The name of the font to use for this control. |
| **FontSize** | The point size of the font to use |
| **FontStyle** | The name of the font style to use. Valid styles are: **"Shadow", "Glow", "Stroke"** |
| **SelectedTextColor** | The color of text to use when in a "selected" state. |
| **TextAnchor** | Anchoring within the grid. (Default is centered, e.g., “C,C”). |
| **TextColor** | Color to set the text, use to override the general "Color" tag that effects the button's vertices as well as the text color. |
| **TextOffset** | Offset (in pixels) for the text. |
| **String** | Contents of a text label. (Default is blank.) |
| **ToolTip** | Tool tip string |

**LUA Methods**

All the methods in <Button> as well as:

| **Function** | **Returns** | **Arguments** | **Description** |
| --- | --- | --- | --- |
| **DoAutoSize** | void | bool | Perform an auto size |
| **GetText** | bool |  | Obtain text in the child text control |
| **GetTextControl** | bool |  | Obtain the child text control |
| **LocalizeAndSetText** | bool |  | Set the text of the text control after going through the localizer system. |
| **SetSizeToText** | void | width, height | Set the backing grid of the button to the size of the text field inside of it, with additional width and height padding. |
| **SetSizeVal** | void | width, height | Override to set the size by value. |
| **SetText** | void |  | Set the text of the text control |
| **SetTextureOffset** | void |  | Clear the registered callback function. |
| **SetTextureOffsetVal** | void |  | Set an offset of the grid. |