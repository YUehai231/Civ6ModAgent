---
title: "Tutorial"
category: "Forge UI Controls"
summary: "<Tutorial> Friday, February 21, 2014 2:21 PM Starts a section of controls that are triggered to be shown/hidden based on the tutorial system.  XML Attribute Type Details AlwaysShow Bool Debug attri..."
keywords: ["tutorial","forge","controls","lua","xml","control"]
---

# Tutorial

**<Tutorial>**

Friday, February 21, 2014

2:21 PM

Starts a section of controls that are triggered to be shown/hidden based on the tutorial system.

**XML**

| **Attribute** | **Type** | **Details** |
| --- | --- | --- |
| AlwaysShow | Bool | Debug attribute when live editing. When true, the control ignores the show/hide calls from the manager and will just always show itself. |
| ID | String | (optional) An ID for the tutorial control. If none is provided the first parent control that contains an ID will be set to the trigger list. |
| TriggerBy | String | Comma separated list of IDs that this tutorial control will react to. (The tutorial's ID is automatically added to the trigger list.) |

*Example:*

<Box        ID="DoSomethingArea" Color="0,255,128,100" Size="100,100">

<Tutorial>

<BoxButton ID="CloseTutorial" Color="255,0,0,200" Size="50,50" />                        

</Tutorial>                

<BoxButton ID="DoSomething" Anchor="C,C" Size="25,25" Color="200,200,200,200" />

<Tutorial>

<Box Color="0,0,255,200" Size="50,50" Anchor="R,B" />

</Tutorial>                

</Box>

-- LUA for the above XML:

Controls.DoSomething:RegisterCallback(Mouse.eLClick,function() UITutorialManager:ShowControlsByID("DoSomethingArea"); end);

Controls.CloseTutorial:RegisterCallback(Mouse.eLClick,function() UITutorialManager:HideControlsByID("DoSomethingArea"); end);

**LUA Functions**

| **Function** | **Returns** | **Arguments** |
| --- | --- | --- |

Currently tutorial controls do not have function on themselves, other than what they inherent from ControlBase.

Be careful using Show/Hide as Tutorial controls should only be shown/hidden via the manager's calls or there is a possibility their visibility state will be out-of-sync with the manager.

The tutorial manager has functions that act on tutorial controls (as well as other controls with matching IDs)

UITutorialManager:ShowControlsByID("MyControlIDorTrigger");

UITutorialManager:HideControlsByID("MyControlIDorTrigger");

UITutorialManager:HideAll();