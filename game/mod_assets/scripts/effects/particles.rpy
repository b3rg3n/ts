# TRUE STORY PARTICLES
# ТУТ И ИЗ ОРИГА, И ИЗ МОДОВ НА БЛ, И МОИ - КРАФТОВЫЕ ЧАСТИЦЫ
# by @b3rg3n & @retroboy & @dansalvato
# Since 2024

init python:
    import math

    snowfg = SnowBlossom(ts_anim + 'particles/et_snow.webp', start=3.0, count=320, border=50, xspeed=(25, 25), yspeed=(80, 105), fast=True)
    snowbg = SnowBlossom(im.Scale(ts_anim + 'particles/et_snow.webp', 5, 5), count=320, yspeed=(60, 85), start=3.0, border=50, xspeed=(45, 65), fast=True)
    renpy.image('norm_sneg', LiveComposite((1280, 720), (0, 0), snowbg, (0, 0), snowfg))

    snowfg = SnowBlossom(ts_anim + 'particles/et_dark_glow.webp', start=3.0, count=90, border=50, xspeed=(50, 85), yspeed=(160, 215), fast=True)
    snowbg = SnowBlossom(im.Scale(ts_anim + 'particles/et_dark_glow.webp', 5, 5), count=90, yspeed=(120, 165), start=3.0, border=50, xspeed=(75, 125), fast=True)
    renpy.image('dgpart', LiveComposite((1280, 720), (0, 0), snowbg, (0, 0), snowfg))

    snowfg = SnowBlossom(ts_anim + 'particles/et_dust.webp', start=3.0, count=90, border=50, xspeed=(50, 85), yspeed=(160, 215), fast=True)
    snowbg = SnowBlossom(im.Scale(ts_anim + 'particles/et_dust.webp', 5, 5), count=90, yspeed=(120, 165), start=3.0, border=50, xspeed=(75, 125), fast=True)
    renpy.image('dustpart', LiveComposite((1280, 720), (0, 0), snowbg, (0, 0), snowfg))

    def ts_black_sparkles(sh=1):
        if sh == 1:
            renpy.show('ts_eff_sparkles_black', layer='front')
        elif sh == 0:
            renpy.hide('ts_eff_sparkles_black', layer='front')
        renpy.transition(dissolve)

    def ts_red_sparkles(sh=1):
        if sh == 1:
            renpy.show('ts_eff_sparkles_red', layer='front')
        elif sh == 0:
            renpy.hide('ts_eff_sparkles_red', layer='front')
        renpy.transition(dissolve)

    class pilukaparticlesblya(object):
        
        def __init__(self):
            
            self.sm = SpriteManager(update=self.update)
            
            self.glows = [ ]
            self.rd = ts_anim + "particles/piluka.webp"
            
            d = Transform(self.rd, zoom=0.25)
            for i in range(0, 50):
                self.add(d, renpy.random.randint(20, 40))
            
            d = Transform(self.rd, zoom=0.5)
            for i in range(0, 50):
                self.add(d, renpy.random.randint(45, 60))
        
        def add(self, d, speed):
            s = self.sm.create(d)
            
            start = renpy.random.randint(0, 1080)
            s.x = renpy.random.randint(0, 1920)
            
            self.glows.append((s, start, speed))
        
        def update(self, st):
            for s, start, speed in self.glows:
                s.y = (start - speed/2 * st) % 1080 - 20
                s.x = s.x + math.sin(s.y/speed*2)
            
            return 0
    renpy.image("piluka", pilukaparticlesblya().sm)

    class yellowparticlesblya(object):
        
        def __init__(self):
            
            self.sm = SpriteManager(update=self.update)
            
            self.glows = [ ]
            self.rd = ts_anim + "particles/particleyellow.webp"
            
            d = Transform(self.rd, zoom=0.25)
            for i in range(0, 50):
                self.add(d, renpy.random.randint(20, 40))
            
            d = Transform(self.rd, zoom=0.5)
            for i in range(0, 50):
                self.add(d, renpy.random.randint(45, 60))
        
        def add(self, d, speed):
            s = self.sm.create(d)
            
            start = renpy.random.randint(0, 1080)
            s.x = renpy.random.randint(0, 1920)
            
            self.glows.append((s, start, speed))
        
        def update(self, st):
            for s, start, speed in self.glows:
                s.y = (start - speed/2 * st) % 1080 - 20
                s.x = s.x + math.sin(s.y/speed*2)
            
            return 0
    renpy.image("yelpart", yellowparticlesblya().sm)

    class fireparticlesblya(object):
        
        def __init__(self):
            
            self.sm = SpriteManager(update=self.update)
            
            self.glows = [ ]
            self.rd = ts_anim + "particles/firedrop.webp"
            
            d = Transform(self.rd, zoom=0.25)
            for i in range(0, 50):
                self.add(d, renpy.random.randint(20, 40))
            
            d = Transform(self.rd, zoom=0.5)
            for i in range(0, 50):
                self.add(d, renpy.random.randint(45, 60))
        
        def add(self, d, speed):
            s = self.sm.create(d)
            
            start = renpy.random.randint(0, 1080)
            s.x = renpy.random.randint(0, 1920)
            
            self.glows.append((s, start, speed))
        
        def update(self, st):
            for s, start, speed in self.glows:
                s.y = (start - speed/2 * st) % 1080 - 20
                s.x = s.x + math.sin(s.y/speed*2)
            
            return 0
    renpy.image("ogonek", fireparticlesblya().sm)

    class redparticlesblya(object):
        
        def __init__(self):
            
            self.sm = SpriteManager(update=self.update)
            
            self.glows = [ ]
            self.rd = ts_anim + "particles/chast1.webp"
            
            d = Transform(self.rd, zoom=0.25)
            for i in range(0, 50):
                self.add(d, renpy.random.randint(20, 40))
            
            d = Transform(self.rd, zoom=0.5)
            for i in range(0, 50):
                self.add(d, renpy.random.randint(45, 60))
        
        def add(self, d, speed):
            s = self.sm.create(d)
            
            start = renpy.random.randint(0, 1080)
            s.x = renpy.random.randint(0, 1920)
            
            self.glows.append((s, start, speed))
        
        def update(self, st):
            for s, start, speed in self.glows:
                s.y = (start - speed/2 * st) % 1080 - 20
                s.x = s.x + math.sin(s.y/speed*2)
            
            return 0
    renpy.image("redpart", redparticlesblya().sm)

    class greenparticlesblya(object):
        
        def __init__(self):
            
            self.sm = SpriteManager(update=self.update)
            
            self.glows = [ ]
            self.rd = ts_anim + "particles/particlegreen.webp"
            
            d = Transform(self.rd, zoom=0.25)
            for i in range(0, 50):
                self.add(d, renpy.random.randint(20, 40))
            
            d = Transform(self.rd, zoom=0.5)
            for i in range(0, 50):
                self.add(d, renpy.random.randint(45, 60))
        
        def add(self, d, speed):
            s = self.sm.create(d)
            
            start = renpy.random.randint(0, 1080)
            s.x = renpy.random.randint(0, 1920)
            
            self.glows.append((s, start, speed))
        
        def update(self, st):
            for s, start, speed in self.glows:
                s.y = (start - speed/2 * st) % 1080 - 20
                s.x = s.x + math.sin(s.y/speed*2)
            
            return 0
    renpy.image("greenpart", greenparticlesblya().sm)


init:
    image ts_sparkle_black:
        ts_anim + "particles/sparkle_black.png"
        anchor (0.5, 0.5)
        align (0.5, 0.5)
        alpha 0.9 zoom 0.75
        pause 3
        ease 3 alpha 0
    image ts_sparkle_red:
        ts_anim + "particles/sparkle_red.png"
        anchor (0.5, 0.5)
        align (0.5, 0.5)
        alpha 0.9 zoom 0.75
        pause 3
        ease 3 alpha 0
    image ts_eff_sparkles_black:
        SnowBlossom(ImageReference("ts_sparkle_black"), 50, 50, (15, 30), (25, 125))
        anchor (0.5, 0.5)
        align (0.5, 0.5)
        rotate 180
    image ts_eff_sparkles_red:
        SnowBlossom(ImageReference("ts_sparkle_red"), 50, 50, (15, 30), (25, 125))
        anchor (0.5, 0.5)
        align (0.5, 0.5)
        rotate 180
#КАК ЮЗАТЬ ЭТУ ДРОЧЬ БЛЯ
# show --и тут имя этой хуйты, например redpart--
#Итог:
# show redpart
#вот и всё блядь