---
title: "Slider"
category: "Forge UI Controls"
summary: "<Slider> Friday, February 21, 2014 5:03 PM The slider control is used for both picking a value along a spectrum volume slider and as the scroll bar for scroll panels.  The background is built from ..."
keywords: ["slider","forge","controls","control"]
---

# Slider

<Slider>

Friday, February 21, 2014

5:03 PM

The slider control is used for both picking a value along a spectrum (volume slider) and as the scroll bar for scroll panels. The background is built from one Grid, and the Thumb is another.

For picking values, the thumb does not need to grow, but for a scroll bar we size the thumb based on the content of the scroll panel.

**Style** - The style attribute should be used to name a grid style to use for the background of the slider

****

**Gutter** - Gutter region to stop the slider before it reaches the ends of the background

****

**Vertical** - Flag to indicate that the slider moves up/down rather than left/right

****

**Length** - Size of the slider, in which ever direction the slider moves

****

**<Thumb>** - The thumb sub-control is itself a grid control and should also use a grid style