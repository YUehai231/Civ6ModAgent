---
title: "TabControl"
category: "Forge UI Controls"
summary: "<TabControl> Wednesday, May 18, 2016 3:08 PM Supports tab pages with buttons to switch between them.  The visual style of the buttons and tab pages is extremely open ended."
keywords: ["tabcontrol","forge","controls","lua","xml","control","reference"]
---

# TabControl

<TabControl>

Wednesday, May 18, 2016

3:08 PM

Supports tab pages with buttons to switch between them. The visual style of the buttons and tab pages is extremely open ended. No lua code is necessary for basic functionality. All configuration takes place in XML. Tab buttons are not necessary if you just want to change the selected tab from lua.

**XML**

| **Attribute** | **Details** |
| --- | --- |
| **TabContainer** | The ID of the control that contains the tab pages. The default value is "TabContainer". All children of this control will be considered tab pages. Tab pages can be any kind of control. The pages will be shown and hidden as they are selected. The tab pages will be referred to by their IDs. |
| **TabButtons** | The ID of the control that contains the tab buttons. The default value is "TabButtons". Any button within the control tree underneath this control that has an ID that starts with "SelectTab_" will be considered a tab button. It can be any kind of button control. The tab button IDs should be in the format "SelectTab_<tab page ID>". The functionality of the buttons will be handled automatically by the TabControl. Buttons will be in the "selected" state when their corresponding tab page is selected. Tab buttons are not necessary if you just want to change the selected tab from lua. |
| **SelectedTab** | The ID of the initial selected tab page. If this attribute is not used the first tab page will be selected by default. |

**LUA Methods**

| **Function** | **Returns** | **Arguments** | **Description** |
| --- | --- | --- | --- |
| **SelectTab** | void | ControlBase* | Select a tab by passing in a reference to the tab page control |
| **SelectTabByID** | void | string | Select a tab using its ID |
| **GetSelectedTab** | ControlBase* |  | Get a reference to the selected tab page |
| **GetSelectedTabID** | string |  | Get the ID of the selected tab page |
| **SetTabSelectedCallback** | void | function | The tab selected callback will be called whenever the selected tab is changed. The tab page and tab button will be provided to the callback as arguments. |