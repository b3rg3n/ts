# TRUE STORY ANIMATIONS
# by @b3rg3n
# Since 2024
init python:
    import math

    class TSGreenParticles(object):
        
        def __init__(self):
            
            self.sm = SpriteManager(update=self.update)
            
            self.glows = [ ]
            self.rd = ts_anim + 'particles/green_part.webp'
            
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
    renpy.image("ts_green_part", TSGreenParticles().sm)

    class TSYellowParticles(object):
        
        def __init__(self):
            
            self.sm = SpriteManager(update=self.update)
            
            self.glows = [ ]
            self.rd = ts_anim + 'particles/yellow_part.webp'
            
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
    renpy.image("ts_yel_part", TSYellowParticles().sm)

    lep1 = SnowBlossom(ts_anim + 'particles/lep/lep_1.webp', start=3.0, count=20, border=50, xspeed=(50, 85), yspeed=(160, 215), fast=True)
    lep2 = SnowBlossom(ts_anim + 'particles/lep/lep_2.webp', count=20, yspeed=(120, 165), start=3.0, border=50, xspeed=(75, 125), fast=True)
    lep3 = SnowBlossom(ts_anim + 'particles/lep/lep_3.webp', start=3.0, count=20, border=50, xspeed=(50, 85), yspeed=(160, 215), fast=True)
    lep4 = SnowBlossom(ts_anim + 'particles/lep/lep_4.webp', count=20, yspeed=(120, 165), start=3.0, border=50, xspeed=(75, 125), fast=True)
    lep5 = SnowBlossom(ts_anim + 'particles/lep/lep_5.webp', count=20, yspeed=(120, 165), start=3.0, border=50, xspeed=(75, 125), fast=True)
    renpy.image('lepestki_krutyatsa', LiveComposite((1280, 720), (0, 0), lep1, (0, 0), lep2, (0, 0), lep3, (0, 0), lep4, (0, 0), lep5))

    lep11 = SnowBlossom(ts_anim + 'particles/lep1/lep_1.webp', start=3.0, count=20, border=50, xspeed=(50, 85), yspeed=(160, 215), fast=True)
    lep21 = SnowBlossom(ts_anim + 'particles/lep1/lep_2.webp', count=20, yspeed=(120, 165), start=3.0, border=50, xspeed=(75, 125), fast=True)
    lep31 = SnowBlossom(ts_anim + 'particles/lep1/lep_3.webp', start=3.0, count=20, border=50, xspeed=(50, 85), yspeed=(160, 215), fast=True)
    lep41 = SnowBlossom(ts_anim + 'particles/lep1/lep_4.webp', count=20, yspeed=(120, 165), start=3.0, border=50, xspeed=(75, 125), fast=True)
    lep51 = SnowBlossom(ts_anim + 'particles/lep1/lep_5.webp', count=20, yspeed=(120, 165), start=3.0, border=50, xspeed=(75, 125), fast=True)
    renpy.image('lepestki_autumn', LiveComposite((1280, 720), (0, 0), lep11, (0, 0), lep21, (0, 0), lep31, (0, 0), lep41, (0, 0), lep51))


init:

    image ts_bloodanim:
        ts_anim + "blood/bloodanim1.webp"
        pause 0.1
        ts_anim + "blood/bloodanim2.webp"
        pause 0.1
        ts_anim + "blood/bloodanim3.webp"
        pause 0.1
        ts_anim + "blood/bloodanim4.webp"
        pause 0.1
        ts_anim + "blood/bloodanim5.webp"
        
    image ts_altbloodanim:
        ts_anim + "blood/altbloodanim1.webp"
        pause 0.1
        ts_anim + "blood/altbloodanim2.webp"
        pause 0.1
        ts_anim + "blood/altbloodanim3.webp"
        pause 0.1
        ts_anim + "blood/altbloodanim4.webp"

    image ts_psihuet1:
        ts_anim + "psih/psih1.webp" with dissolve
        pause .6
        ts_anim + "psih/psih2.webp" with dissolve
        pause .6
        repeat

    image ts_psihuet2:
        ts_anim + "psih/psih1.webp" with dissolve
        pause .6
        ts_anim + "psih/psih2.webp" with dissolve
        pause .6
        ts_anim + "psih/psih3.webp" with dissolve
        pause .6
        repeat

    image ts_psihuet3:
        ts_anim + "psih/psih1.webp" with dissolve
        pause .3
        ts_anim + "psih/psih2.webp" with dissolve
        pause .3
        ts_anim + "psih/psih3.webp" with dissolve
        pause .3
        ts_anim + "psih/psih4.webp" with dissolve
        pause .3
        repeat

    image ts_emergency_room_anim: #ЭФФЕКТ ТЕЛЕКА С ПОЛОСОЙ
        ts_anim + 'emergency/er_aa1.webp'
        pause 0.05
        ts_anim + 'emergency/er_aa2.webp'
        pause 0.05
        ts_anim + 'emergency/er_aa3.webp'
        pause 0.05
        ts_anim + 'emergency/er_aa4.webp'
        pause 0.05
        ts_anim + 'emergency/er_aa5.webp'
        pause 0.1
        ts_anim + 'emergency/er_aa6.webp'
        pause 0.9
        repeat

    image ts_emergency_room_anim4: #ЭФФЕКТ ТЕЛЕКА С ПОЛОСОЙ БЫСТРЕЕ БЛЯТЬ
        ts_anim + 'emergency/er_aa1.webp'
        pause 0.05
        ts_anim + 'emergency/er_aa2.webp'
        pause 0.05
        ts_anim + 'emergency/er_aa3.webp'
        pause 0.05
        ts_anim + 'emergency/er_aa4.webp'
        pause 0.05
        ts_anim + 'emergency/er_aa5.webp'
        pause 0.1
        ts_anim + 'emergency/er_aa6.webp'
        pause 0.4
        repeat

    image ts_club_medlenno_glutch:
        'ts_class' with dissolve2
        pause 0.5
        'ts_club_g1' with dissolve2
        pause 0.01
        'ts_club_g2' with dissolve2
        pause 0.01
        'ts_club_g3' with dissolve2
        pause 0.01

    image mon_piano_glitch_anim: # ПЕРЕД ГУД КОНЦОВКОЙ МЕНЮ АНИМАЦИЯ
        'mon_piano'
        pause 2.1
        'mon_piano_glitch'
        pause 0.11
        'mon_piano'
        pause 2.1
        'mon_piano_glitch'
        pause 0.11
        'mon_piano_glitch1'
        pause 0.11
        'mon_piano'
        pause 2.1
        'mon_piano_glitch'
        pause 0.11
        'mon_piano_glitch1'
        pause 0.11
        'mon_piano_glitch2'
        pause 0.11
        'mon_piano'
        pause 2.1
        'mon_piano_glitch'
        pause 0.11
        'mon_piano_glitch1'
        pause 0.11
        'mon_piano_glitch2'
        pause 0.11
        'mon_piano_glitch3'
        pause 0.11
        repeat

    image mon_piano_another_glitch_anim: # ЧАСТЬ МЕНЮШКИ
        'mon_piano_another'
        pause 2.1
        'mon_piano_another_glitch'
        pause 0.11
        'mon_piano_another'
        pause 2.1
        'mon_piano_another_glitch'
        pause 0.11
        'mon_piano_another_glitch1'
        pause 0.11
        'mon_piano_another'
        pause 2.1
        'mon_piano_another_glitch'
        pause 0.11
        'mon_piano_another_glitch1'
        pause 0.11
        'mon_piano_another_glitch2'
        pause 0.11
        'mon_piano_another'
        pause 2.1
        'mon_piano_another_glitch'
        pause 0.11
        'mon_piano_another_glitch1'
        pause 0.11
        'mon_piano_another_glitch2'
        pause 0.11
        'mon_piano_another_glitch3'
        pause 0.11
        repeat

    image ts_kitchen_psyhodelic_pizdec_glitch: # УБИВАЕМ ЭПИЛЕПТИКОВ НАХУЙ))))0000)))
        ts_gl_bg_path + 'ts_kitchen_g1.webp'
        pause 0.05
        ts_gl_bg_path + 'ts_kitchen_g6.webp'
        pause 0.05
        ts_gl_bg_path + 'ts_kitchen_g2.webp'
        pause 0.05
        ts_gl_bg_path + 'ts_kitchen_g5.webp'
        pause 0.05
        ts_gl_bg_path + 'ts_kitchen_g3.webp'
        pause 0.05
        ts_gl_bg_path + 'ts_kitchen_g4.webp'
        pause 0.05
        ts_gl_bg_path + 'ts_kitchen_g6.webp'
        pause 0.05
        ts_gl_bg_path + 'ts_kitchen_g3.webp'
        pause 0.05
        ts_gl_bg_path + 'ts_kitchen_g5.webp'
        pause 0.05
        ts_gl_bg_path + 'ts_kitchen_g4.webp'
        pause 0.05
        ts_gl_bg_path + 'ts_kitchen_g3.webp'
        pause 0.05
        ts_gl_bg_path + 'ts_kitchen_g6.webp'
        pause 0.05
        ts_gl_bg_path + 'ts_kitchen_g2.webp'
        pause 0.05
        ts_gl_bg_path + 'ts_kitchen_g5.webp'
        pause 0.05
        repeat

    image ts_closet_glitches_balya: # УБИВАЕМ ЭПИЛЕПТИКОВ НАХУЙ))))0000)))
        ts_gl_bg_path + 'ts_closet_g1.webp'
        pause 0.05
        ts_gl_bg_path + 'ts_closet_g2.webp'
        pause 0.05
        ts_gl_bg_path + 'ts_closet_g3.webp'
        pause 0.05
        ts_gl_bg_path + 'ts_closet_g1.webp'
        pause 0.05
        ts_gl_bg_path + 'ts_closet_g2.webp'
        pause 0.05
        ts_gl_bg_path + 'ts_closet_g2.webp'
        pause 0.05
        ts_gl_bg_path + 'ts_closet_g3.webp'
        pause 0.05
        ts_gl_bg_path + 'ts_closet_g2.webp'
        pause 0.05
        ts_gl_bg_path + 'ts_closet_g1.webp'
        pause 0.05
        ts_gl_bg_path + 'ts_closet_g3.webp'
        pause 0.05
        ts_gl_bg_path + 'ts_closet_g1.webp'
        pause 0.05
        ts_gl_bg_path + 'ts_closet_g3.webp'
        pause 0.05
        ts_gl_bg_path + 'ts_closet_g2.webp'
        pause 0.05
        ts_gl_bg_path + 'ts_closet_g1.webp'
        pause 0.05
        repeat

    image ts_hiroto_psyhodelic_pizdoc: # УБИВАЕМ ЭПИЛЕПТИКОВ НАХУЙ))))0000)))
        ts_hiroto_pt + 'glitch/1l_g1.webp'
        pause 0.05
        ts_hiroto_pt + 'glitch/1l_g4.webp'
        pause 0.05
        ts_hiroto_pt + 'glitch/1l_g2.webp'
        pause 0.05
        ts_hiroto_pt + 'glitch/1l_g4.webp'
        pause 0.05
        ts_hiroto_pt + 'glitch/1l_g3.webp'
        pause 0.05
        ts_hiroto_pt + 'glitch/1l_g4.webp'
        pause 0.05
        ts_hiroto_pt + 'glitch/1l_g1.webp'
        pause 0.05
        ts_hiroto_pt + 'glitch/1l_g4.webp'
        pause 0.05
        ts_hiroto_pt + 'glitch/1l_g2.webp'
        pause 0.05
        ts_hiroto_pt + 'glitch/1l_g4.webp'
        pause 0.05
        ts_hiroto_pt + 'glitch/1l_g3.webp'
        pause 0.05
        ts_hiroto_pt + 'glitch/1l_g4.webp'
        pause 0.05
        ts_hiroto_pt + 'glitch/1l_g1.webp'
        pause 0.05
        ts_hiroto_pt + 'glitch/1l_g4.webp'
        pause 0.05
        repeat

    image ts_hiroto_psyhodelic_pizdoc1: # УБИВАЕМ ЭПИЛЕПТИКОВ НАХУЙ))))0000)))
        ts_hiroto_pt + 'glitch/1l_g1.webp'
        pause 0.05
        ts_hiroto_pt + 'glitch/1l_g44.webp'
        pause 0.05
        ts_hiroto_pt + 'glitch/1l_g2.webp'
        pause 0.05
        ts_hiroto_pt + 'glitch/1l_g44.webp'
        pause 0.05
        ts_hiroto_pt + 'glitch/1l_g3.webp'
        pause 0.05
        ts_hiroto_pt + 'glitch/1l_g44.webp'
        pause 0.05
        ts_hiroto_pt + 'glitch/1l_g1.webp'
        pause 0.05
        ts_hiroto_pt + 'glitch/1l_g44.webp'
        pause 0.05
        ts_hiroto_pt + 'glitch/1l_g2.webp'
        pause 0.05
        ts_hiroto_pt + 'glitch/1l_g44.webp'
        pause 0.05
        ts_hiroto_pt + 'glitch/1l_g3.webp'
        pause 0.05
        ts_hiroto_pt + 'glitch/1l_g44.webp'
        pause 0.05
        ts_hiroto_pt + 'glitch/1l_g1.webp'
        pause 0.05
        ts_hiroto_pt + 'glitch/1l_g44.webp'
        pause 0.05
        repeat

    image ts_hiroto_psyhodelic_pizdoc_eye: # ГЛАЗЁНКИ БЕГАЮТ
        ts_hiroto_pt + 'glitch/2l_g1.webp'
        pause 0.5
        ts_hiroto_pt + 'glitch/2l_g3.webp'
        pause 0.5
        ts_hiroto_pt + 'glitch/2l_g2.webp'
        pause 0.5
        ts_hiroto_pt + 'glitch/2l_g4.webp'
        pause 0.5
        ts_hiroto_pt + 'glitch/2l_g2.webp'
        pause 0.5
        ts_hiroto_pt + 'glitch/2l_g5.webp'
        pause 0.5
        ts_hiroto_pt + 'glitch/2l_g3.webp'
        pause 0.5
        ts_hiroto_pt + 'glitch/2l_g1.webp'
        pause 0.5
        ts_hiroto_pt + 'glitch/2l_g2.webp'
        pause 0.5
        ts_hiroto_pt + 'glitch/2l_g4.webp'
        pause 0.5
        repeat

    image ts_hiroto_psyhodelic_pizdoc_eblet: # ЕБАЛО КАРАНДАШОМ
        ts_hiroto_pt + 'glitch/1r_g1.webp'
        pause 0.25
        ts_hiroto_pt + 'glitch/1r_g3.webp'
        pause 0.25
        ts_hiroto_pt + 'glitch/1r_g2.webp'
        pause 0.25
        ts_hiroto_pt + 'glitch/1r_g4.webp'
        pause 0.25
        ts_hiroto_pt + 'glitch/1r_g3.webp'
        pause 0.25
        ts_hiroto_pt + 'glitch/1r_g4.webp'
        pause 0.25
        ts_hiroto_pt + 'glitch/1r_g2.webp'
        pause 0.25
        ts_hiroto_pt + 'glitch/1r_g4.webp'
        pause 0.25
        ts_hiroto_pt + 'glitch/1r_g3.webp'
        pause 0.25
        repeat


    image vladick_pizdos: # ГЛИЧЁВЫЙ СЦЕНАРИСТ ЭТОЙ ХУЙНИ
        contains:
            choice:
                "ts_credits_mad_1"
            choice:
                "ts_credits_mad_2"
            choice:
                "ts_credits_mad_4"
            choice:
                "ts_credits_mad_3"
            choice:
                "ts_credits_mad_4"
            choice:
                "ts_credits_mad_3"
            choice:
                "ts_credits_mad_2"
            choice:
                "ts_credits_mad_3"
            choice:
                "ts_credits_mad_2"
            choice:
                "ts_credits_mad_4"
            pause 0.05
            repeat
        contains:
            choice:
                "ts_credits_mad_1"
            choice:
                "ts_credits_mad_3"
            choice:
                "ts_credits_mad_2"
            choice:
                "ts_credits_mad_4"
            choice:
                "ts_credits_mad_3"
            choice:
                "ts_credits_mad_4"
            choice:
                "ts_credits_mad_2"
            choice:
                "ts_credits_mad_3"
            choice:
                "ts_credits_mad_4"
            choice:
                "ts_credits_mad_2"
            pause 0.05
            repeat
        contains:
            choice:
                "ts_credits_mad_1"
            choice:
                "ts_credits_mad_2"
            choice:
                "ts_credits_mad_3"
            choice:
                "ts_credits_mad_2"
            choice:
                "ts_credits_mad_4"
            choice:
                "ts_credits_mad_3"
            choice:
                "ts_credits_mad_4"
            choice:
                "ts_credits_mad_2"
            choice:
                "ts_credits_mad_3"
            choice:
                "ts_credits_mad_4"
            pause 0.05
            repeat

    image bergencheek_pizdos: # ГЛИЧЁВЫЙ КОДЕР ЭТОЙ ХУЙНИ
        contains:
            choice:
                "ts_credits_bergen_1"
            choice:
                "ts_credits_bergen_2"
            choice:
                "ts_credits_bergen_4"
            choice:
                "ts_credits_bergen_3"
            choice:
                "ts_credits_bergen_4"
            choice:
                "ts_credits_bergen_3"
            choice:
                "ts_credits_bergen_2"
            choice:
                "ts_credits_bergen_3"
            choice:
                "ts_credits_bergen_2"
            choice:
                "ts_credits_bergen_4"
            pause 0.05
            repeat
        contains:
            choice:
                "ts_credits_bergen_1"
            choice:
                "ts_credits_bergen_3"
            choice:
                "ts_credits_bergen_2"
            choice:
                "ts_credits_bergen_4"
            choice:
                "ts_credits_bergen_3"
            choice:
                "ts_credits_bergen_4"
            choice:
                "ts_credits_bergen_2"
            choice:
                "ts_credits_bergen_3"
            choice:
                "ts_credits_bergen_4"
            choice:
                "ts_credits_bergen_2"
            pause 0.05
            repeat
        contains:
            choice:
                "ts_credits_bergen_1"
            choice:
                "ts_credits_bergen_2"
            choice:
                "ts_credits_bergen_3"
            choice:
                "ts_credits_bergen_2"
            choice:
                "ts_credits_bergen_4"
            choice:
                "ts_credits_bergen_3"
            choice:
                "ts_credits_bergen_4"
            choice:
                "ts_credits_bergen_2"
            choice:
                "ts_credits_bergen_3"
            choice:
                "ts_credits_bergen_4"
            pause 0.05
            repeat

    image nat_pizdos: # ГЛИЧЁВАЯ ЛЮБИТЕЛЬНИЦА МАНГИ БЛЕАТЬ
        contains:
            choice:
                "natsuki_pizdec"
            choice:
                "natsuki_pizdec3"
            choice:
                "natsuki_pizdec2"
            choice:
                "natsuki_pizdec3"
            choice:
                "natsuki_pizdec"
            choice:
                "natsuki_pizdec1"
            choice:
                "natsuki_pizdec4"
            choice:
                "natsuki_pizdec3"
            choice:
                "natsuki_pizdec4"
            choice:
                "natsuki_pizdec2"
            pause 0.05
            repeat
        contains:
            choice:
                "natsuki_pizdec"
            choice:
                "natsuki_pizdec2"
            choice:
                "natsuki_pizdec4"
            choice:
                "natsuki_pizdec3"
            choice:
                "natsuki_pizdec1"
            choice:
                "natsuki_pizdec3"
            choice:
                "natsuki_pizdec4"
            choice:
                "natsuki_pizdec2"
            choice:
                "natsuki_pizdec1"
            choice:
                "natsuki_pizdec4"
            pause 0.05
            repeat
        contains:
            choice:
                "natsuki_pizdec"
            choice:
                "natsuki_pizdec4"
            choice:
                "natsuki_pizdec3"
            choice:
                "natsuki_pizdec1"
            choice:
                "natsuki_pizdec2"
            choice:
                "natsuki_pizdec4"
            choice:
                "natsuki_pizdec2"
            choice:
                "natsuki_pizdec3"
            choice:
                "natsuki_pizdec1"
            choice:
                "natsuki_pizdec4"
            pause 0.05
            repeat
###АЛКОТРИП БЛЯ
    image ts_club_alkoner:
        'ts_club'
        subpixel True
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 1
        parallel:
            ease 0.95 pos (0.4, 0.65) zoom 1.935
            pause 0.15
            easein 0.55 pos (0.5, 0.5) zoom 1.2
            pause 0.05
            easeout 0.65 pos (0.7, 0.4) zoom 2.15
            pause 0.1
            ease 1.3 pos (0.5, 0.5) zoom 1
        parallel:
            ease 1.1 rotate 20
            easein 0.6 rotate -2.5
            easeout 0.8 rotate -25
            ease 1.3 rotate 0

###ЛАГАЮЩЕЕ ЛОГО, ЕБАТЬ
    image anarchy_glitch_logo:
        ts_images + "anarchy/anarchisty1.webp"
        pause 0.1
        ts_images + "anarchy/anarchisty3.webp"
        pause 0.1
        ts_images + "anarchy/anarchisty2.webp"
        pause 0.1
        ts_images + "anarchy/anarchisty3.webp"
        pause 0.1
        ts_images + "anarchy/anarchisty1.webp"
        pause 0.1
        ts_images + "anarchy/anarchisty2.webp"
        pause 0.1
        ts_images + "anarchy/anarchisty3.webp"
        pause 0.1
        ts_images + "anarchy/anarchisty1.webp"
        pause 0.1
        ts_images + "anarchy/anarchisty2.webp"
        pause 0.1
        repeat

###ВЕШАЕМСЯ НАХУЙ

    image ts_blinking:
        contains:
            "unblink"
            pos (0,-720)
            ease 0.5 xalign 0 yalign 0
        contains:
            "blink"
            pos (0,720)
            ease 0.5 xalign 0 yalign 0
        pause 0.25
        contains:
            "unblink"
            xalign 0 yalign 0
            ease 0.5 pos (0,-720)
        contains:
            "blink"
            xalign 0 yalign 0
            ease 0.5 pos (0,720)

    image ts_mon_povesilas:
        contains:
            'ts_closet'
            subpixel True
            anchor (0.5, 0.5)
            pos (0.5, 0.5)
            ease 1 zoom 1 rotate 0
            ease 0.5 zoom 1.85 rotate 30
            ease 0.9 zoom 1.45 rotate -15
            ease 0.75 zoom 1.3 rotate 10
            ease 1 zoom 2 rotate -25
            ease 0.5 zoom 1.5 rotate 20
            repeat
        contains:
            'black'
            ease 1 alpha 0
            ease 1.35 alpha 0.75
            ease 1.05 alpha 0
            ease 0.5 alpha 1
            ease 0.85 alpha 0.35
            ease 0.75 alpha 0.65
            repeat
        contains:
            pause 3
            'ts_blinking'
            pause 5
            'ts_blinking'
            pause 2.25
            'ts_blinking'
            pause 4
            'ts_blinking'
            repeat

###АНИМАЦИЯ КОШМАРА МОНИКИ В КОНЦЕ 4 ГЛАВЫ 1 АКТА НАХ
    image vse_pizda_monike:
        ts_cg + "brg_kolhoz_blya/s1.png" with poplil_pacan1
        pause 5
        ts_cg + "brg_kolhoz_blya/1a.webp" with poplil_pacan1
        pause 5
        ts_cg + "brg_kolhoz_blya/n_cg2_bg.webp" with poplil_pacan1
        pause 5
        ts_cg + "brg_kolhoz_blya/monika_scare.webp" with poplil_pacan1
        pause 5
        ts_cg + "brg_kolhoz_blya/s2.png" with poplil_pacan1
        pause 5
        ts_cg + "brg_kolhoz_blya/3b.webp" with poplil_pacan1
        pause 5
        repeat

###АНИМАЦИЯ ПИЗДЕЦА В БЛЕКАУТЕ
    image anim_exhausted:
        ts_anim + "blackout/blackout_exh2.webp"
        0.03 # Задержка
        ts_anim + "blackout/blackout_exh3.webp"
        0.03 # Задержка
        ts_anim + "blackout/blackout_exh2.webp"
        0.03 # Задержка
        ts_anim + "blackout/blackout_exh3.webp"
        0.03 # Задержка
        ts_anim + "blackout/blackout_exh2.webp"
        0.03 # Задержка
        repeat # Не убирать

###АНИМАЦИЯ МОРГАНИЯ ЗАЛУПЫ
    image ts_blinking:
        contains:
            "anim blink_up"
            pos (0,-720)
            ease 0.5 xalign 0 yalign 0
        contains:
            "anim blink_down"
            pos (0,720)
            ease 0.5 xalign 0 yalign 0
        pause 0.25
        contains:
            "anim blink_up"
            xalign 0 yalign 0
            ease 0.5 pos (0,-720)
        contains:
            "anim blink_down"
            xalign 0 yalign 0
            ease 0.5 pos (0,720)

###АНИМАЦИИ МЕНЮШКИ

    image ts_menu_move_anim_bad_end:
        contains:
            ts_images + "intro/menu/monikill.webp" #with Fade(1.5, 1, 2)
            zoom 1.0 xalign 0.0 yalign 0.6 alpha 0.0
            parallel:
                ease 0.2 alpha 1.0
            parallel:
                linear 15.0 xalign 1.0 yalign 0.4
            ts_images + "intro/menu/monikill.webp"
            zoom 1.0 xalign 1.0 yalign 0.4 alpha 0.0

            ts_images + "intro/menu/monikill1.webp" #with Fade(1.5, 1, 2)
            zoom 1.0 xalign 0.0 yalign 0.6 alpha 0.0
            parallel:
                ease 0.2 alpha 1.0
            parallel:
                linear 15.0 xalign 1.0 yalign 0.4
            ts_images + "intro/menu/monikill1.webp"
            zoom 1.0 xalign 1.0 yalign 0.4 alpha 0.0

            

            repeat
        contains:
            parallel:
                choice:
                    ts_anim + "mb/aw_o_1.webp"
                choice:
                    ts_anim + "mb/aw_o_2.webp"
                choice:
                    ts_anim + "mb/aw_o_3.webp"
                choice:
                    ts_anim + "mb/aw_o_4.webp"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            parallel:
                parallel:
                    choice:
                        xzoom 1.0
                    choice:
                        xzoom -1.0
                parallel:
                    choice:
                        yzoom 1.0
                    choice:
                        yzoom -1.0
            alpha 0.5
            pause 0.02
            repeat



    image ts_menu_move_anim_good_end = ts_images + "intro/menu/good_menu_anim_suka.webp"

    image ts_menu_move_anim_good_end1:
        contains:
            ts_images + "intro/menu/good_menu_anim_suka.webp" #with Fade(1.5, 1, 2)
            zoom 1.0 xalign 0.0 yalign 0.6 alpha 0.0
            parallel:
                ease 0.2 alpha 1.0
            parallel:
                linear 15.0 xalign 1.0 yalign 0.4
            ts_images + "intro/menu/good_menu_anim_suka.webp"
            zoom 1.0 xalign 1.0 yalign 0.4 alpha 0.0
            parallel:
                ease 0.2 alpha 1.0
            parallel:
                linear 15.0 xalign 0.0 yalign 0.6
            repeat
        contains:
            parallel:
                choice:
                    ts_anim + "mb/aw_o_1.webp"
                choice:
                    ts_anim + "mb/aw_o_2.webp"
                choice:
                    ts_anim + "mb/aw_o_3.webp"
                choice:
                    ts_anim + "mb/aw_o_4.webp"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            parallel:
                parallel:
                    choice:
                        xzoom 1.0
                    choice:
                        xzoom -1.0
                parallel:
                    choice:
                        yzoom 1.0
                    choice:
                        yzoom -1.0
            alpha 0.5
            pause 0.02
            repeat

    image ts_menu_move_anim_three:
        contains:
            ts_images + "intro/menu/ts_menu_art3.webp"
            zoom 1.0 xalign 0.0 yalign 0.6 alpha 0.0
            parallel:
                ease 0.2 alpha 1.0
            parallel:
                linear 15.0 xalign 1.0 yalign 0.4
            ts_images + "intro/menu/ts_menu_art3.webp"
            zoom 1.0 xalign 1.0 yalign 0.4 alpha 0.0
            parallel:
                ease 0.2 alpha 1.0
            parallel:
                linear 15.0 xalign 0.0 yalign 0.6
            repeat
        contains:
            parallel:
                choice:
                    ts_anim + "mb/aw_o_1.webp"
                choice:
                    ts_anim + "mb/aw_o_2.webp"
                choice:
                    ts_anim + "mb/aw_o_3.webp"
                choice:
                    ts_anim + "mb/aw_o_4.webp"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            parallel:
                parallel:
                    choice:
                        xzoom 1.0
                    choice:
                        xzoom -1.0
                parallel:
                    choice:
                        yzoom 1.0
                    choice:
                        yzoom -1.0
            alpha 0.5
            pause 0.02
            repeat

    image ts_menu_move_anim:
        contains:
            ts_images + "intro/menu/menu_art1.webp" #with Fade(1.5, 1, 2)
            zoom 1.0 xalign 0.0 yalign 0.6 alpha 0.0
            parallel:
                ease 0.2 alpha 1.0
            parallel:
                linear 15.0 xalign 1.0 yalign 0.4
            ts_images + "intro/menu/menu_art2.webp" #with Fade(1.5, 1, 2)
            zoom 1.0 xalign 0.0 yalign 0.6 alpha 0.0
            parallel:
                ease 0.2 alpha 1.0
            parallel:
                linear 15.0 xalign 1.0 yalign 0.4
            ts_images + "intro/menu/menu_art3.webp" #with Fade(1.5, 1, 2)
            zoom 1.0 xalign 0.0 yalign 0.6 alpha 0.0
            parallel:
                ease 0.2 alpha 1.0
            parallel:
                linear 15.0 xalign 1.0 yalign 0.4
            repeat
        contains:
            parallel:
                choice:
                    ts_anim + "mb/aw_o_1.webp"
                choice:
                    ts_anim + "mb/aw_o_2.webp"
                choice:
                    ts_anim + "mb/aw_o_3.webp"
                choice:
                    ts_anim + "mb/aw_o_4.webp"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            parallel:
                parallel:
                    choice:
                        xzoom 1.0
                    choice:
                        xzoom -1.0
                parallel:
                    choice:
                        yzoom 1.0
                    choice:
                        yzoom -1.0
            alpha 0.5
            pause 0.02
            repeat

###АНИМАЦИИ ЗАСТАВКИ
    image ts_intro_move_1:
        contains:
            "ts_corridor"
            zoom 1.1 xalign 0.0 yalign 0.6 alpha 0.0
            parallel:
                ease 0.2 alpha 1.0
            parallel:
                linear 15.0 xalign 1.0 yalign 0.4
        contains:
            parallel:
                choice:
                    ts_anim + "mb/aw_o_1.webp"
                choice:
                    ts_anim + "mb/aw_o_2.webp"
                choice:
                    ts_anim + "mb/aw_o_3.webp"
                choice:
                    ts_anim + "mb/aw_o_4.webp"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            parallel:
                parallel:
                    choice:
                        xzoom 1.0
                    choice:
                        xzoom -1.0
                parallel:
                    choice:
                        yzoom 1.0
                    choice:
                        yzoom -1.0
            alpha 0.5
            pause 0.02
            repeat

    image ts_intro_move_2:
        contains:
            "ts_street"
            zoom 1.1 xalign 0.0 yalign 0.6 alpha 0.0
            parallel:
                ease 0.2 alpha 1.0
            parallel:
                linear 15.0 xalign 1.0 yalign 0.4
        contains:
            parallel:
                choice:
                    ts_anim + "mb/aw_o_1.webp"
                choice:
                    ts_anim + "mb/aw_o_2.webp"
                choice:
                    ts_anim + "mb/aw_o_3.webp"
                choice:
                    ts_anim + "mb/aw_o_4.webp"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            parallel:
                parallel:
                    choice:
                        xzoom 1.0
                    choice:
                        xzoom -1.0
                parallel:
                    choice:
                        yzoom 1.0
                    choice:
                        yzoom -1.0
            alpha 0.5
            pause 0.02
            repeat

    image ts_intro_move_3:
        contains:
            "ts_class"
            zoom 1.1 xalign 0.0 yalign 0.6 alpha 0.0
            parallel:
                ease 0.2 alpha 1.0
            parallel:
                linear 15.0 xalign 1.0 yalign 0.4
        contains:
            parallel:
                choice:
                    ts_anim + "mb/aw_o_1.webp"
                choice:
                    ts_anim + "mb/aw_o_2.webp"
                choice:
                    ts_anim + "mb/aw_o_3.webp"
                choice:
                    ts_anim + "mb/aw_o_4.webp"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            parallel:
                parallel:
                    choice:
                        xzoom 1.0
                    choice:
                        xzoom -1.0
                parallel:
                    choice:
                        yzoom 1.0
                    choice:
                        yzoom -1.0
            alpha 0.5
            pause 0.02
            repeat

    image ts_intro_move_4:
        contains:
            "ts_house"
            zoom 1.1 xalign 0.0 yalign 0.6 alpha 0.0
            parallel:
                ease 0.2 alpha 1.0
            parallel:
                linear 15.0 xalign 1.0 yalign 0.4
        contains:
            parallel:
                choice:
                    ts_anim + "mb/aw_o_1.webp"
                choice:
                    ts_anim + "mb/aw_o_2.webp"
                choice:
                    ts_anim + "mb/aw_o_3.webp"
                choice:
                    ts_anim + "mb/aw_o_4.webp"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            parallel:
                parallel:
                    choice:
                        xzoom 1.0
                    choice:
                        xzoom -1.0
                parallel:
                    choice:
                        yzoom 1.0
                    choice:
                        yzoom -1.0
            alpha 0.5
            pause 0.02
            repeat

###БЕЛЫЙ ШУМ
    image noise:
        truecenter
        ts_anim + "noise/noise1.webp"
        pause 0.1
        ts_anim + "noise/noise2.webp"
        pause 0.1
        ts_anim + "noise/noise3.webp"
        pause 0.1
        ts_anim + "noise/noise4.webp"
        pause 0.1
        xzoom -1
        ts_anim + "noise/noise1.webp"
        pause 0.1
        ts_anim + "noise/noise2.webp"
        pause 0.1
        ts_anim + "noise/noise3.webp"
        pause 0.1
        ts_anim + "noise/noise4.webp"
        pause 0.1
        yzoom -1
        ts_anim + "noise/noise1.webp"
        pause 0.1
        ts_anim + "noise/noise2.webp"
        pause 0.1
        ts_anim + "noise/noise3.webp"
        pause 0.1
        ts_anim + "noise/noise4.webp"
        pause 0.1
        xzoom 1
        ts_anim + "noise/noise1.webp"
        pause 0.1
        ts_anim + "noise/noise2.webp"
        pause 0.1
        ts_anim + "noise/noise3.webp"
        pause 0.1
        ts_anim + "noise/noise4.webp"
        pause 0.1
        yzoom 1
        repeat

###ЭФФЕКТ ЗЕНЕК
    image unblink:
        contains:
            ts_anim + "zenki/blink_up.webp"
            xalign 0 yalign 0
            ease 1.5 pos (0,-1080)
        contains:
            ts_anim + "zenki/blink_down.webp"
            xalign 0 yalign 0
            ease 1.5 pos (0,1080)

    image blink:
        contains:
            ts_anim + "zenki/blink_up.webp"
            pos (0,-1080)
            ease 1.5 xalign 0 yalign 0
        contains:
            ts_anim + "zenki/blink_down.webp"
            pos (0,1080)
            ease 1.5 xalign 0 yalign 0

###ОВЕРЛЕЙ СТАРОЙ ПЛЁНКИ
    image overlay aw_memory_back_1:
        contains:
            parallel:
                choice:
                    ts_anim + "mb/aw_o_1.webp"
                choice:
                    ts_anim + "mb/aw_o_2.webp"
                choice:
                    ts_anim + "mb/aw_o_3.webp"
                choice:
                    ts_anim + "mb/aw_o_4.webp"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            parallel:
                parallel:
                    choice:
                        xzoom 1.0
                    choice:
                        xzoom -1.0
                parallel:
                    choice:
                        yzoom 1.0
                    choice:
                        yzoom -1.0
            alpha 0.5
            pause 0.02
            repeat

    image overlay aw_memory_back_2:
        contains:
            parallel:
                choice:
                    ts_anim + "mb/a_1.webp"
                choice:
                    ts_anim + "mb/a_2.webp"
                choice:
                    ts_anim + "mb/a_3.webp"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            parallel:
                parallel:
                    choice:
                        xzoom 1.0
                    choice:
                        xzoom -1.0
                parallel:
                    choice:
                        yzoom 1.0
                    choice:
                        yzoom -1.0
            alpha 0.5
            pause 0.02
            repeat

###АНИМАЦИЯ ДОЖДЯ
    image ts_rain:
        contains:
            ts_anim + "rain.webp"
            xpos 0.5 ypos -1.0
        contains:
            ts_anim + "rain.webp"
            xpos -0.5 ypos -1.0
        contains:
            ts_anim + "rain.webp"
            xpos 0.5 ypos 0.0
        contains:
            ts_anim + "rain.webp"
            xpos -0.5 ypos 0.0
        contains:
            ts_anim + "rain.webp"
            xpos 0.5 ypos 1.0
        contains:
            ts_anim + "rain.webp"
            xpos -0.5 ypos 1.0
        contains:
            ts_anim + "rain.webp"
            xpos 0.5 ypos 2.0
        contains:
            ts_anim + "rain.webp"
            xpos -0.5 ypos 2.0
        block:
            yanchor 1.0
            linear 0.3 yanchor 0.0
            repeat

###ПЫЛЬ ИЗ ДОКИ
    image dust1:
        ts_anim + "particles/dust/dust1.webp"
        subpixel True
        parallel:
            alpha 1.00
            6.0
            linear 1.0 alpha 0.35
            1.0
            linear 1.0 alpha 1.0
            repeat
        parallel:
            alpha 0
            linear 2.0 alpha 1.0
            10.0
            linear 2.0 alpha 0
            repeat
        parallel:
            xoffset 100 yoffset -100
            linear 14.0 xoffset -100 yoffset 100
            repeat

    image dust2:
        ts_anim + "particles/dust/dust2.webp"
        subpixel True
        parallel:
            alpha 1.00
            6.0
            linear 1.0 alpha 0.35
            1.0
            linear 1.0 alpha 1.0
            repeat
        parallel:
            alpha 0
            linear 2.0 alpha 1.0
            28.0
            linear 2.0 alpha 0
            repeat
        parallel:
            xoffset 100 yoffset -100
            linear 32.0 xoffset -100 yoffset 100
            repeat

    image dust3:
        ts_anim + "particles/dust/dust3.webp"
        subpixel True
        parallel:
            alpha 1.00
            6.0
            linear 1.0 alpha 0.35
            1.0
            linear 1.0 alpha 1.0
            repeat
        parallel:
            alpha 0
            linear 2.0 alpha 1.0
            13.0
            linear 2.0 alpha 0
            repeat
        parallel:
            xoffset 100 yoffset -100
            linear 17.0 xoffset -100 yoffset 100
            repeat

    image dust4:
        ts_anim + "particles/dust/dust4.webp"
        subpixel True
        parallel:
            alpha 1.00
            6.0
            linear 1.0 alpha 0.35
            1.0
            linear 1.0 alpha 1.0
            repeat
        parallel:
            alpha 0
            linear 2.0 alpha 1.0
            15.0
            linear 2.0 alpha 0
            repeat
        parallel:
            xoffset 100 yoffset -100
            linear 19.0 xoffset -100 yoffset 100
            repeat

# TRUE STORY ANIMATION's DEFINE's
# by @b3rg3n
# Since 2024
###ОВРЕЛЕИ
    image zatemnenie = Image(ts_anim + "zatemnenie.webp") # ЗАТЕМНЕНИЕ СРЕДНЕЕ
    image zatemnenie_light = Image(ts_anim + "zatemnenie_light.webp") # ЗАТЕМНЕНИЕ ЛЁГКОЕ
    image blood = ts_anim + "ovr/blood.webp" # КРОВЬ ПО БОКАМ ЭКРАНА
###АНИМАЦИЯ ЗАКРЫТИЯ/ОТКРЫТИЯ ЗЕНЕК
    image anim blink_down = ts_anim + "zenki/blink_down.webp" # ВЕРНХНИЕ ВЕКИ
    image anim blink_up = ts_anim + "zenki/blink_up.webp" # НИЖНИЕ ВЕКИ
###БЛЭКАУТ
    image blackout = ts_anim + "transit/blackout.webp"
    image blackout2 = ts_anim + "transit/blackout2.webp"
    image blackout_exh = ts_anim + "blackout/blackout_exh.webp"
    image blackout_exh2 = ts_anim + "blackout/blackout_exh2.webp"
    image blackout_exh3 = ts_anim + "blackout/blackout_exh3.webp"
###ТРАНЗИТЫ IMAGE
    define ts_lap = ImageDissolve(ts_anim + "transit/ts_lap.webp", 2.0) # ЭФФЕКТ ЧАСОВ
    define ed_night_dis = ImageDissolve(ts_anim + "transit/ed_night_dis.webp", 5.0) # ЭФФЕКТ СГОРАЮЩЕЙ БУМАГИ
    define ed_night_dis_faster = ImageDissolve(ts_anim + "transit/ed_night_dis.webp", 2.5) # ЭФФЕКТ СГОРАЮЩЕЙ БУМАГИ
    define poplil_pacan = ImageDissolve(ts_anim + "transit/wow_blya.webp", 1.66) # ЭФФЕКТ ПЕРЛИВАНИЯ КРОВИ
    define poplil_pacan1 = ImageDissolve(ts_anim + "transit/wow_blya.webp", 6.66) # ЭФФЕКТ ПЕРЛИВАНИЯ КРОВИ
    define awrain = ImageDissolve(ts_anim + "transit/awrain.webp", 1.5, 60, reverse=False) # ЭФФЕКТ СМЫВА ДОЖДЁМ
    define awrain2 = ImageDissolve(ts_anim + "transit/awrain.webp", 4.5, 80, reverse=False) # ЭФФЕКТ СМЫВА ДОЖДЁМ
    define wipeleft = ImageDissolve(ts_anim + "transit/wipeleft.webp", 0.5, ramplen=64)
    define wipeleft_scene = MultipleTransition([
        False, ImageDissolve(ts_anim + "transit/wipeleft.webp", 0.5, ramplen=64),
        Solid("#000"), Pause(0.25),
        Solid("#000"), ImageDissolve(ts_anim + "transit/wipeleft.webp", 0.5, ramplen=64),
        True])
    define wipeleft_scene_long = MultipleTransition([
        False, ImageDissolve(ts_anim + "transit/wipeleft.webp", 1.0, ramplen=64),
        Solid("#000"), Pause(0.5),
        Solid("#000"), ImageDissolve(ts_anim + "transit/wipeleft.webp", 1.0, ramplen=64),
        True])
    define wipeleft_scene_fast = MultipleTransition([
        False, ImageDissolve(ts_anim + "transit/wipeleft.webp", 0.25, ramplen=64),
        Solid("#000"), Pause(0.05),
        Solid("#000"), ImageDissolve(ts_anim + "transit/wipeleft.webp", 0.25, ramplen=64),
        True])
# TRUE STORY SPLIT IMAGES
    image ts_hotel_split = ts_bg + "split/hotel_split.webp"
    image ts_gost_split = ts_bg + "split/gost_split.webp"

    image ts_hotel_split1 = ts_bg + "split/ts_hostel_sleva.webp"
    image ts_kuh_split = ts_bg + "split/ts_kuh_sprava.webp"

    image ts_cor_split = ts_bg + "split/ts_corridor_split.webp"
    image ts_of_split = ts_bg + "split/ts_office_split.webp"

    image ts_bed_split = ts_bg + "split/ts_bedroom_split.webp"
    image ts_club_split = ts_bg + "split/ts_class_split.webp"

    image ts_bed_split_animated: # pause 0.99
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'ts_bed_split'
        parallel:
            ypos 1.5 alpha 0.0
            linear 0.99 ypos 1.0 alpha 1.0

    image ts_club_split_animated: # pause 0.99
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'ts_club_split'
        parallel:
            ypos 0.5 alpha 0.0
            linear 0.99 ypos 1.0 alpha 1.0

    image ts_cor_split_animated: # pause 0.99
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'ts_cor_split'
        parallel:
            ypos 1.5 alpha 0.0
            linear 0.99 ypos 1.0 alpha 1.0

    image ts_kuh_split_animated: # pause 0.99
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'ts_kuh_split'
        parallel:
            ypos 0.5 alpha 0.0
            linear 0.99 ypos 1.0 alpha 1.0

    image ts_of_split_animated: # pause 0.99
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'ts_of_split'
        parallel:
            ypos 0.5 alpha 0.0
            linear 0.99 ypos 1.0 alpha 1.0

    image ts_kuh_split_animated: # pause 0.99
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'ts_kuh_split'
        parallel:
            ypos 0.5 alpha 0.0
            linear 0.99 ypos 1.0 alpha 1.0

    image ts_host_split_animated: # pause 0.99
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'ts_hotel_split1'
        parallel:
            ypos 1.5 alpha 0.0
            linear 0.99 ypos 1.0 alpha 1.0

    image ts_gost_split_animated: # pause 0.99
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'ts_gost_split'
        parallel:
            ypos 1.5 alpha 0.0
            linear 0.99 ypos 1.0 alpha 1.0

    image ts_hotel_split_animated: # pause 0.99
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'ts_hotel_split'
        parallel:
            ypos 0.5 alpha 0.0
            linear 0.99 ypos 1.0 alpha 1.0

###INTERFACE DEFINES
    image ru_ground = ts_images + "gui/lang/russian_ground.png"
    image ru_hover = ts_images + "gui/lang/russian_hover.png"

    image en_ground = ts_images + "gui/lang/english_ground.png"
    image en_hover = ts_images + "gui/lang/english_hover.png"

    image ts_cursor_anim = 'mod_assets/source/images/gui/mouse/ts_mouse_white.png'

###CHESS
    image chess1 = ts_images + "minigame/chess/1.webp"
    image chess2 = ts_images + "minigame/chess/2.webp"
    image chess3 = ts_images + "minigame/chess/3.webp"
    image chess4 = ts_images + "minigame/chess/4.webp"
    image chess5 = ts_images + "minigame/chess/5.webp"
    image chess6 = ts_images + "minigame/chess/6.webp"
    image chess7 = ts_images + "minigame/chess/7.png"
    image chess8 = ts_images + "minigame/chess/8.png"
    image chess9 = ts_images + "minigame/chess/9.png"
    image chess10 = ts_images + "minigame/chess/10.png"
    image chess11 = ts_images + "minigame/chess/11.png"
    image chess12 = ts_images + "minigame/chess/12.png"
    image chess13 = ts_images + "minigame/chess/13.png"
    image chess14 = ts_images + "minigame/chess/14.png"
    image chess15 = ts_images + "minigame/chess/15.png"
    image chess16 = ts_images + "minigame/chess/16.png"
    image chess17 = ts_images + "minigame/chess/17.png"
    image chess18 = ts_images + "minigame/chess/18.png"
    image chess19 = ts_images + "minigame/chess/19.png"

    image atc3_chess1 = ts_images + "minigame/chess/act3_1.webp"
    image atc3_chess2 = ts_images + "minigame/chess/act3_2.webp"
    image atc3_chess3 = ts_images + "minigame/chess/act3_3.webp"
    image atc3_chess4 = ts_images + "minigame/chess/act3_4.webp"
    image atc3_chess5 = ts_images + "minigame/chess/act3_5.webp"
    image atc3_chess6 = ts_images + "minigame/chess/act3_6.webp"
    image atc3_chess7 = ts_images + "minigame/chess/act3_7.webp"
    image atc3_chess8 = ts_images + "minigame/chess/act3_8.webp"
    image atc3_chess9 = ts_images + "minigame/chess/act3_9.webp"
    image atc3_chess10 = ts_images + "minigame/chess/act3_10.webp"
    image atc3_chess11 = ts_images + "minigame/chess/act3_11.webp"
    image atc3_chess12 = ts_images + "minigame/chess/act3_12.webp"
    image atc3_chess13 = ts_images + "minigame/chess/act3_13.webp"
    image atc3_chess14 = ts_images + "minigame/chess/act3_14.webp"
    image atc3_chess15 = ts_images + "minigame/chess/act3_15.webp"
    image atc3_chess16 = ts_images + "minigame/chess/act3_16.webp"
    image atc3_chess17 = ts_images + "minigame/chess/act3_17.webp"
    image atc3_chess18 = ts_images + "minigame/chess/act3_18.webp"
    image atc3_chess19 = ts_images + "minigame/chess/act3_19.webp"
    image atc3_chess20 = ts_images + "minigame/chess/act3_20.webp"
    image atc3_chess21 = ts_images + "minigame/chess/act3_21.webp"
    image atc3_chess22 = ts_images + "minigame/chess/act3_22.webp"
    image atc3_chess23 = ts_images + "minigame/chess/act3_23.webp"
    image atc3_chess24 = ts_images + "minigame/chess/act3_24.webp"
    image atc3_chess25 = ts_images + "minigame/chess/act3_25.webp"
    image atc3_chess26 = ts_images + "minigame/chess/act3_26.webp"


init -1 python:
    ts_paint = ImageDissolve(ts_anim + "transit/ts_paint.webp", 1.5)
    ts_pixel = ImageDissolve(ts_anim + "transit/ts_pixel.webp", 1.0, alpha = True)