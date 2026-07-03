---
title: "FireFX UI Backend"
category: "FireFX"
summary: "<h1 id=\"firefxuibackenddesign\">FireFX UI Backend Design</h1> The way that the UI maps to the FireFX script will be through code injection where the user can select blocks which map to code blocks t..."
keywords: ["firefx","backend","emitter","screen","control"]
---

# FireFX UI Backend

<h1 id="firefx-ui-backend-design">FireFX UI Backend Design</h1>
The way that the UI maps to the FireFX script will be through code injection where the user can select blocks which map to code blocks that get combined

Tags are used to indicate sections that contain code, or sections where that code should be injected into

< > tags represent a section where code should be copied into that matches the tags identifier

[ ] tags represent the identifier for the following block of code that should be copied into a section defined by a matching tag

Code should be copied in order from top to bottom

When copying code into a section, any identical lines of code (white space should be ignored for comparison) should not get duplicated and only the first one should remain.

<h1 id="block-types">Block types:</h1>
Property blocks: These blocks are unique for each emitter and can define several different code blocks where each code block is mapped to an Enum entry that the user can pick from the UI. There might be additional block parameter meta data for description, tooltips, etc. Different options may or may not also expose UI parameters for the user to pick (not yet clear, but we should assume that we’ll need to).

This blocks are used to defined emitter properties, and also write out the appropriate exports that make the property valid. These blocks will also usually initialize critical variables that will be modified by other blocks. These are usually variables that need to be fed to the exports, for things like Position or Color.

Example:

Code Block 1 Property blocks example 1

| Description = "This is determines the way that the particles are blended on the screen (Mesh particles determine their own blending based on their material)"
 # Property blocks have a UI exposed enum, where each one then maps to a code block
 
 
 #This is the first possible code block, and should be the default when added to an emitter
 Enum1: "additive"
 
 [PARTICLE_GLOBAL]
 varying color p_color;
 varying float p_alpha;
 
 [PARTICLE_SPAWN]
 p_color = color(1,1,1);
 p_alpha = 0;
 
 [PARTICLE_PROPERTIES]
 property geometry_type = quad_rotated;
 
 [PARTICLE_RENDER]
 export( "COLOR", p_color);
 export( "ALPHA", p_alpha); |
| --- |

Code Block 2 Property blocks example 2

| # The code block is mutually exclusive from the first
 Enum2: "alpha"
 
 [PARTICLE_GLOBAL]
 varying color p_color;
 varying float p_alpha;
 
 [PARTICLE_SPAWN]
 p_color = color(1,1,1);
 p_alpha = 0;
 
 [PARTICLE_PROPERTIES]
 property geometry_type = quad_rotated;
 
 [PARTICLE_RENDER]
 export( "COLOR", p_color);
 export( "ALPHA", p_alpha); |
| --- |

Particle logic blocks: This is the most common type of block that will compose the meat of the logic for the particles. These blocks will only contain one block of code, and additional metadata to indicate the type of block, it’s uniqueness, other logic block prerequisites, and UI exposures.

Example:

Code Block 3 Particle Logic Blocks

| # Flag for indicating whether this block has to be unique across a group of blocks within an emitter (only one lifetime block allowed per emitter)
 Block_Type = SpawnRate
 Unique = True
 
 # Flag indicating that this block needs other types of blocks to be present to function,
 Before = none
 After = none
 Anywhere = none
 
 # Description to be placed somewhere in the UI for users
 Description = "Particles will spawn at a constant rate of N particles per second"
 
 # This is the section that describes the variables exposed to the UI. This need to describe UI string for the variable, variable name (this is the identifier in the code that will get replaced with the user driven value), type, range, tooltip, and default.
 # Eventually there might be UI hints available to tell the tools which control to use when displaying
 [UI: Particles per second, name: PARTICLE_RATE, float, range:0,1000000, default: 10]
 [UI: Initial Particle burst, name: PARTICLE_BURST, float, range:0,1000000, default: 0]
 [UI: Emitter life, name: EMITTER_LIFE, float, range:-1,1000000, default: -1]
 [UI: Delay Min, name: DELAY_MIN, float, range:-1,1000000, default: 0]
 [UI: Delay Max, name: DELAY_MAX, float, range:-1,1000000, default: 0]
 
 # This section then gets converted into code and merged
 [INCLUDES]
 
 [PARTICLE_GLOBAL]
 
 [PARTICLE_SPAWN]
 
 [PARTICLE_SPAWN_ARGUMENTS]
 (
 <PARTICLE_SPAWN_ARGUMENTS_ADDITIONAL>
 float in_age
 )
 
 [PARTICLE_SIM]
 
 [PARTICLE_PROPERTIES]
 
 [RENDER]
 
 
 [EMITTER_GLOBAL]
 varying float p_age;
 varying float p_inv_lifetime;
 
 [EMITTER_SPAWN]
 p_inv_lifetime = (EMITTER_LIFE > 0)? 1.0 / EMITTER_LIFE : 0;
 p_age = 0.0;
 
 emit_count("EMITTER_NAME" + "_particle", PARTICLE_RATE)
 {
 <PARTICLE_SPAWN_PARAMETERS>
 export("in_age",p_age);
 };
 
 [EMITTER_SIM]
 emit_rate("EMITTER_NAME" + "_particle", PARTICLE_RATE)
 {
 <PARTICLE_SPAWN_PARAMETERS>
 export("in_age",p_age);
 };
 p_age = p_age + delta_time() * p_inv_lifetime;
 kill(p_age > 1); |
| --- |

Blank emitter block: This block gets automatically generated behind the scene for every emitter. It has no User exposures (except for the name), and is just generated to provide the structure for other blocks to build into. The “EMITTER_NAME+_particle” bit just indicates that that line should contain the name of the emitter with the “_particle” suffix.

Code Block 4 Blank emitter block

| #Blank emitter
 
 [PARTICLES]
 emitter EMITTER_NAME+_particle
 {
 <PARTICLE_GLOBAL>
 SPAWN
 <PARTICLE_SPAWN_ARGUMENTS>
 {
 <PARTICLE_SPAWN>
 }
 SIM
 {
 <PARTICLE_SIM>
 }
 
 <PARTICLE_PROPERTIES>
 
 RENDER
 {
 <PARTICLE_RENDER>
 }
 }
 
 [EMITTERS]
 emitter EMITTER_NAME
 {
 <EMITTER_GLOBAL>
 SPAWN
 {
 <EMITTER_SPAWN>
 }
 SIM
 {
 <EMITTER_SIM>
 }
 
 <EMITTER_PROPERTIES>
 
 RENDER
 {
 <EMITTER_RENDER>
 }
 }
 
 [GROUP_SPAWN]
 emit_count( "EMITTER_NAME", 1 ); |
| --- |

Blank group block: Similar to the blank emitter block, this is just an internal structural block of code for the rest of the code to inject into. There is only one group block per effect, and is the first block that gets used and all other block go into:

Code Block 5 Blank group block

| <INCLUDES>
 
 <PARTICLES>
 
 <EMITTERS>
 
 
 group PARTICLE_SYSTEM_NAME
 {
 SPAWN
 {
 <GROUP_SPAWN>
 }
 SIM
 {
 <GROUP_SIM>
 }
 } |
| --- |

Two special cases:

Template Emitter block: These are highly optimized emitter blocks that are self-contained and just expose a few parameters to the user, but cannot have any other blocks added to them. Internally however it should function very much like a regular Emitter Logic Block, that just gets injected directly into the Group Block.

The main purpose of these blocks is to encompass common use cases, but not used for high volume effects.

Template Effects: This is a case where there is a very optimized emitter that should be shared for high volume effects. Like the Template Emitter, this only exposes a handful of parameters and cannot have additional blocks added to it. Unlike it though, the way that this is expressed internally is slightly different. This will probably be implemented as a special Group Block that gets injected into an existing shared FireFX file so that all the effects that use this template can be compiled together.

<h1 id="injection-order">Injection order:</h1>
So the order in which block should be combined is:

Each **Blank Emitter Block** emitter block should get all its **Property Blocks** injected into it in order. Then it should get all its Particle Logic Blocks injected into it in order.

Then each finished **Emitter Block** should get injected into the **Blank Group** Block in order.

When injecting the code, any lines of code that are identical to a line that already exists (ignoring white space) should be ignored.

<h1 id="section"> </h1>
<h1 id="types-and-ui-controls">Types and UI controls:</h1>
Float (with an optional 3D Scale Gizmo, 3D Radius Gizmo, or Greyscale color picker)

Float2

Float3

Float4 (With an optional 3D Rotation Gizmo)

Color (With an HDR color picker, or at least a SRGB color picker)

Point2D (With a 2D Position Gizmo, maybe?)

Point3D (With a 3D Position Gizmo)

Int (maps to an equivalent float)

Bool (true = 1, false = 0)

String ( for referencing other emitters, though automatic Enum generation for existing emitters would be even better)

Spline selector (Scope to be determined, but we need some way for the user to be able to specify a 1D function either from a preset of functions, or as a custom spline)

Code block (This would allow the user to type in code snippets)

Example usage:

In the example directory there are a handful of example blocks that should generate the Output.txt script if all the defaults are used, and the Particle System name was “Root” and the Emitter name was “CenterGlowWhite”