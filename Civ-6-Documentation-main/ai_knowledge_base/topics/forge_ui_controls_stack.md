---
title: "Stack"
category: "Forge UI Controls"
summary: "<Stack> Friday, February 21, 2014 2:47 PM The Stack is used to arrange children into a line, or a grid.  If the children change sizes, their positions will be adjusted correctly, but the Stack itse..."
keywords: ["stack","forge","controls","control","layout"]
---

# Stack

**<Stack>**

Friday, February 21, 2014

2:47 PM

The **Stack** is used to arrange children into a line, or a grid. If the children change sizes, their positions will be adjusted correctly, but the Stack itself will not have its size update until **CalculateSize()** is called.

| **Attribute** | **Details** |
| --- | --- |
| **Padding** | Deprecated: See “StackPadding” |
| **StackGrowth** | Direction the stack grows in: "Bottom" "Down" "Top" "Up" "Left" "Right" |
| **StackPadding** | Number of pixels to insert in between child elements. (Formally: “Padding”) |
| **WrapGrowth** | How items that exceed the wrap width will continue to stack. |
| **WrapWidth** | How far (wide or tall, depending on stack growth) items can be put into the stack before subsequent items are “wrapped”. |

When **WrapGrowth** & **WrapWidth** are utilized, they are what allow for 2D layout to occur once a line of stacking exceeds a certain limit.

![Machine generated alternative text: L> Wrap Width is set. Until it is Without Wrap Width this ...since WrapGrowth is hit items are place in a line, would occur but instead... bottom, a new line, below the original is started.](../Forge UI\Controls\Stack/media/image1.png)