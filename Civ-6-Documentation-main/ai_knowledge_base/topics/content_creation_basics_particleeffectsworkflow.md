---
title: "ParticleEffectsWorkflow"
category: "Content Creation Basics"
summary: "Simplified Particle workflow Monday, September 14, 2015 1:49 PM Since Particle effect Assets are fairly straight forward, the process of creating one will probably the same Until you start doing mo..."
keywords: ["particleeffectsworkflow","content","creation","basics","xlp","firetuner","animation","texture"]
---

# ParticleEffectsWorkflow

Simplified Particle workflow

Monday, September 14, 2015

1:49 PM

Since Particle effect Assets are fairly straight forward, the process of creating one will probably the same (Until you start doing more complex effects that combine multiple Particle effects, meshes, and animations).

You must still create your particle effect in Fork like you would normmally, but once you are ready to bring it into the engine follow these steps:

1. - Ensure that the Asset Cloud is running

- Open AssetEditor

- File > New > Asset

- Select ‘VFX’ Class Name

- Select ‘Particles’ tab

- Click ‘Add New’ tool strip button within ‘Particles’ tab to launch the Mini Importer

- Click the ‘+ Add Source File…’ and navigate to the desired .peb file and click ‘***OK***’

- Ensure that the .peb file selected appears within the text box within the Mini Importer and is checked. And click ‘Import’

<ol style="list-style-type: lower-alpha">
- If you are re-importing the .peb file you need to ensure that the ‘***Check Out***’ button is checked

<ol style="list-style-type: lower-roman">
2. Alternatively, if you are reimporting a .peb file, you can simply select the item within the ‘Particles’ tab and click the ‘Reimport’ tool strip button (it looks like the recycling sign).

</ol></li>
</ol>

![Machine generated alternative text: Cook Params Geometries Filter: Reimport Particle Name FX Cam fire2 Attac h ments Animations Pa rticles Behaviors ](../ParticleEffectsWorkflow/media/image1.png)

1. - Within the Asset Previewer (Window > Asset Previewer) you should see your see particle effect play at least once.

<ol style="list-style-type: lower-alpha">
- NOTE: That the tools team is looking into a bug where particle effects do not play when first added (mentioned above) and so you’ll need to click the ‘Recook’ button in the top left within the ‘Global Previewer Info’ section in order to see your changes.

</ol>
1. - If the particle effect looks correct within the ‘Asset Previewer’ then all that’s left to do is tweak the cook parameters within the ‘Cook Params’ section to your desired values. If the particle effect does not look correct (typically because of unbound textures), then you’ll need to open the .ptl file via this button:

![C:\6C2B1625\956122A8-36E4-41EE-B78C-8956EA84A4D0_files\image002.jpg](../ParticleEffectsWorkflow/media/image2.jpg)

1. - Within the .ptl document, you’ll want to take a look at the cook parameters and import any textures that are not bound. Because the tool automatically binds textures that have been imported previously, any unbound textures are new textures that need to be bound. You can bind the textures quickly using the below button and navigating to the named texture within your ArtDev directory:

![C:\6C2B1625\956122A8-36E4-41EE-B78C-8956EA84A4D0_files\image003.jpg](../ParticleEffectsWorkflow/media/image3.jpg)

1. - After all textures have been bound, your vfx asset should now look correct. After this point, you should you should be able to save both your .ptl and save your vfx asset to a new name (and you should be free to close the .ptl – you can re-open it later if you need to bind additional textures, but otherwise, you don’t need to keep it open).

- You can then go ahead and open the VFX.xlp and add the new asset there or you can open the particle effect in particle studio and tweak it further (using the tools hotload functionality to capture changes or reimporting manually).

- After you get things to where you’d like them, save all modified documents.

- If you’d like to see your changes in the game, you just need to ensure that you added your assets to the VFX.xlp and cooked the VFX.xlp (right-click Asset Cloud > Cook Local Assets… > Files… > VFX.xlp). Launch the game and you can use the Asset Preview tab within the FireTuner2 to plop down your vfx in the game.