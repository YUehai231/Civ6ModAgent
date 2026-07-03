---
title: "SimplePullDown"
category: "Forge UI Controls"
summary: "<SimplePullDown> Wednesday, May 18, 2016 2:33 PM Simplified version of <PullDown> or \"drop down box\" control.  XML Configuration is identical to <PullDown> except for one additional attribute docum..."
keywords: ["simplepulldown","forge","controls","lua","xml","control"]
---

# SimplePullDown

<SimplePullDown>

Wednesday, May 18, 2016

2:33 PM

Simplified version of <PullDown> or "drop down box" control. XML Configuration is identical to <PullDown> except for one additional attribute documented below. Made for tools in the interest of rapid UI development.

**XML**

| **Attribute** | **Details** |
| --- | --- |
| **EntryInstance** | The ID of the instance to use for building entries |

**LUA Methods**

| **Function** | **Returns** | **Arguments** | **Description** |
| --- | --- | --- | --- |
| **SetEntries** | void | Table entries, uint selected | The entries table should be an array of tables. Each table represents an entry for the pulldown and must contain a "Text" value. |
| **ClearEntries** | void |  | Remove all entries |
| **SetSelectedIndex** | void | uint selected, bool callback | Sets the selected entry by index. If callback is set to true then the entry selected callback will be called if the selected index has changed. |
| **GetSelectedIndex** | uint |  |  |
| **GetSelectedEntry** | Table |  | Will return the table provided in SetEntries for the selected entry |
| **SetEntrySelectedCallback** | void | function | The entry selected callback will be called when the selected entry changes. The callback will be passed the table provided in SetEntries for the selected entry. |
| **CalcuateInternals** | void |  | Calculates the size and contents of the grid, scroll panel, and stack. |
| **ClearEntries** |  |  | Remove all entries |
| **ForceClose** | void |  | Hides the grid and it's pieces |
| **GetButton** | Button |  | Obtain component piece |
| **GetGrid** | Grid |  | Obtain component piece |
| **GetScrollPanel** | ScrollPanel |  | Obtain component piece |
| **GetStack** | Stack |  | Obtain component piece |
| **IsOffBottom** | bool |  | Is the pulldown showing above the open button because of limited room? |
| **IsOpen** | bool |  | Are the child elements showing. |
| **SetDisabled** | void | bool | Enable or disables the control |