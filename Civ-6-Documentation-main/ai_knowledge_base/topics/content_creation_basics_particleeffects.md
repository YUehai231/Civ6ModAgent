---
title: "ParticleEffects"
category: "Content Creation Basics"
summary: "Particle Effects . ptl Thursday, April 09, 2015 3:14 PM Particle effects consist of the barebones data that is used by Fork to simulate the procedural animation of a particle system."
keywords: ["particleeffects","content","creation","basics","animation","texture"]
---

# ParticleEffects

Particle Effects (.ptl)

Thursday, April 09, 2015

3:14 PM

Particle effects consist of the barebones data that is used by Fork to simulate the procedural animation of a particle system.

Currently the engine is using Fork for its particle system so you must create your particle system in Fork's Particle Studio before bringing it into the engine.

Using the Asset Editor

- In the Asset Editor go to 'File > New' and select ParticleEffect from the list.

![Machine generated alternative text: aa Pick the file type to create Tenure Analytic Light File Type Entities Animation Environment I_jght Behavior Packages Material ](../ParticleEffects/media/image1.png)

- In the Class Name dropdown select the class that you want (1). Right now all VFX are using just the one 'VFXParticle' Class, but more classes might be created later on.

![Machine generated alternative text: AssetEditor - D. Edit View Window Open Source file VT Particle Effect.peb FT Particle Effect.ptr Basic Name Class Name Desc ri pticn C ategorization Tags Groups Source Source File Path Source Object Imported Time Exported Ti me Data Data Files Cook Parameters Value FT Particle Effect VFXParticle (I items) VFXParticle items) Path D:XprojectsXBALW-AGOULD Civ6 mainXArtDevXFunctionaITest 1/1/0001 AM 1/1/0001 AM Relative Path FT Particle Effect.psb FT Particle Effect Texture ](../ParticleEffects/media/image2.png)

-Click on the line for 'Source File Path', and browse to the .PEB file for your particle effect.

-Once you pick the source file, the 'Cook Parameters' tab will get filled out with the slots for all the textures and model that are used in your effect. If those entities already exist in the cloud, then they will get automatically assigned (3). If they don't exist you will have to create them by clicking the 'Add New' button (4) for each slot and importing the corresponding entity. Go here for further instructions on that.

- The '***Name***' (5)of the Particle Effect will get set automatically to the name of the source file, but you can change it to whatever you want before saving.

- Go to "***File > Save***" and you're done.