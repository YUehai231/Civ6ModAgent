---
title: "UnitPreviewingScript"
category: "Content Creation Basics"
summary: "<h1 id=\"civ6unitpreviewingscript\">Civ 6 Unit Previewing Script</h1> This is how to load a Unit from the game with Culture Variants and props into the Asset Editor From the asset Editor Top Menus se..."
keywords: ["unitpreviewingscript","content","creation","basics","artdef","animation"]
---

# UnitPreviewingScript

<h1 id="civ-6-unit-previewing-script">Civ 6 Unit Previewing Script</h1>
This is how to load a Unit from the game with Culture Variants and props into the Asset Editor

From the asset Editor Top Menus select File\Run Script

Select Preview_Unit.py in the ..\Steam\steamapps\common\Sid Meier's Civilization VI SDK\AssetModTools\AssetEditor\Scripts directory

![](../UnitPreviewingScript/media/image1.png)

Select your UNIT in the 'Pick the Unit' popup and click OK button

![/download/attachments/267366110/image2018-8-29_13-12-36.png?version=1&modificationDate=1535563264137&api=v2](../UnitPreviewingScript/media/image2.png)

Select your CULTURE in the 'Pick the Culture' popup and click OK button

![/download/attachments/267366110/image2018-8-29_13-13-9.png?version=1&modificationDate=1535563264120&api=v2](../UnitPreviewingScript/media/image3.png)

This will open the Unit_Bins.artdef, Units.artdef and a random Armor Asset of the unit you picked.

This also Attaches a Hat, Weapon, Head\Hair combo and body based off of the variations defined for unit and Culture.

Here is the example for Redcoat\European

| ![/download/attachments/267366110/image2018-8-29_13-13-57.png?version=1&modificationDate=1535563264103&api=v2](../UnitPreviewingScript/media/image4.png) | ![/download/attachments/267366110/image2018-8-29_13-14-41.png?version=1&modificationDate=1535563264090&api=v2](../UnitPreviewingScript/media/image5.png) |
| --- | --- |

***** NOTE ***** Cultural Skin color tinting will not be represented here. An example is that African and Middle Eastern bodies will only show up in the default Pink skin color. BUT the actual Head will be pulled from the defined set of Cultural Heads for that culture, but just not the right skin color. Below shows the correct Head for an African Archer ... just not the correct skin color.

| ![/download/attachments/267366110/image2018-8-29_16-15-12.png?version=1&modificationDate=1535573712693&api=v2](../UnitPreviewingScript/media/image6.png) | ![/download/attachments/267366110/image2018-8-29_16-14-21.png?version=1&modificationDate=1535573661457&api=v2](../UnitPreviewingScript/media/image7.png) |  |  |
| --- | --- | --- | --- |

Oddly in the right-hand side Archer unit tab under its *TRANSFORM* tab is where you can change the tint color. Tint is always White as a default. **BUT** that's not all ... It tints the Head, Boday and the Armor. **NOT** the hands

| ![/download/attachments/267366110/image2018-8-29_16-23-48.png?version=1&modificationDate=1535574228177&api=v2](../UnitPreviewingScript/media/image8.png) | ![/download/attachments/267366110/image2018-8-29_16-26-4.png?version=1&modificationDate=1535574364447&api=v2](../UnitPreviewingScript/media/image9.png) |
| --- | --- |

**OK**

Now if you want to edit this unit's Timeline you will need to open its Behavior. In this case it is the Redcoat.bhv

| ![/download/attachments/267366110/image2018-8-29_13-17-34.png?version=1&modificationDate=1535563264090&api=v2](../UnitPreviewingScript/media/image10.png) | ![/download/attachments/267366110/image2018-8-29_13-17-43.png?version=1&modificationDate=1535563264057&api=v2](../UnitPreviewingScript/media/image11.png) |
| --- | --- |

Once that is loaded you can edit the timeline while the bhv is selected. Plus play the animations.

Have at it!