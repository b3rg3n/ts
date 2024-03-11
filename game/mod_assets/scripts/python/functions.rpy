# TRUE STORY SCREEN ANIMATION
# by @b3rg3n (идею гопнул у @superrage)
# since 2024

init -15 python in TS:

    def Master(atl):
        """
        IN:
            atl - transform
        TYPE:
            []
        """
        renpy.show_layer_at(atl, layer='master')

    def Screens(atl):
        """
        IN:
            atl - transform
        TYPE:
            []
        """
        renpy.show_layer_at(atl, layer='screens')

    def Transient(atl):
        """
        IN:
            atl - transform
        TYPE:
            []
        """
        renpy.show_layer_at(atl, layer='transient')

    def Overlay(atl):
        """
        IN:
            atl - transform
        TYPE:
            []
        """
        renpy.show_layer_at(atl, layer='overlay')

    def Front(atl):
        """
        IN:
            atl - transform
        TYPE:
            []
        """
        renpy.show_layer_at(atl, layer='front')

