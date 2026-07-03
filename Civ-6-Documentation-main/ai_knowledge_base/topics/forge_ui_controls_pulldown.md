---
title: "PullDown"
category: "Forge UI Controls"
summary: "<PullDown> Friday, February 21, 2014 5:06 PM Control for selecting one from a list of possible items aka: combo box XML Attribute Details AutoFlip Automatically flips the grid of the pulldown to be..."
keywords: ["pulldown","forge","controls","lua","xml","screen","control"]
---

# PullDown

<PullDown>

Friday, February 21, 2014

5:06 PM

Control for selecting one from a list of possible items (aka: combo box)

**XML**

| **Attribute** | **Details** |
| --- | --- |
| **AutoFlip** | Automatically flips the grid of the pulldown to be above the button, if it is rendered off the bottom of the window/screen area. |
| **AutoSizePopUp** | Flag indicating that the grid should be automatically sized to however many buttons are inside the pulldown. |
| **SpaceForScroll** | Flag indicating that the grid should reserve some internal space for the scroll bar. |
| **ScrollThreshold** | How large to allow the grid to grow before adding a scroll bar to the list. |

| **Child Tag** | **Details** |
| --- | --- |
| **<ButtonData>** | Sub-Control defining the button which opens the pull-down. Some type of **<Button>** should exist immediately within it. |
| **<GridData>** | (Optional) Defines the formatting grid used behind the controls when the pull-down is open. |
| **<ScrollPanelData>** | (Optional) A scroll panel which contains the sub-buttons when the pull-down is open. |
| **<StackData>** | The stack which contains the sub-buttons when the pull-down is open (mostly useful for changing the stack padding). |
| **<InstanceData>** | Template for what the sub-buttons will look like when the pull-down is in an open state. |

**LUA Methods**

| **Function** | **Returns** | **Arguments** | **Description** |
| --- | --- | --- | --- |
| **BuildEntry** |  |  | Add an entry. |
| **CalcuateInternals** | void |  | Calculates the size and contents of the grid, scroll panel, and stack. |
| **ClearEntries** |  |  | Remove all entries |
| **ForceClose** | void |  | Hides the grid and it's pieces |
| **GetButton** | Button |  | Obtain component piece |
| **GetGrid** | Grid |  | Obtain component piece |
| **GetScrollPanel** | ScrollPanel |  | Obtain component piece |
| **GetStack** | Stack |  | Obtain component piece |
| **IsOffBottom** | bool |  | Is the pulldown showing above the open button because of limited room? |
| **IsOpen** | bool |  | Are the child elements showing. |
| **RegisterSelectionCallback** |  | function | Callback to make after a selection is made. |
| **SetDisabled** | void | bool | Enable or disables the control |

**Example**

<PullDown ID="thePullDown" ConsumeMouse="0" Offset="0,0" Anchor="L,T" Size="200,50" AutoSizePopUp="0" SpaceForScroll="0" ScrollThreshold="200">

<Label Anchor="C,C" String="Click me to open!" ID="theLabel" />

<ButtonData ID="theButtonData">

<GridButton ID="theOpenCloseButton" Anchor="L,T" />

</ButtonData>

<StackData ID="theStackData" StackGrowth="Bottom" Padding="0" Size="200,500" Anchor="L,T" />

<GridData Anchor="L,T" Offset="0,100" />

<InstanceData Name="PullDownEntry">

<GridButton ID="Button" Size="200,100" Anchor="L,T" Style="BaseButton"/>

</InstanceData>

</PullDown>