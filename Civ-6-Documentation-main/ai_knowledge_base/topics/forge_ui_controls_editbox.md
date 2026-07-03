---
title: "EditBox"
category: "Forge UI Controls"
summary: "<EditBox> Friday, February 21, 2014 2:25 PM Control for user entered text.  Attribute 5 F Details CallOnChar Y ?"
keywords: ["editbox","forge","controls","control"]
---

# EditBox

**<EditBox>**

Friday, February 21, 2014

2:25 PM

Control for user entered text.

| **Attribute** | **5** | **F** | **Details** |
| --- | --- | --- | --- |
| **CallOnChar** | Y | ? |  |
| **ColorSet** | - | Y | The name of the colorset to use. |
| **CursorColor** | Y | Y | Color of the cursor |
| **EditMode** | Y | Y | Flag to indicate this is for editing an existing string rather than entering a new string. EditMode caches the existing string when it takes focus and will restore the cached version if the esc button is pressed. EditMode also automatically calls the commit callback when the EditBox loses focus. |
| **FocusStop** | Y | Y |  |
| **Font** | - | Y | The name of the font to use for this control. |
| **FontSize** | - | Y | The point size of the font to use. |
| **FontStyle** | - | Y | The name of the font style to use. Valid styles are: **"Shadow", "Glow", "Stroke"** |
| **HighlightColor** | Y | Y | Color of the text highlight |
| **KeepFocus** | Y | Y | Flag to indicate this control should keep focus after the user enters text. |
| **MaxLength** | Y | Y | Maximum number of characters which can be entered. |
| **NumberInput** | Y | Y | Flag to indicate this entry box is only for numbers. |
| **Obscure** | Y | Y | Instead of showing what is entered, use a replacement character. |
| **HighlightOnFocus** | ? | ? | Automatically highlight all the text in the edit box when the box gets focus. Useful for text that should be copy/paste. |