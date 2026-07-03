---
title: "TileBase"
category: "Content Creation Basics"
summary: "Tile Base Monday, March 30, 2015 3:54 PM The Tilebases in Civ 6 have a pretty complex pipeline in order to support the procedural building placement, as well as model and material sharing.  Each Ti..."
keywords: ["tilebase","content","creation","basics","artdef","blp","xlp","animation"]
---

# TileBase

Tile Base

Monday, March 30, 2015

3:54 PM

The Tilebases in Civ 6 have a pretty complex pipeline in order to support the procedural building placement, as well as model and material sharing. Each Tilebase is built out of a Base asset which has attachment point where other Tilebase assets get slotted into in the game.

![Machine generated alternative text: chm Point Attachment Asset (i.e.Tent 01) Base Asset (i.e. Encampment) chm Attachment Asset (i.e.Tent 01) Attachment Asset (i.e.Tent 01) Poin Attachment Asset (i.e.Tent 01) ](../TileBase/media/image1.png)

Following is a set of step to build a Tilebase asset. This is not the only way to build one, but this should explain all the pieces required and from there you can build them in the way that suits the needs of the Tilebase you are building

Prescribed Steps to build a Tilebase:

Step 1: Build your Max scene file:

Build your Max File. The Max scene should be composed of the pieces that the Tilebase is built from, and then copies of those objects, where each copy is named the same thing as the initial piece with a number added at the end. All the object copies should be parented under a root bone that is named the name of the Base Asset (Talk to your lead about what the naming conventions are). Here is an example of what your Max scene should look like:

![Machine generated alternative text: Select Display Edit Name Houseoos House007 LamppostOOI Lamppost002 Lamppost003 PineTreeOOI PineTree003 PineTree004 PineTreeoos PineTree006 PineTree007 PineTreeoog PineTreeOIO PineTreeSmaIOOI PineTreeSma11002 PineTreesma11003 PineTreeSma11004 PineTreeSma11005 PineTreesma11007 PineTreeSma11008 PineTreeSmaIIOOg House Lamppost PineTree PineTreeSmaII Workspace: Default (Perspective) (Realistic) These will become the attachment points of the Base Asset where the Attachment Assets will slot into These will become the Attachment Assets Autodesk 3 cls Max 2015 Tilebase_SampIeA55et.max 0/0 This will become the Base Asset ](../TileBase/media/image2.png)

Note: Keep in mind that the engine will try to help you by automatically assigning material to your assets if the name of the material assigned to them in Max/Maya matches the name of a compatible material in the Asset Cloud.

Once you have your scene laid out the way you want, you need to run the **'TileBase Cleanup'** script that will convert all the object copies into Points with the same name so that they get imported as bones into the engine rather than as meshes:

- Select the Root Bone/Point that has all the piece copies parented to it

- Run the '**TileBase Cleanup**' script which is under '**Civ 6 Tools**' (the image shows one way to get to the script)

- ![Machine generated alternative text: 10 Tilebase Cleanup Do Cleanup Undo Cleanup Utilibes Sets More... Asset ar owser Perspective Match Collapse Color Clipboard Measure MO bon Capture Rese t XF orm Flight Studio (c) MAX Script Open Listener New Script Open Script Run Script Utilities Civ S Tools Civ 6 Tools Amma bon Manager Model Manager Clean Scene TileBase Cleanup Close ](../TileBase/media/image3.png)

- Click the '**Do Cleanup**' button in the tool's dialog box.

- You will see a Point appear at the position of every object under the root.

- Save your Max file, it's ready to be imported into the engine.

Create an asset for each model in the Max File:

We have a script that will automatically turn each model in you Max file into an asset. Go to '***File > Run Script***' and load the script "***C:\Program Files\Civ6\Asset Cloud - Civ6\AssetEditor\Scripts\Create_Assets_From_Source_File.py***". The script will bring up a prompt asking for what asset class should the Assets be, select "**TileBase**" and click **'OK'**

![Machine generated alternative text: Please Pick the Asset Class to use This script wil create individual assets for each root model in one or more Max/Maya Please pick the classfor the assets you want to creatæ ASSET CLASS T,1eBase ](../TileBase/media/image4.png)

Then you'll be prompter by the Mini importer dialog. Click the "***+ Add Source File…***" button and navigate to your Max file in the file browser. The mini importer will then show you a list of all the models that it found in your Max file. By default it sets all of the to import, but if there is a model that you don't want to import then click on the checkbox to the left of it to disable the import for it. Each model will also show a dropdown on the right indicating what geometry class it should be. 3D models should be "***LandmarkModel***" and decal models should be set to "***DecalGeometry***". There is a dropdown at the top of the dialog that will let you assign a geometry class to all the models at once, simply pick the class from the dropdown and click the '***Apply to Selected***' button

![Machine generated alternative text: Mini Importer Entity Type: Geometry LandmarkWodeI Entity Nanne Sort by Name Select/DeseIect All house pineTree PineTreeSma City La m p zost I + Add Source File... Apply ta Selected Entity Class: Check Out All LandmarkModeI LandmarkModeI LandmarkModeI LandmarkModeI LandmarkModeI Impart. Cancel ](../TileBase/media/image5.png)

Depending on how may models are in your Max files this could take up to a couple of minutes, but once it's done it will prompt you to add the newly created Assets to an XLP. Click 'Yes Please…' and pick the XLP that you want to add your assets to. For now the tilebases are being added into the 'tilebases.xlp' file (check with your lead if you're unsure about this). Click 'Yes' when getting prompted to check-out the XLP file and then save the XLP file.

Create Attachment points on the base Asset:

Open up the base asset that was created by the script by going to '***File > Open Entity***' and finding your asset, selecting it in the browser and clicking '***OK***'.

Select the Attachments tab, and click the button to 'Add Attachment Points to all Bones'. This will automatically create an attachment point for every Bone/Point in the Base Asset (these were the bones that were created by the 'TileBase Cleanup' script in Max).

![Machine generated alternative text: Landmarks.aftdef tilebases.xlp (I items) Lamp Post. ast City.ast* Properties Name Class Name Desc ri pticn C ity Tile Base Particles C ategorization Tags Groups o Tile Base items) Geomet ries Attachments Cook Pa rams 0 001 Animations Filter: Add Attachment Points to all Bones Attachment Point Name A Model Instance ](../TileBase/media/image6.png)

Once the attachment points are created, save your Asset. You can test that the Attachment points and Attachment Assets by going to the Knobs on the right, selecting the tab for the asset (The one that has the same name as your asset followed by "_0") and click on the "***Attach by name***" which will slot in the Asset into their corresponding attachment points.

![Machine generated alternative text: Global Previewer Info Module Landmark Base Lighting Values Knobs Reset Camera Reset Lighting H ide Skybox Reset Camera Reset Lighting City_o DefaultGameEnviro.. I Add Asset ktach By Name Attachment Point HouseOOI PineTreeS mallOOI PineTreeSma11002 PineTreeS ma11003 Pi neTreeSma 11004 PineTreeS ma11005 PineT rees ma 11007 PineT rees ma 11008 PineTreeS mal 1009 Attac hed Asset ](../TileBase/media/image7.png)

This does not actually do the connection of the attachments, it's only to preview the attachments. The actual attachment hookups are done in the Landmarks.artdef file.

Hooking up the Attachment Assets to the Base Asset:

The Landmarks.artdef file is where the attachment are associated with the base asset .This information is stored in the artdef because it's possible to have the same Base asset have multiple different sets of attachments. For example Mines will probably use the same base asset, but have different mineral attachment assets associated with the different resource types it could be built on top of.

Because many of the Tilebase Assets have dozens of attachments setting up all the connections by hand can take a significant chunk of time, so there's a script that will automate that step for you. Go to '***File > Run Script***' and load the script "***C:\Program Files\Civ6\Asset Cloud - Civ6\AssetEditor\Scripts\Create_District_Base.py***". This will bring up a dialog prompt showing you a list of all the Assets in the tilebases.xlp file. Pick the Base Asset that you created before from the list and click '***OK***'. This will open up the Ladnmarks.artdef file for you and create the tilebase entry with all the attachments.

![Machine generated alternative text: BLP Entry Browser Name CityCent er_ Lg _ Test CityCenter Sm Test CityCent er_Test Asset Path DIS DIS DIS DIS DIS DIS DIS DIS DIS DIS DIS DIS DIS DIS DIS DIS DIS CTY AW CTY AW CItyCenter Sm Test CTY AW CItyCenter_Test DIS DIS DIS DIS DIS DIS DIS DIS DIS DIS DIS DIS DIS DIS Ancient Ancient Ancient Ancient Ancient Ancient Ancient Cross flag Lg aller Sm Banner Sm Filler Stone Patch Wood Ancient Ancient Ancient Ancient Ancient Ancient Ancient Cross flag Lg aller Sm Banner Sm Filler Stone Patch Wood CM p CM p CM p CM p CM p CM p CM p CM p CM p CM p CM p CM p CM p CM p Ancient Base 01 Ancient Base 02 Ancient _ Lg Filler Ancient Base 01 Ancient Base 02 Ancient Lg Filler Base Classical Base Industrial Classical Base Classical Base _ Temp _ Temp 02 Base Classical Base Industrial Classical Base Classical Base _ Temp _ Temp 01 02 ](../TileBase/media/image8.png)

As with the previous script, the more pieces there are associated with the Asset, the longer the script will take to process, but in the worst case it'll take a minute or so. You'll get a message box telling you the process was completed so that you know when it's done. Makse sure to Save the Landmarks.artdef file after the script is done.

Hook up the Asset into the game:

This process will be slightly different whether you are hooking up a Improvement/Landmark or a District.

**Landmark**:

If you don't have it open, you need to open the Landmarks.artdef file. On the left there's a tree list of the different entries that the game is using, expand the "***Landmarks***" list by clicking on the arrow to the left.

![Machine generated alternative text: AssetEditor - D. Edit View Landma rtdef* Alt Definition Template Landmarks Districts DEFAULT Window Open Source fil M M M M M M M CAMP CAMP CHATEAU FARM FISHING BOATS GOODY HUT LUMBER MILL MINE OFFSHORE OIL RIG OIL WEL PASTURE PLANTATION QUARRY STEPWEL ZIGGURAT Dis trictGenerators Tileaase Her08uiIdingTags Res ourceTags Cul tureTags EraTags UsageTags Globals CITY GL08ALS ](../TileBase/media/image9.png)

This will show you a list of the entries that are currently being used by the game. If the Asset you are working on doesn't have an entry for it yet you'll need to set it up. The instructions on hooking up an artdef entry to a gameplay element are here: Mapping GameCore IDs to ArtDef Entries. If you need help setting it up ask your lead or the pertinent programmer that's working on your system.

If the entry that you need is already there, expand it out and you'll see an entry under that called '***Eras***'. Click on the '***Eras***' entry (1), and on the right you'll a grid that maps the tilebase you just created with a specific era. If the Era you need is already there, just click on the '***Ref_LandmarkBase***' item and it will show you a dropdown where you can pick the tilebase that you created in the last step (2). If the Era that you need is not in the list, click the Add Element button on the top toolbar (3). This will add a new element to the grid, and you can set the 'Tag_Era' for it from the dropdown of available Eras and then assign the tilebase.

![Machine generated alternative text: AssetEditor - D:XprojectsXBALW-AGOULD Civ6 mainXCiv6Xpantry%ArtDefsXLandmarks.artdeff File Edit View Window Landma rtdef* Alt Definition Template Landmarks Open Source file Ref Landmark3ase VIL Tribal Thatch 01 v I Tag Era DEFAULT Filter: Name CAMP Erasl Districts Landmarks DEFAULT M M M M M M M CAMP CHATEAU FARM CMP CMP CMP CMP CMP CMP Ancient Base 01 Ancient Base 02 Base Classical Temp Base Industrial Temp Classical Base 01 Classical Base 02 FISHING BOATS GOODY HUT LUMBER ILL MINE OFFSHORE OIL RIG OIL WEL PASTURE PLANTATION QUARRY STEPWEL ZIGGURAT Dis trictGenerators Tileaase Her08uiIdingTags Res ourceTags Cul tureTags EraTags UsageTags Globals CITY GL08ALS ](../TileBase/media/image10.png)

**District**:

If you don't have it open, you need to open the Landmarks.artdef file. On the left there's a tree list of the different entries that the game is using, expand the "***Landmarks***" list by clicking on the arrow to the left.

![Machine generated alternative text: AssetEditor - D:XprojectsXBALW-AGOULD Civ6 mainXCiv6Xpa File Edit View Window Landma rtdef* Alt Definition Template Landmarks C.i3trict3 ACROPOLIS AERODROME AQUEDUCT CAMPUS CITY CENTER COMMERCIAL HUB ENCAMPMENT ENTERTAINMENT cot, HARBOR HOLY SITE INDUSTRIAL ZONE MBANZA NEIGHBORHOOD SPACEPORT THEATER DEFAULT DISTRICT DISTRICT DISTRICT DISTRICT DISTRICT DISTRICT DISTRICT DISTRICT DISTRICT DISTRICT DISTRICT DISTRICT DISTRICT DISTRICT DISTRICT DISTRICT Landmarks Dis trictGenerators Tileaase Her08uiIdingTags Res ourceTags Cul tureTags EraTags UsageTags Globals CITY GL08ALS ](../TileBase/media/image11.png)

his will show you a list of the entries that are currently being used by the game. If the Asset you are working on doesn't have an entry for it yet you'll need to set it up. The instructions on hooking up an artdef entry to a gameplay element are here: Mapping GameCore IDs to ArtDef Entries. If you need help setting it up ask your lead or the pertinent programmer that's working on your system.

If the entry that you need is already there, expand it out and you'll see an entry under that called '***BaseVariants***'. Click on the '***BaseVariants***' entry (1), and on the right you'll a grid that maps the tilebase you just created with a specific era, culture, and set of Hero Buildings. If the Era/Culture/HeroBuilding combination you need is already there, just click on the '***Ref_DistrictBase***' item and it will show you a dropdown where you can pick the tilebase that you created in the last step (2). If the combination that you need is not in the list, click the Add Element button on the top toolbar (3). This will add a new element to the grid, and you can set the Era/Culture/HeroBuidling for it from the dropdowns available and then assign the tilebase.

![Machine generated alternative text: AssetEditor - D:XprojectsXBALW-AGOULD Civ6 mainXCiv6Xpantry%ArtDefsXLandmarks.artdef File Edit View Window Open Source file Landmarks.artdef tilebas Alt Definition Template Landmarks Districts Tag Era DEFAULT DEFAULT DEFAULT MCDERN ARTERA MODERN ARTERA MODERN ARTERA_MODERN Tag Culture DEFAULT DEFAULT DEFAULT DEFAULT Ref District3ase DIS HBR Base Classical 01 DIS HBR Base Classical 02 DIS HBR Base Classical (B DIS 01 Filter: Name BaseVariantsOOI BaseVariants002 Var iants003 3aseVariantsDDS BaseVariants006 BaseVar iants007 Set Herc3uiIdings EMPTY LIGHTHOUSE LIGHTHOUSE SHIPYARD LIGHTHOUSE LIGHTHOUSE, SHIPYARD HTHOUSE SHIHARD. SEAPOR ACROPOLIS AERODROME AQUEDUCT CAMPUS CITY CENTER COMMERCIAL HUB ENCAMPMENT ENTERTAINMENT cot, HARBOR DEFAULT DISTRICT DISTRICT DISTRICT DISTRICT DISTRICT DISTRICT DISTRICT DISTRICT DISTRICT DISTRICT City CMP CMP CMP CMP CMP CMP Ancient Base 01 Ancient Base 02 Base Classical Temp Base Industrial Temp Classical Base 01 Classical Base 02 BaseVariants Bull dingVariants C:' BuildingSets DISTRICT DISTRICT DISTRICT DISTRICT DISTRICT DISTRICT Landmarks HOLY SITE INDUSTRIAL ZONE MBANZA NEIGHBORHOOD SPACEPORT THEATER Dis trictGenerators Tileaase Her08uiIdingTags Res ourceTags Cul tureTags EraTags UsageTags Globals CITY GL08ALS ](../TileBase/media/image12.png)

Save the artdef file once you're doing hooking up your asset. To see it in the game, you have to Cook the tilebases.xlp and then load up the game and build the tilebase you just added.

Check everything in:

Once you've verified that the tilebase is working in your asset the way you expect, you can either do that through Perforce directly or you can use the Asset Cloud