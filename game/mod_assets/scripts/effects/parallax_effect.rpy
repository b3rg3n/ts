#SR MOUSE PARALLAX EFFECT
#by @b3rg3n & @vaal
#Since 2023
init python:
    import store
    from random import randint

    config.layers.append("over_screens")

    class BrMouseParallax(renpy.Displayable):
        def set(self, *args):
            self.xoffset, self.yoffset = 0.0, 0.0
            self.layer_info = args
            for i in self.layers():
                if i in config.layers + ["master2"]:
                    config.layers.remove(i)
            index = config.layers.index("master") + 1
            for xdist, ydist, layer in args:
                if not layer in config.layers:
                    config.layers.insert(index, layer)
                    index += 1
            config.layers.insert(index, "master2")
        
        def __init__(self, *args):
            super(renpy.Displayable, self).__init__()
            self.set(*args)
            config.overlay_functions.append(self.overlay)
            return
        
        def layers(self):
            layers = []
            for dx, dy, layer in self.layer_info:
                layers.insert(0, layer)
            return layers
        
        def render(self, width, height, st, at):
            return renpy.Render(width, height)
        
        def parallax(self, xdist, ydist):
            func = renpy.curry(trans)(xdist=xdist, ydist=ydist, disp=self)
            return Transform(function=func)
        
        def overlay(self):
            ui.add(self)
            for xdist, ydist, layer in self.layer_info:
                renpy.layer_at_list([self.parallax(xdist, ydist)], layer)
            return
        
        def event(self, ev, x, y, st):
            import pygame
            if ev.type == pygame.MOUSEMOTION:
                self.xoffset, self.yoffset = ((float)(x) / (config.screen_width)) - 0.5, ((float)(y) / (config.screen_height)) - 0.5
            return

    def trans(d, st, at, xdist=None, ydist=None, disp=None):
        d.xoffset, d.yoffset = int(round(xdist * disp.xoffset)), int(round(ydist * disp.yoffset))
        if xdist != 0 or ydist != 0:
            xzoom = (config.screen_width + abs(xdist + xdist)) / float(config.screen_width)
            yzoom = (config.screen_height + abs(ydist + ydist)) / float(config.screen_height)
            if yzoom > xzoom:
                d.zoom = yzoom
            else:
                d.zoom = xzoom
            d.anchor = (.5, 1.0)
            d.align = (.5, 1.0)
        return 0

    br_parallax_images = []

    def br_paral_show(*args):
        global br_parallax_images
        layers = br_mouse_parallax.layers()
        for i in args:
            at = []
            image = i
            if isinstance(image, tuple):
                image, at = image
                if not isinstance(at, list):
                    at = [at]
            l = "master2"
            if len(layers) > 0:
                l = layers.pop()
            renpy.show(image, at_list=at, layer=l)
            i = (image, l)
            if not i in br_parallax_images:
                br_parallax_images.append(i)

    def br_paral_hide(image, dissolve=False, layer=None):
        global br_parallax_images
        if not layer:
            layer = "master2"
            for ii, ll in br_parallax_images:
                if ii == image:
                    layer = ll
        i = (image, layer)
        if not dissolve:
            renpy.hide(image, layer=layer)
        else:
            renpy.hide(image, layer=layer)
            renpy.with_statement(dissolve)
        if i in br_parallax_images:
            br_parallax_images.remove(i)

    def br_paral_scene(*args):
        global br_parallax_images
        for i in br_parallax_images:
            image, layer = i
            renpy.hide(image, layer=layer)
        renpy.with_statement(dissolve)
        br_parallax_images = []
        if args:
            br_paral_show(*args)

    br_mouse_parallax = BrMouseParallax((-60, -15, "l0"), (-20, -5, "l1"), (-20, -5, "l2"), (-20, -5, "l3"), (-20, -5, "l4"), (-20, -5, "l5"))

#КАК ЮЗАТЬ БЛЯДЬ:
#ПРИМЕР БЛЯДЬ
#    $ br_paral_scene(("ext_old_building_night_moonlight"), ("pi normal"))
#    with dissolve2
#КАК УБРАТЬ БЛЯДЬ ЭТУ ХУЙНЮ:
#    $ br_paral_scene()
#    scene bg black
#    with flash