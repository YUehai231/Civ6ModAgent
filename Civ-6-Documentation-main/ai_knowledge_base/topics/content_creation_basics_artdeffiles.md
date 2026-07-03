---
title: "ArtDefFiles"
category: "Content Creation Basics"
summary: "Working with ArtDef Files ArtDef files are XML files that tell the engine how to use assets and entities packaged in BLP files.  ArtDef files reference XLP entries and add meta information needed b..."
keywords: ["artdeffiles","content","creation","basics","artdef","blp","xlp","xml","reference"]
---

# ArtDefFiles

Working with ArtDef Files

ArtDef files are XML files that tell the engine how to use assets and entities packaged in BLP files.

ArtDef files reference XLP entries and add meta information needed by the engine to correctly render the XLP entry. Because each engine system requires different information ArtDef files are structured differently for each system.

You can edit ArtDef files using the Asset Editor. Simply click the Open an existing art definition document and select the ArtDef file you wish to edit. Most of the ArtDef files you will need have been created already for you.

![](../ArtDefFiles/media/image1.png)

Generally, ArtDef files consist of **Collections** and **Parameters**. Collections are unbounded lists of elements which you create. Each element has a finite number of Parameters which you edit. An element can also contain one or more Collections.

![](../ArtDefFiles/media/image2.png)

A Collection can be identified by a triangle to the left of it, which is used to expand it. You can **right click** on a Collection and add a new element to it, which is automatically named after the Collection and appended a running count.

![](../ArtDefFiles/media/image3.png)

Parameters cannot be expanded and upon selecting them the right-hand pane allows you to edit their value. ArtDefs support different Parameter types:

- **Integer** (a whole number, e.g. 42),

- **Float** (a decimal number, e.g. 4.2),

- **String** (ASCII text, e.g. "forty two"),

- **Boolean** (true or false),

- **Enumeration** (drop-down selection from a pre-set set of values, e.g. 2 from 1, 2, or 3),

- **RGB** (red-green-blue color values 0-255 for each color, e.g. R:122 G:255 B:34),

- **2D Coordinate** (a two-dimensional coordinate along X and Y axes, e.g. X:0.5 Y:1.2),

- **BLP Entry** (the identifier from an XLP file referencing an asset or entity, e.g. Features_Marsh),

- **ArtDef Reference** (a reference to another ArtDef entry in the same file, e.g. Collection1), and

- **Collection** (an array of Parameters, e.g. [42, 13, 55]).

ArtDef files are parsed directly by the engine, so the only way to discover any mistakes made is to save your changes and run the game. ArtDef errors usually manifest through so-called assertions, which are pop-up dialogs with a red X. Usually they tell you what is wrong and sometimes even how to fix it.

![Machine generated alternative text: Assert Failed File: ..X..XSrcXAppXGraphicsXStrategicView.cpp Line: 1234 Expression: false Message: This is an assertion, please pay attention to what it says' Press Cancel to debug Press Try Again to ignore once Press Continue to ignore always Cancel Try Again Continue ](../ArtDefFiles/media/image4.png)