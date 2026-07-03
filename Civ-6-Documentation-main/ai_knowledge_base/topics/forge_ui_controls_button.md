---
title: "Button"
category: "Forge UI Controls"
summary: "<Button> Friday, February 21, 2014 4:43 PM Simple button control using a texture map.  When the button state changes, we offset vertically down the texture according to the StateOffsetIncrement val..."
keywords: ["button","forge","controls","lua","xml","texture","control"]
---

# Button

<Button>

Friday, February 21, 2014

4:43 PM

Simple button control using a texture map.

When the button state changes, we offset vertically down the texture according to the StateOffsetIncrement value in following order:

1. - Normal

- MouseOver

- ButtonDown

- Disabled.

If no StateOffsetIncrement is specified, we assume to be moving by the y-size of the control (There are very few cases where this would not be appropriate, so StateOffsetIncrement is usually not necessary).

**XML**

| **Texture** | File to use for the texture |
| --- | --- |
| **TextureOffset** | Offset within the texture |
| **States** | (default 7) The number of states on a button. Valid values are 2,4,5,7, and 8. The states are: 1=up, 2=over, 3=down, 4=disabled, 5=selected, 6=selected over, 7=selected down, 8=8 selected disabled |
| **StateOffsetIncrement** | How far to offset the texture for state changes. If this is not specified, it is assumed to offset by the y-size of the control. |
| **NoStateChange** | Flag that indicates that the texture should not be offset when state changes |
| **Sampler** | The sampler type to use to sample the texture. All images default to a point sampler, but we may specify "Linear" here if we want a non-point-sampled texture. |
| **String** | Text to appear on the button. |
| **ToolTip** | Tool tip string |
| **TextAnchor** | Anchoring flag for the text. |
| **TextOffset** | X,Y offset value for the text. |
| **Color** | RGB tint for the button. |
| **DisabledCallbacks** | Triggers input callbacks when disabled. |

****

**LUA Methods**

| **Function** | **Returns** | **Arguments** | **Description** |
| --- | --- | --- | --- |
| **ClearCallback** | void |  | Clear the registered callback function. |
| **GetVoid1** | void |  |  |
| **GetVoid2** | void |  |  |
| **IsTrackingLeftMouseButton** | bool |  |  |
| **IsTrackingRightMouseButton** | bool |  |  |
| **IsTrackingMiddleMouseButton** | bool |  |  |
| **IsTrackingTouch** | bool |  |  |
| **RegisterCallback** | void | state, function | Sets a LUA function to receive callbacks. State may be one of:  eLClick eRClick eMClick eLDbClick eRDblClick eMDblClick eTap eDblTap eWheel eMouseEnter eMouseExit |
| **ReceiveCallbacksIfDisabled** | void | bool | Sets whether input callbacks trigger when disabled. |
| **SetDisabled** | void | bool | Sets button to be in "Disabled" (note: from ControlBase) |
| **SetSelected** | void | bool | Sets button to be in "Selected Mode" |
| **SetVoid1** | void | bool/string/number | Set a value to be used in a return call. |
| **SetVoid2** | void | bool/string/number | Set a value to be used in a return call. |
| **SetVoids** | void | x2 bool/string/number | Set both of the values to be used in a return call. |

****

****

****