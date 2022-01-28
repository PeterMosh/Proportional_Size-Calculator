import bpy

class VIEW3D_PSC_PT_Proportions_Panel_One(bpy.types.Panel):
    
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Size Calculator"
    bl_label = "Object Size Calculator"
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.Props_prop
        col_main = layout.box().column(align=True)
        col_main.label(text = "Insert Proportional Sizes")
        col_main.prop(mytool, 'length_real', text="Real Length")
        col_main.prop(mytool, 'length_photo', text="Photo Length")
        col_main.prop(mytool, 'height_photo', text="Photo Height")
        col_main = layout.column(align=False)
        col_main.operator('object.estimate_proportions',
            text='Calculate Height')
        row = layout.row()
        if mytool.height_real != 0.0:
            row.label(text = "Real Height =" + str(round(mytool.height_real,2)) + ' meters')
            #row.prop(mytool, 'height_real', text="Real Height")

classesName = (
    VIEW3D_PSC_PT_Proportions_Panel_One,
)

def register():
    from bpy.utils import register_class
    for cls in classesName:
        register_class(cls)
    
    
def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classesName):
        unregister_class(cls)