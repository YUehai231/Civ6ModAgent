---
title: "Unit Mods"
category: "Modding Guides"
summary: "Unit system...  unit system..."
keywords: ["unit","mods","modding","guides","artdef","xlp","xml","animation","texture"]
---

# Unit Mods

Unit system... unit system... How does one make a unit?

There's so much that goes into it!  Where to start?

Maybe at the core principles.

The Unit System in Civilization 6 has been designed to support a tremendous amount of unit variation.
This variation is achieved by utilizing an attachment style system.  Units don't exist as a single model
with a head, body, sword, shield, etc.  Each of the things that I listed are components of a unit, and they
can be put together piece by piece to compose a complete unit.

Units also have additional attributes that define how they behave in game that are also configured, such as what their
formations look like, how they fight, or how they move when escorting someone.  Each of these different categorizations
is a separate Root Collection in the Units ArtDef.

The unit with the most variation is the warrior, so let's start there.  The Warrior Unit has its formation set to the "Warrior"
Formation, it's UnitCombat set to the "Warrior" UnitCombat member, and its EscortFormation set to the "WarriorEscort" formation.
The unit members of the warrior Unit are of type "Warrior", with a scale of 1 and a count of 4.

All of these values are defined in other Root Collections of the Unit ArtDef.

The UnitMemberTypes defines what set of bins will compose a given unit.  The UnitMemberType has a Movement type, a Combat field,
a VFX MaterialType, and a VFXWeaponImpact type.  Additionally, it has a cultures children collection that defines what cultural variations
will exist for a unit.  All units should at least have the "Any" culture.  Additional cultural options include "Barbarian", "EastAsian",
"Mediterranean", "Mughal", "NorthAfrican", "NorthernEuropean", "SouthAfrican", and "SouthAmerican".  Each of these cultures has a
"Variations" collection.  Variations allow you to specify the scale of the unit variation, whether or not the variation is an attachment,
and attachments that the variation will make use of.  The Attachments child collection contains attachment definition elements.  These
elements have a Name (the name of the attachment), a "Point" (the attachment point in the root skeleton that the attachment will be attached
to), and a Tint (custom color scheme that will be used to tint the asset).  The attachment definition element also specifies one or more bins
from which to draw assets from.  These bins are defined as follows:  "Bin_Name/Group_Name".

## Unit Attachment Mods:

Units in Civ VI use attachments to be built compositionally.  Some of the easiest
things to change in the base game include swords, shields, and other attachments
that are used to compose units.

Swords and other unit attachments are Assets of the Unit class.  Unit asset classes
accept Geometries of the "Unit" Geometry Class, and Materials of the "Unit" Material
Class to bind to those geometries.  Typically, an attachment asset is composed of one
Unit Geometry (that contains the model information), with one Unit Material assigned
to that Geometry.

The majority of materials in Civ VI are based on PBR, so these materials slots for
an ambient Occlusion texture, an Albedo/BaseColor texture, a Gloss texture, a
Metalness texture, and a Normal texture.  These textures typically fall under a
"generic" texture class that is based on the given texture type.  (Look up PBR/Metalness
pipelines to understand how each of these texture slots are used).

Our material projects tend to be set up using DDO (by Quixel).  Each texture has its
own separate source file, which is a .tga file that is generated from DDO.  This is
not a requirement to authoring textures for our pipeline - just something that our
Art Team found useful.  If you have Photoshop installed, our texture pipeline supports
any texture that Photoshop supports.  Otherwise it supports 32-bit targa files.  There
are plans to add support for other source-file types in the future.

The easiest way to make a Unit Material is using the Asset Editor.  Open up the Asset
Editor (ensuring that the project you have selected in the upper right-hand corner is
your mod project).  Go to File -> New, and select "Material" from the list of options.
When the new material opens, first select a name for the material, and then change its
class to "Unit".

If the name of the material matches the name of the material/triangle group in the
geometry source file, when the geometry is assigned to the asset, its material will
automatically be bound.  Otherwise, you need to assign the material yourself
(explained below).

After changing the class of the material, you should see the Cook Parameters window
populate with various options.  In the Cook Parameters window, press "Add New".
Select the source files that you will be using for the individual textures in the File
Browser.  Once these are selected, press "Open".

This will bring up an assignment window.  In this window, you can assign each texture
to its corresponding slot.  Slots that are marked yellow indicate that an automatic
assignment could not be made.  Once all of the source files you want to import have
been assigned to a slot, press the "OK" button.  This will import the textures into
your pantry and then assign them to the appropriate slots in the material.  Once
this is done, press the "Save" button.  All of the textures that have been imported
have already been saved.

Now that the material has been created, it's time to create the Asset.  Go to
File -> New and select "Asset" from the choices.  Select a name for the Asset, and
then change its class to "Unit".  After changing the class to "Unit", choose the
appropriate DSG for the asset.  For attachments, this is typically the
"potential_any_graph" DSG.  The DSG should match the DSG of the asset that the
attachment is being attached to.  Save the Asset.

Now that the Asset has been saved, go to the "Geometries" tab and press "Add New".
This will populate a window allowing you to select a geometry source file.  Click
the "+ Add Source File..." button.  A list of models from the source file will he
displayed.  Select the model(s) that you want add to your Asset, and then press the
"OK" button.  The models will be imported.  Save the Asset.  Select the newly imported
Geometry in the Geometry tab.  In the "Mesh" window, under materials, press "Add
Existing", and select the material that you have already created.  Save the Asset.  Your
attachment asset now has been created.

The next step is to create (or modify) an XLP with the "Unit" XLP class.  Go to
File -> New, and select XLP.  Change the XLP class to "Unit".  Choose a package name
(it can be anything, though we try to make use of the xlp name is package name
paradigm).  Save the XLP.  Add the asset that you created above to the XLP.

The next step is to modify the *.Art.xml file that you have created for this mod project
to ensure that it contains the "Units" consumer and the "Unit" library.  Open up the
Project Builder tool.  Go to File -> Open, and select the *.Art.xml file that you have
created for this project.  If "Units" doesn't appear in the "Art Consumers" window,
select it from the drop down below the Add and Remove buttons.  If this drop down doesn't
appear, ensure that your mod depends on the Civ6 art project.

Now, go to Libraries.  If there is not a "Unit" library under the Libraries section, add
it now (again, using the drop down next to the Add/Remove buttons).  Then, select the Unit
library, and in the "Packages" section, press the Add button.  Browse to the XLP that you
created, and press "Open".  The package name that you chose will appear in the Packages list.

After saving the *.Art.xml file for your project, restart the Asset Editor.

The next step is to create (or modify) an ArtDef with the "Units" template.  Go to
File -> New, and select ArtDef.  Change the template to "Units", and then save the file.
Additionally, open the original ArtDef that defines the units you plan on modifying
(File -> Open ArtDef).  The definition for all base Civ6 units is found in the Civ6 Pantry,
with the name "Units.artdef".  The definition for base Civ6 Unit Bins is found in
Unit_Bins.artdef.

From here, there are a few options available, depending on the scope of changes that you are
trying to make.  I will start with the simplest example of adding a weapon to an already
existing bin.  In the mod ArtDef, go to the "UnitAttachmentBins" root collection, and add an
element.  Once the new element has been created, change its name to match the name in the
Unit_Bins.artdef collection (for example, if you are adding a generic melee weapon, change
the attachment bin name to "Weapons").  Then, click on the "Groups" tree node, and add a
group to the collection.  Change the name of the group to match the name of the group that
you are trying to extend (e.g. "Warrior").  Click the "Cultures" tree node, and add an
element to it.  Change the name of the new element to the appropriate culture, or "Any" if
you want this new weapon to show up on units of any culture.

With the "Assets" element selected, press the "Add" button to create a row in the GridView.
Ensure that the new row has a unique name, and then under the "Asset" section, browse for
the asset entry that you created above.

If you want to completely replace the set of weapons that a unit uses instead of adding a
new weapon that can be randomly selected, for each entry in the original bin, create a
corresponding entry with the same name as the original entry.  For each of these entries,
select the asset that you want it to point to.  These new entries will overwrite the
original entries listed in the Unit_Bins.artdef file.

Another way to completely replace the set of weapons that a very specific unit uses is to
create a new, uniquely named attachment bin element, with a new, uniquely named attachment
bin group.  Then, find the UnitMemberType that you are attempting to overwrite in the
original ArtDef (e.g. "Warrior").  Create a new UnitMemberType with the given name, and copy
all of the values from the original that you do not want to change (movement, combat, etc).

Select Cultures, and add a new culture (with the same name as the cultural variant that you
are trying to overwrite).  Select Variations, and create a new variation (with the same name
as the variation that you are trying to overwrite).  Expand the Variations to get the
"Attachments" node, and then create a new Attachment element.  Rename the attachment to the
type of attachment that you plan on overwriting (e.g., Armor, Body, Weapon).  Look at the
primary element, and copy the attachment point name where the asset gets assigned.  (e.g.
WeaponPrimary for Warrior -> Any -> BuffA -> Attachments -> Weapon).  Select a tint if
you desire.

Click on the "Bins" node, and press the Add button.  Set the name in the bin to the
<attachment_bin_name>/<attachment_bin_group>.  This will replace the attachment bin that
units from the given Cultural Variation will draw their attachments from.

## Creating New Units:

I recommend reading the guide about "Unit Attachment Mods" prior to reading the guide
on creating new units.  The Unit Attachments Mods guide contains information on how to
create Unit assets.  This guide will provide an extension to that.

As mentioned in "Unit Attachment Mods", Units in Civilization VI are composed together
from multiple parts.  This allows tremendous unit variation without requiring a tremendous
number of assets.  For an example of the number and variety of pieces that a unit can be
created from, open up the "Units.artdef" file in the Civilization VI pantry, and then expand
the "UnitMemberTypes" root collection.  Here you will see all of the units in the game
defined.  Look for a unit that is similar to the type of unit you want to create, select it,
and expand its tree nodes until you get to the leaves.  For this example, we are going to
look at the "Warrior" entry in the UnitMemberTypes.

When you expand the Warrior, and then Cultures node, all of the different cultural variations
of a Warrior are listed.  Each of these cultures has a distinct look for their warrior.
Within each culture is an additional variation of that culture.  For the warrior, most
cultures simply have a "BuffA" variation (named based on the body asset), but the Barbarian
culture also has a "HeavyA" variation, allowing barbarian warriors to look heavier than
warriors from other cultures.  What is common between each variation is the attachments that
they include.

Expand any of the variations, and its attachments collection, and a list of attachments will
be displayed.  Warriors are built using an Armor attachment, a Body attachment, a Hats
attachment, a Head attachment, a Necklaces attachment, a Skirt attachment, and a Weapon
attachment.  Each one of these attachments defines a point to which it is attached, a possible
tint (to help denote different cultures), and then a set of bins from which to draw assets from.

The "points" that are specified in the ArtDef correspond to joints on the root skeleton that
all body attachments come from.  All body attachments should come from one skeleton.  If you
have no desire to alternate heads, hands, etc, the entire body can be a single asset.  A unit
will be composed of one item from each attachment listed.  If you list only a single attachment,
the unit will be defined by that one attachment (for example, if you want to make a swordsman
that has his sword and shield on his primary body instead of attached using the attachment system).

So, in order to compose a new unit from component parts, select the granularity of the components
that you want, and then begin creating an asset for each component.  Assets should be added to a
units XLP, and the packages and ArtDefs should be added to the appropriate Library/Consumer,
as detailed above.

## Making your Units Move:

The Civ VI Pantry contains numerous animations that can be used out of the box so long as
the unit you are animating has a matching skeleton.  If the unit you are animating does
not have a skeleton that matches our canonical skeleton, or if you want to author your own
animations anyway, the engine provides ways to import animations from Max, Maya, and FBX
file formats.

In order to add animations to your unit, you must ensure that your unit has a DSG assigned
to it.  The DSG that is typically used for bipeds is potential_any_graph.  Other unit types
tend to use other DSGs.  Assigning a DSG populates the "Animations" tab with the animation
slots that the DSG exposes.  In order to bind an animation to a slot, click on the
"Animations" tab, select the slot that you want to bind an animation to, and click on the
"..." button that becomes available.

If you do not have any animations in your pantry yet, you can import new animations from
the Animation tab by selecting the "Add New" button, selecting an appropriate source file
that has an animation (Max, Maya, or FBX file), and then selecting the animation that you
want to import.  Once the animation has been imported, it will appear in the list of
animations when you click on the "..." button.

By convention, "Body" or "Armor" assets define the animation for the whole unit (unless
the unit is mounted - in which case the armor asset defines the animation for the rider,
while the mount unit defines its own animations).  Assets that have the parts of the
skeleton that will be animation should define the animations for a combined unit.

Once your animations have been added to your asset, switch the tab on the bottom of the
Asset Editor to the "Asset Trigger Editor" tab.  Then, press the "Add timelines for..."
button, which will add a timeline for every bound animation.  Then, save the asset.
Timelines allow you to define particle effects, sound effects, and lights on assets that
get played at particular times of a given animation.  These triggers can be transferred
to other assets using "Transfer" triggers (which is how the archer sends an arrow trail
out when it fires).

Units can also share animations between each other through behaviors.  A behavior is an
object that defines the DSG, a set of common animations, a set of common timelines, and
a set of common attachment points that gets shared between assets.  Behaviors can also
contain other behaviors.

An example of a re-usable behavior is the "SingleBiped_Deaths" behavior.  You can load
this behavior by going to File -> Open Entity, selecting the "Behaviors" item, and then
searching for it.  This behavior defines all of the common death animations that are
shared between bipeds.  It also defines attachment points on an arbitrary skeleton,
remapping bone names to attachment point names.  Any skeleton (geometry) that contains
bones with the names listed will automatically inherit the attachment points defined in
the behavior if the behavior is assigned to it.

The order of behaviors in an asset are important.  Behaviors are resolved bottom to top,
with the asset (and then the highest listed behavior) taking precedence.  If you assign
the "SingleBiped_Deaths" behavior to an asset, but want the "DeathBone" attachment point
to refer to a bone named "Head" instead of a bone names "Pelvis", you can create an
attachment point on the asset that has SingleBiped_Deaths equipped to it with the name
"DeathBone", and then assign it the characteristics that you desire.  When the asset is
cooked, the game will see the "DeathBone" defined by the asset, not by the behavior.