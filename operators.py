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
import bpy
from bpy.types import Operator
from .utils.io import IO
# ---------------------------------------------------------------------------------------#
# -------------------------------------------------------------------------- FUNCTIONS --#

# ---------------------------------------------------------------------------------------#
# ---------------------------------------------------------------------------- CLASSES --#

class BRPC_Operator(object):
    pass

class BRPC_TestOperator(BRPC_Operator, Operator):
    bl_idname = 'brpc.test'
    bl_label = "Blender Rich Presence Test"
    bl_description ="Blender Rich Presence Test Operator"
    bl_options = {'REGISTER', "UNDO", 'INTERNAL'}

    def execute(self, context):
        self.login()
        return {"FINISHED"}

    def login(self):
        from .brpc import rpc
        import time
        import bpy
        from .bsetup.preferences import get_prefs
        preferences = get_prefs()
        user_data = (preferences.username, preferences.password)
        IO.debug("Printing User Preferences")
        print("Blender Rich Presence: Preferences")
        print("Username: %s" % preferences.username)

        client_id = '434079082339106827'
        rpc_obj = rpc.DiscordIpcClient.for_platform(client_id)
        time.sleep(5)
        start_time = time.time()
        filename = 'test.blend'
        version_no = '2.79'

        while True:
            activity = {
                "details": "Using Blender " + version_no,
                "state": "Working on " + filename,
                "timestamps": {
                    "start": start_time
                },
                "assets": {
                    "small_text": "Blender " + version_no,
                    "small_image": "blender_logo",
                    "large_text": filename,
                    "large_image": "pretty_render"
                }
            }
            rpc_obj.set_activity(activity)
            time.sleep(30)
            break

# def register():
#     bpy.utils.register_class(BRPC_TestOperator)
#
# def unregister():
#     bpy.utils.unregister_class(BRPC_TestOperator)