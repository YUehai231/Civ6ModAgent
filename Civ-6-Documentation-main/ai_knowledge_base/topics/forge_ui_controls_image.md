---
title: "Image"
category: "Forge UI Controls"
summary: "<Image> Friday, February 21, 2014 2:35 PM The <Image> control is used to display a texture.  XML Attribute Details ColorSpace default: \"RGB\", \"Linear\" Set this to \"linear\" if rendering a linear tex..."
keywords: ["image","forge","controls","xml","texture","icon","control"]
---

# Image

**<Image>**

Friday, February 21, 2014

2:35 PM

The <Image> control is used to display a texture.

**XML**

| **Attribute** | **Details** |
| --- | --- |
| **ColorSpace** | (default: "**RGB"**, "Linear") Set this to "linear" if rendering a linear texture onto the quad (e.g., using it as a Render Target) |
| **FlipX** | Horizontally flip the image |
| **FlipY** | Vertically flip the image |
| **Icon** | Calls the icon manager to obtain the icon specified. |
| **IconSize** | Specifies the width and height of the icon. |
| **MaskTexture** | The filename of a texture to use as an alpha mask. |
| **MaskTextureOffset** | The x,y offset (in pixels) into the mask texture. |
| **NormalizedQuad** | Programmer flag. Indicates that there is not a 1:1 ratio of pixels:texels |
| **Sampler** | Set this to "Linear" if you're scaling a block compressed image. It will try. |
| **Rotate** | Rotate the texture on the quad (degrees) Note: In the current implementation, stretching will occur as the quad itself is not rotate. |
| **Scale** | Uniformly scale up the texture by a multiplier. (e.g., “1.5” will scale it up 150%.) |
| **Size** | (Inherited from **Container**) Specify a size for this control; the texture will take up a portion (or all of it). This attribute is only ignored if the stretch mode is set to auto. |
| **StretchMode** | How to stretch the texture; one of the following values: **None, Uniform, Fill, Tile, TileX, TileY, UniformToFill, Auto** |
| **Texture** | The filename of the texture to use. |
| **TextureOffset** | The x,y offset (in pixels) into the texture for where to start drawing. |
| **TextureOffsetUV** | The offset into the texture in UV coordinates. |
| **TextureSizeUV** | The size in floating-point UV texture coordinates to make this. |

**Example:**

<Image Anchor="L,C" TextureOffset="0,0" AnchorSide="O,O" Texture="buttonsides.dds" Size="8,16" />

StretchModes work in the following manner:

None

- Displays the image at its normal size, clipping if necessary

Uniform

- Fills a portion of the control size with the entire image while maintaining aspect ratio. Image is not clipped.

Fill

- Stretches the texture image to fit within the size.

UniformToFill

- Fills the entire control size with the image while maintaining aspect ratio. Image may be clipped.

Tile

- Repeat the texture to fill a region.

TileX

- Just tile in the horizontal direction, clipping in the vertical direction if necessary.

TileY

- Just tile in the vertical direction, clipping in the horizontal if necessary.

Auto

- Resize the image control to whatever the native size of the texture is… the control will expand or shrink as necessary.