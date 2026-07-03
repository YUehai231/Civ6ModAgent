---
title: "Debug Features"
category: "Forge UI"
summary: "UI Debug Features Friday, December 19, 2014 11:20 Debug XML Attribute All controls derive from <Container> in code this is \"ControlBase\" and on <Container> is a special attribute: \"d\", which stands..."
keywords: ["debug","features","forge","xml","texture","control"]
---

# Debug Features

UI Debug Features

Friday, December 19, 2014

11:20

**Debug XML Attribute**

All controls derive from <Container> (in code this is "ControlBase") and on <Container> is a special attribute: "d", which stands for "debug". When certain values are put into "d" it will display appropriate debug information for the control, and in some cases it's children.

**Attributes Values 1,2,3,4,5,6 and ***

Fast control bounds coloring based on which number is used or picks a random color if * is used.

**Attribute Value +**

Using a plus ("+") will tell ForgeUI to cascade whatever debug values are set on this control to its children.

**Attribute Value id**

If the lowercase letters "id" appears, then the identifier (if any) will be displayed in text in the upper left region of the control. Mousing over the text will display a tooltip (using the default style) of the control path.

**Examples:**

An example of using the "d" attribute for debugging.

Set d to a number 1,2,3,4,5 or 6

e.g., **d=”1”**

<Container   Anchor="R,T" Size="512,1" >

      <Image Anchor="R,T" Size="119,119" Texture="HUDBackingCorner.dds" **d="1"** />

      <!-- etc... -->

![C:\0FAAA085\222AE316-8AD0-43BE-AD7A-3B0A13BF93FC_files\image001.png](../Forge UI\Debug Features/media/image1.png)

 e.g, **d=”6”**

<Container   Anchor="R,T" Size="512,1" >

      <Image Anchor="R,T" Size="119,119" Texture="HUDBackingCorner.dds" **d="6"** />

      <!-- etc... -->

![C:\0FAAA085\222AE316-8AD0-43BE-AD7A-3B0A13BF93FC_files\image002.png](../Forge UI\Debug Features/media/image2.png)

Set d to a number and add a plus (“+”) afterward to cascade to children.

e.g., **d=”6+”**

<Container   Anchor="R,T" Size="512,1" **d="6+"** >

      <Image Anchor="R,T" Size="119,119" Texture="HUDBackingCorner.dds" />

      <!-- etc... -->

![C:\0FAAA085\222AE316-8AD0-43BE-AD7A-3B0A13BF93FC_files\image003.png](../Forge UI\Debug Features/media/image3.png)

Or instead of number just use an asterisk (“*”) and ForgeUI will cycle through 12 random colors:

e.g., **d=”*+”**

<Container   Anchor="R,T" Size="512,1" **d="*+"** >

      <Image Anchor="R,T" Size="119,119" Texture="HUDBackingCorner.dds" />

      <!-- etc... -->

![C:\0FAAA085\222AE316-8AD0-43BE-AD7A-3B0A13BF93FC_files\image004.png](../Forge UI\Debug Features/media/image4.png)

e.g., **d=”id”**

<Container  ID="CultureArea"    Anchor="R,T" Offset="100,0" Size="100,140" **d=”id”**>

  <Image                        Anchor="L,T" Offset="3,20"  Size="71,79"   Texture="TopBarRingCulture.dds">

    <Meter  ID="CultureMeter"   Anchor="L,T" Offset="7,17"  Size="56,56"   Texture="HUDTopBarCultureMeter.dds" />

  </Image>

</Container>

![cid:image001.png@01D01AF0.32FBA450](../Forge UI\Debug Features/media/image5.jpg)

Mouse over the text:

![cid:image002.png@01D01AF0.32FBA450](../Forge UI\Debug Features/media/image6.jpg)

e.g., **d=”id+”**

<Container  ID="CultureArea"    Anchor="R,T" Offset="100,0" Size="100,140" **d=”id+”**>

  <Image                        Anchor="L,T" Offset="3,20"  Size="71,79"   Texture="TopBarRingCulture.dds">

    <Meter  ID="CultureMeter"   Anchor="L,T" Offset="7,17"  Size="56,56"   Texture="HUDTopBarCultureMeter.dds" />

  </Image>

</Container>

![cid:image003.png@01D01AF0.32FBA450](../Forge UI\Debug Features/media/image7.jpg)

Combining IDs with coloring, and cascading:

e.g., **d=”id*+”**

<Container  ID="CultureArea"    Anchor="R,T" Offset="100,0" Size="100,140" **d=”id*+”**>

  <Image                        Anchor="L,T" Offset="3,20"  Size="71,79"   Texture="TopBarRingCulture.dds">

    <Meter  ID="CultureMeter"   Anchor="L,T" Offset="7,17"  Size="56,56"   Texture="HUDTopBarCultureMeter.dds" />

  </Image>

</Container>

![cid:image004.png@01D01B7B.A5DD3750](../Forge UI\Debug Features/media/image8.jpg)