---
title: "PackagingAssets"
category: "Content Creation Basics"
summary: "Packaging Assets Once you have created an asset or freestanding entity, e. g."
keywords: ["packagingassets","content","creation","basics","blp","xlp","modbuddy","xml","texture"]
---

# PackagingAssets

Packaging Assets

Once you have created an asset (or free-standing entity, e.g. texture) you will need to package it in order for the engine to be able to load it.

The engine cannot load loose files. All assets and entities have to be "cooked" into a **Binary Library Package (BLP)**, which is a binary file format that contains processed art data organized for fast loading during engine startup.

**ModBuddy** contains the **Cooker**, which is a tool that takes assets and entities from your Mod, processes them according to the game configuration file, and writes the results to a platform-specific file (i.e. a Windows BLP won't work on iOS and vice versa).

The Cooker uses an **XML Library Package (XLP)** file to determine which assets and entities are part of a single BLP. The XLP file lists assets and entities from the Asset Cloud and assigns them identifiers (names). The engine as well as the remaining tools refer only to these identifiers, not the actual asset and entity names from the Asset Cloud.

Editing XLPs

In order to get a new art asset (or entity) into the game you will have to first package it:

- Open the Asset Editor.

- Most XLP files should already be created for you, so click the **Open an Existing XLP Document** button and select the XLP you wish to edit.

![](../PackagingAssets/media/image1.png)

- If you cannot find an appropriate XLP document talk with your lead to ensure that a new BLP is the appropriate place for your new assets.

- In the XLP click either the **Add Existing** button (if the asset or entity you want to add already exists in the Asset Cloud) or the **Add New** button (if the asset or entity you want to add does not yet exist in the Asset Cloud).

![](../PackagingAssets/media/image2.png)

- When you click the Add Existing button a new **Asset Browser** window pops up and allows you to select an asset or entity from the Asset Cloud.

<ul>
- The Asset Editor may ask you for confirmation that you wish to check out the XLP file from Perforce, which you should do.

- The newly added entry in the XLP will use the asset's or entity's name by default, which you may want to change.

- Once you have added all assets or entities you wish to add to the game to the XLP file be sure to **save** it and then navigate to **File > Cook** to update the BLP with your newly added changes.

- Pay attention to the Output window at the bottom to make sure the cook completed successfully.

</ul>

Creating New XLPs:

In most cases you probably want to use an XLP that already exists that is part of the system you're working on, but there are a couple of reasons you might want to create a new XLP:

- You might want to break apart the Entity packages into logical groups (i.e. you might have a separate for assets for a certain Era) for organizational purposes

- If you want to add content that is specific to a Game Mod or Expansion

- The system you're working in requires BLPs to be separated in such a way that they can be individually loaded (Like the leader system, which only loads the BLPs for leaders that are in your game)