# TRUE STORY CG's
# ПОЧТИ ВСЁ - ИЗ ОРИГА ДОКИЧЕЙ
# by @b3rg3n & @dansalvato
# Since 2024

image exception_bg = "#dadada"
image fake_exception = Text("Произошла ошибка.", size=40, style="_default")
image fake_exception2 = Text("File \"game/script-ch5.rpy\", line 307\nSee traceback.txt for details.", size=20, style="_default")
image white = "#ffffff"

image mask_child:
    "mod_assets/source/images/cg/monika/child_2.webp"
    xtile 2

image mask_mask:
    "mod_assets/source/images/cg/monika/mask.webp"
    xtile 3

image mask_mask_flip:
    "mod_assets/source/images/cg/monika/mask.webp"
    xtile 3 xzoom -1


image maskb:
    "mod_assets/source/images/cg/monika/maskb.webp"
    xtile 3

image mask_test = AnimatedMask("#ff6000", "mask_mask", "maskb", 0.10, 32)
image mask_test2 = AnimatedMask("#ffffff", "mask_mask", "maskb", 0.03, 16)
image mask_test3 = AnimatedMask("#ff6000", "mask_mask_flip", "maskb", 0.10, 32)
image mask_test4 = AnimatedMask("#ffffff", "mask_mask_flip", "maskb", 0.03, 16)

image mask_2:
    "mod_assets/source/images/cg/monika/mask_2.webp"
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 1200 xoffset 0
        repeat

image mask_3:
    "mod_assets/source/images/cg/monika/mask_3.webp"
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 180 xoffset 0
        repeat

image monika_room = "mod_assets/source/images/cg/monika/monika_room.webp"
image monika_room_highlight:
    "mod_assets/source/images/cg/monika/monika_room_highlight.webp"
    function monika_alpha
image monika_bg = "mod_assets/source/images/cg/monika/monika_bg.webp"
image monika_bg_highlight:
    "mod_assets/source/images/cg/monika/monika_bg_highlight.webp"
    function monika_alpha
image monika_scare = "mod_assets/source/images/cg/monika/monika_scare.webp"

image monika_body_glitch1:
    "mod_assets/source/images/cg/monika/monika_glitch1.webp"
    0.15
    "mod_assets/source/images/cg/monika/monika_glitch2.webp"
    0.15
    "mod_assets/source/images/cg/monika/monika_glitch1.webp"
    0.15
    "mod_assets/source/images/cg/monika/monika_glitch2.webp"
    1.00
    "mod_assets/source/images/cg/monika/monika_glitch1.webp"
    0.15
    "mod_assets/source/images/cg/monika/monika_glitch2.webp"
    0.15
    "mod_assets/source/images/cg/monika/monika_glitch1.webp"
    0.15
    "mod_assets/source/images/cg/monika/monika_glitch2.webp"

image monika_body_glitch2:
    "mod_assets/source/images/cg/monika/monika_glitch3.webp"
    0.15
    "mod_assets/source/images/cg/monika/monika_glitch4.webp"
    0.15
    "mod_assets/source/images/cg/monika/monika_glitch3.webp"
    0.15
    "mod_assets/source/images/cg/monika/monika_glitch4.webp"
    1.00
    "mod_assets/source/images/cg/monika/monika_glitch3.webp"
    0.15
    "mod_assets/source/images/cg/monika/monika_glitch4.webp"
    0.15
    "mod_assets/source/images/cg/monika/monika_glitch3.webp"
    0.15
    "mod_assets/source/images/cg/monika/monika_glitch4.webp"


image room_glitch = "mod_assets/source/images/cg/monika/monika_bg_glitch.webp"

image room_mask = LiveComposite((1280, 720), (0, 0), "mask_test", (0, 0), "mask_test2")
image room_mask2 = LiveComposite((1280, 720), (0, 0), "mask_test3", (0, 0), "mask_test4")

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

image y_cg2_bg:
    "mod_assets/source/images/cg/y_cg2_bg1.webp"
    6.0
    "mod_assets/source/images/cg/y_cg2_bg2.webp" with Dissolve(1)
    2
    "mod_assets/source/images/cg/y_cg2_bg1.webp" with Dissolve(1)
    1
    repeat
image y_cg2_base:
    "mod_assets/source/images/cg/y_cg2_base.webp"
image y_cg2_nochoc:
    "mod_assets/source/images/cg/y_cg2_nochoc.webp"
    on hide:
        linear 0.5 alpha 0
image y_cg2_details:
    "mod_assets/source/images/cg/y_cg2_details.webp"
    alpha 1.00
    6.0
    linear 1.0 alpha 0.35
    1.0
    linear 1.0 alpha 1.0
    repeat

image y_cg2_exp2:
    "mod_assets/source/images/cg/y_cg2_exp2.webp"
    alpha 0
    linear 0.5 alpha 1
    on hide:
        linear 0.5 alpha 0
image y_cg2_exp3:
    "mod_assets/source/images/cg/y_cg2_exp3.webp"
    alpha 0
    linear 0.5 alpha 1
    on hide:
        linear 0.5 alpha 0

image y_cg2_dust1:
    "mod_assets/source/images/cg/y_cg2_dust1.webp"
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
image y_cg2_dust2:
    "mod_assets/source/images/cg/y_cg2_dust2.webp"
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
image y_cg2_dust3:
    "mod_assets/source/images/cg/y_cg2_dust3.webp"
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

image y_cg2_dust4:
    "mod_assets/source/images/cg/y_cg2_dust4.webp"
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

image n_cg1_bg:
    "mod_assets/source/images/cg/n_cg1_bg.webp"
image n_cg1_base:
    "mod_assets/source/images/cg/n_cg1_base.webp"

image n_cg1_exp1:
    "mod_assets/source/images/cg/n_cg1_exp1.webp"
image n_cg1_exp2:
    "mod_assets/source/images/cg/n_cg1_exp2.webp"
image n_cg1_exp3:
    "mod_assets/source/images/cg/n_cg1_exp3.webp"
image n_cg1_exp4:
    "mod_assets/source/images/cg/n_cg1_exp4.webp"
image n_cg1_exp5:
    "mod_assets/source/images/cg/n_cg1_exp5.webp"

image n_cg1b = LiveComposite((1280,720), (0,0), "mod_assets/source/images/cg/n_cg1b.webp", (882,325), "n_rects1", (732,400), "n_rects2", (850,475), "n_rects3")

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
    "mod_assets/source/images/cg/n_cg2_bg.webp"
image n_cg2_base:
    "mod_assets/source/images/cg/n_cg2_base.webp"
image n_cg2_exp1:
    "mod_assets/source/images/cg/n_cg2_exp1.webp"
image n_cg2_exp2:
    "mod_assets/source/images/cg/n_cg2_exp2.webp"

image n_cg3_base:
    "mod_assets/source/images/cg/n_cg3_base.webp"
image n_cg3_cake:
    "mod_assets/source/images/cg/n_cg3_cake.webp"
image n_cg3_exp1:
    "mod_assets/source/images/cg/n_cg3_exp1.webp"
image n_cg3_exp2:
    "mod_assets/source/images/cg/n_cg3_exp2.webp"

image y_cg1_base:
    "mod_assets/source/images/cg/y_cg1_base.webp"
image y_cg1_exp1:
    "mod_assets/source/images/cg/y_cg1_exp1.webp"
image y_cg1_exp2:
    "mod_assets/source/images/cg/y_cg1_exp2.webp"
image y_cg1_exp3:
    "mod_assets/source/images/cg/y_cg1_exp3.webp"

image y_cg3_base:
    "mod_assets/source/images/cg/y_cg3_base.webp"
image y_cg3_exp1:
    "mod_assets/source/images/cg/y_cg3_exp1.webp"

image s_cg1:
    "mod_assets/source/images/cg/s_cg1.webp"

image s_cg2_base1:
    "mod_assets/source/images/cg/s_cg2_base1.webp"
image s_cg2_base2:
    "mod_assets/source/images/cg/s_cg2_base2.webp"
image s_cg2_exp1:
    "mod_assets/source/images/cg/s_cg2_exp1.webp"
image s_cg2_exp2:
    "mod_assets/source/images/cg/s_cg2_exp2.webp"
image s_cg2_exp3:
    "mod_assets/source/images/cg/s_cg2_exp3.webp"

image s_cg3:
    "mod_assets/source/images/cg/s_cg3.webp"

image s_kill_bg:
    subpixel True
    "mod_assets/source/images/cg/s_kill_bg.webp"

image s_kill:
    subpixel True
    "mod_assets/source/images/cg/s_kill.webp"

image s_kill_bg2:
    subpixel True
    "mod_assets/source/images/cg/s_kill_bg2.webp"

image s_kill2:
    subpixel True
    "mod_assets/source/images/cg/s_kill2.webp"

image y_kill:
    subpixel True
    "mod_assets/source/images/cg/y_kill/1a.webp"

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
