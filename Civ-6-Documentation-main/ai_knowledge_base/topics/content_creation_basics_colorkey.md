---
title: "ColorKey"
category: "Content Creation Basics"
summary: "Color Keys ColorKeys are not technically Assets, they are just loose entities specifically textures that are used by the game directly.  Viewing Color Keys in Game We now apply a color key to the w..."
keywords: ["colorkey","content","creation","basics","artdef","xlp","texture","screen"]
---

# ColorKey

Color Keys

ColorKeys are not technically Assets, they are just loose entities (specifically textures) that are used by the game directly.

Viewing Color Keys in Game

We now apply a color key to the worldview.  By default, it is turned off.  To turn it on, enter ‘colorkey’ <xxx> in the console, where <xxx> is the name of the color key you want.   To turn it back off, just type ‘colorkey’

To see a list of the available color key names, type ‘colorkey listnames’

Creating Color Keys

Step 0:  Capture a screenshot from the game using the console.   ‘screenshot colorkey’ or ‘screenshot colorkey noui’ 

![C:\0F89CE25\D7DEA720-039D-4E38-9029-D41134FF7220_files\image001.jpg](../ColorKey/media/image1.jpg)

This will create a screenshot with a color table embedded in it.  Open the screenshot file in photoshop.  Do whatever you want to it.  Anything that you do to the image

Will be reflected in the color table, as long as it is done to the entire image and not a subset of it.  Save the screenshot someplace in artdev so you can find it later.

Step 1:  Import the texture into the asset cloud

Open asset editor.   File->New.  You will be asked to pick an Entity type.  Choose texture.   Follow directions below:

- 1. Select ‘ColorKey’ from the drop down

- 2. Browse to the desired file

- 3. If the file is a PSD, select the appropriate group here

![](../ColorKey/media/image2.png)

Step 2:  Add the cloud texture to the color key package

Open Package -> ColorKeys.XLP.  (Located in <YOUR_PERFORCE_ROOT>/Civ6/pantry/XLPs)   Follow directions on image below to add the Colorkey to the XLP

- 1. Click the ‘add existing’ button

- 2. The Entry ID is a name by which the engine will refer to the color key. By default it’s the same name as the ColorKey, but you can change it if you want.

- 3. File->Save your file and then File->Cook. Your ColorKey is now ready to use.

![](../ColorKey/media/image3.png)

Step 3:  Iterating on it

         Open asset editor.  File->Open.  Open the colorkey that you want to change.    File->Reimport will reimport the texture from the original source file (assuming it can find it).  If the source file is checked into perforce under artdev, other people will be able to reimport it if they have synced.    If you have both the Colorkey texture and XLP open, the tools will do an automatic re-cook when a color key is re-imported.  If you also have the game open, it will hotload.    If any of the above do not occur, please let the tools team know.

Step 4: At this point The color key can now be called up by artdefs. Currently the ScreenWashEffects, and the GameLighting artdefs can take colorkeys to be used in the game.