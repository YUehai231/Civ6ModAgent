---
title: "Texture"
category: "Content Creation Basics"
summary: "Texture . tex Texture are the entities that represent pixel data, these are used for the different maps in a material, or they can be used for UI, or as sprites in the strategic view layer."
keywords: ["texture","content","creation","basics"]
---

# Texture

Texture (.tex)

Texture are the entities that represent pixel data, these are used for the different maps in a material, or they can be used for UI, or as sprites in the strategic view layer.

The engine currently supports two different source formats for creating Textures: TGA, and PSD. You can create textures using either the Asset Editor (one at a time) or using the Asset Importer (many at once as long as they come from the same source file).

Using the Asset Editor

The Asset Editor allows you to create one texture at a time by first creating the entity and then selecting the texture class and other parameters.

From TGA

- In the Asset Editor, go to **File > New**

- You'll be prompted to pick what type of file you'd like to create. Pick **Texture**, and hit **OK**

![](../Texture/media/image1.png)

- Now you need to pick the Class for the texture you're creating by selecting it from the **ClassName** dropdown

![](../Texture/media/image2.png)

- Now you need to assign your source file to the texture, so click on the **Source File Path** line and the browse button will appear. click the and it will bring up a browser where you can navigate to your .tga file

![](../Texture/media/image3.png)

- Once you pick a source file, you'll see the **Name** of the Texture change to match the name of the source file, it will also attempt to import the source file at this point.

- If you want you can change the **Name** of the texture to whatever you want

- At the bottom of the window you can also tweak the Texture's Export Settings

- Finally you need to save your Texture by going to **File > Save**