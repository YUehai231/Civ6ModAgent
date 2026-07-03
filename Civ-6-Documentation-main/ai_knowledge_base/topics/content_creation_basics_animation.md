---
title: "Animation"
category: "Content Creation Basics"
summary: "Animation . anm Animations consist of animation track information for one or more bones."
keywords: ["animation","content","creation","basics"]
---

# Animation

Animation (.anm)

Animations consist of animation track information for one or more bones. Currently we support importing geometry directly from 3DSMax and Maya

Using the Asset Editor

- In the Asset Editor go to 'File > New' and select Animation from the list.

![](../Animation/media/image1.png)

- In the Class Name dropdown select the class that you want (1). It can be tricky to change the class for entities after they are created, so try to make sure you have the correct class.

![](../Animation/media/image2.png)

- Click on the line for '***Source File Path***' (2), and browse to the Max or Maya file that has your animation.

- When you select your file, the editor will parse the file and find which animation objects are available for export. This will fill out the '***Source Object***' dropdown (3) with all the available animations for you to pick from, so click the dropdown and select the animation object that you want.

- The '***Name***' (4)of the animation will get set automatically to the name of the source object, but you can change it to whatever you want before saving the Animation.

- Go to "***File > Save***" and you're done.