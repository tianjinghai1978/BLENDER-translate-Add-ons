bl_info = {
    "name": "Switch Language",
    "author": "Wang Xu",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "Window > Ctrl+Shift+Alt+T",
    "description": "Switch language with a shortcut (Ctrl+Shift+Alt+T)",
    "category": "System",
}


import bpy


languages = ["zh_CN", "en_US", "zh_TW", "ja_JP"]

def switch_language():

    current_language = bpy.context.preferences.view.language

    current_index = languages.index(current_language)

    next_index = (current_index + 1) % len(languages)


    next_language = languages[next_index]

    bpy.context.preferences.view.language = next_language

    if next_language in ["zh_CN", "zh_TW", "ja_JP"]:
        bpy.context.preferences.view.use_translate_new_dataname = False


class SwitchLanguageOperator(bpy.types.Operator):
    """Switch language with a shortcut (Ctrl+Shift+Alt+T)"""
    bl_idname = "wm.switch_language"
    bl_label = "Switch Language"

    def execute(self, context):
        switch_language()
        return {'FINISHED'}

def register():
    bpy.utils.register_class(SwitchLanguageOperator)
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='Window', space_type='EMPTY')
    kmi = km.keymap_items.new(SwitchLanguageOperator.bl_idname, 'T', 'PRESS', ctrl=True, shift=True, alt=True)
    kmi = km.keymap_items.new(SwitchLanguageOperator.bl_idname, 'T', 'PRESS', oskey=True, shift=True, alt=True) # 

    print("Switch Language addon enabled. Press Ctrl+Shift+Alt+T to switch language.")

def unregister():

    bpy.utils.unregister_class(SwitchLanguageOperator)
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps['Window']
    for kmi in km.keymap_items:
        if kmi.idname == SwitchLanguageOperator.bl_idname:
            km.keymap_items.remove(kmi)

if __name__ == "__main__":
    register()