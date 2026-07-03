---
title: "Emitter Properties"
category: "FireFX"
summary: "<h1 id=\"emitterproperties\">Emitter Properties</h1> These are all the emitter properties that can be assigned to a given emitter.  This properties must be defined at compile time they cannot be chan..."
keywords: ["emitter","properties","firefx","texture"]
---

# Emitter Properties

<h1 id="emitter-properties">Emitter Properties</h1>
These are all the emitter properties that can be assigned to a given emitter. This properties must be defined at compile time (they cannot be changed at run-time based using script logic).

The syntax for properties is the keyword "property", followed by the property identifier, followed by the equals (=) sign, followed by the value. For example:

| property blend_type = alpha
 
 
 geometry_type = [none, quad_rotated, quad_aligned, quad_fixed, string_aligned, string_fixed] |
| --- |

Default is 'none'.

Only valid on emitters that have a sim block.

Description: Determines the geometry type of the emitter.

| material_type = [none, quad_unlit, string_unlit, quad_unlit_masked, string_unlit_masked, quad_unlit_distorted, string_unlit_distorted] |
| --- |

Default is 'none'.

Only valid on emitters that have a sim block.

Description: DEPRECATED: use combination of other material properties instead.

| blend_type = [none, alpha, additive] |
| --- |

Default is 'none'.

Only valid on emitters that have a sim block.

Description: Sets the blend mode for the particle.

| distorted = [true,false] |
| --- |

Default is 'false'.

Only valid on emitters that have a sim block.

Description: Enable distortion texture slot.

| masked = [true,false] |
| --- |

Default is 'false'.

Only valid on emitters that have a sim block.

Description: Enable mask texture slot.

| normalmap = [true,false] |
| --- |

Default is 'false'.

Only valid on emitters that have a sim block.

Description: Enable NormalMap texture slot. Only used if directional lighting is enabled.

| material_lighting = [none, directional, non_directional] |
| --- |

Default is 'none'.

Only valid on emitters that have a sim block.

Description: Set the lighting mode for the particle.

| sort_order = [emit_order, reverse_emit_order] |
| --- |

Default is 'emit_order'.

Only valid on emitters that have a sim block.

Description: Set the sort mode for particles emitter by this emitter.

| priority = [Integer in the interval [0, 256)] |
| --- |

Default is 0.

Only valid on emitters that have a sim block.

Description: Determines the rendering order of emitters within the same tree. Lower priority emitters render before higher priority emitters.

| layer = [opaque, blended, underwater, overblended, overlay, primary] |
| --- |

Default is 'primary'.

Only valid on emitters that have a sim block.

Description: Layer to render the emitter into.

| callbacks = [true,false] |
| --- |

Default is 'false'.

Description: Enable callbacks for emitter lifetime events. This is expensive, so only enable it if you really need the callbacks.

| shadows = [true,false] |
| --- |

Default is 'true'.

Only valid on emitters that have a sim block.

Description: Enable shadow casting by this emitter. Not available in the Overlay layer, or with Additive blend mode.