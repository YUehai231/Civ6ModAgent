---
title: "IconXML"
category: "Content Creation Basics"
summary: "<h1 id=\"iconpackagesandiconxmlcreation\">Icon Packages and Icon XML Creation</h1> Adding icons is a multistep process, certain steps can be skipped if a project or icon files have been setup.  Steps..."
keywords: ["iconxml","content","creation","basics","xlp","xml","texture","icon","control"]
---

# IconXML

<h1 id="icon-packages-and-icon-xml-creation">Icon Packages and Icon XML Creation</h1>
Adding icons is a multi-step process, certain steps can be skipped if a project or icon file(s) have been setup. Steps are the following:

1. - Create Icon Package(s)

- Add Icon Package(s) to project

- Edit Icon XML for icon entries.

<h1 id="create-icon-packages">1. Create Icon Package(s)</h1>
Open up **AssetEditor** and either open the existing Icons.xlp or create a new XLP by selecting File > New > "XLP" (under packages).

![/download/attachments/161288176/image2018-4-16_13-36-16.png?version=1&modificationDate=1523900176160&api=v2](../IconXML/media/image1.png)

Under the Entries list, choose the "Add New" icon to map an Icon file to a package name. The mapping of names is usually the same asset name as file name.

![/download/attachments/161288176/image2018-4-16_13-41-22.png?version=1&modificationDate=1523900482953&api=v2](../IconXML/media/image2.png)

Above here, the XP1_UnitActions80 EntryID is mapped the XP1_UnitActions80.dds file.

(The indexing for XP1_UnitActions80 icons are setup *in Expansion1_Icons_UnitActions.xml* explained in step 3.)

<h1 id="add-icon-packages-to-project">2. Add Icon Package(s) to project</h1>
Open up **Project Builder** and choose from the File menu "Game Art Specification" for that project.

For the base game this is in *$\Civ6\pantry\Civ6.Art.xml*

For XP1 this is in *$\Civ6\DLC\Expansion1\pantry\Expansion1.Art.xml*

For XP2 this is in *$\Civ6\DLC\Expansion2\pantry\Expansion2.Art.xml*

![](../IconXML/media/image3.png)

In the Libraries section, press "Add..." or select the existing "UITexture" Library. A list of packages will show up on the right:

![](../IconXML/media/image4.png)

Click the right-most "Add..." next to "Packages" and select the new XLPs.

<h1 id="edit-the-icon-xml-for-icon-entires">3. Edit the Icon XML for icon entires</h1>
<h2 id="step-by-step-guide">Step-by-step guide</h2>
1. - In the **IconTextureAtlases** section of the corresponding XML file, add an entry that maps from **texture asset name** (from package) to **atlas name**. This file may not exist, and will have to be created and then have its **IconTextureAtlases** section defined. You can map multiple textures of different resolutions to the same atlas name. The correct size will be chosen automatically based on the UI control size.

Example -

| <IconTextureAtlases>
 <Row Name="ICON_ATLAS_POTTERY" IconSize="32" Filename="TechPottery32"/>
 <Row Name="ICON_ATLAS_POTTERY" Iconsize="48" Filename="TechPottery48"/>
 </IconTextureAtlases> |
| --- |

Example with hand atlased texture -

| <IconTextureAtlases>
 <Row Name="ICON_ATLAS_TECH" IconSize="32" IconsPerRow="8" IconsPerColumn="8" Filename="Tech32"/>
 <Row Name="ICON_ATLAS_TECH" IconSize="48" IconsPerRow="8" IconsPerColumn="8" Filename="Tech48"/>
 </IconTextureAtlases> |
| --- |

2. In the **IconDefinitions** section, add an entry that maps **atlas name** to **icon name**. If the icon is hand atlased, you need to specify the atlas location **index**. The icon name is what is used to get the correct texture in the UI.

Example -

| <IconDefinitions>
 <Row Name="ICON_TECH_POTTERY" Atlas="ICON_ATLAS_POTTERY"/>
 </IconDefinitions> |
| --- |

Example with hand atlased texture -

| <IconDefinitions>
 <Row Name="ICON_TECH_MINING" Index="2" Atlas="ICON_ATLAS_TECH"/>
 </IconDefinitions> |
| --- |