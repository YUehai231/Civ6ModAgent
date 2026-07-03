---
title: "Iteration"
category: "Content Creation Basics"
summary: "Iterating on an Entity Once you've imported an entity into the Asset cloud, there are a few ways of updating it if you make changes to the original source file File Watches Whenever you open an ent..."
keywords: ["iteration","content","creation","basics","xlp","animation","reference"]
---

# Iteration

Iterating on an Entity

Once you've imported an entity into the Asset cloud, there are a few ways of updating it if you make changes to the original source file

File Watches

Whenever you open an entity in the Asset Editor, it creates a file watch on the corresponding source file, so that if you have the instance open in the editor it will attempt to reimport the entity every time it detects a change in the source file. It will also place a watch on any entities that compose the one you have open, so if you open an Asset, it will place file watches on all the entities that compose it.

You can see a list of all the File Watches in the Asset Editor by looking at the File Watches Tab which by default is at the bottom of the editor. If it's not there, you need to enable it by going to **Window > File Watches**

![Machine generated alternative text: AssetEditor - D:XprojectsXBALW-AGOULD Civ6 mainXCiv6Xpa Edit View Window Lig hting_ P robe.geo Basic Name Class Name Desc ri pticn C ategorization Tags Groups Source Source File Path Source Object Imported Time Exported Ti me Data Data Files File Watches Unit Path (I items) Unit items) D:XprojectsXBALW-AGOULD Civ6 1/1/0001 AM 1/1/0001 AM Relative Path Lig hting_P robe.gr2 GR2 CIVE mainlCIvBpantryXGeomethesXLighting_Probegeo D AprojectsXBALW-AGOLlLD CIVE main* DevXLjghtingXHeIper ObjectsXLjghting Probe.max ](../Iteration/media/image1.jpg)

Manual Reimport:

Sometimes if the File watch doesn't successfully detect your change, or if you made a change to your source file without the entity open in the tools.

You have two options:

1. - Open the Entity that you need to reimport and go to '***File > Import***' (CTRL + SHIFT +I), or hit the Import button on the top toolbar

![Machine generated alternative text: AssetEditor - Edit D:XprojectsXBALW-AGOULD Civ6_mainXCiv6NpantryNGeometriesX16 Scouts.geo View Window tilebases.xlp 16 Scouts Unit en Source file 16_Scouts.geo Asset Pr. 16 Scouts.ast* Basic Name Class Name Desc ri pticn ](../Iteration/media/image2.png)

1. - If the Entity you are trying to reimport is being referenced by another Asset or Entity, find where the entity is being referenced, and there will usually be a button to reimport it somewhere near by:

1. - ![Machine generated alternative text: Categorization (I items) items) Tags Groups Mesh O Unit Animations chments A Group Particles Behaviors Material v State ](../Iteration/media/image3.png)

*For Geometries, Animations and Particles in an Asset the button is here*

1. - ![Machine generated alternative text: Groups o Unit -0 items) (128128) Black Base_CoIor (2048x2048) Material Test Linear Gradient (512x512) Cook Parameters Value 3aseCcIcr Gloss Metal ness Normal Seperate_AO TintMask ](../Iteration/media/image4.png)

For Cook Parameters (which can be any kind of entity) the button is here