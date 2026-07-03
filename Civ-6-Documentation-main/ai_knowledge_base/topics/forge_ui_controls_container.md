---
title: "Container"
category: "Forge UI Controls"
summary: "<Container> Friday, February 21, 2014 1:50 PM The <Container> is the most basic control in the system.  All other controls extend this and so all of these tags are usable on all other controls."
keywords: ["container","forge","controls","lua","xml","animation","screen","control"]
---

# Container

<Container>

Friday, February 21, 2014

1:50 PM

The **<Container>** is the most basic control in the system. All other controls extend this and so all of these tags are usable on all other controls. It is most useful for making a group of controls that can be shown/hidden easily. It is likely more useful to the UI Programmer than the UI Artist.

Class name ControlBase.

**XML**

| **Attributed** | **Details** |
| --- | --- |
| **Alpha** | A 0-1 value used for the alpha for this control AND all of its children. |
| **Anchor** | Where on its parent this control is attached. |
| **AnchorSide** | Whether the control is attached to the Inside or Outside of its parent (in X and Y). |
| **AutoSize** | 0, 1, V or H. If 1 control will completely autosize. If 0 it won't at all. If V will only autosize vertically. If H will only autosize horizontally. Autosizing is based on the total size of its children. This will only happen at load time. If the children are changing sizes, the programmer must call DoAutoSize() at runtime. |
| **AutoSizePadding** | The amount of padding in X,Y to add when doing the AutoSize calculation. Formally “**Padding**”. |
| **Color** | What color this control should be. The scale is 0-255, can include an alpha channel, and can use a named color. This is not used for all control types and only affects this control, not its children. |
| **ConsumeAllMouse** | Flag to indicate that this control should consume all mouse events that happen while it is being moused-over. |
| **ConsumeMouseButton** | Flag to indicate that this control should consume mouse button events that happen while it is being moused-over. |
| **ConsumeMouseOver** | Flag to indicate that this control should consume mouse move events that happen while it is being moused-over. |
| **ConsumeMouseWheel** | Flag to indicate that this control should consume mouse wheel events that happen while it is being moused-over. |
| **d** | 1-6, or "*" and an optional "+". Set debug flags. 1-6 will set a color. "*" will pick a random color. "+" will cascade to child controls. This attribute is purposely lowercase and a single letter so a author can add/remove quickly. |
| **Disabled** | Flag to indicate that this control is disabled and should not get mouseover state or be clickable. |
| **GlobalUpdate** | Programmer flag. Used to make controls receive update ticks even when invisible. |
| **Hidden** | Whether this control (and all of its children) should be drawn. |
| **HideOnMouseOver** | Flag to indicate that this control should only be visible when its parent is NOT being moused-over. |
| **ID** | The controls name. Used by the programmer to work with this control at runtime. This value must be unique. |
| **InnerOffset** | Used with AutoSize |
| **InnerPadding** | Used with AutoSize |
| **NeedsMouseOver** | Programmer flag. Indicates that the control needs mouse information. |
| **NoClip** | Flag to indicate that this control is not affected when put inside of a scroll panel. |
| **Offset** | How far away from the anchor point the control is. |
| **ShowOnMouseOver** | Flag to indicate that this control should only be visible when its parent is being moused-over. |
| **ShowOnMouseOut** | Similar to HideOnMouseOver but will not show the contents when first visible. Best utilized for mouse out animations. |
| **Size** | The size on screen in pixels. |
| **SizePadding** | Alt name for “**AutoSizePadding**” (see above). |
| **ToolTip** | Simple tooltip text string when mousing over this control. |
| **ToolTipType** | Name of a complex tool tip type to use when mousing over this control. |
| **TutorialActive** | This control, and its children, will show on top of the tutorial overlay and be responsive to input. Essentially, when a tutorial is on, this control continues to behave as it normally would. |

**LUA**

| **Function** | **Returns** | **Arguments** | **Description** |
| --- | --- | --- | --- |
| **RegisterMouseEnterCallback** |  |  |  |
| **RegisterMouseExitCallback** |  |  |  |
| **RegisterMouseOverCallback** |  |  |  |
| **(RegisterWhenClippedCallback)** | float | void | WARNING! This is per-frame and likely the most expensive of any LUA operation. You will hurt performance by using this and it's very likely this function will go away. Don't use it. |
| **RegisterWhenShown** |  |  |  |
| **RegisterWhenHidden** |  |  |  |
| **SetColorByName** | void | string | Sets the color of the control based on a name from the color atlas. |
| **SetHide** | void | bool |  |
| **SetOffsetVal** | void | float x, float y |  |
| **GetOffsetVal** | float x, float y | .. |  |
| **SetSizeVal** | void | float x, float y |  |
| **GetSizeVal** | float x, float y | .. |  |
| **SetAnchor** | void | String - See *'Anchor'* attribute |  |
| **SetDisabled** | void | bool |  |
| **SetHide** | void | bool |  |
| **SetSizeX** | void | float |  |
| **SetSizeY** | void | float |  |
| **GetSizeX** | float | .. |  |
| **GetSizeY** | float | .. |  |
| **SetOffsetX** | void | float |  |
| **SetOffsetY** | void | float |  |
| **GetOffsetX** | float | .. |  |
| **GetOffsetY** | float | .. |  |