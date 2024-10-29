# ЛЮТЕЙШИЙ КОЛХОЗ, НО БЛЯТЬ, НИЧЕГО НЕ ПОДЕЛАЕШЬ
# СВАЯЛ BERGEN
# TEAM ANARCHY (c) 2024
init -15 python in TS:

    def m(transform):
        renpy.show_layer_at(transform, layer='master')

    def s(transform):
        renpy.show_layer_at(transform, layer='screens')

    def p(time):
        renpy.pause(delay=time, hard=True)
    
    def pn():
        renpy.pause(hard=True)

    def b():
        renpy.block_rollback()

init python:
    def ts_ss(vol):
        _preferences.volumes['sfx'] = vol
    
    def ts_mm(vol):
        _preferences.volumes['music'] = vol
    
    def ts_aa(vol):
        _preferences.volumes['voice'] = vol
    
    def ts_hlclear():
        _history_list = []