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