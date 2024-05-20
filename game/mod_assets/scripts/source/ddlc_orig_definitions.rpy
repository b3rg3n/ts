# TRUE STORY CG's
# ПОЧТИ ВСЁ - ИЗ ОРИГА ДОКИЧЕЙ
# by @b3rg3n & @dansalvato
# Since 2024

# ORIGINAL DOKI

image exception_bg = "#dadada"
image fake_exception = Text("Произошла ошибка.", size=40, style="_default")
image fake_exception2 = Text("File \"mod_assets/scripts/scenario/ts_scenario4.rpy\", line 1576\nSee traceback.txt for details.", size=20, style="_default")
image white = "#ffffff"

image monika_scare = ts_cg + "monika/monika_scare.webp"
image splash_glitch1:
    "mod_assets/source/images/pizda/splash-glitch.webp"

image splash_glitch:
    subpixel True
    "mod_assets/source/images/pizda/splash-glitch.webp"
    alpha 0.0
    pause 0.5
    linear 0.5 alpha 1.0
    pause 2.5
    linear 0.5 alpha 0.0
    "mod_assets/source/images/pizda/menu_bg.webp"
    topleft
    alpha 0.0
    parallel:
        xoffset 0 yoffset 0
        linear 0.25 xoffset -100 yoffset -100
        repeat
    parallel:
        linear 0.5 alpha 1.0
    parallel:
        ypos 0
        pause 1.0
        easeout 1.0 ypos -500
image splash_glitch2:
    subpixel True
    "mod_assets/source/images/pizda/menu_bg.webp"
    topleft
    block:
        xoffset 0 yoffset 0
        linear 0.05 xoffset -100 yoffset -100
        repeat

image splash_glitch_m:
    subpixel True
    "mod_assets/source/images/pizda/menu_art_m_ghost.webp"
    zoom 0.5
    xpos 0.5 ypos 0.5
    pause 0.1
    parallel:
        xpos 0.3 ypos 1.2
        linear 0.08 ypos 0.1
        repeat
    parallel:
        pause 0.5
        alpha 0.0

image splash_glitch_n:
    subpixel True
    "mod_assets/source/images/pizda/menu_art_s_ghost.webp"
    zoom 0.5
    pause 0.2
    xpos 0.8 ypos 0.8
    pause 0.05
    xpos 0.2 ypos 0.7
    pause 0.05
    xpos 0.4 ypos 0.2
    pause 0.05
    xpos 0.7 ypos 1.2
    pause 0.05
    xpos 0.1 ypos 1.0
    pause 0.05
    xpos 0.2 ypos 0.6
    pause 0.05
    xpos 0.9 ypos 0.4
    pause 0.05
    alpha 0.0

image splash_glitch_y:
    subpixel True
    "mod_assets/source/images/pizda/menu_art_y_ghost.webp"
    zoom 0.5
    ypos 1.3
    block:
        xpos 0.85
        pause 0.02
        xpos 0.81
        pause 0.02
        repeat


image n_rects_ghost1:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (580, 270)
    size (20, 25)
    alpha 0.0
    8.0
    easeout 12 alpha 1.0

image n_rects_ghost2:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (652, 264)
    size (20, 25)
    alpha 0.0
    8.0
    easeout 12 alpha 1.0

image n_rects_ghost3:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (616, 310)
    size (25, 15)
    alpha 0.0
    8.0
    easeout 12 alpha 1.0

image n_rects_ghost4:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (735, 310)
    size (25, 20)
    0.5
    easeout 0.25 zoom 4.5 xoffset 250 yoffset -250

image n_rects_ghost5:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (740, 376)
    size (25, 20)
    0.5
    easeout 0.25 zoom 4.5 xoffset 250 yoffset -100

image n_cg1_bg:
    ts_cg + "n_cg1_bg.webp"
image n_cg1_b1:
    ts_cg + "n_cg1b.webp"
image n_cg1_base:
    ts_cg + "n_cg1_base.webp"

image n_cg1_exp1:
    ts_cg + "n_cg1_exp1.webp"
image n_cg1_exp2:
    ts_cg + "n_cg1_exp2.webp"
image n_cg1_exp3:
    ts_cg + "n_cg1_exp3.webp"
image n_cg1_exp4:
    ts_cg + "n_cg1_exp4.webp"
image n_cg1_exp5:
    ts_cg + "n_cg1_exp5.webp"

image n_cg1b = LiveComposite((1280,720), (0,0), ts_cg + "n_cg1b.webp", (882,325), "n_rects1", (732,400), "n_rects2", (850,475), "n_rects3")

image n_rects1:
    RectCluster(Solid("#000"), 12, 30, 30).sm
    pos (899, 350)
    size (34, 34)

image n_rects2:
    RectCluster(Solid("#000"), 12, 30, 24).sm
    pos (749, 430)
    size (34, 34)

image n_rects3:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (764, 490)
    size (30, 20)

image n_cg2_bg:
    ts_cg + "n_cg2_bg.webp"
image n_cg2_base:
    ts_cg + "n_cg2_base.webp"
image n_cg2_exp1:
    ts_cg + "n_cg2_exp1.webp"
image n_cg2_exp2:
    ts_cg + "n_cg2_exp2.webp"

image n_cg3_base:
    ts_cg + "n_cg3_base.webp"
image n_cg3_cake:
    ts_cg + "n_cg3_cake.webp"
image n_cg3_exp1:
    ts_cg + "n_cg3_exp1.webp"
image n_cg3_exp2:
    ts_cg + "n_cg3_exp2.webp"

image s_kill_bg:
    subpixel True
    ts_cg + "s_kill_bg.webp"

image s_kill:
    subpixel True
    ts_cg + "s_kill.webp"

image s_kill_bg2:
    subpixel True
    ts_cg + "s_kill_bg2.webp"

image s_kill2:
    subpixel True
    ts_cg + "s_kill2.webp"

image y_kill:
    subpixel True
    ts_cg + "y_kill/1a.webp"

transform s_kill_bg_start:
    truecenter
    zoom 1.10
    linear 4 zoom 1.00

transform s_kill_start:
    truecenter
    xalign 0.3 yalign 0.25 zoom 0.8
    linear 4 zoom 0.75 xalign 0.315 yoffset 10

image s_kill_bg_zoom:
    contains:
        "s_kill_bg"
        xalign 0.2 yalign 0.3 zoom 2.0
    dizzy(0.25, 1.0)

transform dizzy(m, t, subpixel=True):
    subpixel subpixel
    parallel:
        xoffset 0
        ease 0.75 * t xoffset 10 * m
        ease 0.75 * t xoffset 5 * m
        ease 0.75 * t xoffset -5 * m
        ease 0.75 * t xoffset -3 * m
        ease 0.75 * t xoffset -10 * m
        ease 0.75 * t xoffset 0
        ease 0.75 * t xoffset 5 * m
        ease 0.75 * t xoffset 0
        repeat
    parallel:
        yoffset 0
        ease 1.0 * t yoffset 5 * m
        ease 2.0 * t yoffset -5 * m
        easein 1.0 * t yoffset 0
        repeat

image s_kill_zoom:
    contains:
        "s_kill"
        truecenter
        zoom 2.0 xalign 0.5 yalign 0.05
    dizzy(1, 1.0)

image s_kill_bg2_zoom:
    contains:
        "s_kill_bg2"
        xalign 0.2 yalign 0.3 zoom 2.0
    parallel:
        dizzy(0.25, 1.0)
    parallel:
        alpha 0.2
        linear 0.25 alpha 0.2
        linear 0.25 alpha 0.25
        linear 0.25 alpha 0.2
        linear 0.25 alpha 0.3
        linear 0.25 alpha 0.25
        linear 0.25 alpha 0.35
        linear 0.25 alpha 0.3
        linear 0.25 alpha 0.35
        linear 0.25 alpha 0.2
        repeat

image s_kill2_zoom:
    contains:
        "s_kill2"
        truecenter
        zoom 2.0 xalign 0.5 yalign 0.05
    parallel:
        dizzy(1, 1.0)
    parallel:
        alpha 0.3
        linear 0.25 alpha 0.3
        linear 0.25 alpha 0.4
        linear 0.25 alpha 0.3
        linear 0.25 alpha 0.5
        linear 0.25 alpha 0.4
        linear 0.25 alpha 0.6
        linear 0.25 alpha 0.5
        linear 0.25 alpha 0.6
        linear 0.25 alpha 0.4
        repeat

# DDLC ORIGINAL MUSIC DEFINES
# by @dansalvato
# Since 2024

define audio.t2 = "<loop 4.499>mod_assets/source/audio/ost/orig/2.ogg"
define audio.t2g2 = "<from 4.499 loop 4.499>mod_assets/source/audio/ost/orig/2.ogg"
define audio.t2g3 = "<loop 4.492>mod_assets/source/audio/ost/orig/2g2.ogg"
define audio.t3 = "<loop 4.618>mod_assets/source/audio/ost/orig/3.ogg"
define audio.t4 = "<loop 19.451>mod_assets/source/audio/ost/orig/4.ogg"
define audio.t6 = "<loop 10.893>mod_assets/source/audio/ost/orig/6.ogg"
define audio.t6o = "<loop 10.893>mod_assets/source/audio/ost/orig/6o.ogg"
define audio.t6s = "<loop 43.572>mod_assets/source/audio/ost/orig/6s.ogg"
define audio.t8 = "<loop 9.938>mod_assets/source/audio/ost/orig/8.ogg"
define audio.t9 = "<loop 3.172>mod_assets/source/audio/ost/orig/9.ogg"
define audio.t10 = "<loop 5.861>mod_assets/source/audio/ost/orig/10.ogg"
define audio.t10y = "<loop 0>mod_assets/source/audio/ost/orig/10-yuri.ogg"

define audio.m1 = "<loop 0>mod_assets/source/audio/ost/orig/m1.ogg"

define audio.okevrsay = "<loop 4.444>mod_assets/source/audio/ost/orig/5_sayori.ogg"
define audio.okevryuri = "<loop 4.444>mod_assets/source/audio/ost/orig/5_yuri.ogg"
define audio.okevrnat = "<loop 4.444>mod_assets/source/audio/ost/orig/5_natsuki.ogg"
define audio.okevrnat1 = "<loop 4.444>mod_assets/source/audio/ost/orig/5_ghost.ogg"
define audio.okevrmon = "<loop 4.444>mod_assets/source/audio/ost/orig/5_monika.ogg"
define audio.t5_all = "<loop 4.444>mod_assets/source/audio/ost/orig/5_all.ogg"
define audio.t5_yn = "<loop 4.444>mod_assets/source/audio/ost/orig/5_yn.ogg"
