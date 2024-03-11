# TRUE STORY TRANSFORMS
# ПОЧТИ ВСЕ ИЗ ОРИГА ДОКИЧЕЙ
# by @b3rg3n & @dansalvato & @superrage
# Since 2024

# небольшое пояснение по анимациям спрайтов на будущее:
# xx - 11, 22, 33, 44 и прочее
# fxx - фокус на персонаже (т.е. из обычного положения он чуть больше становится и остаётся в этом положении)
# sxx - приседает (не юзать два и более раз подряд - он тпхается на исходную и приседает ещё раз (колхоз кароче пиздец) - если нужно дважды сделать анимацию, но шоп она была "грустная" использую между s - d)
# dxx - приседает и возвращается на исходную
# hxx - подпрыгивает и возвращается на исходную
# txx - просто спавнится на позиции с диссолвом
# ixx - тот же самый t, только без диссолва (т.е. мгновенный)
# используем так - show sayori 1a at s11 условно
# про цифры:
# 11 - только одна позиция по центру
# 21, 22 - две позиции
# 31, 32, 33 - три позиции
# 41, 42, 43, 44 - четыре позиции

init:

    transform camera_zoom:
        ease 2.0 pos (-0.3, 0.0) zoom 1.50

    transform camera_zoom1:
        ease 2.0 pos (-0.4, -0.4) zoom 1.90

    transform noise_alpha:
        alpha 0.25

    transform na10:
        alpha 0.10

    transform noisefade(t=0):
        alpha 0.0
        t
        linear 5.0 alpha 0.40

    transform br_rotate(l, z, x, y):
        parallel:
            zoom z xalign x yalign y rotate_pad True rotate 0
            linear l rotate 360
            repeat

    transform ec_tr_choice:
        on hover:
            easein 0.1 yoffset -2
        on idle:
            easein 0.1 yoffset 2

    transform ts_razebal:
        xalign 0.5 yalign 0.5
        parallel:
            ease 0.25 zoom 1.1
            ease 0.5 zoom 1.0
        parallel:
            ease 0.25 rotate -1.5
            ease 0.25 rotate 1.0
            ease 0.25 rotate 0.0

    transform ts_get_achievement:
        pos (0.2, 0.8)
        anchor (0.5, 0.5)
        zoom 0.0
        ease 1.5 zoom 1.05
        ease 0.25 zoom 0.95
        ease 0.25 zoom 1.0
        pause 4.0
        ease 0.5 pos (-0.8, 0.85)
        ease 0.5 pos (-1.0, 0.85) alpha 0.0

    transform ts_running_fast:
        truecenter
        zoom 1.25
        parallel:
            ease 0.25 zoom 1.30 rotate 0.75
            ease 0.20 zoom 1.25 rotate -0.75
            ease 0.25 zoom 1.30 rotate 0.75
            ease 0.20 zoom 1.35 rotate -0.75
            repeat
        parallel:
            ease 0.25 xpos 0.495
            ease 0.20 xpos 0.505
            repeat
        parallel:
            ease 0.25 ypos 0.495
            ease 0.30 ypos 0.505
            repeat

    transform ts_beg:
        parallel:
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            ease 0.2 zoom 1.04 xpos 0.5 ypos 0.49
        parallel:
            ease 0.2 xpos 0.5 ypos 0.49
            ease 0.2 xpos 0.48 ypos 0.51
            ease 0.2 xpos 0.5 ypos 0.49
            ease 0.2 xpos 0.52 ypos 0.51
            repeat

    transform ts_heartattack(img):


        contains:
            img
            alpha 0.0 zoom 1.0 xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            parallel:
                ease 0.25 alpha 0.25
                ease 0.5 alpha 0.0
            parallel:
                ease 0.75 zoom 1.10
            repeat
        contains:
            img
            alpha 0.0 zoom 1.0 xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            parallel:
                ease 0.25 alpha 0.25
                ease 0.5 alpha 0.0
            parallel:
                ease 0.75 zoom 0.90
            repeat
        contains:
            "blood"
            alpha 0.0
            block:
                ease 0.25 alpha 1.0
                ease 0.75 alpha 0.75
                repeat
    python:
        def Aw_HeartAttack(img):
            renpy.show(img, tag="bg2", at_list=[ts_heartattack(img)])

    transform ts_alko(img):


        contains:
            img
            alpha 0.0 zoom 1.0 xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            parallel:
                ease 0.25 alpha 0.25
                ease 0.5 alpha 0.0
            parallel:
                ease 0.75 zoom 1.10
            repeat
        contains:
            img
            alpha 0.0 zoom 1.0 xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            parallel:
                ease 0.25 alpha 0.25
                ease 0.5 alpha 0.0
            parallel:
                ease 0.75 zoom 0.90
            repeat

    python:
        def Aw_Alko(img):
            renpy.show(img, tag="bg2", at_list=[ts_alko(img)])

    transform chapter_anim:
        block:
            parallel:
                parallel:
                    choice:
                        xanchor 0.2
                    choice:
                        xanchor 0.3
                    choice:
                        xanchor 0.4
                    choice:
                        xanchor 0.5
                    choice:
                        xanchor 0.6
                    choice:
                        xanchor 0.7
                    choice:
                        xanchor 0.8
                parallel:
                    choice:
                        yanchor 0.2
                    choice:
                        yanchor 0.3
                    choice:
                        yanchor 0.4
                    choice:
                        yanchor 0.5
                    choice:
                        yanchor 0.6
                    choice:
                        yanchor 0.7
                    choice:
                        yanchor 0.8
            parallel:
                choice:
                    rotate -2
                choice:
                    rotate -1
                choice:
                    rotate 0
                choice:
                    rotate 1
                choice:
                    rotate 2
            parallel:
                choice:
                    alpha 1.0
                choice:
                    alpha 0.9
                choice:
                    alpha 0.8
                choice:
                    alpha 0.7
                choice:
                    alpha 0.6
                choice:
                    alpha 0.5
                choice:
                    alpha 0.4
            pause 0.02
            repeat 20
        block:
            parallel:
                parallel:
                    choice:
                        xanchor 0.498
                    choice:
                        xanchor 0.5
                    choice:
                        xanchor 0.502
                parallel:
                    choice:
                        yanchor 0.498
                    choice:
                        yanchor 0.5
                    choice:
                        yanchor 0.502
            parallel:
                choice:
                    rotate -0.2
                choice:
                    rotate -0.1
                choice:
                    rotate 0
                choice:
                    rotate 0.1
                choice:
                    rotate 0.2
            parallel:
                choice:
                    alpha 1.0
                choice:
                    alpha 0.9
                choice:
                    alpha 0.8
            pause 0.02
            repeat

    python:
        style.chapter_text.font = "mod_assets/source/fonts/Surfbars.otf"
        style.chapter_text.xalign = 0.5
        style.chapter_text.yalign = 0.5
        style.chapter_text.size = 100    
        style.chapter_text.color = "#ffffff"

        def Chapter(name, time=3):
            renpy.show_screen("chapter", name)
            renpy.pause(time-0.4, hard=True)
            renpy.hide("chapter", layer="screens")
            renpy.show_screen("chapter", name)
            renpy.pause(0.4, hard=True)
            renpy.hide("chapter", layer="screens")

screen chapter(name):
    text name:
        style "chapter_text"
        at chapter_anim



transform tcommon(x=640, z=0.80):
    yanchor 1.0 subpixel True
    on show:
        ypos 1.03
        zoom z*0.95 alpha 0.00
        xcenter x yoffset -20
        easein .25 yoffset 0 zoom z*1.00 alpha 1.00
    on replace:

        alpha 1.00
        parallel:
            easein .25 xcenter x zoom z*1.00
        parallel:
            easein .15 yoffset 0 ypos 1.03

transform tinstant(x=640, z=0.80):
    xcenter x yoffset 0 zoom z*1.00 alpha 1.00 yanchor 1.0 ypos 1.03

transform focus(x=640, z=0.80):
    yanchor 1.0 ypos 1.03 subpixel True
    on show:

        zoom z*0.95 alpha 0.00
        xcenter x yoffset -20
        easein .25 yoffset 0 zoom z*1.05 alpha 1.00
        yanchor 1.0 ypos 1.03
    on replace:
        alpha 1.00
        parallel:
            easein .25 xcenter x zoom z*1.05
        parallel:
            easein .15 yoffset 0

transform sink(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .5 ypos 1.06

transform hop(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .1 yoffset -20
    easeout .1 yoffset 0

transform hopfocus(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.05 alpha 1.00 subpixel True
    easein .1 yoffset -21
    easeout .1 yoffset 0

transform dip(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .25 yoffset 25
    easeout .25 yoffset 0

transform panic(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    parallel:
        ease 1.2 yoffset 25
        ease 1.2 yoffset 0
        repeat
    parallel:
        easein .3 xoffset 20
        ease .6 xoffset -20
        easeout .3 xoffset 0
        repeat

transform leftin(x=640, z=0.80):
    xcenter -300 yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .25 xcenter x


transform thide(z=0.80):
    subpixel True
    transform_anchor True
    on hide:

        easein .25 zoom z*0.95 alpha 0.00 yoffset -20
transform lhide:
    subpixel True
    on hide:
        easeout .25 xcenter -300

transform lang_ru_ground:
    align (0.5, 0.45)
    ease 0.5 align (0.2, 0.45)
    linear 1.0 align (1.6, 0.45)

transform lang_ru_hover:
    align (0.5, 0.45)
    pause 1.5
    ease 1.0 align (0.5, 0.45)
    linear 1.5 zoom 1.5
    pause 1.5

transform lang_en_ground:
    align (0.5, 0.65)
    ease 0.5 align (0.2, 0.65)
    linear 1.0 align (1.6, 0.65)

transform lang_en_hover:
    align (0.5, 0.65)
    pause 1.5
    ease 1.0 align (0.5, 0.65)
    linear 1.5 zoom 1.5
    pause 1.5

transform ts_move_up(y):
    yoffset 300 subpixel True
    ease 0.3 yoffset 50
    ease 0.3 yoffset y

transform ts_move_down(y):
    yoffset y subpixel True
    ease 0.5 yoffset 800

transform t41:
    tcommon(200)
transform t42:
    tcommon(493)
transform t43:
    tcommon(786)
transform t44:
    tcommon(1080)
transform t31:
    tcommon(240)
transform t32:
    tcommon(640)
transform t33:
    tcommon(1040)
transform t21:
    tcommon(400)
transform t22:
    tcommon(880)
transform t11:
    tcommon(640)

transform i41:
    tinstant(200)
transform i42:
    tinstant(493)
transform i43:
    tinstant(786)
transform i44:
    tinstant(1080)
transform i31:
    tinstant(240)
transform i32:
    tinstant(640)
transform i33:
    tinstant(1040)
transform i21:
    tinstant(400)
transform i22:
    tinstant(880)
transform i11:
    tinstant(640)

transform f41:
    focus(200)
transform f42:
    focus(493)
transform f43:
    focus(786)
transform f44:
    focus(1080)
transform f31:
    focus(240)
transform f32:
    focus(640)
transform f33:
    focus(1040)
transform f21:
    focus(400)
transform f22:
    focus(880)
transform f11:
    focus(640)

transform s41:
    sink(200)
transform s42:
    sink(493)
transform s43:
    sink(786)
transform s44:
    sink(1080)
transform s31:
    sink(240)
transform s32:
    sink(640)
transform s33:
    sink(1040)
transform s21:
    sink(400)
transform s22:
    sink(880)
transform s11:
    sink(640)

transform h41:
    hop(200)
transform h42:
    hop(493)
transform h43:
    hop(786)
transform h44:
    hop(1080)
transform h31:
    hop(240)
transform h32:
    hop(640)
transform h33:
    hop(1040)
transform h21:
    hop(400)
transform h22:
    hop(880)
transform h11:
    hop(640)

transform hf41:
    hopfocus(200)
transform hf42:
    hopfocus(493)
transform hf43:
    hopfocus(786)
transform hf44:
    hopfocus(1080)
transform hf31:
    hopfocus(240)
transform hf32:
    hopfocus(640)
transform hf33:
    hopfocus(1040)
transform hf21:
    hopfocus(400)
transform hf22:
    hopfocus(880)
transform hf11:
    hopfocus(640)

transform d41:
    dip(200)
transform d42:
    dip(493)
transform d43:
    dip(786)
transform d44:
    dip(1080)
transform d31:
    dip(240)
transform d32:
    dip(640)
transform d33:
    dip(1040)
transform d21:
    dip(400)
transform d22:
    dip(880)
transform d11:
    dip(640)

transform l41:
    leftin(200)
transform l42:
    leftin(493)
transform l43:
    leftin(786)
transform l44:
    leftin(1080)
transform l31:
    leftin(240)
transform l32:
    leftin(640)
transform l33:
    leftin(1040)
transform l21:
    leftin(400)
transform l22:
    leftin(880)
transform l11:
    leftin(640)


transform face(z=0.80, y=500):
    subpixel True
    xcenter 640
    yanchor 1.0 ypos 1.03
    yoffset y
    zoom z*2.00

transform cgfade:
    on show:
        alpha 0.0
        linear 0.5 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.5 alpha 0.0

transform n_cg2_wiggle:
    subpixel True
    xoffset 0
    easein 0.15 xoffset 20
    easeout 0.15 xoffset 0
    easein 0.15 xoffset -15
    easeout 0.15 xoffset 0
    easein 0.15 xoffset 10
    easeout 0.15 xoffset 0
    easein 0.15 xoffset -5
    ease 0.15 xoffset 0

transform n_cg2_wiggle_loop:
    n_cg2_wiggle
    1.0
    repeat

transform n_cg2_zoom:
    subpixel True
    truecenter
    xoffset 0
    easeout 0.20 zoom 2.5 xoffset 200


define dissolve = Dissolve(0.25)

define dissolve_cg = Dissolve(0.75)
define dissolve_scene = Dissolve(1.0)

define dissolve_scene_full = MultipleTransition([
    False, Dissolve(1.0),
    Solid("#000"), Pause(1.0),
    Solid("#000"), Dissolve(1.0),
    True])

define dissolve_scene_half = MultipleTransition([
    Solid("#000"), Pause(1.0),
    Solid("#000"), Dissolve(1.0),
    True])

define close_eyes = MultipleTransition([
    False, Dissolve(0.5),
    Solid("#000"), Pause(0.25),
    True])

define open_eyes = MultipleTransition([
    False, Dissolve(0.5),
    True])

define trueblack = MultipleTransition([
    Solid("#000"), Pause(0.25),
    Solid("#000")
    ])

define tpause = Pause(0.25)

transform noise_alpha:
    alpha 0.25

transform noisefade(t=0):
    alpha 0.0
    t
    linear 5.0 alpha 0.40

image vignette:
    truecenter
    "mod_assets/source/images/bg/vignette.webp"

transform vignettefade(t=0):
    alpha 0.0
    t
    linear 25.0 alpha 1.00

transform vignetteflicker(t=0):
    alpha 0.0
    t + 2.030
    parallel:
        alpha 1.00
        linear 0.2 alpha 0.8
        0.1
        alpha 0.7
        linear 0.1 alpha 1.00
        alpha 0.0
        1.19
        repeat
    parallel:
        easeout 20 zoom 3.0

transform layerflicker(t=0):
    truecenter
    t + 2.030
    parallel:
        zoom 1.05
        linear 0.2 zoom 1.04
        0.1
        zoom 1.035
        linear 0.1 zoom 1.05
        zoom 1.0
        1.19
        repeat
    parallel:
        easeout_bounce 0.3 xalign 0.6
        easeout_bounce 0.3 xalign 0.4
        repeat

transform rewind:
    truecenter
    zoom 1.20
    parallel:
        easeout_bounce 0.2 xalign 0.55
        easeout_bounce 0.2 xalign 0.45
        repeat
    parallel:
        easeout_bounce 0.33 yalign 0.55
        easeout_bounce 0.33 yalign 0.45
        repeat

transform heartbeat:
    heartbeat2(1)

transform heartbeat2(m):
    truecenter
    parallel:
        0.144
        zoom 1.00 + 0.07 * m
        easein 0.250 zoom 1.00 + 0.04 * m
        easeout 0.269 zoom 1.00 + 0.07 * m
        zoom 1.00
        1.479
        repeat
    parallel:
        easeout_bounce 0.3 xalign 0.5 + 0.02 * m
        easeout_bounce 0.3 xalign 0.5 - 0.02 * m
        repeat

transform yuripupils_move:
    function yuripupils_function

init python:
    def yuripupils_function(trans, st, at):
        trans.xoffset = -1 + random.random() * 9 - 4
        trans.yoffset = 3 + random.random() * 6 - 3
        return random.random() * 1.2 + 0.3

transform malpha(a=1.00):
    i11
    alpha a


#

transform ts_leftin(e=1.0, x=640, y=1.03, z=0.80):
    xcenter -300 yoffset 0 yanchor 1.0 ypos y zoom z*1.00 alpha 1.00 subpixel True
    easein e xcenter x

transform ts_rightin(e=1.0, x=640, y=1.03, z=0.80):
    xcenter 1400 yoffset 0 yanchor 1.0 ypos y zoom z*1.00 alpha 1.00 subpixel True
    easein e xcenter x

transform ts_leftout(e=1.0, x=640, y=1.03, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos y zoom z*1.00 alpha 1.00 subpixel True
    easein e xcenter -300

transform ts_rightout(e=1.0, x=640, y=1.03, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos y zoom z*1.00 alpha 1.00 subpixel True
    easein e xcenter 1400

transform ts_tcommon(e=1.0, x=640):
    yanchor 1.0 subpixel True
    on show:
        ypos 1.03
        zoom 0.80*0.95 alpha 0.00
        xcenter x yoffset -20
        easein e yoffset 0 zoom 0.80*1.00 alpha 1.00
    on replace:

        alpha 1.00
        parallel:
            easein e xcenter x zoom 0.80*1.00
        parallel:
            easein 0.5 yoffset 0 ypos 1.03

transform ts_sprite_alpha(a=0.5):
    xcenter 640 yoffset 0 zoom 0.80 alpha a subpixel True

transform ts_move_up(y):
    yoffset 300 subpixel True
    ease 0.3 yoffset 50
    ease 0.3 yoffset y

transform ts_move_down(y):
    yoffset y subpixel True
    ease 0.5 yoffset 800

transform ts_chess_move_up:
    xoffset 400 yoffset 300 alpha 0.0 subpixel True
    ease 0.6 yoffset 50 alpha 1.0

####
transform ln41:
    ts_leftin(1.0, 200)
transform ln42:
    ts_leftin(1.0, 493)
transform ln43:
    ts_leftin(1.0, 786)
transform ln44:
    ts_leftin(1.0, 1080)
transform ln31:
    ts_leftin(1.0, 240)
transform ln32:
    ts_leftin(1.0, 640)
transform ln33:
    ts_leftin(1.0, 1040)
transform ln21:
    ts_leftin(1.0, 400)
transform ln22:
    ts_leftin(1.0, 880)
transform ln11:
    ts_leftin(1.0, 640)

transform lf41:
    ts_leftin(0.5, 200)
transform lf42:
    ts_leftin(0.5, 493)
transform lf43:
    ts_leftin(0.5, 786)
transform lf44:
    ts_leftin(0.5, 1080)
transform lf31:
    ts_leftin(0.5, 240)
transform lf32:
    ts_leftin(0.5, 640)
transform lf33:
    ts_leftin(0.5, 1040)
transform lf21:
    ts_leftin(0.5, 400)
transform lf22:
    ts_leftin(0.5, 880)
transform lf11:
    ts_leftin(0.5, 640)

transform ls41:
    ts_leftin(1.5, 200)
transform ls42:
    ts_leftin(1.5, 493)
transform ls43:
    ts_leftin(1.5, 786)
transform ls44:
    ts_leftin(1.5, 1080)
transform ls31:
    ts_leftin(1.5, 240)
transform ls32:
    ts_leftin(1.5, 640)
transform ls33:
    ts_leftin(1.5, 1040)
transform ls21:
    ts_leftin(1.5, 400)
transform ls22:
    ts_leftin(1.5, 880)
transform ls11:
    ts_leftin(1.5, 640)

transform lss41:
    ts_leftin(2.0, 200)
transform lss42:
    ts_leftin(2.0, 493)
transform lss43:
    ts_leftin(2.0, 786)
transform lss44:
    ts_leftin(2.0, 1080)
transform lss31:
    ts_leftin(2.0, 240)
transform lss32:
    ts_leftin(2.0, 640)
transform lss33:
    ts_leftin(2.0, 1040)
transform lss21:
    ts_leftin(2.0, 400)
transform lss22:
    ts_leftin(2.0, 880)
transform lss11:
    ts_leftin(2.0, 640)
####
transform rn41:
    ts_rightin(1.0, 200)
transform rn42:
    ts_rightin(1.0, 493)
transform rn43:
    ts_rightin(1.0, 786)
transform rn44:
    ts_rightin(1.0, 1080)
transform rn31:
    ts_rightin(1.0, 240)
transform rn32:
    ts_rightin(1.0, 640)
transform rn33:
    ts_rightin(1.0, 1040)
transform rn21:
    ts_rightin(1.0, 400)
transform rn22:
    ts_rightin(1.0, 880)
transform rn11:
    ts_rightin(1.0, 640)

transform rf41:
    ts_rightin(0.5, 200)
transform rf42:
    ts_rightin(0.5, 493)
transform rf43:
    ts_rightin(0.5, 786)
transform rf44:
    ts_rightin(0.5, 1080)
transform rf31:
    ts_rightin(0.5, 240)
transform rf32:
    ts_rightin(0.5, 640)
transform rf33:
    ts_rightin(0.5, 1040)
transform rf21:
    ts_rightin(0.5, 400)
transform rf22:
    ts_rightin(0.5, 880)
transform rf11:
    ts_rightin(0.5, 640)

transform rs41:
    ts_rightin(1.5, 200)
transform rs42:
    ts_rightin(1.5, 493)
transform rs43:
    ts_rightin(1.5, 786)
transform rs44:
    ts_rightin(1.5, 1080)
transform rs31:
    ts_rightin(1.5, 240)
transform rs32:
    ts_rightin(1.5, 640)
transform rs33:
    ts_rightin(1.5, 1040)
transform rs21:
    ts_rightin(1.5, 400)
transform rs22:
    ts_rightin(1.5, 880)
transform rs11:
    ts_rightin(1.5, 640)
transform rs51:
    ts_rightin(1.5, 216)
transform rs52:
    ts_rightin(1.5, 432)
transform rs53:
    ts_rightin(1.5, 648)
transform rs54:
    ts_rightin(1.5, 864)
transform rs55:
    ts_rightin(1.5, 1080)

transform rss41:
    ts_rightin(2.0, 200)
transform rss42:
    ts_rightin(2.0, 493)
transform rss43:
    ts_rightin(2.0, 786)
transform rss44:
    ts_rightin(2.0, 1080)
transform rss31:
    ts_rightin(2.0, 240)
transform rss32:
    ts_rightin(2.0, 640)
transform rss33:
    ts_rightin(2.0, 1040)
transform rss21:
    ts_rightin(2.0, 400)
transform rss22:
    ts_rightin(2.0, 880)
transform rss11:
    ts_rightin(2.0, 640)
#####

transform ron41:
    ts_rightout(1.0, 200)
transform ron42:
    ts_rightout(1.0, 493)
transform ron43:
    ts_rightout(1.0, 786)
transform ron44:
    ts_rightout(1.0, 1080)
transform ron31:
    ts_rightout(1.0, 240)
transform ron32:
    ts_rightout(1.0, 640)
transform ron33:
    ts_rightout(1.0, 1040)
transform ron21:
    ts_rightout(1.0, 400)
transform ron22:
    ts_rightout(1.0, 880)
transform ron11:
    ts_rightout(1.0, 640)

transform rof41:
    ts_rightout(0.5, 200)
transform rof42:
    ts_rightout(0.5, 493)
transform rof43:
    ts_rightout(0.5, 786)
transform rof44:
    ts_rightout(0.5, 1080)
transform rof31:
    ts_rightout(0.5, 240)
transform rof32:
    ts_rightout(0.5, 640)
transform rof33:
    ts_rightout(0.5, 1040)
transform rof21:
    ts_rightout(0.5, 400)
transform rof22:
    ts_rightout(0.5, 880)
transform rof11:
    ts_rightout(0.5, 640)

transform ros41:
    ts_rightout(1.5, 200)
transform ros42:
    ts_rightout(1.5, 493)
transform ros43:
    ts_rightout(1.5, 786)
transform ros44:
    ts_rightout(1.5, 1080)
transform ros31:
    ts_rightout(1.5, 240)
transform ros32:
    ts_rightout(1.5, 640)
transform ros33:
    ts_rightout(1.5, 1040)
transform ros21:
    ts_rightout(1.5, 400)
transform ros22:
    ts_rightout(1.5, 880)
transform ros11:
    ts_rightout(1.5, 640)
transform ros51:
    ts_rightout(1.5, 216)
transform ros52:
    ts_rightout(1.5, 432)
transform ros53:
    ts_rightout(1.5, 648)
transform ros54:
    ts_rightout(1.5, 864)
transform ros55:
    ts_rightout(1.5, 1080)

transform ross41:
    ts_rightout(2.0, 200)
transform ross42:
    ts_rightout(2.0, 493)
transform ross43:
    ts_rightout(2.0, 786)
transform ross44:
    ts_rightout(2.0, 1080)
transform ross31:
    ts_rightout(2.0, 240)
transform ross32:
    ts_rightout(2.0, 640)
transform ross33:
    ts_rightout(2.0, 1040)
transform ross21:
    ts_rightout(2.0, 400)
transform ross22:
    ts_rightout(2.0, 880)
transform ross11:
    ts_rightout(2.0, 640)
####
transform tn41:
    ts_tcommon(1.0, 200)
transform tn42:
    ts_tcommon(1.0, 493)
transform tn43:
    ts_tcommon(1.0, 786)
transform tn44:
    ts_tcommon(1.0, 1080)
transform tn31:
    ts_tcommon(1.0, 240)
transform tn32:
    ts_tcommon(1.0, 640)
transform tn33:
    ts_tcommon(1.0, 1040)
transform tn21:
    ts_tcommon(1.0, 400)
transform tn22:
    ts_tcommon(1.0, 880)
transform tn11:
    ts_tcommon(1.0, 640)

transform tn41:
    ts_tcommon(1.0, 200)
transform tn42:
    ts_tcommon(1.0, 493)
transform tn43:
    ts_tcommon(1.0, 786)
transform tn44:
    ts_tcommon(1.0, 1080)
transform tn31:
    ts_tcommon(1.0, 240)
transform tn32:
    ts_tcommon(1.0, 640)
transform tn33:
    ts_tcommon(1.0, 1040)
transform tn21:
    ts_tcommon(1.0, 400)
transform tn22:
    ts_tcommon(1.0, 880)
transform tn11:
    ts_tcommon(1.0, 640)

transform tf41:
    ts_tcommon(0.5, 200)
transform tf42:
    ts_tcommon(0.5, 493)
transform tf43:
    ts_tcommon(0.5, 786)
transform tf44:
    ts_tcommon(0.5, 1080)
transform tf31:
    ts_tcommon(0.5, 240)
transform tf32:
    ts_tcommon(0.5, 640)
transform tf33:
    ts_tcommon(0.5, 1040)
transform tf21:
    ts_tcommon(0.5, 400)
transform tf22:
    ts_tcommon(0.5, 880)
transform tf11:
    ts_tcommon(0.5, 640)

transform ts41:
    ts_tcommon(1.5, 200)
transform ts42:
    ts_tcommon(1.5, 493)
transform ts43:
    ts_tcommon(1.5, 786)
transform ts44:
    ts_tcommon(1.5, 1080)
transform ts31:
    ts_tcommon(1.5, 240)
transform ts32:
    ts_tcommon(1.5, 640)
transform ts33:
    ts_tcommon(1.5, 1040)
transform ts21:
    ts_tcommon(1.5, 400)
transform ts22:
    ts_tcommon(1.5, 880)
transform ts11:
    ts_tcommon(1.5, 640)

transform tss41:
    ts_tcommon(2.0, 200)
transform tss42:
    ts_tcommon(2.0, 493)
transform tss43:
    ts_tcommon(2.0, 786)
transform tss44:
    ts_tcommon(2.0, 1080)
transform tss31:
    ts_tcommon(2.0, 240)
transform tss32:
    ts_tcommon(2.0, 640)
transform tss33:
    ts_tcommon(2.0, 1040)
transform tss21:
    ts_tcommon(2.0, 400)
transform tss22:
    ts_tcommon(2.0, 880)
transform tss11:
    ts_tcommon(2.0, 640)

transform ts_hidescreens:
    xpos 0.0 ypos 0.0 alpha 1.0 subpixel True
    ease 1.0 xpos 0.0 ypos 0.2 alpha 0.0

transform ts_showscreens:
    ypos 0.2 alpha 0.0 subpixel True
    ease 1.0 ypos 0.0 alpha 1.0

transform ts_super_effect:
    xalign 0.5 yalign 0.5 zoom 1.1 subpixel True
    parallel:
        ease 2.0 xpos 0.505
        ease 2.0 xpos 0.4915
        ease 2.0 xpos 0.5115
        ease 2.0 xpos 0.495
        repeat
    parallel:
        ease 1.9 ypos 0.52
        ease 1.9 ypos 0.489
        ease 1.9 ypos 0.52
        ease 1.9 ypos 0.489
        repeat
    parallel:
        ease 2.25 rotate -0.5
        ease 2.25 rotate -0.57
        ease 2.25 rotate -0.2
        ease 2.25 rotate 0.17
        ease 2.25 rotate 0.5
        ease 2.25 rotate 0.2
        ease 2.25 rotate 0.57
        repeat
    parallel:
        pause 1.15
        ease 0.25 zoom 1.5
        ease 0.5 zoom 1.1
        repeat
    parallel:
        pause 1.15
        ease 0.25 rotate 8.9
        ease 0.25 rotate 1.0
        ease 0.25 rotate 0.0
        repeat

transform ts_bg_zoom_e(z=1.0, zz=1.0, t=0.25, x=0.5, xx=0.5, y=0.5, yy=0.5, a=1.0, aa=1.0):
    zoom z xalign x yalign y alpha a subpixel True
    ease t zoom zz xalign xx yalign yy alpha aa

transform ts_null_transform:
    pause 0.1

transform ts_shake(t1=ts_null_transform, t2=ts_null_transform, t3=ts_null_transform, t4=ts_null_transform, t5=ts_null_transform, t6=ts_null_transform):
    parallel:
        t1
    parallel:
        t2
    parallel:
        t3
    parallel:
        t4
    parallel:
        t5
    parallel:
        t6

transform ts_xypos(xp=0.5, yp=1.0, time=0.0):
    ease time xpos xp ypos yp subpixel True

transform ts_menu_trans:
    xalign 0.5
    yalign 0.5
    #zoom 1.0
    #parallel:
    #    linear 1.0 zoom 1.05
    parallel:
        ease 1.5 rotate 0.2
        ease 1.5 rotate -0.2
        repeat

transform ts_blur_zadnika:
    blur 0.0
    parallel:
        linear 1.0 blur 15.0

transform ts_ukachivaet_blya:
    xalign 0.5
    yalign 0.5
    zoom 1.0
    parallel:
        linear 1.0 zoom 1.05
    parallel:
        ease 1.0 xalign 0.45
        ease 1.0 xalign 0.54
        repeat
    parallel:
        ease 1.5 rotate 1.2 zoom 1.07
        ease 1.5 rotate -1.4 zoom 1.045
        repeat

transform ts_super_shake:
    block:
        parallel:
            parallel:
                choice:
                    xanchor 0.2
                choice:
                    xanchor 0.3
                choice:
                    xanchor 0.4
                choice:
                    xanchor 0.5
                choice:
                    xanchor 0.6
                choice:
                    xanchor 0.7
                choice:
                    xanchor 0.8
            parallel:
                choice:
                    yanchor 0.2
                choice:
                    yanchor 0.3
                choice:
                    yanchor 0.4
                choice:
                    yanchor 0.5
                choice:
                    yanchor 0.6
                choice:
                    yanchor 0.7
                choice:
                    yanchor 0.8
        parallel:
            choice:
                rotate -2
            choice:
                rotate -0.5
            choice:
                rotate 0
            choice:
                rotate 0.5
            choice:
                rotate 2
        pause 0.04
        repeat 10
    block:
        parallel:
            parallel:
                choice:
                    xanchor 0.499
                choice:
                    xanchor 0.5
                choice:
                    xanchor 0.501
            parallel:
                choice:
                    yanchor 0.499
                choice:
                    yanchor 0.5
                choice:
                    yanchor 0.501
        parallel:
            choice:
                rotate -0.2
            choice:
                rotate -0.1
            choice:
                rotate 0
            choice:
                rotate 0.1
            choice:
                rotate 0.2
        pause 0.04
        repeat

transform ts_black_glitch:
    alpha 0.5
    parallel:
        0.36
        alpha 0.5
        repeat
    parallel:
        0.49
        alpha 0.475
        repeat

transform ts_coridor_glitch:
    xoffset 0
    parallel:
        0.36
        xoffset 1
        repeat
    parallel:
        0.49
        xoffset 0
        repeat