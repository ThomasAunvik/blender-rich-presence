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
# ---------------------------------------------------------------------------------------#
# -------------------------------------------------------------------------- FUNCTIONS --#

# ---------------------------------------------------------------------------------------#
# ---------------------------------------------------------------------------- CLASSES --#
def exec_run(func):
    """
    Execute | Run decorator to evaluate runtime safe execution of a method not bound to
    a Blender Operator. Will raise a RuntimeError if the file has not been saved.
    Otherwise, will run the original function using it's pargs and kwargs as arguments.
    :param func: Original Function
    :return: Decorated Function
    """
    def check_bpy_state(*args, **kwargs):
        """
        Check if Blender file has been saved.
        :param args: positional arguments
        :param kwargs: keyword arguments
        :return: __call__(func, args, kwargs) or RuntimeError;bpy.data.is_saved is False
        """
        if not bpy.data.is_saved:
            raise RuntimeError(
                "RuntimeError detected. Save the Blend File before continuing"
            )
        return func(*args, **kwargs)
    return check_bpy_state

