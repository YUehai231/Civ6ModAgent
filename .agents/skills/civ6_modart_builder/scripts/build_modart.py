import os
import sys
import argparse
import re
import xml.etree.ElementTree as ET

# Embed lib_modart dictionaries for self-containment
ART_CONSUMERS = {
    'Units': {
        'relativeArtDefPaths': ['Units.artdef', 'Unit_Bins.artdef', 'Units_Great_People.artdef', 'Eras.artdef', 'UnitActivities.artdef'],
        'libraryDependencies': ["Unit", "VFX", "Light"],
        'loadsLibraries': "true"
    },
    'Clutter': {
        'relativeArtDefPaths': ["Clutter.artdef"],
        'libraryDependencies': ["Landmark"],
        'loadsLibraries': "true"
    },
    'Landmarks': {
        'relativeArtDefPaths': ['Landmarks.artdef', 'CityGenerators.artdef', 'Eras.artdef', 'Cultures.artdef', 'Civilizations.artdef', 'Improvements.artdef', 'Resources.artdef'],
        'libraryDependencies': ["CityBuildings", "TileBase", "RouteDecalMaterial"],
        'loadsLibraries': "true"
    },
    'Farms': {
        'relativeArtDefPaths': ["Farms.artdef"],
        'libraryDependencies': ["TileBase", "CityBuildings"],
        'loadsLibraries': "true"
    },
    'GameLighting': {
        'relativeArtDefPaths': ["GameLighting.artdef"],
        'libraryDependencies': ["ColorKey", "GameLighting"],
        'loadsLibraries': "true"
    },
    'StrategicView_Properties': {
        'relativeArtDefPaths': ["StrategicView.artdef"],
        'libraryDependencies': [],
        'loadsLibraries': "false"
    },
    'StrategicView_Sprite': {
        'relativeArtDefPaths': ["StrategicView.artdef"],
        'libraryDependencies': ["StrategicView_Sprite", "StrategicView_DirectedAsset"],
        'loadsLibraries': "true"
    },
    'StrategicView_Route': {
        'relativeArtDefPaths': ["StrategicView.artdef"],
        'libraryDependencies': ["StrategicView_Route", "StrategicView_DirectedAsset"],
        'loadsLibraries': "true"
    },
    'StrategicView_TerrainType': {
        'relativeArtDefPaths': ["StrategicView.artdef"],
        'libraryDependencies': ["StrategicView_TerrainBlend", "StrategicView_TerrainBlendCorners", "StrategicView_TerrainType", "StrategicView_DirectedAsset"],
        'loadsLibraries': "true"
    },
    'StrategicView_TerrainBlendCorners': {
        'relativeArtDefPaths': ["StrategicView.artdef"],
        'libraryDependencies': ["StrategicView_TerrainBlendCorners", "StrategicView_DirectedAsset"],
        'loadsLibraries': "true"
    },
    'StrategicView_TerrainBlend': {
        'relativeArtDefPaths': ["StrategicView.artdef"],
        'libraryDependencies': ["StrategicView_TerrainBlend", "StrategicView_DirectedAsset"],
        'loadsLibraries': "true"
    },
    'Terrain': {
        'relativeArtDefPaths': ["TerrainStyle.artdef", "GraphicsTweaks.artdef"],
        'libraryDependencies': ["TerrainAsset", "TerrainElement", "TerrainMaterial"],
        'loadsLibraries': "true"
    },
    'WorldViewRoutes': {
        'relativeArtDefPaths': ["WorldViewRoutes.artdef", "Eras.artdef"],
        'libraryDependencies': ["RouteDecalMaterial", "RouteDoodad"],
        'loadsLibraries': "true"
    },
    'UI': {
        'relativeArtDefPaths': ["UserInterface.artdef"],
        'libraryDependencies': ["UITexture"],
        'loadsLibraries': "true"
    },
    'FOW': {
        'relativeArtDefPaths': ["FOW.artdef"],
        'libraryDependencies': ["FOWSprite", "FOWTexture"],
        'loadsLibraries': "true"
    },
    'WonderMovie': {
        'relativeArtDefPaths': ["WonderMovie.artdef"],
        'libraryDependencies': ["WonderMovie", "TileBase", "GameLighting", "ColorKey"],
        'loadsLibraries': "true"
    },
    'UILensAsset': {
        'relativeArtDefPaths': ["Overlay.artdef"],
        'libraryDependencies': ["OverlayTexture", "UILensAsset"],
        'loadsLibraries': "true"
    },
    'Overlay': {
        'relativeArtDefPaths': ["Overlay.artdef"],
        'libraryDependencies': ["OverlayTexture", "UILensAsset"],
        'loadsLibraries': "true"
    },
    'VFX': {
        'relativeArtDefPaths': ["VFX.artdef"],
        'libraryDependencies': ["VFX", "Light"],
        'loadsLibraries': "true"
    },
    'Water': {
        'relativeArtDefPaths': ["Water.artdef"],
        'libraryDependencies': ["Water"],
        'loadsLibraries': "true"
    },
    'ColorKeys': {
        'relativeArtDefPaths': [],
        'libraryDependencies': ["ColorKey"],
        'loadsLibraries': "true"
    },
    'Camera': {
        'relativeArtDefPaths': ["Camera.artdef"],
        'libraryDependencies': ["CameraAnimation"],
        'loadsLibraries': "true"
    },
    'Terrains': {
        'relativeArtDefPaths': ["Terrains.artdef"],
        'libraryDependencies': [],
        'loadsLibraries': "false"
    },
    'Features': {
        'relativeArtDefPaths': ["Features.artdef"],
        'libraryDependencies': [],
        'loadsLibraries': "false"
    },
    'Civilizations': {
        'relativeArtDefPaths': ["Civilizations.artdef"],
        'libraryDependencies': [],
        'loadsLibraries': "false"
    },
    'Cultures': {
        'relativeArtDefPaths': ["Cultures.artdef", "Civilizations.artdef"],
        'libraryDependencies': [],
        'loadsLibraries': "false"
    },
    'Resources': {
        'relativeArtDefPaths': ["Resources.artdef"],
        'libraryDependencies': [],
        'loadsLibraries': "false"
    },
    'Improvements': {
        'relativeArtDefPaths': ["Improvements.artdef"],
        'libraryDependencies': [],
        'loadsLibraries': "false"
    },
    'WorldView_Translate': {
        'relativeArtDefPaths': ['Districts.artdef', 'Buildings.artdef', 'Eras.artdef', 'Features.artdef', 'Improvements.artdef', 'Resources.artdef', 'Terrains.artdef', 'Civilizations.artdef', 'WorldViewRoutes.artdef', 'Appeal.artdef', 'Cultures.artdef'],
        'libraryDependencies': [],
        'loadsLibraries': "false"
    },
    'StrategicView_Translate': {
        'relativeArtDefPaths': ['Eras.artdef', 'Terrains.artdef', 'Features.artdef', 'Routes.artdef', 'Improvements.artdef', 'Districts.artdef', 'Buildings.artdef', 'Cities.artdef'],
        'libraryDependencies': [],
        'loadsLibraries': "false"
    },
    'Audio': {
        'relativeArtDefPaths': ['Civilizations.artdef', 'Features.artdef', 'GoodyHuts.artdef', 'Terrains.artdef', 'Units.artdef', 'Improvements.artdef', 'Resources.artdef', 'Eras.artdef', 'Districts.artdef', 'Leaders.artdef'],
        'libraryDependencies': [],
        'loadsLibraries': "false"
    },
    'LeaderLighting': {
        'relativeArtDefPaths': ["Leaders.artdef"],
        'libraryDependencies': ["LeaderLighting", "ColorKey"],
        'loadsLibraries': "true"
    },
    'Leaders': {
        'relativeArtDefPaths': ["Leaders.artdef"],
        'libraryDependencies': ["Leader", "LeaderLighting", "ColorKey"],
        'loadsLibraries': "true"
    },
    'LeaderFallback': {
        'relativeArtDefPaths': ["FallbackLeaders.artdef"],
        'libraryDependencies': ["LeaderFallback"],
        'loadsLibraries': "true"
    },
    'Lenses': {
        'relativeArtDefPaths': ["Lenses.artdef"],
        'libraryDependencies': [],
        'loadsLibraries': "false"
    },
    'IndirectGrid': {
        'relativeArtDefPaths': ["Features.artdef", "GraphicsTweaks.artdef", "Improvements.artdef", "Terrains.artdef"],
        'libraryDependencies': [],
        'loadsLibraries': "false"
    },
    'AOSystem': {
        'relativeArtDefPaths': ["GraphicsTweaks.artdef"],
        'libraryDependencies': [],
        'loadsLibraries': "false"
    },
    'GenericObject': {
        'relativeArtDefPaths': [],
        'libraryDependencies': [],
        'loadsLibraries': "false"
    },
    'Wave': {
        'relativeArtDefPaths': ["Wave.artdef"],
        'libraryDependencies': ["Wave"],
        'loadsLibraries': "true"
    },
    'DynamicGeometry': {
        'relativeArtDefPaths': ["Walls.artdef"],
        'libraryDependencies': ["DynamicGeometry"],
        'loadsLibraries': "true"
    },
    'UIPreview': {
        'relativeArtDefPaths': ["UIPreview.artdef"],
        'libraryDependencies': [],
        'loadsLibraries': "false"
    },
    'SkyBox': {
        'relativeArtDefPaths': ["SkyBox.artdef"],
        'libraryDependencies': ["SkyBoxTexture"],
        'loadsLibraries': "true"
    },
    'Minimap': {
        'relativeArtDefPaths': ["Minimap.artdef"],
        'libraryDependencies': [],
        'loadsLibraries': "false"
    },
    'UnitSimulation': {
        'relativeArtDefPaths': ["UnitOperations.artdef", "Improvements.artdef"],
        'libraryDependencies': [],
        'loadsLibraries': "false"
    },
    'RangeArrows': {
        'relativeArtDefPaths': ["Overlay.artdef"],
        'libraryDependencies': ["OverlayTexture", "UILensAsset"],
        'loadsLibraries': "true"
    }
}

GAME_LIBRARIES = [
    'CityBuildings', 'ColorKey', 'DynamicGeometry', 'FOWSprite', 'FOWTexture',
    'GameLighting', 'Landmark', 'Leader', 'LeaderFallback', 'LeaderLighting',
    'Light', 'OverlayTexture', 'RouteDecalMaterial', 'RouteDoodad', 'SkyBoxTexture',
    'StrategicView_DirectedAsset', 'StrategicView_Route', 'StrategicView_Sprite',
    'StrategicView_TerrainBlend', 'StrategicView_TerrainBlendCorners',
    'StrategicView_TerrainType', 'TerrainAsset', 'TerrainElement', 'TerrainMaterial',
    'TileBase', 'UILensAsset', 'UITexture', 'Unit', 'VFX', 'Water', 'Wave', 'WonderMovie'
]

def get_art_template_name(artdef_path):
    try:
        with open(artdef_path, "r", encoding="utf-8", errors="ignore") as f:
            match = re.search(r'<m_TemplateName text="([^"]*)"/>', f.read())
            if match:
                return match.group(1)
    except Exception as e:
        print(f"Error parsing template in {artdef_path}: {e}")
    return ""

def get_xlp_class_package(xlp_path):
    try:
        with open(xlp_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            m_class = re.search(r'<m_ClassName text="([^"]*)"/>', content)
            m_package = re.search(r'<m_PackageName text="([^"]*)"/>', content)
            c = m_class.group(1) if m_class else ""
            p = m_package.group(1) if m_package else ""
            return c, p
    except Exception as e:
        print(f"Error parsing XLP in {xlp_path}: {e}")
    return "", ""

def main():
    parser = argparse.ArgumentParser(description="Civilization VI ModArt Compiler")
    parser.add_argument("--project-dir", required=True, help="Path to project directory containing Artdefs/ and/or XLPs/")
    parser.add_argument("--mod-name", required=True, help="Mod name")
    parser.add_argument("--mod-id", required=True, help="Mod UUID/GUID")
    args = parser.parse_args()

    project_dir = os.path.abspath(args.project_dir)
    artdefs_dir = os.path.join(project_dir, "Artdefs")
    xlps_dir = os.path.join(project_dir, "XLPs")

    # Scan Artdefs
    art_files = {}
    if os.path.exists(artdefs_dir):
        for f in os.listdir(artdefs_dir):
            if f.endswith(".artdef"):
                tname = get_art_template_name(os.path.join(artdefs_dir, f))
                art_files[f] = {"tname": tname, "bname": f}

    # Scan XLPs
    xlp_files = {}
    if os.path.exists(xlps_dir):
        for f in os.listdir(xlps_dir):
            if f.endswith(".xlp"):
                cname, pkgname = get_xlp_class_package(os.path.join(xlps_dir, f))
                if cname:
                    xlp_files[cname] = {"pkg": pkgname, "bname": f}

    # Build XML structure
    root = ET.Element("AssetObjects::GameArtSpecification")
    
    # ID
    id_node = ET.SubElement(root, "id")
    ET.SubElement(id_node, "name").text = args.mod_name
    ET.SubElement(id_node, "id").text = args.mod_id

    # Art Consumers
    consumers_node = ET.SubElement(root, "artConsumers")
    for name, config in ART_CONSUMERS.items():
        element = ET.SubElement(consumers_node, "Element")
        ET.SubElement(element, "consumerName").text = name
        
        # relativeArtDefPaths
        art_paths_node = ET.SubElement(element, "relativeArtDefPaths")
        if name == "Clutter":
            # Clutter is always added if we have it
            ET.SubElement(art_paths_node, "Element").text = "Clutter.artdef"
        else:
            relative_paths = config["relativeArtDefPaths"]
            for artdef_file, artdef_info in art_files.items():
                if artdef_file in relative_paths or artdef_info["tname"] == name or artdef_info["bname"] == name:
                    ET.SubElement(art_paths_node, "Element").text = artdef_file
                    
        # libraryDependencies
        lib_deps_node = ET.SubElement(element, "libraryDependencies")
        for dep in config["libraryDependencies"]:
            ET.SubElement(lib_deps_node, "Element").text = dep
            
        # loadsLibraries
        ET.SubElement(element, "loadsLibraries").text = "true" if config["libraryDependencies"] else "false"

    # Game Libraries
    libraries_node = ET.SubElement(root, "gameLibraries")
    for name in GAME_LIBRARIES:
        element = ET.SubElement(libraries_node, "Element")
        ET.SubElement(element, "libraryName").text = name
        
        pkg_paths_node = ET.SubElement(element, "relativePackagePaths")
        if name in xlp_files:
            ET.SubElement(pkg_paths_node, "Element").text = xlp_files[name]["pkg"]

    # Required Game Art IDs
    req_ids_node = ET.SubElement(root, "requiredGameArtIDs")
    element = ET.SubElement(req_ids_node, "Element")
    ET.SubElement(element, "name").text = "Civ6"
    ET.SubElement(element, "id").text = "cb2f71b7-843e-4af3-9ca7-992acda9c195"

    # Write out Mod.Art.xml
    out_path = os.path.join(project_dir, "Mod.Art.xml")
    
    # Custom XML writer to format in AssetObjects style (e.g. self-closing, double quotes)
    def indent_node(elem, level=0):
        i = "\n" + level*"    "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "    "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for child in elem:
                indent_node(child, level+1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i

    indent_node(root)
    tree = ET.ElementTree(root)
    tree.write(out_path, encoding="utf-8", xml_declaration=True)
    print(f"Successfully generated Mod.Art.xml: {out_path}")

if __name__ == "__main__":
    main()
