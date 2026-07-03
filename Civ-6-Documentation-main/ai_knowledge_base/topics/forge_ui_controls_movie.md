---
title: "Movie"
category: "Forge UI Controls"
summary: "<Movie> Friday, February 21, 2014 2:35 PM The <Movie> control formally part of Image is used to display a movie texture.  XML Attribute Details FlipX Horizontally flip the image FlipY Vertically fl..."
keywords: ["movie","forge","controls","xml","texture","control"]
---

# Movie

**<Movie>**

Friday, February 21, 2014

2:35 PM

The <Movie> control (formally part of Image) is used to display a movie texture.

**XML**

| **Attribute** | **Details** |
| --- | --- |
| **FlipX** | Horizontally flip the image |
| **FlipY** | Vertically flip the image |
| **LoopMovie** | If a Movie is specified, repeat the playing movie after it is done playing. |
| **LoopMoviemask** | If a MovieMask is specified, repeat playing the movie after it is done playing. |
| **MaskTexture** | The filename of a texture to use as an alpha mask. |
| **MaskTextureOffset** | The x,y offset (in pixels) into the mask texture. |
| **Movie** | A BINK (or other supported movie) to display in the image area. |
| **MovieMask** | A BINK (or other supported movie) to mask the displayed image. (A moviemask can be used to mask a movie!) |
| **NormalizedQuad** | Programmer flag. Indicates that there is not a 1:1 ratio of pixels:texels |
| **PointSample** | All images default to a point sampler, but if **False** then a linear sampling will be used instead. |
| **Rotate** | Rotate the texture on the quad (degrees) Note: In the current implementation, stretching will occur as the quad itself is not rotate. |
| **Scale** | Uniformly scale up the texture by a multiplier. (e.g., “1.5” will scale it up 150%.) |
| **StretchMode** | How to stretch the texture; one of the following values: **None**, **Uniform**, **Fill**, **Tile**, or **UniformToFill** |
| **Texture** | The filename of the texture to use. |
| **TextureOffset** | The x,y offset (in pixels) into the texture for where to start drawing. |
| **TextureOffsetUV** | The offset into the texture in UV coordinates. |
| **TextureSizeUV** | The size in floating-point UV texture coordinates to make this. |

**Example:**

<Movie Movie="Test.bik" Size="200,200" />

MovieControl