import bpy

class OBJECT_PSC_Estimate_Proportions(bpy.types.Operator):
    bl_idname = "object.estimate_proportions"
    bl_label = "Estimate Objects Proportions"
    
    def execute(self,context):
        scene = context.scene
        mytool = scene.Props_prop
        mytool.height_real = mytool.height_photo * mytool.length_real / mytool.length_photo
        
        
        return {'FINISHED'}

classesName = (
    OBJECT_PSC_Estimate_Proportions,
)

def register():
    from bpy.utils import register_class
    for cls in classesName:
        register_class(cls)
    
def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classesName):
        unregister_class(cls)