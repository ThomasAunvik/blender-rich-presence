# ---------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------- HEADER --#

"""
:author:


:synopsis:
    

:description:
    

:applications:
    
:see_also:
   
:license:
    see license.txt and EULA.txt 

"""

# ---------------------------------------------------------------------------------------#
# ---------------------------------------------------------------------------- IMPORTS --#

import bpy
import os
from .utils.io import IO

# Enable for verbose printing
v = True
# Enable for very verbose printing
vv = True


datablock_icons =[('action', 'Action', 'Action', 'ACTION', 0),
                ('armature', 'Armature', 'Armature', 'MOD_ARMATURE', 1),
                ('cache', 'Cache', 'Cache', 'DISK_DRIVE', 2 ),
                ('camera', 'Camera', 'Camera', 'CAMERA_STEREO', 3),
                ('curve', 'Curve', 'Curve', 'MOD_CURVE', 4),
                ('group', 'Group', 'Group', 'GROUP', 5),
                ('image', 'Image', 'Image', 'IMAGE_COL', 6),
                ('lamp', 'Lamp', 'Lamp', 'LAMP', 7),
                ('library', 'Library', 'Library', 'LIBRARY_DATA_INDIRECT', 8),
                ('material', 'Material', 'Material', 'MATERIAL', 9),
                ('mesh', 'Mesh', 'Mesh', 'OUTLINER_OB_MESH', 10),
                ('node', 'Node Group', 'Node Group', 'NODETREE', 11),
                ('object', 'Object', 'Object', 'OBJECT_DATA', 12),
                ('particle', 'Particle System', 'Particle System', 'MOD_PARTICLES', 13),
                ('scene', 'Scene', 'Scene', 'SCENE', 14),
                ('text', 'Text', 'Text', 'TEXT', 15),
                ('world', 'World', 'World', 'WORLD', 16),
                ('none', 'None', 'None', 'CANCEL', 17)]


# ---------------------------------------------------------------------------------------#
# -------------------------------------------------------------------------- FUNCTIONS --#
# default false, icons not supporter till proven supported
use_icons = False
# global collection for custom icons, save different subsets as needed
preview_collections = {}
# storing full list of loaded asset_thumb_ids in case of filtering enums


# function called in register to load icons
def load_icons():
    pcoll_icons = bpy.utils.previews.new()

    # icon path
    icons_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "icons")

    # load a specific icon
    pcoll_icons.load(
        "blender_logo",
        os.path.join(icons_dir, "blender_logo.png"),
        'IMAGE')
    pcoll_icons.load(
        "pretty_render",
        os.path.join(icons_dir, "pretty_render.png"),
        'IMAGE')

    # name one set of general purpose icons
    preview_collections["icons"] = pcoll_icons
    pcoll_asset_gallery = bpy.utils.previews.new()


# ---------------------------------------------------------------------------------------#
# ---------------------------------------------------------------------------- CLASSES --#

def register():

    # -----------------------------------------------
    # For preview icons
    # -----------------------------------------------

    global use_icons
    try: # We only need to check this once here
        import bpy.utils.previews
        use_icons = True
    except:
        use_icons = False

    # load the icons here, only need to do so once
    if use_icons:
        load_icons()

    # -----------------------------------------------
    # Misc
    # -----------------------------------------------

    if vv:
        IO.info("Blender Rich Presence registered successfully.")


def unregister():

    # -----------------------------------------------
    # Remove icons if used
    # -----------------------------------------------

    # de-reg/load the pcoll
    global use_icons, preview_collections
    if use_icons:
        for pcoll in preview_collections.values():
            bpy.utils.previews.remove(pcoll)
        preview_collections.clear()
