---
title: "Geometry"
category: "Content Creation Basics"
summary: "Geometry . geo Geometry files contain the 3D data used for units, buildings, leaders, etc."
keywords: ["geometry","content","creation","basics"]
---

# Geometry

Geometry (.geo)

Geometry files contain the 3D data used for units, buildings, leaders, etc. Currently we support importing geometry directly from 3DSMax and Maya

Structure of a Geometry File

Geometry files are organized in a very specific way that the engine relies on to be able to set up assets

- .Geo File

<ul>
- Model

<ul>
<li>
Mesh

<ul>
<li>
Triangle Group

- Mesh

- Triangle Group

- Mesh

- Triangle Group

- Triangle Group

- Mesh

- Triangle Group

</ul></li>
</ul></li>
</ul>

So every Geo File contains only a single Model, which is the logical grouping of all the Meshes in the Geo file, and each Mesh file can have any number of Triangle groups. When orienting a mesh, keep in mind that the pivot of the mesh will be set to 0,0,0 on export. This means that any desired offsets will have to be added to the mesh itself.![](../Geometry/media/image1.png)

However, any child objects of the top mesh in the hierarchy will retain their pivot offsets.

Using the Asset Editor

- In the Asset Editor go to 'File > New' and select Geometry from the list.

![](../Geometry/media/image2.png)

- In the Class Name dropdown select the class that you want (1). It can be tricky to change the class for entities after they are created, so try to make sure you have the correct class.

![](../Geometry/media/image3.png)

- Click on the line for '***Source File Path***' (2), and browse to the Max or Maya file that has your geometry.

- When you select your file, the editor will parse the file and find which models are available for export. This will fill out the '***Source Object***' dropdown (3) with all the available models for you to pick from, so click the dropdown and select the model object that you want.

- The '***Name***' (4)of the geometry will get set automatically to the name of the source object, but you can change it to whatever you want before saving.

- Go to "***File > Save***" and you're done.