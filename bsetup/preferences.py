# ---------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------------- HEADER --#

"""
:author:
    Jared Webber
    

:synopsis:
    

:description:
    

:applications:
    
:see_also:
   
:license:
    see license.txt and EULA.txt 

"""

# ---------------------------------------------------------------------------------------#
# ---------------------------------------------------------------------------- IMPORTS --#


# ---------------------------------------------------------------------------------------#
# -------------------------------------------------------------------------- FUNCTIONS --#

# ---------------------------------------------------------------------------------------#
# ---------------------------------------------------------------------------- CLASSES --#
import bpy
from bpy.types import AddonPreferences
from bpy.props import StringProperty

addonName = str("blender-rich-presence")

def get_prefs():
    import bpy
    return bpy.context.user_preferences.addons[addonName].preferences

class BlenderRichPresencePreferences(AddonPreferences):
    bl_idname = addonName

    username = StringProperty(
        name='Username',
        default='',
    )

    password = StringProperty(
        name="Password",
        default="",
        subtype='PASSWORD'
    )

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.prop(self, "username", text="Username")
        row.prop(self, "password", text="Password")
        row = layout.row()
        row.operator('brpc.test')


def register():
    bpy.utils.register_class(BlenderRichPresencePreferences)

def unregister():
    bpy.utils.unregister_class(BlenderRichPresencePreferences)