---
title: "Understanding FireFX Scripts"
category: "FireFX"
summary: "<h1 id=\"understandingfirefxscripts\">Understanding FireFX Scripts</h1> FireFX is a language for expressing the motion and rendering of particles, or particlelike things.  The language is based heavi..."
keywords: ["understanding","firefx","scripts","lua","emitter","control"]
---

# Understanding FireFX Scripts

<h1 id="understanding-firefx-scripts">Understanding FireFX Scripts</h1>
FireFX is a language for expressing the motion and rendering of particles, or particle-like things.

The language is based heavily on C for it's structure and syntax, so this documentation might gloss over some syntax details. This documentation also assumes the readers has some experience programming but should cover everything needed to get you writing your own scripts. If you find any gaps in documentation, please fill them or ask someone else to do so.

One script file can contain the logic for multiple different particles. Each particle is broken up into a chunk of code that defines the initial conditions and simulation logic for a single particle. It also has code to then feed certain outputs back to the engine so that the engine that define how to render the particle.

One thing to note is that FireFX doesn't make any distinction between a particle and a particle emitter. All particles can emit other particles (we'll go into the syntax later), so the terms emitter and particle will be used interchangeably in this document.

A very bare bones particle script would look something like this:

Code Block 1 Simple Script

| group My_First_Particle
 {
 SPAWN
 {
 }
 
 SIM
 {
 }
 property geometry_type = quad_rotated;
 property blend_type = additive;
 
 RENDER
 {
 export( "BASECOLOR_UV", float4(0,0,1,1) );
 export( "SCALE", float2(15, 5 ));
 export( "ROTATION", 0 );
 export( "POSITION", float3(0,0,0));
 export( "COLOR", float3(1,1,1));
 export( "ALPHA", 1);
 }
 } |
| --- |

The first line is composed to two parts. The Keyword "group" is used to indicate that this an entry point for the script file, followed by an identifier of your choice, in this case "My_First_Particle". All particle systems must define a Group which is the starting code for that particle system. A script file may define multiple groups in it, but only one can be used by a particle system at a time.

The code for the Group must then be contained within pair of curly braces.

Inside the Group there are 4 sections, the SPAWN code, the SIM code, the properties, and the RENDER code. This particle isn't defining any spawn or simulation logic, so those sections are empty. The properties section lets you set a handful of engine specific properties that are fixed for each particle that tell the engine what to do with the data that the particle system is going to give it. For a full list of all the properties go here (<a href="https://hub.firaxis.com/display/FXSMadrid/Emitter+Properties" class="uri">https://hub.firaxis.com/display/FXSMadrid/Emitter+Properties</a>). Finally the Render section has several lines, where each line is feeding a labeled export back to the engine telling it how to render this particle.

In Civ 6, this particle will look something like this:

![/download/attachments/304711043/worddav2d5a38bf2b5f2bf75d9e2dafbdad3254.png?version=1&modificationDate=1549399541090&api=v2](../FireFX\Understanding FireFX Scripts/media/image1.png)

Not much to look at right now, but the language allows for expressing much more complex particle systems.

<h1 id="variables-and-types">Variables and types:</h1>
Things get much more interesting once you start using variables rather than fixed values for driving particle behavior. FireFX currently only supports floating point math, so the only variable types that are available are just groupings of floats:

float, number ( a single float)

float2, point2d (two floats)

flaot3, point3d, color (three floats)

float4 (four floats)

There are two scopes that variables can exist in: varying and local. A "varying" variable is persistent through the whole life of a particle, and is accessible anywhere within the particle's code. This allows you to initialize the variable in the spawn block, and modify it every frame in the sim block and use it in the render block. Varying variables, also called "varyings", must be defined outside of any of the particle's blocks.

The syntax for a varying variable is the keyword "varying", followed by the variable type, followed by the name or identifier you want to use followed by a semi-colon. For example:

| group My_Particle
 {
 varying float silly_variable;
 SPAWN
 {
 silly_variable = 3;
 }
 SIM
 {
 silly_variable = silly_variable + 1;
 }
 property geometry_type = quad_rotated;
 property blend_type = additive;
 RENDER
 {
 export( "BASECOLOR_UV", float4(0,0,1,1) );
 export( "SCALE", float2(15, 5 ));
 export( "ROTATION", silly_variable );
 export( "POSITION", float3(0,0,0));
 export( "COLOR", float3(1,1,1));
 export( "ALPHA", 1);
 }
 } |
| --- |

This particle has a variable called "silly_variable", it is initialized to the value of 3 in the spawn block, and then the variable is increased by one every time the sim block runs (more on that later). The variable is then output in the render block as the ROTATION value for the particle. This would produce a quickly spinning particle:

![/download/attachments/304711043/worddav444314236a06fa123f12a2daf114a66d.png?version=1&modificationDate=1549399541153&api=v2](../FireFX\Understanding FireFX Scripts/media/image2.png)

On the other hand, a "local" variable only exists within the scope of one of the blocks in the particle, and immediately disposed of when that block ends. Local variables are used to temporarily store values within a block and are mostly useful to just make your code more readable or to calculate a value once and reuse it several times in the same block. Local variables within the sim block get re-initialized every time the sim block runs, so the data does not persist across iterations of the block. Local variables in the spawn block are not accessible in the sim block, however local variables in the sim block are accessible in the render block. Internally, the sim block and the render block are merged into one, so that you can more easily pass sim data into the render step.

The syntax for local variables is similar to varyings. Local variables must be defined inside the block they are going to be used in. use the keyword "local" followed by the type, followed by the variable name, followed by a semi colon. You can also initialize the variable in the same line as you define it the way you might expect.

| group My_Particle
 {
 varying float silly_variable;
 SPAWN
 {
 silly_variable = 3;
 }
 SIM
 {
 silly_variable = silly_variable + 1;
 local float output_rotation = silly_variable / 10;
 local float3 output_position;
 output_position = float3(0,0, silly_variable / 5);
 }
 property geometry_type = quad_rotated;
 property blend_type = additive;
 RENDER
 {
 export( "BASECOLOR_UV", float4(0,0,1,1) );
 export( "SCALE", float2(15, 5 ));
 export( "ROTATION", output_rotation );
 export( "POSITION", output_position);
 export( "COLOR", float3(1,1,1));
 export( "ALPHA", 1);
 }
 } |
| --- |

In this example you can see that in the Sim block we created two local variables "output_rotation" and "output_position" which are recalculated every time the Sim loop runs. The two variables are then used in the Render as exports to control the rendering behavior. In this case you could do the calculation for these variables in-line with the export function, but that can get messy once your calculations are more involved.

NOTE: As a rule of thumb, a bit more math is always preferable to using more varyings. Memory tends to be much slower to access that just recalculating a value every frame. Also, CivTech games tend to be more limited by memory than by CPU performance.

<h1 id="spawn">Spawn:</h1>
The Spawn block is the first bit of code executed as soon as a particle is instantiated. The Spawn Block only ever gets executed once per particle and is guaranteed to fully execute before any of the code in the Sim block happens. The Spawn block is where you initialize any varyings that you are going in your particle, and it's also where you handle any of the particle's Spawn parameters (more on Spawn parameters later).

<h1 id="sim">Sim:</h1>
The Sim block is where you define the behavior of a particles through time. The Sim block gets run once per frame for every particle. The only way to pass data from one frame to the next is using varyings, since every local variable will get re-initialized every frame. Also remember that you are writing the logic for a single particle which has no information about other particles.

Since the Sim code is run once per frame, it means that the Sim block is frame-rate dependent, and you should program accordingly. To help you with that there is a helpful system function delta_time() which returns the number of seconds since the last frame. So wherever possible you should write your particle logic relative to the result from that function. For example:

| group My_Particle
 {
 varying float3 particle_position;
 SPAWN
 {
 particle_position = float3(0,0,0);
 }
 SIM
 {
 local float3 particle_velocity = float3(15,0,0);
 particle_position = particle_position + particle_velocity * delta_time();
 }
 property geometry_type = quad_rotated;
 property blend_type = additive;
 RENDER
 {
 export( "BASECOLOR_UV", float4(0,0,1,1) );
 export( "SCALE", float2(15, 5 ));
 export( "ROTATION", 0 );
 export( "POSITION", particle_position);
 export( "COLOR", float3(1,1,1));
 export( "ALPHA", 1);
 }
 } |
| --- |

In this example you can see that we set an initial position in the Spawn block, and then in the Sim block we're changing the position using a velocity. If we just added the velocity value every frame without multiplying it by the delta_time value the particle would move twice as fast if the game was running at 60 FPS than if it was running at 30 FPS.

<h1 id="properties">Properties:</h1>
Every particle program has a set of particle properties which are used to tell the engine what to do with the data that the program is going to export. A particle's properties are fixed at compile time and cannot be changed at runtime. Some properties require certain exports to be filled out. For example the "quad_rotated" property for the "geometry_type" requires the program to export a "ROTATION" value.

Most of the properties have default values which are the most common based on traditional particle effects. So, if you don't specify a property the default value will be used.

For more information on which properties are available, and what are their possible values and required exports go here (<a href="https://hub.firaxis.com/display/FXSMadrid/Emitter+Properties" class="uri">https://hub.firaxis.com/display/FXSMadrid/Emitter+Properties</a>*)*.

Each property can only be set once per particle program.

<h1 id="exports">Exports:</h1>
The exports in your program are ultimately the most important part. You can think of the exports as the actual output of the particle program back to the engine. Which exports you need to fill out is dependent on the Properties of the particle program whether explicit or implicit (which would be any properties you don't pick values for which would get their defaults).

You can fill out exports that you are not required based on the selected properties and that program will still compile but the exported data will be ignored. This can be useful if you're trying to iterate by changing what properties you are using so you can just export valid data into all the required exports. Otherwise you must remember to change your exports every time you change a program's properties.

| property geometry_type = quad_rotated;
 //property geometry_type = quad_aligned;
 property blend_type = additive;
 RENDER
 {
 export( "BASECOLOR_UV", float4(0,0,1,1) );
 export( "SCALE", float2(15, 5 ));
 export( "ROTATION", 0 );
 export( "TANGENT", float3(0,1,0) );
 export( "POSITION", particle_position);
 export( "COLOR", float3(1,1,1));
 export( "ALPHA", 1);
 } |
| --- |

The example shows that you can export the "ROTATION" and "TANGENT" values, even though they are required exclusively for the "quad_rotated" and "quad_aligned" properties respectively. That way you could easily try out the different geometry types by just swapping the comments in the properties section.

<h1 id="emitting-particles">Emitting particles:</h1>

| Up until this point we've been writing logic for a single particle which is not particularly interesting. In FireFX every particle can emit other particles at any point. You need to two things to be able to emit a particle, a particle definition, and an emit statement.
 A Particle definition has the same syntax as a group, the only difference is that you use the keyword "emitter" instead. So for example here is a very basic particle definition:
 emitter My_Particle
 \{
 SPAWN
 \{
 \}
 \\
 SIM
 \{
 \}
 \\
 property geometry_type = quad_rotated;
 property blend_type = additive;
 \\
 RENDER
 \{
 export( "BASECOLOR_UV", float4(0,0,1,1) );
 export( "SCALE", float2(15, 5 ));
 export( "ROTATION", 0 );
 export( "POSITION", float3(0,0,0));
 export( "COLOR", float3(1,1,1));
 export( "ALPHA", 1);
 \}
 \}
 You can then have your particle system emit particles of this type using an emit statement as follows:
 group My_Particle_System
 \{
 SPAWN
 \{
 emit_count("My_Particle", 7);
 \}
 \}
 This group will then emit seven particles of the type "My_Particle" as soon as it is spawned. There are two emit functions, emit_count() and emit_rate(), with the following syntax:
 emit_count("\[name of the emitter to emit\]", \[number of particles to emit\]);
 emit_rate("\[name of the emitter to emit\]", \[number of particles to emit per second\], \[Min number to emit, optional\]);
 the first one will immediately emit exactly that number of particles on that frame, while the second will emit however many particles in that frame as it needs to try to maintain the emission rate passed in. So if you are running at 30 frames per second, and you have an emit rate of 10 particles per second, it will emit a particle approximately once every third frame.
 The emit_count() function can be used in both the Spawn, and the Sim block of a particle, while the emit_rate() function can only be used in the Sim block since that's the only place it makes sense.
 Any particle can emit other particle at any point with a few exceptions: |
| --- |

- An emitter cannot emit other groups, you can only emit emitters

- An emitter cannot emit emitters of the same type as itself

- An emitter cannot emit emitters that would cause a cyclic dependency

- An emitter can only emit an emitter type once per frame. So you can't call the emit function multiple times in a block with the same emitter type. But you can emit any number of different emitters in a frame

<h2 id="emit-spawn-parameters">Emit Spawn Parameters:</h2>
The emit functions also allow you to pass arbitrary data into a particle when emitting it using the following syntax:

| emit_count("\[particle name\]", \[number of particles to emit\]) |
| --- |

<h1 id="section">{</h1>

| export("\[Parameter name 1\]", \[Parameter value 1\] ); |
| --- |

| export("\[Parameter name 2\]", \[Parameter value 2\] ); |
| --- |

<h1 id="section-1">…</h1>

| export("\[Parameter name n\]", \[Parameter value n\] ); |
| --- |

<h1 id="section-2">};</h1>

| \\
 When the particles get emitted, those parameters will get passed into them by matching up the parameter names to input parameters that the particles themselves define. Each particle can define what parameters it expects as either required or optional. You can pass in parameters that a particle is not expecting but they won't be used for anything. The order of the parameters does not matter since they are matched up by name. Any Spawn parameters that are exposed by an emitter that are not optional have to be passed in.
 An emitter defines the expected Spawn parameters as a set of function arguments on its Spawn block:
 group My_Particle
 \{
 SPAWN(\[Parameter type\] \[Parameter name 1\],
 \[Parameter type\] \[Parameter name 2\],
 …,
 \[Parameter type\] \[Parameter name n\]
 )
 \{
 …
 \}
 \}
 The Spawn parameters are then available as variables within the Spawn block, and will be initialized to the value that got passed in at the time the particle is emitted.
 For example:
 group My_Particle_System
 \{
 SPAWN
 \{
 emit_count("My_Particle", 1)
 \{
 export("minimum_size", 5 );
 export("maximum_size", 10 );
 \};
 \}
 \}
 emitter My_Particle
 \{
 varying float size;
 \\
 SPAWN( float minimum_size,
 float maximum_size
 )
 \{
 size = mix(minimum_size, maximum_size, random());
 \}
 \\
 property geometry_type = quad_rotated;
 property blend_type = additive;
 \\
 RENDER
 \{
 export( "BASECOLOR_UV", float4(0,0,1,1) );
 export( "SCALE", float2(size, size ));
 export( "ROTATION", 0 );
 export( "POSITION", float3(0,0,0));
 export( "COLOR", float3(1,1,1));
 export( "ALPHA", 1);
 \}
 \\
 \}
 \\
 In this example, the group is emitting a single particle that expects two parameters: "minimum_size" and "maximum_size". The particle then uses the mix() function (which linearly interpolates between two values using an interpolant value that goes from 0 to 1) and the random() function (which generates a pseudo random value form 0 to 1) to randomly pick a value between those two values and use that as the size of the particle.
 \\
 To define an emitter's Spawn parameter as optional add an equal sign (=) after the parameter name followed by the default value. If the parameter is not passed into the emit function, then the default value is used. Something like this:
 \\
 …
 SPAWN( float minimum_size = 1)
 …
 \\ |
| --- |

<h1 id="killing-particles">Killing particles:</h1>
Killing a particle allows you to stop the execution of a given particle. To kill a particle you must use the kill() function. The function takes a comparison expression, and the particle will get killed if the comparison evaluates to true.

| group My_Particle
 {
 varying float time;
 SPAWN
 {
 time = 0;
 }
 SIM
 {
 time = time + delta_time();
 kill(time > 3);
 }
 property geometry_type = quad_rotated;
 property blend_type = additive;
 RENDER
 {
 export( "BASECOLOR_UV", float4(0,0,1,1) );
 export( "SCALE", float2(15, 5 ));
 export( "ROTATION", 0 );
 export( "POSITION", float3(0,0,0));
 export( "COLOR", float3(1,1,1));
 export( "ALPHA", 1);
 }
 } |
| --- |

This example shows a particle with a time variable that keeps track of how long the particle has been alive. The kill() statement then checks if the time variable is greater than 3, and if it is then it will kill the particle. Effectively this makes the particle exist for three seconds and then disappear.

The kill statement will get executed at the location that it is in the script, so if a particle is killed it will not execute any lines of code that come after the kill statement. This is especially important for emit calls being done on the frame that the particle will be killed. If you want the particles to be emitted before the particle is killed, then those calls need to be before the kill() statement.

Note: particles that are no longer being managed by some system in the game will eventually be killed after 10 seconds to avoid flooding the game with particles that weren't killed.

<h1 id="flow-control">Flow control:</h1>
FireFX does not support any kind of traditional flow control like "if" or "for" statements. The closest thing that is currently available is a ternary selector operator with the following syntax:

(conditional expression)? expression1 : expression2

If the conditional expression is true, then the operator returns the first expression, and if the condition is false then the second condition is returned.

You can use this to mask out certain behavior based on whether a condition is true. For example:

| group My_Particle
 {
 varying float3 particle_position;
 varying float time;
 SPAWN
 {
 time = 0;
 particle_position = float3(0,0,0);
 }
 SIM
 {
 time = time + delta_time();
 local float velocity_mask = (time < 5)? 1 : 0;
 local float3 particle_velocity = float3(15,0,0) * velocity_mask;
 particle_position = particle_position + particle_velocity * delta_time();
 }
 property geometry_type = quad_rotated;
 property blend_type = additive;
 RENDER
 {
 export( "BASECOLOR_UV", float4(0,0,1,1) );
 export( "SCALE", float2(15, 5 ));
 export( "ROTATION", 0 );
 export( "POSITION", particle_position);
 export( "COLOR", float3(1,1,1));
 export( "ALPHA", 1);
 }
 } |
| --- |

This example shows a particle that keeps track of how long it's been alive, and then masks whether to apply a velocity to it if the time elapsed is less than 5.

<h1 id="includes-and-defines">Includes and defines:</h1>
The FireFX scripting system includes a c-style preprocessing step that lets you do things like have Include files and define directives.

Include files let you write libraries of script functions that are frequently used. Includes must be done in the outermost scope of the script file, grouped together at the top of the file for readability. Syntax is: Pound symbol (#) followed by the keyword "include" followed by the name of the file to be included in quotations:

#include "Math.FXH"

Defines let you define commonly used constants readable names and simple functions to be inlined. The define syntax is a little more complicated and will not be covered here. You can look up the syntax for C style preprocessor on the webs.

<h1 id="system-functions">System functions:</h1>
Here's a few of the more common system functions:

hash(float x): return a pseudo random value between 0 to 1 that is deterministic based on the input float. So if you give it the same input number you'll get the same random number back.

max(float a, float b): returns the highest of the two values a or b.

min(float a, float b): returns the lowest of the two values a or b.

sin(float angle): returns the sine of he given input angle. Input angle expected in radians.

cos(float angle): returns the cosine of he given input angle. Input angle expected in radians.

floor(float x): returns the nearest integer value to the input number rounded down.

ceil(float x): returns the nearest integer value to the input number rounded up.

frac(float x): returns the fractional component of the input number

mix(float a, float b, float time): return the linearly interpolated value between a and b using the value t as the time from zero to one. So if t = 0 then it will return a, if t = 1 it will return b, and t = 0.5 will return a value half way between a and b.

<h2 id="spawn-specific">Spawn specific:</h2>
This functions can only be used in the Spawn block of a program

random(): returns a pseudo random between 0 and 1.

index(): returns the index of the particle within the system. Each particle in a system is given an ordered index value based on spawn order (the first particle emitted has index 0, the next one has index 1, and so forth). Each emitter in a system has its own set of indices each starting at index 0.

instance_id(): returns a unique identifier number for the entire effect instance, and all of its particles.

<h2 id="sim-specific">Sim specific:</h2>
This functions can only be used in the Sim block of a program

delta_time(): returns the time in seconds that has elapsed since the last frame.

<h1 id="best-practices">Best Practices:</h1>
Following are some best practices and paradigms that should help you create scripts that are efficient and easy to understand.

<h2 id="particle-age">Particle age:</h2>
Divisions are relatively expensive (compared to multiplications and additions), so we try to avoid doing them wherever possible. Having a normalized age value (from zero to one) for a particle is a very common use case. If you know the lifetime of the particle at the Spawn of a particle you can calculate the reciprocal, and then use that to keep your age as a normalized value using only one division in the Spawn block:

| group My_Particle
 {
 varying float age;
 varying float inverse_lifetime;
 SPAWN
 {
 age = 0;
 local float lifetime = random() * 10;
 inverse_lifetime = 1 / lifetime;
 }
 SIM
 {
 age = age + delta_time() * inverse_lifetime;
 kill(age > 1);
 }
 property geometry_type = quad_rotated;
 property blend_type = additive;
 RENDER
 {
 export( "BASECOLOR_UV", float4(0,0,1,1) );
 export( "SCALE", float2(5, 5 ) * (1-age));
 export( "ROTATION", 0 );
 export( "POSITION", float3(0,0,0));
 export( "COLOR", float3(1,1,1));
 export( "ALPHA", 1);
 }
 } |
| --- |

In this example the "age" value will start at 0 in the Spawn, and will become 1 at the particle's "lifetime" value which is randomly calculated in the Spawn block.

<h2 id="tweens-and-shaping-functions">Tweens and shaping functions:</h2>
<h2 id="forces-and-integration">Forces and integration:</h2>
<h2 id="terrain-collision">Terrain collision:</h2>
<h2 id="world-and-local-spaces">World and local spaces:</h2>
<h2 id="flipbooks">Flipbooks:</h2>