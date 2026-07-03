---
title: "TerrainBounceLighting"
category: "Content Creation Basics"
summary: "<h1 id=\"terrainbouncelighting\">Terrain Bounce Lighting</h1> Overview /download/attachments/59081138/image20151019%2011%3A42%3A24. png?"
keywords: ["terrainbouncelighting","content","creation","basics","artdef"]
---

# TerrainBounceLighting

<h1 id="terrain-bounce-lighting">Terrain Bounce Lighting</h1>
**Overview**

![/download/attachments/59081138/image2015-10-19%2011%3A42%3A24.png?version=1&modificationDate=1445269408300&api=v2](../TerrainBounceLighting/media/image1.png) ![/download/attachments/59081138/image2015-10-19%2011%3A42%3A31.png?version=1&modificationDate=1445269408300&api=v2](../TerrainBounceLighting/media/image2.png)

We have the ability to do a crude approximation of bounced lighting of the directional light off of the terrain to help seat models onto the terrain. For visual inspection, this feature can be toggled via the “shaders bounce” console command. Each hex has a representative color that is calculated as a composite of artist supplied colors for terrain type, feature type and improvement type. These values are specified in the ArtDef for each of these different types. The field should be under "Lighting" and then "BounceColor".

![/download/attachments/59081138/image2015-10-19%2011%3A42%3A51.png?version=1&modificationDate=1445269408283&api=v2](../TerrainBounceLighting/media/image3.png)

**Layering**

**
**

![/download/attachments/59081138/image2015-10-19%2011%3A43%3A17.png?version=1&modificationDate=1445269408253&api=v2](../TerrainBounceLighting/media/image4.png)

Some types also have a "BounceAlpha" which specifies how much that layer should override the layers under it. This feature can be used to:

1) **Blend in the color of a feature** - E.g. Shifting the color towards water color for marshland/flood plains, accounting for dirt decal placed under goody huts

2) **Simulate ambient occlusion** - Having a forest ramp down the bounce color of the terrain type makes sense

**Calculating Lighting**

The bounce lighting is simulated as a light source below the unit. The final bounce lighting color is the final hex color multiplied with the directional light color. The angle of the sun is also taken into account so that the effect is dimmed as the sun reaches the horizon. The effect also fades out vertically from the bottom of the model so large models that penetrate the terrain significantly may look strange as the falloff doesn’t follow the terrain surface