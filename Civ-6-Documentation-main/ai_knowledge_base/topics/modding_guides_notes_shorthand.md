---
title: "Notes shorthand"
category: "Modding Guides"
summary: "The Civ VI engine and pantry makes it quite easy to create new units from existing pieces.  In this example, we are going to go through the process of creating a warrior clad in full armor that fig..."
keywords: ["notes","shorthand","modding","guides"]
---

# Notes shorthand

## Creating Units from Existing Pieces:

The Civ VI engine and pantry makes it quite easy to create new units from existing pieces.
In this example, we are going to go through the process of creating a warrior clad in full
armor that fights using a sword and shield.  We will create a new asset for the body (based
on existing geometry and materials), but everything else will be based on existing assets.

- Open up the asset that has the geometry you want to re-use.

- Determine what the geometry name is.

- Create a new asset of the same class as the existing asset.

- Go to the "Geometries" tab, and select "Add Existing".

- Browse for the geometry that you want (In this case, Knight_European_Armor_A).

- Add the geometry to the asset.

- Add the behaviors that you want to your asset.  (This example, Swordsman and SingleBiped_Deaths; ensure "Swordsman" behavior is topmost).