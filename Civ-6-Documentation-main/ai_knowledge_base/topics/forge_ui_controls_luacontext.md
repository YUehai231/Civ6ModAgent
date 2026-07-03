---
title: "LuaContext"
category: "Forge UI Controls"
summary: "<LuaContext> Tuesday, March 04, 2014 4:48 PM Control to load a new . XML file of controls that is backed by a ."
keywords: ["luacontext","forge","controls","lua","xml","screen","control","reference"]
---

# LuaContext

<LuaContext>

Tuesday, March 04, 2014

4:48 PM

Control to load a new .XML file of controls that is backed by a .LUA scripting file.

When not the top level tag of the file (a root context), the following attributes are allowed:

**XML**

| **Attribute** | **Details** |
| --- | --- |
| **FileName** | Name of the xml file to load (without the .xml extension) |
| **ID** | (optional) An identifier for the LUA context |

**LUA**

Note: Since a Context is a ControlBase (e.g., <Container>), all LUA functions on a ControlBase can be used here as well. Below are the Context specific functions:

| **Function** | **Returns** | **Arguments** |
| --- | --- | --- |
| **BuildInstance** | nil | Creates an instance and attached is to the context as the parent. |
| **BuildInstanceForControl( name, outTable, parent)** | nil | Creates an instance and attaches is to a control. **name** is the string name of a control **outTable** is an (empty) table which will reference the control in LUA **parent** is an existing control that will be the parent of the newly created instance |
| **BuildInstanceForControlAtIndex( )** | nil | Creates an instance and attaches is to a control at a specified index. |
| **CallParentShowHideHandler( func )** | nil | DEPRECATED |
| **ClearRefreshHandler( )** | nil | Removes the refresh callback function. |
| **ClearRequestRefresh( )** | nil | Manually reset the flag that tells the context to refresh next C++ Update(). Note: this is internally (automatically) called after a refresh occurs. |
| **ClearUpdate( )** | nil | Clears the update callback function. |
| **IsHotLoad** | bool | Is the context in a hotload situation. |
| **LoadNewContext( nameAndPath )** | nil | Dynamically load a new context and make it a child of this one. |
| **Reload( )** | nil | Reload the context. |
| **RequestRefresh( )** | nil | Requests a refresh callback to occur on the next C++ Update(). |
| **SetAppLostFocusHandler( func )** | nil | Called when a player's OS focus of the application is lost. (Not supported on iOS). |
| **SetAppRegainedFocusHandler( func )** | nil | Called when a player's OS focus of the application is regained. (Not support on iOS). |
| **SetHideHandler( func )** | nil | Called when the context is made hidden. |
| **SetInitHandler( func )** | nil | Set a callback function when the first context has just finished initializing. The callback function will also be called when a hotload occurs. |
| **SetInputHandler( func, isUsingStruct )** | nil | func, A callback function it's method signature depends on whether the 2nd argument is true/false. bool, If false the function is expected to use the old, DEPRECATED, style of receiving input as 3 values. If true, the function will receive an input structure object. See *LUA Input* for more information. |
| **SetPostInit( func )** | nil | Sets a function to call after the C++ Initialize() has completed. |
| **SetRefreshHandler( func )** | nil | Sets a callback function which will occur explicitly, once on C++ Update(). Used when a lot of values are changing but rather than realize real-time, a delay is fine; usually to prevent recomputing sub-pieces of a complex screen. |
| **SetShowHandler( func )** | nil | Called when the context is made visible. |
| **SetShowHideHandler( func )** | nil | DEPRECATED: single function called when context is shown/hidden. **WARNING**: This callback will not work if SetShowHandler or SetHidHandler are used. |
| **SetShutdown( func )** | nil | function, Will callback before the context shuts down. (e.g., will occur during a hotload) |
| **SetUpdate( func )** | nil | **WARNING**: Avoid using this function at all costs (check out refresh handler above), as this will call per C++ Update() which really does a number on fragmenting memory, since LUA loves to make many small allocations. A function to be updated each frame; where the function signature is: **function( fdTime )** Each frame **fdTime** will contain a number representing how long since the last update. |
| **UnifyClickAndTap( isUnified )** | nil | Set mouse clicking and finger tapping to be considered one and the same. |

Example:

**ContextPtr:ClearRequestRefresh( );**