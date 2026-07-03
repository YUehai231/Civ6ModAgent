---
title: "The Life of a Leader"
category: "Content Creation Basics"
summary: "/The Life of a Leader/media/image1. png Leaders make up arguably the most expensive aspects of Civ VI."
keywords: ["life","leader","content","creation","basics","lua","animation","texture","screen","control","layout","reference"]
---

# The Life of a Leader

![](../The Life of a Leader/media/image1.png)

Leaders make up arguably the most expensive aspects of Civ VI. Whether it be through the months it takes to create a fully animated leader, or the complexities of the different cultural costumes, Leaders are a challenge. Within this paper we hope to document the process of creating one of these guys the best we know how.

To begin the creation of such a complicated moving piece, we start like most other concepts in game development: a conversation.

**The Kick Off:
**

Once we have the idea of who the civilization is and who the leader for the civ will be, we sit down as a team and go over any and all ideas for production. During this time a rough sketch from concept (or a few) may be presented, and we discuss any and all ideas modeling and animation might have for this leader.

![](../The Life of a Leader/media/image2.jpeg)

The concept ref folder is very important. This is a folder of images collected by concept and is used throughout the pipeline. Within this folder are general cultural notes on clothing, color, and alternative pieces of props and items that modeling can sort through

![C:\Users\mkean\AppData\Local\Microsoft\Windows\INetCache\Content.Word\Capture2.png](../The Life of a Leader/media/image3.png)

**Voice Work:**

An incredibly important aspect of the pipeline often left towards the end is the VO recording of the leader dialogue. Once we have a personality established and an understanding of the general look of the culture, the writers go and begin assembling the script that the leader will say. The hope in this is that modeling will begin with the line recorded so that we hit the 3D part of the pipeline with all the information we need.

It is important to note here that design is set on the VO lines to be recorded. There should be no lines recorded that design is no longer considering or are ambivalent on. This way, down the pipeline, no time is wasted reviewing and choosing between lines that are not even an option.

![](../The Life of a Leader/media/image4.jpeg)

**Concept:**

Once the meeting is over, concept and modeling meet to discuss the next step forward. The usual next step is for concept to begin blocking the more final ideas.

When audition VO is recorded, Animation will start shooting test reference to explore ways in which the Leader might move and behave. This will help inform Concept as they finalize their ideas.

Once we really start to jive on where the concept is going it is presented for final feedback. Usually this is the hand-off stage, a place where modeling can begin. Here modeling deems if there is everything they need (or at least a good chunk of it there), to begin and if there might be any red flags. At this point we should all be on board with the general idea of who this leader is.

![](../The Life of a Leader/media/image5.jpeg)

**Final Concept?**

Though we try not to go back to 2D sketches very often, there are chances that concept will continue to refine ideas found within the concept, or attempt new color pallet ideas.

Modeling can pull from the new ideas if need be or use them to try out different versions of the final leader textures.

Also, at times, paint overs will be required for the block-in to feel right, these tend to become the base for more final drawings later on.

![](../The Life of a Leader/media/image6.png)

**Modeling:**

Starting with one of the base meshes we use for the leaders, modeling begins to block in a sculpt for which we can give rough feedback on. This block in usually includes a facial pass and a rough estimate of the forms of the clothing. We can begin to break things down here. We decide a bunch of things at this stage as well, like whether or not to use marvelous designer for the clothing, and how much will be done with substance. Usually at the point, during the translation of 2D to 3D the red flags will appear. Concept usually gets pinged again and we go back and forth a bit, but only if there is difficulties in the translation. Modeling attempts to have most forms blocked in rough. Better to have and not need than to miss something.

Once we are good with the blocking we begin the process of the final high poly. This is the stage in which the models become bit more realized. Within Zbrush we attempt to give some material definition in the sculpt itself (not too much as most of the heavy lifting will be done in substance) and clean up any gummy forms. Things are broken out and separated. The modeler begins to think about the low poly form and how he or she will retopo the pieces for the low poly.

Within this section are a many smaller tasks that don’t always happen on all the leaders. If marvelous designer was used, we then go in a cleanup those meshes, as they are usually triangulated and at a much high fidelity than what we can realistically render. One of the things we find is baked in wrinkles don’t look very good if they do not move. If the character has a lot of hard surface pieces (armor), then we begin to separate those out, and figure which parts will be separate or not.

![](../The Life of a Leader/media/image7.png)

Once we are happy with the high poly we begin the process of generating the lowpoly model. Though software may differ to retopologize, we generally either use topogun or Maya to model on top of the high poly.

![C:\Users\mkean\AppData\Local\Microsoft\Windows\INetCache\Content.Word\Capture.png](../The Life of a Leader/media/image8.png)

Items that may be mirrored and elements of UVing are thought about. Many times a back and forth is created between the high poly and low poly, reprojecting and adjusting the mesh to generate the cleanest model we can.

![C:\Users\mkean\AppData\Local\Microsoft\Windows\INetCache\Content.Word\Capture2.png](../The Life of a Leader/media/image9.png)![C:\Users\mkean\AppData\Local\Microsoft\Windows\INetCache\Content.Word\Capture2.png](../The Life of a Leader/media/image10.png)

Using a program like UV layout, we quickly jump back and forth between it and Maya, adjusting meshes as we go to get the cleanest UV’s as we can. UVs are done in a linear fashion

The reasoning here is that any and all stretching will be due to the mesh itself will not be noticeable. Also our texture pipeline deals mostly in tiling textures, so they tend to apply better when a linear UV is present.

Once the UVs are done and packed, we throw a Texel texture on there to makes sure everything is around the same density. I say around, because we do cheat at times cramming more detail into items we deem to be POI’s (points of interests). Any POI tends to get a little more Texel resolution.

We make our way over to marmoset where we begin our first HUB program. In our pipeline the art resources are captured into two HUB programs:

Marmoset for all highpoly and lowpoly bake meshes

Substance for all textures and source textures.

This keeps things clean and creates a “living pipeline”.

By this we mean that everything in marmoset is live-linked to the source assets location on the drive, so if that updates so does the marmoset scene, and that in turn cranks out a normal map in real-time, that is then pumped back into substance…etc. etc. Basically each adjustment we make can trickle through the texture pipeline with relative ease, though that’s not always the case.

![](../The Life of a Leader/media/image11.png)

Baking In marmoset is easy, and is one of the few programs (outside of Maya and substance) that the modeling team is hard locked into using. Bake consistency is everything, and being able to rely on the same kind of normal quality and Ambient occlusion quality (the two maps we bake) makes everything down the line that much easier. After grouping the high polys and the low polys in their respective groups it’s as simple as clicking “Bake” and then adjusting the automated cage mesh and normal skew using the brushed provided to create a clean bake.

![C:\Users\mkean\AppData\Local\Microsoft\Windows\INetCache\Content.Word\screenshot054.png](../The Life of a Leader/media/image12.png)

Continuing the modeling pipeline, we plug into substance the low poly and all the source textures we created (normal and AO) and use substance’s internal map converter to create the other maps need. Its cleaner this way, and smart materials assume these maps to be created in this fashion. Then it’s a generic substance workflow in which we are blocking in materials based on concept, and adjusting materials as we need them to be adjusted as ideas hit us. Because we have the civ tech shader inside of painter, this allows us to live a bit inside of substance before we make our way into the engine.

![](../The Life of a Leader/media/image13.png)

Using our premade civtech export preset, we export our textures after we have blocked them in a bit. After that we load up the asset editor and create a leader asset in the engine. This consists of us selecting the asset type and importing the geometry from Maya into the scene. Then we create a shader for the skin and clothing.

Once modeling sets this all up, we begin to go back and forth between the engine and substance, as all textures update live and can be iterated on fairly easily.

The leaders have two shader types for clothing, a cloth shader and an all-purpose uber-shader for everything else. The mesh definitions for these shaders are done in Maya, by assigning a material to the mesh. Each material in Maya is read as a material group and therefore able to have a material assigned to it.

This leads us to a textured version that is ready for initial feedback.

![](../The Life of a Leader/media/image14.png)

**Animation:**

Final VO has been recorded by now. Animators choose the lines they will use. Animators re-synch with writers and designers on VO choices. These VO lines and deliveries inform the animators on how to pose the leader in their base set.

**Poses to test:**

Arms across the chest, arms down by their sides, and hands clasped in front to check proportions and to make sure the Leader can look relaxed. This can result in model change requests

![TestPoses](../The Life of a Leader/media/image15.jpeg)

IK and FK switches with props, the torso twists and folds, foot roll, and finger skinning. We do a thorough investigation of every control on the body. Making a fist, facial poses, and mouth shapes. We need to see that the character can make a convincing O, M, and T shape, puff their cheeks, and close their eyes. We want to see that the eyebrows can make appealing shapes.

![Tshape](../The Life of a Leader/media/image16.jpeg)![Mshape](../The Life of a Leader/media/image17.jpeg)![OShape](../The Life of a Leader/media/image18.jpeg)![Eyebrows](../The Life of a Leader/media/image19.jpeg)

Animation starts to create and evaluate base idle poses with a functional rig. [happy, neutral, unhappy].

![](../The Life of a Leader/media/image20.png)

This is massively informative for a few reasons, such as seeing how the poses react to basic lighting and seeing how the proportions of the character hold up. Around this time, we all meet up and take a look at the poses and discuss changes that need to happen. As stated before, at time this includes modeling changes, as well as rig and weighting adjustments. Rigging and modeling might get another round of notes to finalize the rig.

Lighting does an initial pass here with the base poses.

![](../The Life of a Leader/media/image21.png)

The animator shoots reference video of VO lines and Base set using chosen idle poses. Acting choices are made and approved by Animation Lead.

**Blocking**

Blocking is when the animator picks their main poses out that describe the acting. They time these poses out approximately. While doing this process discoveries can be made about the limitations and differences between the rig compared to what the reference does. This is the part of the process where we can make big acting changes and timing changes. We can go back and re-shoot reference if needed.

Blocking passes can be in stepped mode or splined and smooth. The thing that makes them a blocking pass is that they lack the detail that a polished pass has. There may be some facial poses but not all. The points at which hands switch from IK to FK may NOT be smoothed. All we need to glean from the blocking pass is the animator’s intent.

**Splining**

After the animator has an approved blocking pass they go on to add in the detail. The lip synch is added, switches are smooth out, and hitches are cleaned up. Timing is tightened. If the blocking pass was in stepped mode the animator changes over to smooth splined. More transitional poses are added to better describe actions.

**Polish**

Now the animation is smooth and has everything it needs to make sense and be workable. What it lacks is the fine tuning. In the polish pass we take another visit to the eyes, the pupils, the eyebrows. We add in fine eye movements. We take another pass on the fingers to make sure all contact points feel believable. We make everything feel like butter

**Testing in Editor and Game**

Throughout animation process animation tests animations out in asset editor and game. This makes sure we are seeing the true aim of their eyes, spot issues with compression and blending. Keep up to date and see what changes the other departments have been making to the character and make sure those changes are working well.

Meanwhile…materials begin to finalize. Lighting continues to be adjusted. We do not animate and texture to a lighting set up, rather the lighting set up is created to what we make.

**Stitching**

When multiple animators have worked on one character that requires dynamics, stitching is required.

This allows for dynamics to be done on the entire string of animations together and provides a massive time savings.

![](../The Life of a Leader/media/image22.png)

As animation gets closer to being ready for feedback we begin a cycle of adjustments and model tweaks. Usually the animation lead and modeling lead sit down and fine tune things. Modeling gives notes on how they intended things to look, and animation has a more clear presentation with what they intend to do with the character.

With animation going along, lighting begins its process, blocking in something that works with the idle poses. It will continue to be revised as the animations and materials begin to finalize. We do not animate and texture to a lighting set up, rather the lighting set up is created to what we make.

To stitch, animation uses RedNine to bring all animations for VO into one VO file and all animations for the Base set into one Base Set file.

Once the stitching happens, all large form animation changes halt and small form facial and hand tweaks continue. Material work from modeling happens as well, but at this point most modeling tweaks halt, and become on request only. Animators work only in the stitched file to make tweaks.

In Civ none of the dynamic items (cloth, necklaces, etc) are done in realtime. We must bake out simulations done within Maya.

Audio can start a pass of sound effects now. Animation and dynamics are mostly tied down.

Finally, we begin the final polish stages. As Dynamics get finalized, we begin to review how it all fits together. Lighting gets tweaked to the backgrounds (intensity) and we start to lay in the final material tweaks and such. Final bug lists get cleared and hopefully if all is said and done correctly we should be left with a leader scene that doesn’t clash with what we did on the base game.

Audio can now completely have at it now to drive it home.