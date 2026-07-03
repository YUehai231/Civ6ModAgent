---
title: "StrategicView Overview"
category: "Modding Guides"
summary: "The StrategicView provides a 2D visualization of the map in a Civ game.  Numerous aspects of its visuals can be modified by changing the StrategicView."
keywords: ["strategicview","overview","modding","guides","artdef","xlp","lua","animation","texture","reference"]
---

# StrategicView Overview

The StrategicView provides a 2D visualization of the map in a Civ game.  Numerous aspects of its visuals can be modified by changing the StrategicView.artdef file.

This document provides an overview of the different Root Collections in the StrategicView ArtDef.

### Properties Collection

The properties collection contains general propreties that affect how the entire StrategicView is displayed, particularly colors between or
around hexes and the size of a terrain texture in world units.  TerrainTiling is used as a scale factor for how frequently terrain textures
are repeated.  Lower numbers cause terrain textures to get drawn at a higher frequency, as each texture takes up less world space.

### PositionSets Collection

Position sets are used to determine the location of sprites within a StrategicView Tile.  Each PositionSet has a collection of positions.
Each Position has a name and a coordinate value ([x,y] pair).  The valid range of positions is from -0.5 to 0.5 for the x value,
and -0.57 to 0.57 for the y value, though values beyond +/- 0.3 are very near to the hex edge.

Each entry in the position set corresponds to an entry in the element that is making use of it.  When a StrategicView Sprite entry makes use
of a PositionSet, the PositionSet needs to have at least one position defined for each entry in the Sprite.

### PlacementRules Collection

This is a fixed collection and should not be modified.  Sprite entries make use of this to determine how they get arranged around the hex.

AtEdges_NotScaled ->
Centered -> The first entry is selected and it is displayed in the center of the hex.
Centered_NotScaled -> The first entry is selected and it is displayed in the center of the hex.  It is not scaled.
Centered_NotScaled_Animate
Centered_Random -> A random entry from the collection is selected and it is displayed in the center.
GreatWall
OneEntryPerTile -> For multiple tile features, this informs the feature that a single entry will be displayed per tile.

### TerrainBlends

TO-DO:

### TerrainBlendCorners:

TO-DO:

### TerrainSpriteEntries

Defines the set of possible terrain sprite.  Each entry has a name, a Visble XLP Entry reference with positional offsets, and a Revealed XLP Entry reference with positional offsets.

### TerrainSprites

Defines the terrain sprite collections that will be used by the game.  Each element has a name, position set, a placement rule, a render flag, and the number of tiles it occupies.  Additionally, these elements have child
collections that reference TerrainSpriteEntries that have been defined by the TerrainSpriteEntries collection.

When a terrain sprite has multiple entries within it AND the "Centered_Random" PlacementRule is chosen, the entry that is rendered by the StrategicView is chosen at random.  Each entry has an equally likely chance of getting chosen.

### TerrainTypes

Assigns art to the different types of terrain in the game.  The terrain name is based on the GameCore name.  For any given terrain, an entry is chosen at random from the terrain entries collection.  An entry maps a visible texture
and offset, a revealed texture and offset, and an optional sprite (used for rendering hills and mountains - but it can be used for anything) to a particular type of terrain.  Each terrain type (coast, desert, ocean, grassland, plains,
snow, tundra) is its own entry.  Additionally, any terrain that can support mountains or hills also has an additional entry for that type (e.g. Snow, SnowHills, and SnowMountains are all different TerrainTypes).

The sprites that are chosen for the TerrainTypes collection are defined in the TerrainSprites root collection above.

These terrain types need to match the terrain types that are defined by GameCore.

### FeatureEntries

Defines the set of possible feature asset entries.  Each feature asset entry has a name, a Visble XLP entry with offsets, and a revealed XLP entry with offsets.

### Features

Features are anything that naturally appears on top of terrain without player intervention.  Examples of this include forest and rainforest, as well as all natural wonders.

The Features collection assigns feature entry art to features in the game.  Each element in the Features collection has a name (must match a GameCore name), a PositionSet (varies heavily), a PlacementRule (also varies), a render flag
(true if this feature should be rendered, false otherwise), a flag to render a terrain sprite on top of the terrain, a TileCount field (which must match the number of tiles the Natural Wonder occupies as defined by GameCore), and a
TerrainTypeOverride list.  The TerrainTypeOverride list allows you to specify that a given feature (typically a Natural Wonder) completely overrides terrains with the types displayed in the list.

Each Feature element also has an Entries collection, which is used to map FeatureEntries to the Feature.

### EffectEntries

Defines the set of possible effect entries.  Each entry has a name, a Visible XLP entry and offsets, and a Revealed XLP Entry and offsets.

### Effects

Assigns are to the different effects in the game.  Currently, the only effect is "NuclearFallout".  This can be assigned a position set, a placement rule, a render variable, and a tile-count.  Additionally, it has an effects collection
that allow it to reference effect entries.

### Routes

Assigns art to different routes used in the game.  Each entry has a name (which must match its GameCore name), a route XLP entry, and a bridge XLP entry.

### ImprovementEntries

Defines the set of possible improvement asset entries.  Each improvement asset entry has a name, a Visble XLP entry with offsets, and a revealed XLP entry with offsets.

### Improvements

An improvement is anything that is placed on a tile by a builder (e.g. farms, pastures, etc.).  Barbarian Camps and Airstrips also count as improvements.

The Improvements collection assigns art to in-game improvements.  The name of the element should be the GameCore name of the improvement.  If the improvement can be pillaged, there should be one element for its regular state, and one
element for its pillaged state.  Each element has a position set (typically "1_Center" is chosen), a PlacementRule (typically "Centered") is chosen, a Render flag (if the improvement should be visible, set this flag to true), and a tile-count
value (this needs to match the GameCore value that says how large the improvement is - currently all improvements are only one tile).

Each Improvement element has an "Entries" collection, where entries defined in the ImprovementEntries collection are assigned to the improvement element.

### DistrictEntries

Defines the set of possible district asset entries.  Each district asset entry has a name, a Visble XLP entry with offsets, and a revealed XLP entry with offsets.

### Districts

Districts are extensions of the city, built by the city itself in a tile outside of its city center, but within the city borders.  Districts contain buildings based on their specialty.

The Districts collection assigns art to districts, based on the name of the district in GameCore.  All districts can be pillaged, and all districts must be constructed, so there are three states that any district art should include -
the base, constructed district, the pillaged district, and the district under construction.  Each state has its own element within the Districts collection.  The naming convention is District, District_Pillaged, and District_UnderConstruction.
Each element has a PositionSet (typically 1_Center), a PlacementRule (typically Centered), a Render flag (true for all visible districts, false for Wonder and CityCenter), and a TileCount (currently always 1) that must match its GameCore definition.

Additionally, each District has an Entries collection that maps one of the entries defined in the DistrictEntries collection above to the District.

### BuildingEntries

Defines the set of possible building asset entries.  Each building asset entry has a name, a Visble XLP entry with offsets, and a revealed XLP entry with offsets.
There should be a building entry for each of the construction states - constructed, pillaged, and under construction.

Our naming convention is typically Building, Building_Pillaged, Building_UnderConstruction, but this is simply a convention.

### Buildings

Buildings comprise of every structure that a city can build that is not a district.  This includes buildings that go within each district, buildings that go within the City Center, and any World Wonders that a City produces.

The Buildings collection assigns art to in-game buildings.  The name of the element should be the GameCore name of the building.  There should be one element for each building's regular state, one element for its pillaged state,
and one element for its under construction state.  All buildings, including World Wonders, can be placed into the pillaged state, so having art for this state is advised.

Each element has a position set (typically "1_Center" is chosen), a PlacementRule (typically "Centered") is chosen, a Render flag (if the building should be visible, set this flag to true), a tile-count value (this needs to match
the GameCore value that says how large the building is - currently all buildings are only one tile), and a BuildingChain.  The BuildingChain determines which district the building appears in.  City Center Buildings and World Wonders
leave the BuildingChain value blank.  All other buildings must be assigned to the correct chain to display in the appropriate district.

Each building element has an "Entries" collection, where entries defined in the BuildingEntries collection are assigned to the building element.

### CityEntries

Defines the set of possible city asset entries.  Each city asset entry has a name, a Visble XLP entry with offsets, and a revealed XLP entry with offsets.

### Cities

A city is constructed when a settler settles in a location.  Cities change their appearance throughout the game.  As the game time progresses, the visuals for a city reflect the current age of the game.

The city definition need to match the GameCore names.  The current set of names are Ancient_City, Industrial_City, Medieval_City, and Modern_City.  Each element in the Cities collection has a name, a PositionSet (typically 1_Center),
a PlacementRule (typically Centered), a Render flag (render the city or not), and a TileCount (typically 1).  Each city element also has an Entries collection that contains a value from the CityEntries collection defined above.

### UILenses

UI Lenses are views that are displayed on top of the map to help provide additional information about an activity or state of the game.

The names of the elements of the UI Lens collection follow no hard rule, however, they need to match the same name that is being called from LUA.

Each UI Lens element has a PositionSet (as described above), a PlacementRule (as described above), and a render flag (true to render the element, false otherwise).  There are no consistent defaults for UI lens entries.
Additionally, each UI Lens element has an AnimDuration parameter, an AnimType parameter, and a RotateToAlign parameter.

UI lenses can animate between textures (if any INTERPOLATE animation type is chosen) or between alpha values (if any FADE animation type is chosen).  If an INTERPOLATE animation type is chosen, the lens element animates
between its first two texture entries (first -> second if forward is chosen, second -> first is backwards is chosen, and first -> second -> first -> second etc. if loop is chosen).  If a FADE animation type is chosen, the
lens element animates from invisible to visible if FADE_IN_ONCE is chosen, visible to invisible if FADE_OUT_ONCE is chosen, and between visible and invisible repeatedly if FADE_LOOP is chosen.

Each UI lens entry has a certain number of parameters associated with it.  They can be set at the asset level itself.  The UI Lenses which derived from those entries have a position set with it, a placement rule, a render flag.

In the base game, placement lenses are examples of UI Lens elements that make use of animations.

The rotate to align flag allows textures to be aligned along the egde of the hex (as opposed to forcing their alignment to the center of the hex).  It makes placing lenses that lay along hex boundaries easier.

### UILensEntries

Defines the set of possible UI Lens asset entries.  Each UI Lens asset entry has a name, a Visble XLP entry with offsets, a revealed XLP entry with offsetsm a tint color, and a scale factor.