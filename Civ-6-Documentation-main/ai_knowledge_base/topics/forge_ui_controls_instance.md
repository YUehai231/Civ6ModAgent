---
title: "Instance"
category: "Forge UI Controls"
summary: "<Instance> Tuesday, July 25, 2017 5:22 PM Defines a collection of controls that can be created either using the <MakeInstance> tag or by calling ContextPtr:BuildInstanceForControl Example: <Instanc..."
keywords: ["instance","forge","controls","lua","control"]
---

# Instance

<Instance>

Tuesday, July 25, 2017

5:22 PM

Defines a collection of controls that can be created either using the **<MakeInstance>** tag or by calling **ContextPtr:BuildInstanceForControl()**

**Example:**

<Instance Name="MyInstance">

<Bar ID="TopControl" Size="10,10" Hidden="1"/>

</Instance>

<Stack ID="MyStack">

<MakeInstance Name="MyInstance"/>

</Stack>

-- Create instance in Lua:

local myInstance:table = {};

ContextPtr:BuildInstanceForControl("MyInstance", myInstance, Controls.MyStack);