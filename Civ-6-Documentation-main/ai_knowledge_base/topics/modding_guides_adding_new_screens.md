---
title: "Adding New Screens"
category: "Modding Guides"
summary: "In Civ 6, screens are referred to as LuaContexts.  LuaContexts are made up of two separate files: 1."
keywords: ["adding","screens","modding","guides","lua","xml","screen","control","layout","reference"]
---

# Adding New Screens

In Civ 6, screens are referred to as LuaContexts. LuaContexts are made up of two separate files:

1. - An XML file that defines the layout and composition of the screen

- A LUA script file that populates controls with game data and handles user interaction

Both of these files must have the same filename, ex:

```lua
MyNewScreen.xml
MyNewScreen.lua
```

---

*Note:*
The `<ReplaceUIScript>` modinfo element allows you to specify a different lua file for a LuaContext. This is mainly used for extending base game UI files, and not something you need to worry about if creating entirely new UI screens.

---

Adding new UI screens to Civ 6 consists of a few steps:

1. - Create the XML and LUA files, for example:

`MyNewScreen.xml`

```xml
<code class="language-xml"><?xml version="1.0" encoding="utf-8"?>

<Context Name="MyNewScreen">
    <Label ID="MyText" Anchor="C,C" Align="Center" Style="HeaderFont" String="My New Screen"/>
</Context>
</code>
```

`MyNewScreen.lua`:

```xml
<code class="language-lua">-- We usually define an Initialize function at the bottom of the file and immediately call it. This is a convention we use to organizate our code and is completely optional.
function Initialize()
    Controls.MyText:SetText(Controls.MyText:GetText() .. " is Awesome!");
end
Initialize();
</code>
```

1. - Add a reference to both files in the `<Files>` section of the modinfo using the `<File>` tag, ex:

```xml
<code class="language-xml"><Files>
    <File>UI/MyNewScreen.xml</File>
    <File>UI/MyNewScreen.lua</File>
</Files>
</code>
```

1. - Ensure your modinfo defines a `<InGameActions>` and `<Files>` sections, then:
<ol>
2. Create `<AddUserInteraces>` section within `<InGameActions>`.

- Create `<Properties>` section within `<AddUserInteraces>`.

- Add `<Context>InGame</Context>` within `<Properties>` section, this specifies that the following LuaContexts will only be loaded within the game.

- Create `<ImportFiles>` section within `<InGameActions>`.

- Add a reference to your new files in the `<ImportFiles>` section using the `<File>` tag.

</li>
</ol>

---

Here's an example asimple  modinfo file that incorporates all of the steps above:

`MyMod.modinfo`:

```xml
<code class="language-xml"><?xml version="1.0" encoding="utf-8"?>
<Mod id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" version="1">
    <Properties>
        <Name>MyMod</Name>
        <Teaser>My Mod is Awesome</Teaser>
        <Description>My Mod adds new UI screens</Description>
        <Authors>Me</Authors>
        <EnabledByDefault>1</EnabledByDefault>
    </Properties>
    <ActionCriteria>
        <Criteria id="MyNewMod">
            <RuleSetInUse>My New Rules!</RuleSetInUse>
        </Criteria>
    </ActionCriteria>
    <InGameActions>
        <AddUserInterfaces id="MyNewModInGameUI" criteria="MyNewMod">
            <Properties>
                <Context>InGame</Context>
            </Properties>
            <File>UI/MyNewScreen.xml</File>
            <File>UI/MyNewScreen.lua</File>
        </AddUserInterfaces>
        <ImportFiles id="MyNewModFiles" criteria="MyNewMod">
            <File>UI/MyNewScreen.xml</File>
            <File>UI/MyNewScreen.lua</File>
        </ImportFiles>
    </InGameActions>
    <Files>
        <File>UI/MyNewScreen.xml</File>
        <File>UI/MyNewScreen.lua</File>
    </Files>
</Mod>
</code>
```

// TODO: Explain id and criteria attributes