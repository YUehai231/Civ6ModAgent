---
title: "DataDocumentation"
category: "Content Creation Basics"
summary: "Data documentation Madrid Exported on Feb 08, 2019 Modders and your coworkers need help understanding how our data works.  Please go through the following list and write something about each class ..."
keywords: ["datadocumentation","content","creation","basics","artdef","blp","xlp","xml","animation","texture","screen","icon","control","reference"]
---

# DataDocumentation

Data documentation

Madrid

Exported on Feb 08, 2019

Modders (and your co-workers) need help understanding how our data works. Please go through the following list and write something about each class you know something about.

Keep in mind these docs should be targetting someone who doesn’t know our tech. For assets and art entities its good to know what other entities they are used with and how ArtDefs refer to them.

For ArtDefs and XLPs it’s nice to know what systems use them and how.

We are trying to put enough detail in these docs so the modders can answer questions like, if I want to add a building what data do I need to modify?

<h1 id="assets">Assets</h1>

| Asset Class | Description |
| --- | --- |
| CityBlock | Placed around cities and districts in the form of procedural filler. Considered to be a "Landmark". For process, consult Buildings Process. |
| Landmark | Used to be used by everything, now only used by DynamicGeometry for splined geometry and towers. |
| Leader |  |
| RouteDoodad | Placed along roads according to certain rules, currently only supports bridges. Considered to be a "Landmark". |
| StrategicView_DirectedAsset | Represents StrategicView assets that are placed along a tile (hex) edge and therefore need 12 permutations (6 edges of a tile times two fog-of-war states, visible and revealed). The permutations are cook parameters ([StrategicView_Sprite](#scroll-bookmark-4) textures) and are named following compass directions, i.e. North-East Revealed, North-East Visible, East Revealed, East Visible, South-East Revealed, etc.) Examples used in game are bridges and cliffs. The [StrategicVIew.artdef](#scroll-bookmark-5)'s TerrainBlends, Features, and Improvements collections reference directed asset XLP entries. |
| StrategicView_Route | Represents StrategicView roads, which connect the middle points of each tile (hex) edge. Because the roads can be mirrored and in most cases pass through the tile center, only 8 permutations (4 road segments times two fog-of-war states, visible and revealed) are required. The four road segments are:  - north-west to north-east tile edge,  - north-east to east tile edge,  - north-west tile edge to tile center, and  - west tile edge to tile center.    Examples used in game are roads. The [StrategicVIew.artdef](#scroll-bookmark-5)'s Routes collection references route XLP entries. |
| StrategicView_TerrainBlend | Represents a StrategicView terrain blend containing 70 cook parameters that can be filled with 17, 31 or 70 textures representing the different terrain blend categories (see [StrategicView Terrain Overview](https://hub.take2games.com/display/FXSMadrid/Terrain+Overview) and the **Base game's Art OneNote's StrategicView → Generating Terrain Blends section**). The [StrategicVIew.artdef](#scroll-bookmark-5)'s TerrainBlends collection references terrain blend XLP entries. |
| StrategicView_TerrainBlendCorners | Represents the shared terrain blend corners containing 4 cook parameters ((see [StrategicView Terrain Overview](https://hub.take2games.com/display/FXSMadrid/Terrain+Overview) and the **Base game's Art OneNote's StrategicView → Generating Terrain Blends section**). The [StrategicVIew.artdef](#scroll-bookmark-5)'s TerrainBlendCorners collection references terrain blend corner XLP entries. It is unlikely that you should need to create or modify any terrain blend corner assets. |
| TerrainElementAsset | Assets that represent |
| TileBase | Placed as districts, buildings, improvements, etc. Can be attached to other TileBase assets. Considered to be a "Landmark". For process, consult Buildings Process. |
| UILensAsset | Describes which lens layers to turn on/off for a given "lens". |
| Unit |  |
| VFX | Represents assets that are managed by the visual effect system or that can be spawned by the particle effect system. It is not required that a VFX asset have a dsg, geometry, animations, or particle efffects. |
| WonderMovie | Represents assets that are used to represent world wonders in the game. These assets usually have WonderMovie geometry class and camera information from the WonderMovieCamera geometry class. Typically, the camera and base geometry come from the same 3DS Max file, but are in different hierarchies. Geometry from the DecalGeometry asset class may also be added to this asset as well. DecalGeometry added directly to the WonderMovie asset will always be visible when the asset is placed down in game. Additionally, attachment geometry (from the TileBase asset class) can be added to the WonderMovie asset. The attachment geometry (as well as any decals associated with it) will only be visible if the attachment point geometry associated with the attachment point is visible (as defined by the WonderMovie asset state) and the attachment point itself is visible (as defined by the reveal animation visibility). Also note that attachments with a connection type of ROAD will be added as connections points immediately when the asset is placed in game (regardless of the visibility of the attachment point that it is associated with). Note that wonder movie assets do not require an animation or camera animation in order to be placeable in game; however, at least a base geometry is require in order to be functional. Visual Progress Change During Construction - While the wonder is being built, the amount of build progress that it has achieved is normalized and used to sample the visibility track associated with its reveal animation in order to determine what geometry should be displayed. In addition, the visibility associated with attachment point bones is used to only show visual effects on attachment points associated with visible bones. This attachment point visibility information is important because it allows the construction animation to loop and cull out the calling of visual effects on invisible bones. The following information can be used to determine the state that the wonder asset will be in when it is placed down in game:  - Before the wonder reveal:   - Asset State: UNWORKED (same for TileBase and all DecalGeometry)  - DSG State: ANY → CONSTRUCTION (TileBase: ANY → UNWORKED)     - During the wonder reveal:   - Asset State: UNWORKED (same for TileBase and all DecalGeometry)  - DSG State: ANY → REVEAL (TileBase: ANY → CONSTRUCTION)     - After the wonder reveal:   - Asset State: WORKED (same for TileBase and all DecalGeometry)  - DSG State: ANY → WORKED (TileBase: ANY → WORKED) |

<h1 id="materials">Materials</h1>

| Material Class | Description |
| --- | --- |
| BurnMaterial | The Burn material causes an existing material to appear burnt. It contains a set of textures to override the material textures in burnt regions, and a set of parameters which control the procedural noise which is used to blend between the burnt and non-burnt materials. Any asset with a burn material will have the procedural burn effect applied. The procedural burn effect also depends on a number of asset-level parameters, which are specified as cook parameters for CityBlock and Landmark assets. These parameters are:  - GradientScale: Controls the speed at which the burn effect blends in. Higher scales result in sharper transitions from burnt to unburnt.  - BurnEdgeBlend:  - BurnHeight: Controls the height from the base of the asset at which the burn effect starts blending in |
| DecalMaterial | Material used for decals placed on the terrain. |
| FOWLineDrawing | This material controls the types of FOW strokes which will be drawn for the mesh edges on the geometry. The FOW material can be used to disable wing strokes, fin strokes, or both. The default FOWLineDrawing material draws both stroke types. A common usage of the FOW material is to disable FOW strokes on alpha-tested geometry such as wheat. This is necessary to prevent the outlines of the base geometry from being drawn. You can also prevent geometry from appearing in FOW by omitting the material. If the material is null, then the geometry is completely invisible in FOW. For more information, see the documentation for the 'LandmarkModel' geometry class. |
| Landmark | Material used for all assets considered to be 'Landmarks'. |
| Leader |  |
| Leader_Cloth |  |
| Leader_Glass |  |
| Leader_Hair |  |
| Leader_Matte |  |
| Leader_Skin |  |
| RiverWater | Simplified variation of the water material which is used on rivers. |
| SnowMaterial | The snow material is a placeholder. If a snow material is assigned to a triangle group, it will have the procedural snow effect. Otherwise, it will not. The settings from the procedural snow shader, if present, are specified at the asset level. |
| TerrainElement | A local hand-built region of terrain that is blended into the procedural terrain. |
| TerrainMaterial | Terrain material used by either TerrainElement or procedural terrain layer. |
| UILensMaterial | Simple material used on UI lens model assets, such as the movement ring. |
| Unit |  |
| VFXModel | Represents the more basic version of the material used for VFX related content. |
| VFXModel_FX | Represents the more advanced version of the material used for VFX related content. This material contains additional features such as multiple texture layers, uv scrolling, and alpha mode selection. |
| Water | Material controls for water materials used by oceans, shallows, lakes, and natural wonders. |
| WaveMaterial | Material which specifies a texture atlas for coastal waves. The wave atlas is treated as a greyscale image. Only the Red channel is used. |

<h1 id="geometry">Geometry</h1>

| Geometry Class | Description |
| --- | --- |
| DecalGeometry | Represents the class of geometry that can be used for terrain decals. |
| LandmarkModel | Represents the class of geometry used for buildings, clutter, city blocks, and other such elements. The LandmarkModel geometry class may be visible in FOW. Landmark models in FOW will render with their BaseColor map, mixed in with a parchment texture. They will also render 'strokes' on mesh edges. There are two types of FOW strokes:  - Wing Strokes: The purpose of a wing stroke is to highlight important features on a model, such as sharp corners and roof lines. Wing strokes are generated in the following circumstances:   - On edges in which connect to only one triangle  - On edges which connect to 3 or more triangles ("pin-wheels")  - On edges with two triangles, where the angle between triangles exceeds a given threshold.       - Fin Strokes: Fin strokes are generated for every edge in the mesh which connects two triangles. The purpose of the fin stroke is to highlight the silhouettes of the model. Fin strokes are not rendered unless the edge is a silhouette, meaning that one triangle is back-facing and the other front facing.    The FOWLineDrawing material controls the types of strokes which are rendered (wings or fins), while the geometry class defines parameters which control stroke placement:  - FOWForceThreshold: FOW strokes are "forced" (always drawn) on edges where the angle between the incident faces is larger than this value  - FOWFlatThreshold: FOW strokes are never drawn on edges where the angle between the incident faces is less than or equal to this value. This test is used to prevent spurious edges from appearing between co-planar polygons. |
| LandmarkObstructionProfile | Indicates an area, usually on a TileBase asset, that cannot be occupied by other assets. Must be XY planar, the Z coordinate of every vertex must be the same. |
| Leader_ShadowVolume |  |
| UILensModel |  |
| Unit |  |
| VFXModel | Represents the class of geometry that can be added to VFX related content. In the game and AssetEditor, when VFX assets are placed they will be placed in the Default asset state. |
| WonderMovieCamera | Represents the class of geometry that can be used to represent a camera for wonder related content. |
| WonderMovieModel | Represents the class of geometry that can be used to represent the base skeleton/mesh for wonder related content. Additional Export Information - Be sure that objects with visibility information are uniquely named; otherwise, the system will not be able to properly acquire the visibility information. Also, in order to export visibility for bones in 3DS Max, you will need to create a mesh with visibility and then set the “Export as Bone” option on those meshes within the Model Manager. |

<h1 id="animation">Animation</h1>

| Animation Class | Description |
| --- | --- |
| Landmark | Class of animations that can be added to any asset considered to be a 'Landmark'. |
| Leader |  |
| Unit |  |
| VFX | Represents the class of animation that can be added to VFX related content. |
| WonderMovie | Represents the class of animation that can be added to wonder related content. |

<h1 id="dsg">DSG</h1>

| DSG Class | Description |
| --- | --- |
| Clutter |  |
| Landmark | Class of state graph that can be used with any asset considered to be a 'Landmark'. |
| LeaderDSG |  |
| TerrainElementAsset | Class of state graph that can be used with any asset considered to be a 'TerrainElementAsset' |
| Unit |  |
| VFX | Represents the class of state graph that can be added to VFX related context. In the game and AssetEditor, when VFX assets are placed they will have the ANY to IDLE state graph transition applied. |
| WonderMovie | Represents the class of state graph that can be added to wonder related content. |

<h1 id="texture">Texture</h1>

| Texture Class | Description |
| --- | --- |
| ColorKey | ColorKey textures are used to implement tabulated color correction. To generate a colorkey, you must first take a special screenshot using the in-game debug console. Open the console and type 'screenshot colorkey'. This will generate an image file in your screenshots directory containing a game screenshot and an embedded color table. You can then color-correct the resulting image, and import it using the asset editor. The asset cooker will extract the color table from the imported image and discard the rest. |
| Decal_BaseColor | This texture class defines decal material base color. The base color is used to scale diffuse lighting. It is an sRGB color image with alpha. |
| Decal_FOWColor | This texture class defines decal material FOW color. When the terrain is in FOW this texture is used to directly set the color for the terrain with no lighting. It is an sRGB color image with alpha. |
| Decal_Heightmap | This texture class defines decal material detail height data to blend into the terrain before the normal map is generated. It is a linear texture where the red channel is the height and the alpha channel is the blend. |
| Decal_Spec | This texture class defines decal material gloss. White pixels are shiny, black pixels are dull. This is a linear value which encodes GGX roughness. The Civ6 engine uses a GGX approximation based on a pair of Beckman lobes which are filtered using CLEAN mapping to avoid specular loss in the exceedingly common case of minified textures. The specular results should appear similar to GGX but may not produce a 1 to 1 match. |
| FOW | This texture class is used for FOW parchment and hatch textures. |
| FOWGreyscale | A greyscale FOW texture with only one color channel. This may also be used for parchment and hatch textures. |
| FOWSprite | This texture class is used for FOW sprites. |
| Generic_AO | This texture class is used for AO textures. It is a greyscale image interpreted as a linear value by the shader. |
| Generic_BaseColor | This texture class is used for base color. The base color is used to scale diffuse lighting. On metal surfaces, diffuse lighting is disabled, and the base color scales specular lighting instead. The basecolor map is an sRGB color image. |
| Generic_BurnMap | This texture class defines an alternate base color map which is blended with the base color for the procedural burn effect. It is an sRGB color image which is blended with the base color after conversion to linear color space. |
| Generic_Emissive | This texture class is used for emissive surfaces like lit windows. It is an sRGB color image. The emissive color is added verbatim to the shading result AFTER conversion into linear color space. |
| Generic_Gloss | This texture class is used for gloss. White pixels are shiny, black pixels are dull. This is a linear value which encodes GGX roughness. The Civ6 engine uses a GGX approximation based on a pair of Beckman lobes which are filtered using CLEAN mapping to avoid specular loss in the exceedingly common case of minified textures. The specular results should appear similar to GGX but may not produce a 1 to 1 match. |
| Generic_LightMap | This texture class is used for pre-computed global illumination, which is supported for building textures. It is an sRGB color image which is modulated by base color after conversion to linear space. |
| Generic_Metalness | This texture class is used to mark areas of the surface as being metallic. It is a greyscale image which is interpreted as a linear value by the shader. |
| Generic_Normal | This is a normal map. It will be post-processed by the asset cooker to produce a CLEAN map. |
| Generic_OPAC | This is an opacity map. It is a greyscale image interpretted as a linear value by the shader. Civ6 uses screendoor transparency based on MSAA coverage mask export, so the number of available opacity levels is proportional to the MSAA level which the user has selected in the graphics options. In the limit case, when MSAA is disabled, this technique degrades to classical alpha testing. Therefore, high contrast maps with blended edges are the most effective. Mid-tones and subtle patterns will generally not resolve well. |
| Generic_TintMask | This texture class is used to blend between the base color and a "tint color", which is defined externally to the asset. It is a greyscale image which is interpreted as a linear value by the shader. The unit material also supports a translucency mode, which allows for effects such as back lighting and subsurface scattering on sails and such like. In translucency mode, the tint mask is re-purposed as a translucency mask. |
| Leader_Anisotropy |  |
| Leader_AO |  |
| Leader_BaseColor |  |
| Leader_BlurWidth |  |
| Leader_Fallback |  |
| Leader_FilmGrain |  |
| Leader_Fuzz |  |
| Leader_Gloss |  |
| Leader_Metalness |  |
| Leader_Normal |  |
| Leader_OPAC |  |
| Leader_Tangent |  |
| Leader_Tint |  |
| Leader_Translucency |  |
| Overlay | Textures used by the culture borders, movement lenses, reticules, and various other in-game overlays. |
| SkyboxTexture2D | Textures used as "skyboxes". This is the background texture which is visible through the top and bottom of the world map. Textures of this type are cooked into the 'SkyboxTexture' XLP. |
| StrategicView_CultureBorder | A 2D, 256x256, RGBA8 texture representing the culture-border mask used in [StrategicView_TerrainBlend](#scroll-bookmark-7) assets. |
| StrategicView_Riverbank | A 2D, 256x256, RGBA8 texture representing the riverbank and coastline mask used in [StrategicView_TerrainBlend](#scroll-bookmark-7) assets. |
| StrategicView_Sprite | A 2D, RGBA8 texture of variable size (4x4 - 4096x4096) representing any sprites (features, improvements, buildings, etc.) used in the StrategicView. Mostly referenced through [StrategicView_Sprite](#scroll-bookmark-16) XLP entries in [StrategicVIew.artdef](#scroll-bookmark-5)'s various collections. See the **Base game's Art OneNote's StrategicView → How to Get Art into the Strategic View → "Photoshop File Organization for Sprites and Terrain Types" and "Importing New Sprites and Terrain Types into the Asset Cloud" sections**. |
| StrategicView_TerrainBlend | A 2D, 256x256, RGBA8 texture representing the terrain blend mask used in [StrategicView_TerrainBlend](#scroll-bookmark-7) assets. |
| StrategicView_TerrainType | A 2D, RGBA8 texture of variable size (4x4 - 4096x4096) representing the terrain type (grass, plains, snow, etc.). Mostly referenced through [StrategicView_TerrainType](#scroll-bookmark-19) XLP entries in [StrategicVIew.artdef](#scroll-bookmark-5)'s TerrainType collection. |
| Terrain_BaseColor | This texture class defines terrain material base color. The base color is used to scale diffuse lighting. It is an sRGB color image. |
| Terrain_FOWColor | This texture class defines terrain material FOW color. When the terrain is in FOW this texture is used to directly set the color for the terrain with no lighting. It is an sRGB color image. |
| Terrain_Fuzz |  |
| Terrain_Heightmap | This texture class defines terrain material detail height data used to generate the normal map. It is a linear texture where the red channel is the height and black is lower, white is higher. |
| Terrain_Spec | This texture class defines terrain material gloss. White pixels are shiny, black pixels are dull. This is a linear value which encodes GGX roughness. The Civ6 engine uses a GGX approximation based on a pair of Beckman lobes which are filtered using CLEAN mapping to avoid specular loss in the exceedingly common case of minified textures. The specular results should appear similar to GGX but may not produce a 1 to 1 match. |
| TerrainElementBlendmap | This texture class defines a blendmap used to drive blending of a TerrainElementHeightmap. |
| TerrainElementHeightmap | This texture class defines a heightmap used to define the height of the terrain geometry. |
| TerrainElementIDMap | This texture class defines which terrain materials should be drawn in a specific region of terrain. It is a linear texture with alpha, where the alpha channel is used to identify the material to use for each pixel. The alpha channel must be set to a valid AlphaIdentifier (see TerrainMaterial) or 0 to leave the existing material. |
| TerrainElementNoise2D | This texture class defines a noise texture used in some of the procedurally generated terrain passes. It is a linear texture with noise in the red and green channels. |
| UserInterface | UI Textures can be encoded in two different ways:  - Scalable: the texture is stored in an atlas, using the TexturePadding and IsStandalone parameters to control how it is fit in with other textures. This format is ideal for textures that need to rotate or scale higher than double their original resolution.  - Compressed: the texture is block compressed, dramatically reducing the memory footprint, especially on textures with large regions of a repeating pattern. This format can only do point and bilinear filtering, so textures that need to rotate/scale large amounts should be marked as scalable. |
| VFXParticle_BaseColor | Color map for VFX texture assets. |
| VFXParticle_Mask | Greyscale map used by the VFXModel_FX material for layer masking. |
| VFXParticle_Ramp | Color ramp used by the VFXModel_FX material for blending color over lifetime. This is a 1D texture, only the top row of pixels is used. |
| Water_Color | THIS TEXTURE CLASS IS NO LONGER USED. IT IS DECLARED IN THE PROJECT CONFIG BUT NEVER REFERENCED. DELETE IT! |
| WaterDensityMap | This map controls how quickly light is absorbed or attenuated at different water depths. It is a one-dimensional texture, only the top row of pixels will be used. Left is at the water surface, right as at the depth specified by the "DensityMapRange" parameter (depths lower than this are clamped). You should set the DensityMapRange based on the degree of fine control you need/want for a particular water type. High density values will make objects look like the inverted color. This means that a solid blue map will cause the underwater objects to appear yellow, because no blue light is reaching them. The further underwater they are, the yellower they will appear. The color channels are multiplied by the alpha channel to give the actual value of the density map. Color can be used to controle hue, and alpha intensity |

<h1 id="behaviors">Behaviors</h1>

| Behavior Class | Description |
| --- | --- |
| Unit |  |

<h1 id="particle-effects">Particle Effects</h1>

| Particle Class | Description |
| --- | --- |
| FireFXParticle | This class is for particles using the new FireFX scripting system. For documentation on understanding the scripting language go [here](https://hub.take2games.com/display/FXSMadrid/Understanding+FireFX+Scripts) |
| VFXParticle | Represents a class of particle effect that can be added to VFX related content. |

<h1 id="lights-analytic">Lights (ANALYTIC)</h1>

| Light (ANALYTIC) Class | Description |
| --- | --- |
| Generic_PointLight | Represents a class of a point light. This class exposes various properties that allow users to define the way that a light affects the scene and surrounding objects. |
| Generic_SpotLight |  |

<h1 id="lights-environment">Lights (ENVIRONMENT)</h1>

| Light (ENV) Class | Description |
| --- | --- |
| GameEnvironment | Game environment lights are referenced by 'GameEnvironment' light rigs. |
| LeaderEnvironment |  |

<h1 id="light-rigs">Light Rigs</h1>

| Light Rig Class | Description |
| --- | --- |
| GameEnvironment | 'GameEnvironment' light rigs are referenced by the time of day art def. The time of day system defines a blend between different environment lights over time. |
| LeaderEnvironment |  |

<h1 id="xlp">XLP</h1>

| XLP Class | Description |
| --- | --- |
| CameraAnimation |  |
| CityBuildings | Contains CityBlock assets. |
| ColorKey | This package contains all of the cooked color keys, which are available for color correction. |
| DynamicGeometry | Contains Landmark Assets used by Dynamic Geometry system. |
| FireFX |  |
| FOWSprite | Contains FOW sprite textures. |
| FOWTexture | Contains global FOW textures such as hatch patterns and parchments. |
| GameLighting | Contains cooked game environment light rights. |
| Landmark | Contains Landmark Assets used by nobody in particular. |
| Leader |  |
| LeaderFallback |  |
| LeaderLighting |  |
| Light | References assets created with the Light asset class. It is expected that the entry name and entry value fields will be the same name. This is necessary in order for the Light assets to be correctly referenced by other assets through Light triggers. The LT_Warning asset is the warning asset for Lights (looks a cyan spot light). The LT_Warning asset will appear in game (in non-Final Release builds) when a Light trigger is fired on an asset, but there is no Light asset in an cooked xlp with a name that corresponds to the Light triggers asset name. |
| OverlayTexture | This package contains cooked overlay textures which are used by various in-game UI elements. |
| RouteDecalMaterial | Contains decal materials used by procedural routes. |
| RouteDoodad | Contains RouteDoodad assets used by procedural routes. |
| SkyBoxTexture | This package contains cooked skybox textures which may be used as background images. |
| StrategicView_DirectedAsset | References all [StrategicView_DirectedAssets](#scroll-bookmark-3) that are used by the game. This includes bridges and cliffs. The TerrainBlends, Features, and Improvements collections in [StrategicView.artdef](#scroll-bookmark-5) reference directed assets XLP entries in addition to the default sprite texture XLP entries. |
| StrategicView_Route | References all [StrategicView_Route](#scroll-bookmark-6) assets that are used by the game. The Routes collection in [StrategicView.artdef](#scroll-bookmark-5) references route XLP entries. |
| StrategicView_Sprite | References [StrategicView_Sprite](#scroll-bookmark-4) textures that are used by the game. There are several BLPs using this class, e.g. StrategicView_Features, StrategicView_Districts, etc. Most collections in [StrategicView.artdef](#scroll-bookmark-5) reference sprite XLP entries. See the **Base game's Art OneNote's StrategicView → How to Get Art into the Strategic View → "Photoshop File Organization for Sprites and Terrain Types" and "Importing New Sprites and Terrain Types into the Asset Cloud" sections**. |
| StrategicView_TerrainBlend | References [StrategicView_TerrainBlend](#scroll-bookmark-7) assets that are used by the game. The TerrainBlends collection in [StrategicView.artdef](#scroll-bookmark-5) references terrain blend XLP entries. |
| StrategicView_TerrainBlendCorners | References [StrategicView_TerrainBlendCorners](#scroll-bookmark-8) assets that used used by the game. The TerrainBlendCorners collection in [StrategicView.artdef](#scroll-bookmark-5) references terrain blend corners XLP entries. |
| StrategicView_TerrainType | References [StrategicView_TerrainType](#scroll-bookmark-18) textures that are used by the game. The TerrainTypes collection in [StrategicView.artdef](#scroll-bookmark-5) references terrain type XLP entries. |
| TerrainAsset |  |
| TerrainElement |  |
| TerrainMaterial |  |
| TileBase | Contains TileBase assets. |
| UILensAsset |  |
| UITexture | This package type contains references to [UserInterface](#scroll-bookmark-20) textures used by the game's UI |
| Unit |  |
| VFX | References assets created with the VFX asset class. It is expected that the entry name and entry value fields will be the same name. This is necessary in order for the VFX assets to be correctly referenced by other assets through VFX Asset triggers. The FX_Warning asset is the warning asset for VFX (looks like a fountain of yellow yield sign icons). The FX_Warning asset will appear in game (in non-Final Release builds) when a VFX Asset trigger is fired on an asset, but there is no VFX asset in any cooked xlp with a name that corresponds to the VFX Asset triggers asset name. |
| Water | Contains cooked water materials which are referenced by art definitions. |
| Wave | Contains cooked wave materials which are referenced by art definitions. |
| WonderMovie | References assets created with the WonderMovie asset class. |

<h1 id="artdefs">ArtDefs</h1>

| ArtDef Class | Description |
| --- | --- |
| Appeal | Binds ranges of hex 'Appeal' values to specific names that may be referenced by other artdefs. Contains Game-Dependent Content. |
| Buildings | Binds building names to usable assets for various systems. Contains Game-Dependent Content. "Building" element names must be identical to "type" attribute in corresponding game XML entries. The StrategicView property creates an association between BuildStates and entries in [StrategicView.artdef](#scroll-bookmark-5)'s Buildings collection. The BuildStates collection contains valid build states for buildings and have to match the game's hard-coded values. The BuildingChains contains named collections that are referenced by entries in [StrategicView.artdef](#scroll-bookmark-5)'s Buildings collection. A BuildingChain encodes the progression of district → building level 1 → building level 2 → building level 3 (e.g. Science District → Library → University → Research Center). While the WorldView draws the district and all buildings in it (in their potentially pillaged states), the StrategicView only draws the most recent (or most recently pillaged) district / building. To accomplish this it needs to know the order in which the districts / buildings appear and be able to move up and down (in case of pillaging) the list. Note that within a level, specialty items (i.e. civilization-specific districts or buildings) should come after "normal" items, because the game goes through the elements of a level in reverse order and uses the first one it finds. Also note that DLC and mod versions of this ArtDef append their new elements to the end of each level and overwrite elements only if they are named identically. |
| Camera | Defines configuration settings for the in game camera. Each entry in the camera artdef is a block of settings, and supports editing the following:  - FOV, Tilt, and Altitude, as functions of zoom level  - Atmospheric fog parameters, as functions of zoom level  - Near and Far clip distances  - Bloom and exposure parameters    The DEFAULT_CAMERA entry is used by default. There is currently no way to override the camera configuration without using the in-game console. |
| Cities | Binds eras from the [Eras.artdef](#scroll-bookmark-33) to entries in [StrategicView.artdef](#scroll-bookmark-5)'s Cities collection. |
| CityGenerators | Defines procedural generation parameters and asset lists that CityGen uses to create the procedural 'City Center' districts and small filler buildings around nearby disticts. |
| Civilizations | Source for all artdefs that must refer to a civilization. Contains Game-Dependent Content. "Civilization" element names must be identical to "type" attribute in corresponding game XML entries. |
| Clutter | Defines a set of clutter assets for randomly scattered models. |
| Cultures | Groups Civilizations for ease of reference in other artdefs. Why add 15 entries, when you can add one entry and one culture? |
| Districts | Binds district names to usable assets for various systems. Contains Game-Dependent Content. "District" element names must be identical to "type" attribute in corresponding game XML entries. The StrategicView property creates an association between BuildStates and entries in [StrategicView.artdef](#scroll-bookmark-5)'s Districts collection. The BuildStates collection contains valid build states for districts and have to match the game's hard-coded values. |
| DynamicGeo | Defines "Walls": sets of dynamic geometry assets with metadata that allows them to be used in game. |
| Eras | Binds era names to usable assets for various systems. Binds groups of eras to specific ArtEra names that can be referenced by other artdefs. Contains Game-Dependent Content. "Era" element names must be identical to "type" attribute in corresponding game XML entries. |
| Farms | Defines the sets of asset tiles used by the farm system. |
| Features | Binds feature names to usable assets for various systems. Contains Game-Dependent Content. "Feature" element names must be identical to "type" attribute in corresponding game XML entries. The StrategicView property creates an association between Shapes and entries in [StrategicView.artdef](#scroll-bookmark-5)'s Features collection. Shapes can be:  - 1Dot (one tile),  - 2Dash (two tiles horizontal),  - 2Dash_East (two tiles horizontal with the east tile being water),  - 2Dash_West (two tiles horizontal with the west tile being water),  - 2ForwardSlash (two tiles diagonal left-to-right),  - 2ForwardSlash_NorthEast (two tiles diagonal left-to-right with the north-east tile being water),  - 2ForwardSlash_SouthWest (two tiles diagonal left-to-right with the south-west tile being water),  - 2Backslash (two tiles diagonal right-to-left),  - 2Backslash_SouthEast (two tiles diagonal right-to-left with the south-east tile being water),  - 2Backslash_NorthWest (two tiles diagonal right-to-left with the north-west tile being water),  - 3Dash (three tiles horizontal),  - 3ForwardSlash (three tiles diagonal left-to-right),  - 3Backslash (three tiles diagonal right-to-left),  - 3V_North (three tiles in an A-shape, i.e. two tiles in bottom row and one tile in top row),  - 3V_NorthEast (three tiles in a V-shape with the bottom tile's west neighbor being water),  - 3V_SouthEast (three tiles in an A-shape with the top tile's west neighbor being water),  - 3V_South (three tiles in a V-shape, i.e. one tile in the bottom row and two tiles in the top row),  - 3V_SouthWest (three tiles in an A-shape with the top tile's east neighbor being water),  - 3V_NorthWest (three tiles in a V-shape with the bottom tile's east neighbor being water),  - 4Z (four tiles in a Z-shape, i.e. two rows of two with the top row offset to the left),  - 4S (four tiles in an S-shape, i.e. two rows of two with the top row offset to the right),  - 4Diamond (four tiles in a diamond shape, i.e. one tile in the bottom row, two tiles in the middle row, and one tile in the top row),  - 4Tail_NorthEast (four tiles, three in the bottom row one in the top row, with the three bottom tiles pointing north-east),  - 4Tail_East (four tiles, three in the bottom row one in the top row, with the three bottom tiles pointing east),  - 4Tail_SouthEast (four tiles, three in the bottom row one in the top row, with the three bottom tiles pointing south-east),  - 4Tail_SouthWest (four tiles, three in the bottom row one in the top row, with the three bottom tiles pointing south-west),  - 4Tail_West (four tiles, three in the bottom row one in the top row, with the three bottom tiles pointing west),  - 4Tail_NorthWest (four tiles, three in the bottom row one in the top row, with the three bottom tiles pointing north-west),  - 6Dash (six tiles horizontal),  - 6ForwardSlash (six tiles diagonal, left-to-right), and  - 6Backslash (six tiles diagonal, right-to-left).    (Any order mentioned above is in game coordinates, which go from lower-left to upper-right in row-order.) |
| FOWConfig | Defines FOW configuration. The FOW configuration is a laundry list of global controls which govern the appearance of the fogged areas. It also defines the placement rules for the various sprites which are scattered throughout the full-fog and mid-fog. The FOW artdef references textures cooked into the FOWSprites and FOWTextures xlps |
| GamePropertyRanges |  |
| GenericObjectBLPs |  |
| GoodyHuts |  |
| GraphicsTweaks | Contains various knobs and switches for low-level control over graphics settings. |
| Improvements | Binds improvement names to usable assets for various systems. Contains Game-Dependent Content. "Improvement" element names must be identical to "type" attribute in corresponding game XML entries. The StrategicView property creates an association between BuildStates and entries in [StrategicView.artdef](#scroll-bookmark-5)'s Improvements collection. The BuildStates collection contains valid build states for improvements and have to match the game's hard-coded values. |
| Landmarks | Contains a large amount of metadata describing Districts, the Buildings inside of them, the assets that make up both, and the relationship each has with the other. Also describes 'Landmarks', which are mostly Tile Improvements, with some Resources and Features sprinkled in. Abandon hope all ye who enter here |
| LeaderFallback |  |
| Leaders |  |
| Lenses |  |
| Minimap |  |
| Overlay |  |
| Resources | Binds resource names to usable assets for various systems. Contains Game-Dependent Content. "Resource" element names must be identical to "type" attribute in corresponding game XML entries. |
| Routes | Binds resource names to usable assets for various systems. Contains Game-Dependent Content. "Route" element names must be identical to "type" attribute in corresponding game XML entries. The StrategicView property creates an association between BuildStates and entries in [StrategicView.artdef](#scroll-bookmark-5)'s Routes collection. The BuildStates collection contains valid build states for routes and have to match the game's hard-coded values. |
| ScriptedArtSelector |  |
| SkyBox | Allows for overriding the background texture. |
| StrategicView | Controls all drawable content in the StrategicView. Most drawable content requires two fog-of-war states: revealed (aka mid-fog) and visible. Because of this, most drawable content in the StrategicView.artdef is first grouped into "entries" (e.g. FeatureEntries, ImprovementEntries, BuildingEntries, etc.), which are then grouped into the actual drawable "elements" (e.g. Features, Improvements, Buildings, etc.). *Entries* group references to texture XLP entries with draw-specific meta information (such as which part of the textures to draw). *Elements* group multiple entries together and add usage-specific meta information (such as where and how the entries are supposed to be drawn on the map). An entry (found in any *Entries collection) consists of the following:  - Visible_XLPEntry,  - Visible_TopLeft,  - Visible_BottomRight,  - Revealed_XLPEntry,  - Revealed_TopLeft, and  - Revealed_Bottom_Right.    Visible_XLPEntry and Revealed_XLPEntry are XLP references to the visible and revealed textures that represent the drawable content.. Visible_TopLeft and Revealed_TopLeft are 2D coordinates representing the top-left corner (in pixels) of the area of the texture that represents the visible and revealed drawable content. Visible_BottomRight and Revealed_BottomRight are 2D coordinates representing the bottom-right corner (in pixels) of the area of the texture that represents the visible and revealed drawable content. The *_TopLeft and *_BottomRight 2D coordinates allow you to create atlassed textures containing multiple sprites in a single image and have each ArtDef entry reference only a small rectangular part of that image. If both the *_TopLeft and *_BottomRight 2D coordinates are identical the whole image is drawn. An element (found in any other collection except for Properties, PositionSets, PlacementRules, TerrainBlends, and TerrainBlendCorners) consists of the following:  - PositionSet,  - PlacementRule,  - Render,  - TileCount, and  - Entries.    A PositionSet is an ArtDef reference to an entry in the PositionSet collection. This entry determines where the drawable content is placed within a tile. A PlacementRule is an ArtDef reference to an entry in the PlacementRules collection. This entry determines how the PositionSet values are mapped to the individual entries. The Render flag is a boolean value that determines whether the sprite will be drawn on screen. This is useful for things like the Palace or Walls, which are drawn in the WorldView but are shown as UI elements only in the StrategicView. TileCount determines how many in-game tiles will be covered by the entries referenced in the Entries collection. Depending on the selected PlacementRule, this number may or may not need to be equal to the number of elements in the Entries collection. Entries is a sub-collection of ArtDef references to an entry in the corresponding *Entries collection. This entry represents the actual visible and revealed textures that will be rendered. StrategicView.artdef contains the following collections:  - Properties contain generic values that apply to the whole StrategicView, e.g. the color of coastlines and river water.  - PositionSets contain named collections of 2D coordinates that determine where within the hex something will be drawn. The coordinate system's origin (0.0, 0.0) is aligned with the hex center. The right hex boundary is located at (0.5, 0.0) while the left hex boundary is located at (-0.5, 0.0). The top hex vertex is located at (0.0, 0.57) and the bottom hex vertex is located at (0.0, -0.57).  - PlacementRules are an enumeration of known identifiers that tell the engine how to map the 2D coordinates from a PositionSet to a collection of texture entries. The following values are supported:   - Centered takes the first texture entry and centers it around the first entry of the PositionSet.  - Centered_NotScaled Same as Centered in terms of placement but it does not squish the sprite in vertical direction.  - AtEdges_NotScaled takes the first texture entry and places it on the hex edges as provided in 2_Edges PositionSet.  - Centered_NotScaled_Animate Same as Centered_NotScaled and has some sort of simple lerp animation.  - Centered_Random takes a random texture entry and centers it around the first entry of the PositionSet.  - GreatWall is used by the Great Wall improvement and combines one texture entry (tower) with one directed asset (wall pieces in different directions)  - MultipleEntriesPerTile Used by yield icons where each tile can have multiple texture entries of same UI Lens type  - OneEntryPerTile is used by multi-tile natural wonders and it places each texture entry on a separate tile.     - TerrainBlends contain references to XLP entries of [StrategicView_TerrainBlend](#scroll-bookmark-7) assets and optionally a [StrategicView_DirectedAsset](#scroll-bookmark-3) for cliffs (since cliffs have to match the coastline determined by the terrain blend).  - TerrainBlendCorners contain references to XLP entries of [StrategicView_TerrainBlendCorners](#scroll-bookmark-8) assets.  - TerrainSpriteEntries are [entries](#scroll-bookmark-34) containing references to XLP entries of [StrategicView_Sprite](#scroll-bookmark-4) textures that are referenced by TerrainSprites.  - TerrainSprites are [elements](#scroll-bookmark-35) referencing TerrainSpriteEntries that contain terrain-related textures that can overlap surrounding tiles (as opposed to [StrategicView_TerrainType](#scroll-bookmark-18) textures in the TerrainTypes collection, which are drawn only within the borders of the tile). Examples including mountains and hills.  - TerrainTypes contain a category and in-line (i.e. not referenced) [entry](#scroll-bookmark-34) containing references to XLP entries of [StrategicView_TerrainType](#scroll-bookmark-18) textures. The category can be one of Hills, Mountains, Coast, Ocean, and Default (everything else). The game applies different rules to each category. Additionally, each inline entry can contain a reference to a TerrainSprite. (For example, "Mountains" is a TerrainType, which has a background texture that fills the tile up to its borders, and references a "Mountains" TerrainSprite, which has the actual mountain texture that overlaps the tile borders.)    - FeatureEntries are [entries](#scroll-bookmark-34) containing references to XLP entries of [StrategicView_Sprite](#scroll-bookmark-4) textures that are referenced by Features.  - Features are [elements](#scroll-bookmark-35) referencing FeatureEntries that contain in-game features (ice, jungle, etc.) and natural wonders (Crater Lake, Mount Everest, etc.). Additionally, Features can reference [StrategicView_DirectedAssets](#scroll-bookmark-3) (for cliff-based natural wonders like the Cliffs of Dover) and contain a RenderTerrainSprite checkbox and a TerrainTypeOverride list. The RenderTerrainSprite checkbox determines whether the terrain sprite of the underlying game tile will be drawn underneath the feature or not. The TerrainTypeOverride list allows the game to override the underlying terrain type for lake-like natural wonders. (An implementation side-effect of lakes is that their terrain type implicitly changes to coast. In StrategicView, the lake textures have their own coastlines, so the game has to create a non-coast terrain type to fill in the gaps between the tile borders and the lake coastlines baked into the texture. This list allows you to influence which terrain types are created.)  - Routes contain two references to XLP entries, one roads ([StrategicView_Route](#scroll-bookmark-6) assets) and one for bridges ([StrategicView_DirectedAssets](#scroll-bookmark-3) assets).  - ImprovementEntries are [entries](#scroll-bookmark-34) containing references to XLP entries of [StrategicView_Sprite](#scroll-bookmark-4) textures that are referenced by Improvements.  - Improvements are [elements](#scroll-bookmark-35) referencing ImprovementEntries that contain in-game improvements (farms, mines, etc.). Additionally, Improvements can reference [StrategicView_DirectedAssets](#scroll-bookmark-3) for special-case improvements like The Greal Wall.  - DistrictEntries are [entries](#scroll-bookmark-34) containing references to XLP entries of [StrategicView_Sprite](#scroll-bookmark-4) textures that are referenced by Districts.  - Districs are [elements](#scroll-bookmark-35) referencing DistrictEntries that contain in-game districts (science, faith, etc.).  - BuildingEntries are [entries](#scroll-bookmark-34) containing references to XLP entries of [StrategicView_Sprite](#scroll-bookmark-4) textures that are referenced by Buildings.  - Buildings are [elements](#scroll-bookmark-35) referencing BuildingEntries that contain in-game buildings (library, market, etc.). Additionally, Buildings contain a reference to a BuildingChain entry in [Buildings.artdef](#scroll-bookmark-32).  - CityEntries are [entries](#scroll-bookmark-34) containing references to XLP entries of [StrategicView_Sprite](#scroll-bookmark-4) textures that are referenced by Cities.  - Cities are [elements](#scroll-bookmark-35) referencing CityEntries that contain in-game cities in their various eras.  - ParkEntries are [entries](#scroll-bookmark-34) containing references to XLP entries of [StrategicView_Sprite](#scroll-bookmark-4) textures that are referenced by Parks.  - Parks are [elements](#scroll-bookmark-35) referencing ParkEntries that contain in-game national parks.  - EffectEntries are [entries](#scroll-bookmark-34) containing references to XLP entries of [StrategicView_Sprite](#scroll-bookmark-4) textures that are referenced by Effects.  - Effects are [elements](#scroll-bookmark-35) referencing EffectEntries that contain in-game effects (e.g. fallout).  - UILensEntries are [entries](#scroll-bookmark-34) containing references to XLP entries of [StrategicView_Sprite](#scroll-bookmark-4) textures that are referenced by UILenses.  - UILenses are [elements](#scroll-bookmark-35) referencing UILensEntries that contain in-game UI Lens Textures. |
| TerrainMaterialSet |  |
| TerrainStyle | Controls for the procedural terrain layers. RidgelineMountain: Controls the look of the procedural ridgeline mountains. StandardHills: Controls the look for hills for the basic terrain types. These hills are controlled with TerrainElement heightmaps that are blended into the terrain. DuneDesertHills: Controls the desert hills, which are procedurally generated sand dunes. StandardCoastline: Controls the appearance of the procedural coastlines in the game. StandardRiver: Controls the appearance of the procedural rivers in the game, as well as a list of TerrainElement entries used for river sources and the Clutter entry used for the randomly scattered river assets. StandardFlat: Controls the look of flat terrain types in the game. Flat terrain consists of terrain material as well as TerrainElement for subtle height variation. StandardOcean: Controls the look of the procedural ocean. StandardIceShelf: Controls the look for the procedural ice shelf around ice terrain tiles. DesertMountain: Controls the look of the new desert mountain style. Delete this entry to have all mountains use the RidgelineMountain style. NaturalWonders: List of entries that define natural wonder assets, including the TerrainAsset, TerrainElement, and water style settings. The TerrainElement for natural wonders is required to have either 512 square textures (to cover a single hex) or 1024 square textures (to cover a larger region). The two diagrams below show how these two size textures will line up to hexes in the game. The entries in the Pattern group allow you to define certain properties for hexes 1 - 6, and the game will automatically rotate the asset if require to ensure it lines up properly. These properties are: 1. - BlockingHexN - This natural wonder fills this hex, blocking and overriding the procedural terrain. By default hex 0 (the center hex) is blocking.  - TerrainTypeN - This natural wonder asset requires special conditions to line up properly, such as being next to water in a specific direction.   ![/download/attachments/152437570/TerrainElementTemplate_Small.jpg?version=1&modificationDate=1498249375480&api=v2](../DataDocumentation/media/image1.jpeg) ![/download/attachments/152437570/TerrainElementTemplate_Medium.jpg?version=1&modificationDate=1498249713867&api=v2](../DataDocumentation/media/image2.jpeg) MaterialSet: List of terrain materials that are referenced by the TerrainElementIDMap entry of a TerrainElement in the NaturalWonders list. If you do not put the material in this list, the game will not load it and the black error error material will be used. |
| Terrains | Binds resource names to usable assets for various systems. Contains Game-Dependent Content. "Terrain" element names must be identical to "type" attribute in corresponding game XML entries.The StrategicView property references entries in [StrategicView.artdef](#scroll-bookmark-5)'s TerrainTypes collection. |
| TimeOfDay | Controls the time of day system. The TimeOfDay setting named 'DEFAULT_LIGHTING' is used most of the time. The setting named 'WONDER_TOD' is used when a wonder movie is active. The engine and wonder movies will set time of day using a value between 0 and 24 (midnight to midnight). The time of day system provides the following controls, all of which can be animated over time:  - Blending environment lights over time: The 'CubeLights' collection defines a set of GameEnvironment light rigs to be used for image-based lighting, and a weight curve to be applied over time to each light. The weight curve can be used to adjust the influence of a given light over time (for example, fading it out at night). The engine supports up to 8 simultaneous non-zero weights.  - Animating the sun direction: The SunAzimuth, SunTilt, SunZenith, and SunColor controls all control the behavior of the sun as a function of time of day.  - Turning lightmaps and emission maps off over time: The 'LightMapWeight' curve specifies a scale factor that is applied to all light maps and emission maps in the shaders. Among other things, this can be used to turn emissive window lights on and off at night time.  - Exposure: This is a camera exposure control which can be animated over time of day. Exposure is measured in f-stops.  - Color Keys correction time: The color key system is under the control of the time of day system. The 'ColorKeys' collection specifies a set of color keys and a weight curve, similar to the environment lights. The engine supports up to 2 simultaneously active color keys. |
| UIPreview |  |
| UnitActivities |  |
| UnitOperations |  |
| Units |  |
| UserInterfaceBLPs |  |
| VFX | Contains information about globally named visual effects. The visual effects within the NormalVFX collection are typically referenced directly from the game (by name) when particular game conditions occur. These visual effects can also be referenced by assets via ArtDef triggers. The WeaponVFX, TerrainVFX, and MaterialVFX collections contain tables that represent the type of visual effect that should be displayed for each of the named elements when a particular weapon is used, terrain/feature type is hit, or material is encountered. WeaponVFX, TerrainVFX, and MaterialVFX collections are typically referenced by ArtDef triggers on units and the game's unit system takes care of ensuring that the appropriate context for each collection is supplied in order to correctly select the visual effect to be displayed (these typically occur during combat). Note that the DEFAULT entry within the WeaponVFX, TerrainVFX, and MaterialVFX collections will be used in the event that an appropriate match is not found within the named element's table. |
| WaterMaterials |  |
| WaterSettings | Provides global controls for the appearance of river and ocean water. This includes:  - Specifying the water materials used around ice, and in oceans, lakes, and rivers.  - Controlling the procedural haze effect which is applied around coastlines.  - Specifying global visual settings for the water such as specular power, reflectivity. Certain values are specified globally, rather than in the individual materials, in order to guarantee a consistent water appearance. |
| WaveSettings | Various controls and tweaks for the coastal waves. |
| WonderMovie | Contains information for each world wonder that can be displayed by the game. Additionally, special buildings such as the small, medium, and large rockets are also represented as wonders. When creating visual representations for buildings, the wonder artdef is checked for the building before checking the buildings artdef. |
| WorldViewRoutes | Defines materials and models to be used when creating procedural roads in the World View (NOT the Strategic View!). Additionally, defines some parameters that control for shape and formation of procedural roads. |