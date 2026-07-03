---
title: "Grid"
category: "Forge UI Controls"
summary: "<Grid> Friday, February 21, 2014 2:27 PM Textured, 9slicable, dynamically sized control.  Attribute Details NoStateChange Flag that indicates that the texture should not be offset when used as a bu..."
keywords: ["grid","forge","controls","texture","control"]
---

# Grid

**<Grid>**

Friday, February 21, 2014

2:27 PM

Textured, 9-slicable, dynamically sized control.

| **Attribute** | **Details** |
| --- | --- |
| **NoStateChange** | Flag that indicates that the texture should not be offset when used as a button |
| **StateOffsetIncrement** | How far to offset the texture for state changes when used as a button |
| **Texture** | Filename of the texture to build the grid from |
| **SliceStart** | (optional) The x,y coordinates where a particular texture starts in an image sheet. If the entire image IS the texture, then this can be omitted. Default 0,0. |
| **SliceCorner** | An x,y offset from the start of the texture where to begin the 9-slicing. |
| **SliceSize** | Width and height of the actual 9 slice. (aka: Size of the center rectangle in the grid.) Default: 1,1. |
| **SliceTextureSize** | The width and height of the image from the texture. If omitted, assumes cutting is symmetrical. |

![SliceStart SliceCorner SlicerSize SliceTextureSize](../Forge UI\Controls\Grid/media/image1.png)