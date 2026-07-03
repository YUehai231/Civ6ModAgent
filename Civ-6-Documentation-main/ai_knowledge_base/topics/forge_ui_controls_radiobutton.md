---
title: "RadioButton"
category: "Forge UI Controls"
summary: "<RadioButton> Friday, February 21, 2014 5:01 PM A RadioButton control is very similar to the CheckBox and shares a lot of the same properties.  A RadioButton is used when the selected state is mutu..."
keywords: ["radiobutton","forge","controls","xml","texture","control"]
---

# RadioButton

<RadioButton>

Friday, February 21, 2014

5:01 PM

A RadioButton control is very similar to the **CheckBox** and shares a lot of the same properties. A RadioButton is used when the selected state is mutually exclusive with other RadioButtons that share the same group. This group is specified using the **RadioGroup** parameter. The name set in the RadioGroup must be the same between all radio buttons in this group.

| **Attribute** | **5** | **F** | **Details** |
| --- | --- | --- | --- |
| **RadioGroup** |  |  | Name of the mutually exclusive group of radio buttons |
| **BoxOnLeft** | N | Y | Replaces “**TextAnchor**”, if true places the box on the left of the text button, instead of to the right. |
| **ButtonSize** |  | Y | Size of the check button itself. |
| **ButtonTexture** |  | Y | Texture to use for the button |
| **CheckOffset** |  | Y | Coordinate for positioning the check over the button. |
| **CheckSize** |  | Y | Size of the check texture. |
| **CheckTexture** |  | Y | Texture to use as the check mark. |
| **CheckTextureOffset** |  | Y | Offset into the check texture. |
| **IsChecked** |  | Y | Flag indicating the box should start checked |
| **String** | Y | Y | Set the label |
| **TextAnchor** | Y |  | Anchor flag for the TextButton |
| **TextAnchorSide** |  | D | DEPRECATED Anchor side flag for the TextButton |
| **TextButtonData** | Y | Y | All of the tags used for the TextButton control are used here to describe the text button portion of the check box |
| **TextOffset** |  | Y | Offset of the TextButton portion from the check button |

**XML Example:**

<Stack ID="ListFilters" StackGrowth="Right" AnchorSide="I,O" Anchor ="C,T" Offset="0,0" StackPadding="10">

<CheckBox ID="MilitaryFilterCheck" RadioGroup="FilterGroup" ButtonTexture="CivicsGrid_Military.dds" CheckTexture="MainMenuCheckMark.dds" IsChecked="true" BoxOnLeft="true"/>

<CheckBox ID="EconomicFilterCheck" RadioGroup="FilterGroup" ButtonTexture="CivicsGrid_Economic.dds" CheckTexture="MainMenuCheckMark.dds" IsChecked="true" BoxOnLeft="true" />

<CheckBox ID="DiplomaticFilterCheck" RadioGroup="FilterGroup" ButtonTexture="CivicsGrid_Diplomatic.dds" CheckTexture="MainMenuCheckMark.dds" IsChecked="true" BoxOnLeft="true" />

</Stack>