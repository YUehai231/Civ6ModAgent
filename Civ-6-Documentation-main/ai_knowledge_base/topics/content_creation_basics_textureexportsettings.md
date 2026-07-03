---
title: "TextureExportSettings"
category: "Content Creation Basics"
summary: "Texture Export Settings Thursday, April 09, 2015 12:19 PM Pixel Format: This is the actual Texture data format that will get exported and used in the engine.  This is decided by the engineer that d..."
keywords: ["textureexportsettings","content","creation","basics","texture"]
---

# TextureExportSettings

Texture Export Settings

Thursday, April 09, 2015

12:19 PM

Pixel Format:

This is the actual Texture data format that will get exported and used in the engine. This is decided by the engineer that defined the class and is not modifiable at the import stage

Filter Type:

This is the algorithm that the cooker will use to generate the texture mip maps. Unfortunately it can be tricky to pick the right filter to use because they all have different performance characteristics that depend heavily on the type of content in the image (Some are better for texture with a lot of small details, while others are good for textures with sharp straight edges). The full discussion of what filter to use is beyond the scope of this documentation, but feel free to discuss it with your local graphics engineer if you're interested. By default we use the Box filter which will tend to make things look a bit blurrier at a distance, but it's very fast to compute, and does not tend to produce visual artifacts at a distance.

Sample From Top:

This is used to tell the Mip map generation step to calculate every mip based on the highest resolution rather than the mip step before it. Enabling it will generally produce slightly better results, but can become extremely slow to compute if the texture is large (over 1k per size)

Export Mode:

This lets you pick between the default texture export and mip generation or use the mips set up manually in the source file

![Machine generated alternative text: ](../TextureExportSettings/media/image1.png)

*This is how your source file how to look like when setting up manual mips.*

Use Mips:

I'm not sure what this does…

Number of Manual Mips:

If you've only created a certain number of mip levels manually you can set that number here.

Complete Mip Chain:

If you generated all the mips levels manually check this box, otherwise it will use the **Number of Manual Mips**

Value Clamp Max/Min:

This sets the maximum and minimum values that are allowed inside the texture, and it will clamp any pixels that go beyond those

Scale:

This lets you override the pixel size at which the texture will be exported (If you authored your texture at a really large size, but you don't mind it being scaled down before getting into the cloud)