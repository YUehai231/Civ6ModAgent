---
title: "Context"
category: "Forge UI Controls"
summary: "<Context> Friday, February 21, 2014 5:08 PM Control to load a new . XML file of controls."
keywords: ["context","forge","controls","xml","control"]
---

# Context

<Context>

Friday, February 21, 2014

5:08 PM

Control to load a new .XML file of controls.

This is also frequently the top level XML tag for a file; it's used differently based on where it's used.

When not the top level tag of the file, the following attributes are allowed:

| **Attribute** | **Details** |
| --- | --- |
| **FileName** | Name of the xml file to load (without the .xml extension) |

When it is the top level of a file these attributes can be used:

| **Attribute** | **Details** |
| --- | --- |
| **Layer** | (optional) Name of what rendering layer to draw on. Typically a game engine will be setup with named layers such as "Debug" or "Modal". If the attribute is omitted, all contents will be rendered to the default rending layer.
 This should NOT be used for Z-order sorting UI as there are a limited # of layers, and typically the only reason a UI elements needs to be on a specific layer is because a shader effect is being applied to the default layer. (e.g., Bluring out the game and UI when a pop-up occurs; the pop-up will be on a special "Modal" layer so the shader isn't applied to it, but all UI on the default layer will be blurred.) |