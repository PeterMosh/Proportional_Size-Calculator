import bpy

class PSC_Proportions_Settings(bpy.types.PropertyGroup):
    
    length_real : bpy.props.FloatProperty(
        name="Length real",
        description="Length of Object in Real (m)",
        default = 1.0,
        min = 0,
        max=1000,
        subtype='UNSIGNED'
        )
    length_photo : bpy.props.FloatProperty(
        name="Length photo",
        description="Length of Object on the Photo (cm)",
        default = 1.0,
        min = 0,
        max=1000,
        subtype='UNSIGNED'
        )
    height_real : bpy.props.FloatProperty(
        name="Length real",
        description="Height of Object in Real (m)",
        default = 0.0,
        min = 0,
        max=1000,
        subtype='UNSIGNED'
        )
    height_photo : bpy.props.FloatProperty(
        name="Length photo",
        description="Height of Object on the Photo (cm)",
        default = 1.0,
        min = 0,
        max=1000,
        subtype='UNSIGNED'
        )

classesName = (
    PSC_Proportions_Settings,
)

def register():
    from bpy.utils import register_class
    for cls in classesName:
        register_class(cls)
    bpy.types.Scene.Props_prop = bpy.props.PointerProperty(type = PSC_Proportions_Settings)
    
    
def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classesName):
        unregister_class(cls)
    del bpy.types.Scene.Props_prop