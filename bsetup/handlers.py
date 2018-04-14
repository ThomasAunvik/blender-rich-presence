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
import bpy.app.handlers as handlers
# ---------------------------------------------------------------------------------------#
# -------------------------------------------------------------------------- FUNCTIONS --#

# ---------------------------------------------------------------------------------------#
# ---------------------------------------------------------------------------- CLASSES --#

@handlers.persistent
def tidal_load_handler():
    pass


@handlers.persistent
def tidal_cleanup_handler():
    pass


def register_handler():
    if not tidal_load_handler in handlers.load_post:
        handlers.load_pre.append(tidal_load_handler)
    if not tidal_cleanup_handler in handlers.load_post:
        handlers.load_pre.append(tidal_cleanup_handler)

def unregister_handler():
    if tidal_cleanup_handler in handlers.load_post:
        handlers.load_pre.remove(tidal_cleanup_handler)
    if tidal_load_handler in handlers.load_post:
        handlers.load_pre.remove(tidal_load_handler)