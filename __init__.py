bl_info = {
    'name': 'Proportional_Size-Calculator',
    'author': "Petr Moshkantsev",
    'category': 'All',
    'version': (0, 0, 1),
    'blender': (2, 93, 7)
}

import sys
debug = 1 # 0 (ON) or 1 (OFF)
 
modules = ["PSC_Operator", "PSC_Panel", "PSC_Properties"]
 
for mod in modules:
    try:
        exec("from . import {mod}".format(mod=mod))
    except Exception as e:
        print(e)
import importlib
def register():    
    for mod in modules:
        try:
            if debug:
                exec("importlib.reload({mod})".format(mod=mod))
            exec("{mod}.register()".format(mod=mod))
        except Exception as e:
            print(e)
 
def unregister():
    for mod in modules:
        try:
            exec("{mod}.unregister()".format(mod=mod))
        except Exception as e:
            print(e)

if __name__ == "__main__":
    register()