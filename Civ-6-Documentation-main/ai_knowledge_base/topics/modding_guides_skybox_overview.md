---
title: "SkyBox Overview"
category: "Modding Guides"
summary: "The Civ6 SkyBox system determine what is drawn off the edges of the map.  It displays a single texture that has this detail in it."
keywords: ["skybox","overview","modding","guides","artdef","blp","texture","reference"]
---

# SkyBox Overview

The Civ6 SkyBox system determine what is drawn off the edges of the map.  It displays a single texture that has this detail in it.

In order to modify this texture, you must create a new ArtDef with the ArtDef Template of "SkyBox".

The SkyBox template has one collection inside of it - named SkyBox.  This collection has one element inside of it.  This element must be named "SkyPlane".
The "SkyPlane" element has one reference in it - a BLP entry reference.  It draws its BLP from the SkyBox library.

See the "SkyBox Texture Mod" document for more information.