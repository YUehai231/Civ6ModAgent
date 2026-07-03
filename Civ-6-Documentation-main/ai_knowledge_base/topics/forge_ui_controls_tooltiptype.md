---
title: "ToolTipType"
category: "Forge UI Controls"
summary: "<ToolTipType> Friday, February 21, 2014 2:21 PM Defines a custom tool tip that overrides the default tool tip.  XML Attribute Type Details Name String The tool tip instance name used by other compo..."
keywords: ["tooltiptype","forge","controls","lua","xml","texture","control","reference"]
---

# ToolTipType

**<ToolTipType>**

Friday, February 21, 2014

2:21 PM

Defines a custom tool tip that overrides the default tool tip.

**XML**

| **Attribute** | **Type** | **Details** |
| --- | --- | --- |
| Name | String | The tool tip instance name used by other components to reference this tooltip. |

*<em>Example:*</em>

<ToolTipType Name="TypeRoundImage">

<Image ID="ToolTipFrame" Anchor="L,T" Size="64,64" Offset="20,-32" Texture="64x64FrameButtons.dds" >

<Image ID="ToolTipImage" Anchor="C,C" Size="64,64" Texture="UnitPortraitsEarly512.dds" />

</Image>

</ToolTipType>

<!-- Defining use of the tooltip -->

<GridButton        ID="CustomButton" ToolTipType="TypeRoundImage" />

**LUA Functions**

| **Function** | **Returns** | **Arguments** |
| --- | --- | --- |
| SetToolTipCallback() | nil | Tooltip callback function. |

*<em>Example:*</em>

-- Set the function to call when a tooltip is activated

Controls.MyButton:SetToolTipCallback( OnToolTip );

-- Fill a table with the controls used by the tooltip

local tipControlTable = {};

TTManager:GetTypeControlTable( "TypeRoundImage", tipControlTable );

-- Callback function populating elements

function OnToolTip( control )

local id = control:GetVoid1();        

local article = m_categorizedListOfArticles[(m_selectedCategory * MAX_ENTRIES_PER_CATEGORY) + id];

if article and article.tooltipTexture then

tipControlTable.ToolTipImage:SetTexture( article.tooltipTexture );

tipControlTable.ToolTipImage:SetTextureOffset( article.tooltipTextureOffset );

tipControlTable.ToolTipFrame:SetHide( false );

else

tipControlTable.ToolTipFrame:SetHide( true );

end                

end