bl_info = {
    "name": "Clear Vertex Groups",
    "author": "Wang Xu",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Object > Clear Vertex Groups",
    "description": "Clear all vertex groups of selected objects",
    "category": "Object",
}

import bpy
import sys

class OBJECT_OT_clear_vertex_groups(bpy.types.Operator):
    """Clear all vertex groups of selected objects"""
    bl_idname = "object.clear_vertex_groups"
    bl_label = "Clear Vertex Groups"

    def execute(self, context):
        objects = bpy.context.selected_objects
        for obj in objects:
            if obj.type == 'MESH' or obj.type == 'CURVE':
                obj.vertex_groups.clear()
        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(OBJECT_OT_clear_vertex_groups.bl_idname)

addon_keymaps = []

def register():
    bpy.utils.register_class(OBJECT_OT_clear_vertex_groups)
    bpy.types.VIEW3D_MT_object.append(menu_func)
    
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')
    
    if sys.platform.startswith('win'): 
        kmi = km.keymap_items.new(OBJECT_OT_clear_vertex_groups.bl_idname, 'D', 'PRESS', ctrl=True, shift=True, alt=True) 
    elif sys.platform.startswith('darwin'): 
        kmi = km.keymap_items.new(OBJECT_OT_clear_vertex_groups.bl_idname, 'D', 'PRESS', oskey=True, shift=True, alt=True) 
    
    addon_keymaps.append((km, kmi))

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_clear_vertex_groups)
    
bpy.types.VIEW3D_MT_object.remove(menu_func)

for km, kmi in addon_keymaps:
    km.keymap_items.remove(kmi)
addon_keymaps.clear()

if __name__ == "__main__":
    register()
