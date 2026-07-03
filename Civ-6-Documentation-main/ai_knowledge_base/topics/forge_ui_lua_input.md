---
title: "LUA Input"
category: "Forge UI"
summary: "LUA Input Wednesday, April 08, 2015 9:53 To receive input in a LUA context, set a function to be a callback handler.  The handler function should return true if the input was handled."
keywords: ["input","forge","lua","control"]
---

# LUA Input

LUA Input

Wednesday, April 08, 2015

9:53

To receive input in a LUA context, set a function to be a callback handler.

The handler function should return **true** if the input was handled.

The handler function should return **false** if the input was not handled or it was handled but should be considered by other inputs.

Once input is marked as handled (**true**), no other controls (or contexts) within that ***root*** context will receive input. But other controls/contexts within other ***root*** contexts will receive a chance to handle the input, despite if it was marked has handled (**true**) in a different root context.

*(NOTE: Root contexts are set via C++, chances are you are working within a single root context.)*

Only one input handler callback can be set per context.

There are two types of handlers that can receive input.

**Simple Handler**

The simple handler will callback when input occurs passing in 3 parameters:

**function InputHandler( uiMsg, wParam, lParam )**

The uiMsg will be the type of input (keyboard, mouse, pointer, etc…), wParam and lParam will be values that have meaning, based on the type of input that comes in.

To set the handler call **SetInputHandler()** on the context, passing in the name of function to receive input.

ContextPtr:SetInputHandler( InputHandler );

**Example**

function InputHandler( uiMsg, wParam, lParam )

if (uiMsg==KeyEvents.KeyDown) then

if (wParam==Keys.VK_ESCAPE) then

OnBack();

return true;

end

end

if (uiMsg==MouseEvents.MouseMove) then        

InspectWhatsBelowTheCursor();

return true;

end

return false;

end

ContextPtr:SetInputHandler( InputHandler );

**Extended Handler**

The extended handler works almost the same as the simple handler except that it receives a single parameter which is a table of input information:

**function InputHandler( inputStruct )**

The **inputStruct** is the same one as "**InputStruct**" defined in ForgeUI. It allows for detailed querying of the input through various functions.

To set the input handler:

| ContextPtr:SetInputHandler( | InputHandler, true ); |
| --- | --- |

**InputStruct** functions include:

| **Function** | **Returns** | **Description** |
| --- | --- | --- |
| GetFlags | number | Return the low level bit-flags the input system is using. |
| GetKey | number | Obtain the AppHost key code. |
| GetMessageType | number | The type of input message contained in this instance of the structure. Values include:  KeyEvents.KeyDown KeyEvents.KeyUp MouseEvents.LButtonDown MouseEvents.LButtonDoubleClick MouseEvents.LButtonUp MouseEvents.MButtonDown MouseEvents.MButtonDoubleClick MouseEvents.MButtonUp MouseEvents.PointerDown MouseEvents.PointerUp MouseEvents.RButtonDown MouseEvents.RButtonDoubleClick MouseEvents.RButtonUp |
| GetMouseDX | number | Obtain the horizontal delta for the mouse since the last frame of input. |
| GetMouseDY | number | Obtain the vertical delta for the mouse since the last frame of input. |
| GetTouchID | number | The unique ID associate with this touch generating an event. |
| GetWheel | number | Get mouse wheel value |
| GetX | number | Horizontal coordinate for this mouse or touch event. |
| GetY | number | Vertical coordinate for this mouse or touch event. |
| IsShiftDown | bool | Is the shift key held down? |
| IsControlDown | bool | Is the control key held down? |
| IsLButtonDown | bool | Is the left mouse button (or touch equivalent) down? |
| IsRButtonDown | bool | Is the right mouse button down? |
| IsMButtonDown | bool | Is the middle mouse button (commonly the mouse wheel) down? |
| IsAnyButtonDown | bool | Is the left, right, or middle mouse button down? |

**Example**

function KeyHandler( key:number )

if (key == Keys.VK_ESCAPE) then Close(); return true; end

return false;

end

function InputHandler( inputStruct:table )

local uiMsg = inputStruct:GetMessageType();

if (uiMsg == KeyEvents.KeyDown) then return KeyHandler( inputStruct:GetKey() ); end;

return false;

end

ContextPtr:SetInputHandler( InputHandler, true );