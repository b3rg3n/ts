# TRUE STORY SCREEN ANIMATION
# by @b3rg3n (идею гопнул у @superrage)
# since 2024

init -15 python in TS:

    def Master(atl):
        renpy.show_layer_at(atl, layer='master')

    def Screens(atl):
        renpy.show_layer_at(atl, layer='screens')

    def Transient(atl):
        renpy.show_layer_at(atl, layer='transient')

    def Overlay(atl):
        renpy.show_layer_at(atl, layer='overlay')

    def Front(atl):
        renpy.show_layer_at(atl, layer='front')

