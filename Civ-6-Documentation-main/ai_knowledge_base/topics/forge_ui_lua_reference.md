---
title: "LUA Reference"
category: "Forge UI"
summary: "LUA Reference Wednesday, October 08, 2014 3:12 PM Common attributes of a control can be changed and edited during runtime using specific methods in LUA.  For example, changing the size of a window,..."
keywords: ["reference","forge","lua","screen","icon","control"]
---

# LUA Reference

LUA Reference

Wednesday, October 08, 2014

3:12 PM

Common attributes of a control can be changed and edited during runtime using specific methods in LUA. For example, changing the size of a window, showing or hiding it, changing its screen location, etc. can all be done in this manner.

*Examples:*

Controls.MyControl:SetSizeVal(width, height);

Controls.MyControl:SetHide(false);

**Control Operations**

**ContextPtr:LookUpControl( path )**

Looks up a control based on it's placement in the UI control tree. If found returns the control itself; otherwise returns NIL.

The path uses forward slashes ("/") between contexts and controls in the tree.

If the context being used has to step up the tree, from where it's at, two dots ("..") can be used to jump up to the parent.

Wildcards via an asterisk ("*") can be used anywhere in the path except for the controls name. If there are more than two controls with the same name, the first control found with a matching name will be returned. When possible, avoid wildcard lookups, as they can be expensive.

**Examples:**

local a = ContextPtr:LookUpControl("/FrontEnd/FrontEndPopup/CloseButton"); -- Start at root

local b = ContextPtr:LookUpControl("../FrontEndPopup/CloseButton"); -- Go up one level from current context

local c = ContextPtr:LookUpControl("/FrontEnd/*/CloseButton"); -- Use a wildcard for a child context

local d = ContextPtr:LookUpControl("*/FrontEndPopup/CloseButton"); -- Use a wildcard from the root contexts

local e = ContextPtr:LookUpControl("*/*/CloseButton"); -- Multiple wildcards from the root contexts

local f = ContextPtr:LookUpControl("../FrontEndPopup/*"); -- NOT LEGAL, wildcards cannot be used for a control name

**String Operators:**

Commands that, when placed in a string, will result in special behavior.

| **[NEWLINE]** | inserts a carriage return into a string. |
| --- | --- |
| **[COLOR:ColorName] text string you want to color [ENDCOLOR]** | to dynamically set the color of a string of text to something other than the default. 'ColorName' is the name of the color defined in the project color atlas. |
| **[ICON_name]** | Pulls out a graphic "icon" from the Text Icon Atlas and inserts it into the text field. |

**Text and Localization**

**LocalizeAndSetText()**

Localize then set the text string on a control.

**SetToolTipString("myString")**

Set the text for the tooltip of the control.

**SetText("mystring")**

Set the text on a control.

**LocalizeAndSetToolTip("MY_TEXT_KEY")**

Localize then set the text for the tooltip of the control.

**Locale.Lookup("MY_TEXT_KEY")**

Convert the text key to its localized equivalent.

**Tutorial Manager**

**UITutorialManager:ShowControlsByID("triggerID")**

Turn on a control (or series of controls) that are listening for a certain trigger ID.

**UITutorialManager:HideControlsByID("triggerID")**

Turn off a control (or series of controls) that are listening for a certain trigger ID.

**UITutorialManager:HideAll()**

Turn off any/all tutorial controls.

**UITutorialManager:AddControlToAlwaysReceiveInput( control );**

Set a control to always be active (essentially ignore tutorial calls)