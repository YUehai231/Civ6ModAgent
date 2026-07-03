---
title: "LUA Conventions"
category: "Forge UI"
summary: "LUA Conventions The below conventions are highly recommended to those writing LUA script which are for Forge.  Use Havokscript type qualifiers Havokscript offers an extension to LUA where variables..."
keywords: ["conventions","forge","blp","lua","xml","texture","screen","control","reference"]
---

# LUA Conventions

LUA Conventions

The below conventions are highly recommended to those writing LUA script which are for Forge.

Use Havokscript type qualifiers

Havokscript offers an extension to LUA where variables can be defined as taking a type (number, string, boolean, ifunction, table).  When possible, use a strongly typed define to potential reap the Havokscript benefits of: preventing invalid types to be assigned, faster execution, less memory.

*Example*

local numPlayers     :number = 0;

local isReady        :boolean = false;

local data           :table = {};

local callback       :ifunction = nil;

Naming LUA variables

Scope

**Use “m_” to prefix variables scoped to a file.**

At a glance shows meaningful scope of a variable and helps to prevent function vs file name collisions.

*Example:*

local m_currentPlayer;

**Use “g_” to prefix variables of global scope.**

Variables without “**local**” that are accessible globally (when included) have their scope known with “g_”.

*Example:*

g_debugColor :number  = 0x3344ffee;

Constant Naming

| **Prefix** | **Suffix** | **Type** | **Example** | **Description** |
| --- | --- | --- | --- | --- |
| COLOR_ |  | number | COLOR_FILTERED_NOT | ABGR color number. |
| m_debug |  | * | m_debugOutputInfo | A setting for some debugging feature. |
| PIC_ |  | string | PIC_MARKER_PLAYER | Name of a texture (either loose .DDS or ID in BLP) |
| SIZE_ | _X | number | SIZE_MIN_SPEC_X | Size in pixels for a width. |
| SIZE_ | _Y | number | SIZE_MIN_SPEC_Y | Size in pixels for a height. |
| TXT_ |  | string | TXT_TO_BOOST | A constant localized string that has been obtained via Locale.Lookup() |

Variable Naming

| **Prefix** | **Suffix** | **Type** | **Example** | **Description** |
| --- | --- | --- | --- | --- |
| cached |  | * | m_cachedPathUnit | A check value that is used locally to prevent extraneous computations and/or C++ calls. |
| e |  | number | m_ePlayer | A C++ enumeration (typically 0 based, with -1 being invalid) |
| k |  | table | m_kFilters | Generic LUA table. |
| k | IM | table | m_kEraLabelIM | Table acting as an Instance Manager (helper for dynamically creating instances of controls for use in a pooled structure.) |
| m_ |  |  |  |  |
| max |  | number | m_maxColumns | Highest number for a range of values. |
| min |  | number | m_minMoves | Lowest number for a range of values. |
| p |  | table | pInputStruct | Table created from C++ (likely has C++ method calls off of it) |
| is |  | boolean | isHandled | Generic boolean |
| ui |  | table | m_uiEraLabels | Table that holds references to UI controls created dynamically. |
|  | Control | table | civTextControl | A UI control instance |

Function Naming

Functions should be in PascalCase; where the first letter of each word is capitalized; avoiding underscores unless part of a group of similarly called functions.

| **Prefix** | **Suffix** | **Example** | **Description** |
| --- | --- | --- | --- |
| On |  | OnPlayerElected | Function which acts as an Event, LUAEvent, or UI callback. |

Define an Initialize function

The equivalent of a CTOR for a LUA context, is having an “Initialize” function, defined near the bottom of the file and executed on context load.

This is useful when initialization off of the file scope may be difficult to determine, especially if it occurs across many lines and the file is particularly large.

*Example:*

function Initialize()

    -- Do setup stuff

end

Initialize();

Place UI callback linkages in Initialize()

Formally UI events linkages were defined immediately after the function they call. This made it more difficult to determine what callbacks were wired up to XML.

*Example:*

function OnExitButtonPressed()

    ExitScreen();

end

function Initialize()

Controls.ExitButton:RegisterCallback( Mouse.eLClick, OnExitButtonPressed);

end

Event Registering

Place broadcast callbacks at the bottom of the file in an “Events” section in Initialize().

These events are either raised by other files (LuaEvents), or the C++ side, and they broadcast so there may be more than one listener, even in the same file.

*Example:*

function Initialize()

    -- Events

    ContextPtr:SetInitHandler( OnContextInitialize );

    ContextPtr:SetRefreshHandler( OnRefresh );

    Events.CitySelectionChanged.Add( OnCitySelectionChanged );

   Events.LocalPlayerTurnBegin.Add( OnLocalPlayerTurnBegin );

Events.UnitOperationsCleared.Add( OnUnitOperationsCleared );

LuaEvent.TestPanel_AllSectionsClosed.Add( OnAllSectionsClosed );

end

LUAEvents

Name based on the context from where its raised

In order to know who may be raising a LUA event, name the event based on the context that raises it.

If the same event could be raised from two different contexts, the event should either be considered to be moved into the engine or they should be broken out as 2 separate LUA events. 

This mitigates the confusion as to which LUA event is being raised from where in terms of logic being applied to the UI and simplifies debugging LUA event based issues.

*Example:*

LuaEvent.ActionPanel_OpenChooseResearch();  -- Raised from ActionPanel.lua for any listeners

Only pass simple types

Only strings, numbers, and booleans should be passed as arguments to a LUAEvent. A table can be passed as well, as long as it's not a table returned from the game engine nor a table that, somewhere, holds a game engine object. This includes UI objects.

On first glance it would appear to work but it's dangerous in that when the LUA context, which received the event, is working on the complex type passed in, it's possible for the owning context to have already deleted the backing to the object.

e.g., A button control, that was passed across contexts, will be working fine then all of a sudden become invalid when it's owning context cleans up.

Include Files

Any included files will have all contents copied into the local context. For this reason, include files should minimize any local variables and state utilized in them as this will increase size and could create potential name conflicts.