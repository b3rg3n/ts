#TRUE STORY ANIMATIONS
#by @b3rg3n
#Since 2024
init:
###ЭФФЕКТ RTX ЛУЧЕЙ (БЛЯ БУДУ)
    image god_light:
        contains:
            "mod_assets/source/images/anim/light_eff.webp"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5 rotate 0
            linear 120 rotate 360
            repeat
        contains:
            "mod_assets/source/images/anim/light_eff.webp"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5 rotate 180
            linear 150 rotate -180
            repeat
        contains:
            "mod_assets/source/images/anim/light_eff.webp"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5 rotate 90
            linear 180 rotate 450
            repeat
        contains:
            "mod_assets/source/images/anim/light_eff.webp"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5 rotate -90
            linear 210 rotate -450
            repeat
        contains:
            "mod_assets/source/images/anim/light_eff.webp"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5 rotate 45
            linear 240 rotate 405
            repeat
        contains:
            "mod_assets/source/images/anim/light_eff.webp"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5 rotate -45
            linear 270 rotate -405
            repeat

###ЭФФЕКТ МАТРИЦЫ
    image matrixanim:
        "mod_assets/source/images/anim/matrix/matrixanim1.png"
        pause 0.12
        "mod_assets/source/images/anim/matrix/matrixanim2.png"
        pause 0.12
        "mod_assets/source/images/anim/matrix/matrixanim3.png"
        pause 0.12
        "mod_assets/source/images/anim/matrix/matrixanim4.png"
        pause 0.12
        "mod_assets/source/images/anim/matrix/matrixanim5.png"
        pause 0.12
        "mod_assets/source/images/anim/matrix/matrixanim6.png"
        pause 0.12
        "mod_assets/source/images/anim/matrix/matrixanim7.png"
        pause 0.12
        "mod_assets/source/images/anim/matrix/matrixanim8.png"
        pause 0.12
        "mod_assets/source/images/anim/matrix/matrixanim9.png"
        pause 0.12
        "mod_assets/source/images/anim/matrix/matrixanim10.png"
        pause 0.12
        "mod_assets/source/images/anim/matrix/matrixanim11.png"
        pause 0.12
        repeat

###ЭФФЕКТЫ КРОВАВОГО СКВИРТА
    image bloodanim:
        "mod_assets/source/images/anim/blood/bloodanim1.png"
        pause 0.1
        "mod_assets/source/images/anim/blood/bloodanim2.png"
        pause 0.1
        "mod_assets/source/images/anim/blood/bloodanim3.png"
        pause 0.1
        "mod_assets/source/images/anim/blood/bloodanim4.png"
        pause 0.1
        "mod_assets/source/images/anim/blood/bloodanim5.png"
        
    image altbloodanim:
        "mod_assets/source/images/anim/blood/altbloodanim1.png"
        pause 0.1
        "mod_assets/source/images/anim/blood/altbloodanim2.png"
        pause 0.1
        "mod_assets/source/images/anim/blood/altbloodanim3.png"
        pause 0.1
        "mod_assets/source/images/anim/blood/altbloodanim4.png"

###НАСТОЯЩИЙ ПСИХОДЕЛ
    image overlay psy_pizdos:
        contains:
            choice:
                "himori"
            choice:
                "kk"
            choice:
                "vasdead"
            choice:
                "domext"
            choice:
                "tachila"
            choice:
                "bergenbook"
            choice:
                "morozovcover"
            choice:
                "ch_sek"
            choice:
                "skitscary"
            choice:
                "novomall"
            pause 0.05
            repeat
        contains:
            choice:
                "himori"
            choice:
                "kk"
            choice:
                "vasdead"
            choice:
                "domext"
            choice:
                "tachila"
            choice:
                "bergenbook"
            choice:
                "morozovcover"
            choice:
                "ch_sek"
            choice:
                "skitscary"
            choice:
                "novomall"
            pause 0.05
            repeat
        contains:
            choice:
                "himori"
            choice:
                "kk"
            choice:
                "vasdead"
            choice:
                "domext"
            choice:
                "tachila"
            choice:
                "bergenbook"
            choice:
                "morozovcover"
            choice:
                "ch_sek"
            choice:
                "skitscary"
            choice:
                "novomall"
            pause 0.05
            repeat

###БЕЛЫЙ ШУМ
    image noise:
        truecenter
        "mod_assets/source/images/anim/noise/noise1.webp"
        pause 0.1
        "mod_assets/source/images/anim/noise/noise2.webp"
        pause 0.1
        "mod_assets/source/images/anim/noise/noise3.webp"
        pause 0.1
        "mod_assets/source/images/anim/noise/noise4.webp"
        pause 0.1
        xzoom -1
        "mod_assets/source/images/anim/noise/noise1.webp"
        pause 0.1
        "mod_assets/source/images/anim/noise/noise2.webp"
        pause 0.1
        "mod_assets/source/images/anim/noise/noise3.webp"
        pause 0.1
        "mod_assets/source/images/anim/noise/noise4.webp"
        pause 0.1
        yzoom -1
        "mod_assets/source/images/anim/noise/noise1.webp"
        pause 0.1
        "mod_assets/source/images/anim/noise/noise2.webp"
        pause 0.1
        "mod_assets/source/images/anim/noise/noise3.webp"
        pause 0.1
        "mod_assets/source/images/anim/noise/noise4.webp"
        pause 0.1
        xzoom 1
        "mod_assets/source/images/anim/noise/noise1.webp"
        pause 0.1
        "mod_assets/source/images/anim/noise/noise2.webp"
        pause 0.1
        "mod_assets/source/images/anim/noise/noise3.webp"
        pause 0.1
        "mod_assets/source/images/anim/noise/noise4.webp"
        pause 0.1
        yzoom 1
        repeat

###ЭФФЕКТЫ ПИЗДЕЛКИ
    image Fight_Ddv_Dun_png:
        'mod_assets/source/images/anim/pizdelka/fight_png_01_LW0607.webp' with dissolve
        pause (0.1)
        'mod_assets/source/images/anim/pizdelka/fight_png_02_LW0607.webp' with dissolve
        pause (0.1)
        repeat

###КОЛДА ТАРАЩИТ
    image coldherovo:
        'mod_assets/source/images/spr/cld/pip.webp'
        zoom 1.0
        ease 1.0 xzoom 6.5
        ease 1.0 xzoom 13.1
        ease 1.0 xzoom 15.2
        ease 1.0 xzoom 3.2
        ease 1.0 xzoom 7.7
        ease 1.0 xzoom 14.2
        ease 1.0 xzoom 1.2
        ease 1.0 xzoom 17.45
        ease 1.0 xzoom 7.27
        ease 1.0 xzoom 8.2
        ease 1.0 xzoom 9.2
        ease 1.0 xzoom 1.0
        repeat

###ЭФФЕКТ ПСИХОЗА
    image rageone:
        "et_rage1" with dissolve
        pause .6
        "et_rage2" with dissolve
        pause .6
        repeat

    image ragetwo:
        "et_rage1" with dissolve
        pause .6
        "et_rage2" with dissolve
        pause .6
        "et_rage3" with dissolve
        pause .6
        repeat

    image ragethree:
        "et_rage1" with dissolve
        pause .3
        "et_rage2" with dissolve
        pause .3
        "et_rage3" with dissolve
        pause .3
        "et_rage4" with dissolve
        pause .3
        repeat

###ЭФФЕКТ ЗЕНЕК
    image unblink:
        contains:
            "mod_assets/source/images/anim/zenki/blink_up.webp"
            xalign 0 yalign 0
            ease 1.5 pos (0,-1080)
        contains:
            "mod_assets/source/images/anim/zenki/blink_down.webp"
            xalign 0 yalign 0
            ease 1.5 pos (0,1080)

    image blink:
        contains:
            "mod_assets/source/images/anim/zenki/blink_up.webp"
            pos (0,-1080)
            ease 1.5 xalign 0 yalign 0
        contains:
            "mod_assets/source/images/anim/zenki/blink_down.webp"
            pos (0,1080)
            ease 1.5 xalign 0 yalign 0

###ЭФФЕКТ ВЗРЫВА ЖОПЫ
    image normalno_ebanulo:
        'mod_assets/source/images/anim/babah/babah1.webp' with dissolve
        pause (0.1)
        'mod_assets/source/images/anim/babah/babah2.webp' with dissolve
        pause (0.1)
        'mod_assets/source/images/anim/babah/babah3.webp' with dissolve
        pause (0.1)
        'mod_assets/source/images/anim/babah/babah4.webp' with dissolve
        pause (0.1)
        'mod_assets/source/images/anim/babah/babah5.webp' with dissolve
        pause (0.1)
        'mod_assets/source/images/anim/babah/babah6.webp' with dissolve
        pause (0.1)

###ДУНУЛ ПОДИК
    image anim br_smoke:
        contains:
            'mod_assets/source/images/anim/smoke/br_smoke_1.webp'
            xalign 0.5 yalign 0.5 ypos 0.9 alpha 0.0 zoom 1.0
            pause (0.5)
            linear 0.75 ypos 0.8 zoom 0.9 alpha 1.0
            linear 0.75 ypos 0.7 zoom 0.96 alpha 0.0
        contains:
            'mod_assets/source/images/anim/smoke/br_smoke_2.webp'
            xalign 0.5 yalign 0.5 ypos 0.9 alpha 0.0 zoom 1.0
            pause (0.6)
            linear 0.75 ypos 0.8 zoom 0.9 alpha 1.0
            linear 0.75 ypos 0.7 zoom 0.96 alpha 0.0
        contains:
            'mod_assets/source/images/anim/smoke/br_smoke_3.webp'
            xalign 0.5 yalign 0.5 ypos 0.9 alpha 0.0 zoom 1.0
            pause (0.7)
            linear 0.75 ypos 0.8 zoom 0.9 alpha 1.0
            linear 0.75 ypos 0.7 zoom 0.96 alpha 0.0
        contains:
            'mod_assets/source/images/anim/smoke/br_smoke_4.webp'
            xalign 0.5 yalign 0.5 ypos 0.9 alpha 0.0 zoom 1.0
            pause (0.8)
            linear 0.75 ypos 0.8 zoom 0.9 alpha 1.0
            linear 0.75 ypos 0.7 zoom 0.96 alpha 0.0
        contains:
            'mod_assets/source/images/anim/smoke/br_smoke_5.webp'
            xalign 0.5 yalign 0.5 ypos 0.9 alpha 0.0 zoom 1.0
            pause (0.9)
            linear 0.75 ypos 0.8 zoom 0.9 alpha 1.0
            linear 0.75 ypos 0.7 zoom 0.96 alpha 0.0

###ОВЕРЛЕЙ СТАРОЙ ПЛЁНКИ
    image overlay aw_memory_back_1:
        contains:
            parallel:
                choice:
                    "mod_assets/source/images/anim/mb/aw_o_1.webp"
                choice:
                    "mod_assets/source/images/anim/mb/aw_o_2.webp"
                choice:
                    "mod_assets/source/images/anim/mb/aw_o_3.webp"
                choice:
                    "mod_assets/source/images/anim/mb/aw_o_4.webp"
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
                    "mod_assets/source/images/anim/mb/a_1.webp"
                choice:
                    "mod_assets/source/images/anim/mb/a_2.webp"
                choice:
                    "mod_assets/source/images/anim/mb/a_3.webp"
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
            "mod_assets/source/images/anim/rain.webp"
            xpos 0.5 ypos -1.0
        contains:
            "mod_assets/source/images/anim/rain.webp"
            xpos -0.5 ypos -1.0
        contains:
            "mod_assets/source/images/anim/rain.webp"
            xpos 0.5 ypos 0.0
        contains:
            "mod_assets/source/images/anim/rain.webp"
            xpos -0.5 ypos 0.0
        contains:
            "mod_assets/source/images/anim/rain.webp"
            xpos 0.5 ypos 1.0
        contains:
            "mod_assets/source/images/anim/rain.webp"
            xpos -0.5 ypos 1.0
        contains:
            "mod_assets/source/images/anim/rain.webp"
            xpos 0.5 ypos 2.0
        contains:
            "mod_assets/source/images/anim/rain.webp"
            xpos -0.5 ypos 2.0
        block:
            yanchor 1.0
            linear 0.3 yanchor 0.0
            repeat

###ЛЕПЕСТКИ

    image lepestki:
        choice:
            "mod_assets/source/images/anim/particles/lep/lep_1.webp"
        choice:
            "mod_assets/source/images/anim/particles/lep/lep_2.webp"
        choice:
            "mod_assets/source/images/anim/particles/lep/lep_3.webp"
        choice:
            "mod_assets/source/images/anim/particles/lep/lep_4.webp"
        choice:
            "mod_assets/source/images/anim/particles/lep/lep_5.webp"
        xanchor 0.5 yanchor 0.5 rotate 0
        parallel:
            choice:
                rotate 0
                linear 5 rotate 360
                repeat
            choice:
                rotate 0
                linear 7 rotate -360
                repeat
            choice:
                rotate 0
                linear 9 rotate 360
                repeat
            choice:
                rotate 0
                linear 11 rotate -360
                repeat
            choice:
                rotate 0
                linear 13 rotate 360
                repeat
            choice:
                rotate 0
                linear 15 rotate -360
                repeat

    image ftf_moving_lepestki:
        "lepestki"
        parallel:
            choice:
                xpos -0.1 ypos 0.2
            choice:
                xpos -0.1 ypos 0.1
            choice:
                xpos -0.1 ypos 0.0
            choice:
                xpos 0.0 ypos -0.1
            choice:
                xpos 0.0 ypos -0.2
            choice:
                xpos 0.1 ypos -0.1
            choice:
                xpos 0.1 ypos -0.2
            choice:
                xpos 0.2 ypos -0.1
            choice:
                xpos 0.2 ypos -0.2
            choice:
                xpos 0.3 ypos -0.1
            choice:
                xpos 0.3 ypos -0.2
        parallel:
            choice:
                easeout 10 xpos 0.5
            choice:
                easeout 10 xpos 0.6
            choice:
                easeout 10 xpos 0.7
            choice:
                easeout 10 xpos 0.8
            choice:
                easeout 10 xpos 0.9
            choice:
                easeout 10 xpos 1.0
            choice:
                easeout 10 xpos 1.1
        parallel:
            choice:
                linear 7 ypos 1.1
            choice:
                linear 8 ypos 1.1
            choice:
                linear 9 ypos 1.1
            choice:
                linear 10 ypos 1.1
            choice:
                linear 10 ypos 1.1
        repeat

    image lepestki_krutyatsa:
        contains:
            "ftf_moving_lepestki"
        contains:
            pause 0.5
            "ftf_moving_lepestki"
        contains:
            pause 1.0
            "ftf_moving_lepestki"
        contains:
            pause 1.5
            "ftf_moving_lepestki"
        contains:
            pause 2.0
            "ftf_moving_lepestki"
        contains:
            pause 2.5
            "ftf_moving_lepestki"
        contains:
            pause 3.0
            "ftf_moving_lepestki"
        contains:
            pause 3.5
            "ftf_moving_lepestki"
        contains:
            pause 4.0
            "ftf_moving_lepestki"
        contains:
            pause 4.5
            "ftf_moving_lepestki"
        contains:
            pause 5.0
            "ftf_moving_lepestki"
        contains:
            pause 5.5
            "ftf_moving_lepestki"
        contains:
            pause 6.0
            "ftf_moving_lepestki"
        contains:
            pause 6.5
            "ftf_moving_lepestki"
        contains:
            pause 7.0
            "ftf_moving_lepestki"
        contains:
            pause 7.5
            "ftf_moving_lepestki"
        contains:
            pause 8.0
            "ftf_moving_lepestki"
        contains:
            pause 8.5
            "ftf_moving_lepestki"
        contains:
            pause 9.0
            "ftf_moving_lepestki"
        contains:
            pause 9.5
            "ftf_moving_lepestki"

###ЭФФЕКТ ТРИПА
    image tripsMVWWW777:
        'mod_assets/source/images/anim/trip/trip1MVWWW777.webp' with dissolve
        pause (0.5)
        'mod_assets/source/images/anim/trip/trip2MVWWW777.webp' with dissolve
        pause (0.5)
        'mod_assets/source/images/anim/trip/trip3MVWWW777.webp' with dissolve
        pause (0.5)
        repeat

###ПЫЛЬ ИЗ ДОКИ
    image dust1:
        "mod_assets/source/images/anim/particles/dust/dust1.webp"
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
        "mod_assets/source/images/anim/particles/dust/dust2.webp"
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
        "mod_assets/source/images/anim/particles/dust/dust3.webp"
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
        "mod_assets/source/images/anim/particles/dust/dust4.webp"
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

    image ts_menu_vid = Movie(fps=24, size = (1280, 720), play="mod_assets/source/videosos/jm.webm")
    image ts_menu_vid_night = Movie(fps=24, size = (1280, 720), play="mod_assets/source/videosos/mr.webm")
    image ts_menu_vid_sunset = Movie(fps=24, size = (1280, 720), play="mod_assets/source/videosos/mn.webm")
