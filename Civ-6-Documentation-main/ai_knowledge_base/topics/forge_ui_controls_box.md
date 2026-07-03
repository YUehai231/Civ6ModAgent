---
title: "Box"
category: "Forge UI Controls"
summary: "<Box> Friday, February 21, 2014 2:21 PM Box of solid color.  Also <ColorBox> but that is deprecated."
keywords: ["forge","controls","lua","xml"]
---

# Box

**<Box>**

Friday, February 21, 2014

2:21 PM

Box of solid color. (Also <ColorBox> but that is deprecated.)

For an empty region, use **<Container>** instead.

**XML**

| **Attribute** | **Type** | **Details** |
| --- | --- | --- |
| Color | String | Values (0-255) for red, green, blue, and (optionally) alpha, separated by commas. e.g., an orange color: "255,128,0,200" |

**LUA Functions**

| **Function** | **Returns** | **Arguments** |
| --- | --- | --- |
| **SetColor** | **n/a** | **uint**, Either a single ABGR or RGBA value to represent the red, green, blue, and alpha values. By default uses ABGR. This can be changed to RGBA if the ForgeUI manager is called once at startup with **SetColorFormatRGBA(true)**. |