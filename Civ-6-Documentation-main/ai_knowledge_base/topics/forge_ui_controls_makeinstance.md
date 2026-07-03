---
title: "MakeInstance"
category: "Forge UI Controls"
summary: "<MakeInstance> Friday, February 21, 2014 2:35 PM Immediately creates an instance of an object; similar to calling ContextPtr:BuildInstanceForControl.  You can define how to access the instance with..."
keywords: ["makeinstance","forge","controls","lua","control"]
---

# MakeInstance

**<MakeInstance>**

Friday, February 21, 2014

2:35 PM

Immediately creates an instance of an object; similar to calling **ContextPtr:BuildInstanceForControl**.

You can define how to access the instance within the **Controls** table by setting the **ID** attribute. If you don't set the attribute, the **Name** of the instance will be used instead.

**Examples:**

<Instance Name="MyBarInstance">

<Bar ID="BarControl" Size="10,10" Hidden="1"/>

</Instance>

<Instance Name="MyBoxInstance">

<Box ID="BoxControl" Size="10,10" Hidden="1"/>

</Instance>

<Stack>

<MakeInstance Name="MyBarInstance"/>

<MakeInstance Name="MyBoxInstance" ID="MyBoxWithID"/>

</Stack>

-- In Lua:

Controls.MyBarInstance.BarControl:SetHide(false);

Controls.MyBoxWithID.BoxControl:SetHide(false);