---
title: "ScrollPanel"
category: "Forge UI Controls"
summary: "<ScrollPanel> Friday, February 21, 2014 5:04 PM The scroll panel has a large panel with a smaller viewport into that space.  AutoScrollBar Flag to indicate that we should automatically hide the scr..."
keywords: ["scrollpanel","forge","controls","lua","control"]
---

# ScrollPanel

<ScrollPanel>

Friday, February 21, 2014

5:04 PM

The scroll panel has a large panel with a smaller viewport into that space.

**AutoScrollBar** - Flag to indicate that we should automatically hide the scroll bar when the internal size is equal to the viewport size and scrolling is not necessary.

****

**HideScrollBar** - Flag to never show the scroll bar.

****

**Vertical** - Flag to indicate that we scroll up/down rather than left/right

***NOTE* for some reason the default is horizontal, this needs to be set to true in order for a vertical scroll panel to properly clip**

****

**FullClip** - By default we only clip the visuals in the direction which we scroll, this flag indicates that we should clip in both dimensions.

****

**Sub-Controls:**

**<UpButton>** - Sub-control which defines the button to scroll up

****

**<DownButton>** - Sub-control which defines the button to scroll down

****

**<ScrollBar>** - Sub-control which defines the slider used to move the panel

**LUA**

| **Function** | **Returns** | **Arguments** |
| --- | --- | --- |
| **CalculateSize** | **void** |  |
| **CalculateInternalSize** | **void** | **DEPRECATED** |
| **GetScrollValue** | float | .. |
| **SetScrollValue** | void | Float (0.0-1.0) |
| **GetUpButton** |  |  |
| **GetDownButton** |  |  |
| **GetRatio** |  |  |
| **RegisterScrollCallback** |  |  |
| **RegisterUpEndCallback** |  |  |
| **RegisterDownEndCallback** |  |  |