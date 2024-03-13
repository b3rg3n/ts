# TRUE STORY ANIMATIONS
# by @b3rg3n
# Since 2024

init:
###АНИМАЦИЯ КОШМАРА МОНИКИ В КОНЦЕ 4 ГЛАВЫ 1 АКТА НАХ
    image vse_pizda_monike:
        get_image("cg/brg_kolhoz_blya/s1.png") with poplil_pacan1
        pause 5
        get_image("cg/brg_kolhoz_blya/1a.webp") with poplil_pacan1
        pause 5
        get_image("cg/brg_kolhoz_blya/n_cg2_bg.webp") with poplil_pacan1
        pause 5
        get_image("cg/brg_kolhoz_blya/monika_scare.webp") with poplil_pacan1
        pause 5
        get_image("cg/brg_kolhoz_blya/s2.png") with poplil_pacan1
        pause 5
        get_image("cg/brg_kolhoz_blya/3b.webp") with poplil_pacan1
        pause 5
        repeat

###АНИМАЦИЯ ПИЗДЕЦА В БЛЕКАУТЕ
    image anim_exhausted:
        get_image("anim/blackout/blackout_exh2.webp")
        0.03 # Задержка
        get_image("anim/blackout/blackout_exh3.webp")
        0.03 # Задержка
        get_image("anim/blackout/blackout_exh2.webp")
        0.03 # Задержка
        get_image("anim/blackout/blackout_exh3.webp")
        0.03 # Задержка
        get_image("anim/blackout/blackout_exh2.webp")
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
    image ts_menu_move_anim_three:
        contains:
            get_image("intro/menu/ts_menu_art3.webp")
            zoom 1.0 xalign 0.0 yalign 0.6 alpha 0.0
            parallel:
                ease 0.2 alpha 1.0
            parallel:
                linear 15.0 xalign 1.0 yalign 0.4
            get_image("intro/menu/ts_menu_art3.webp")
            zoom 1.0 xalign 1.0 yalign 0.4 alpha 0.0
            parallel:
                ease 0.2 alpha 1.0
            parallel:
                linear 15.0 xalign 0.0 yalign 0.6
            repeat
        contains:
            parallel:
                choice:
                    get_image("anim/mb/aw_o_1.webp")
                choice:
                    get_image("anim/mb/aw_o_2.webp")
                choice:
                    get_image("anim/mb/aw_o_3.webp")
                choice:
                    get_image("anim/mb/aw_o_4.webp")
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
            get_image("intro/menu/menu_art1.webp") #with Fade(1.5, 1, 2)
            zoom 1.0 xalign 0.0 yalign 0.6 alpha 0.0
            parallel:
                ease 0.2 alpha 1.0
            parallel:
                linear 15.0 xalign 1.0 yalign 0.4
            get_image("intro/menu/menu_art2.webp") #with Fade(1.5, 1, 2)
            zoom 1.0 xalign 0.0 yalign 0.6 alpha 0.0
            parallel:
                ease 0.2 alpha 1.0
            parallel:
                linear 15.0 xalign 1.0 yalign 0.4
            get_image("intro/menu/menu_art3.webp") #with Fade(1.5, 1, 2)
            zoom 1.0 xalign 0.0 yalign 0.6 alpha 0.0
            parallel:
                ease 0.2 alpha 1.0
            parallel:
                linear 15.0 xalign 1.0 yalign 0.4
            repeat
        contains:
            parallel:
                choice:
                    get_image("anim/mb/aw_o_1.webp")
                choice:
                    get_image("anim/mb/aw_o_2.webp")
                choice:
                    get_image("anim/mb/aw_o_3.webp")
                choice:
                    get_image("anim/mb/aw_o_4.webp")
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
                    get_image("anim/mb/aw_o_1.webp")
                choice:
                    get_image("anim/mb/aw_o_2.webp")
                choice:
                    get_image("anim/mb/aw_o_3.webp")
                choice:
                    get_image("anim/mb/aw_o_4.webp")
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
                    get_image("anim/mb/aw_o_1.webp")
                choice:
                    get_image("anim/mb/aw_o_2.webp")
                choice:
                    get_image("anim/mb/aw_o_3.webp")
                choice:
                    get_image("anim/mb/aw_o_4.webp")
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
                    get_image("anim/mb/aw_o_1.webp")
                choice:
                    get_image("anim/mb/aw_o_2.webp")
                choice:
                    get_image("anim/mb/aw_o_3.webp")
                choice:
                    get_image("anim/mb/aw_o_4.webp")
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
                    get_image("anim/mb/aw_o_1.webp")
                choice:
                    get_image("anim/mb/aw_o_2.webp")
                choice:
                    get_image("anim/mb/aw_o_3.webp")
                choice:
                    get_image("anim/mb/aw_o_4.webp")
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
        get_image("anim/noise/noise1.webp")
        pause 0.1
        get_image("anim/noise/noise2.webp")
        pause 0.1
        get_image("anim/noise/noise3.webp")
        pause 0.1
        get_image("anim/noise/noise4.webp")
        pause 0.1
        xzoom -1
        get_image("anim/noise/noise1.webp")
        pause 0.1
        get_image("anim/noise/noise2.webp")
        pause 0.1
        get_image("anim/noise/noise3.webp")
        pause 0.1
        get_image("anim/noise/noise4.webp")
        pause 0.1
        yzoom -1
        get_image("anim/noise/noise1.webp")
        pause 0.1
        get_image("anim/noise/noise2.webp")
        pause 0.1
        get_image("anim/noise/noise3.webp")
        pause 0.1
        get_image("anim/noise/noise4.webp")
        pause 0.1
        xzoom 1
        get_image("anim/noise/noise1.webp")
        pause 0.1
        get_image("anim/noise/noise2.webp")
        pause 0.1
        get_image("anim/noise/noise3.webp")
        pause 0.1
        get_image("anim/noise/noise4.webp")
        pause 0.1
        yzoom 1
        repeat

###ЭФФЕКТ ЗЕНЕК
    image unblink:
        contains:
            get_image("anim/zenki/blink_up.webp")
            xalign 0 yalign 0
            ease 1.5 pos (0,-1080)
        contains:
            get_image("anim/zenki/blink_down.webp")
            xalign 0 yalign 0
            ease 1.5 pos (0,1080)

    image blink:
        contains:
            get_image("anim/zenki/blink_up.webp")
            pos (0,-1080)
            ease 1.5 xalign 0 yalign 0
        contains:
            get_image("anim/zenki/blink_down.webp")
            pos (0,1080)
            ease 1.5 xalign 0 yalign 0

###ОВЕРЛЕЙ СТАРОЙ ПЛЁНКИ
    image overlay aw_memory_back_1:
        contains:
            parallel:
                choice:
                    get_image("anim/mb/aw_o_1.webp")
                choice:
                    get_image("anim/mb/aw_o_2.webp")
                choice:
                    get_image("anim/mb/aw_o_3.webp")
                choice:
                    get_image("anim/mb/aw_o_4.webp")
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
                    get_image("anim/mb/a_1.webp")
                choice:
                    get_image("anim/mb/a_2.webp")
                choice:
                    get_image("anim/mb/a_3.webp")
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
            get_image("anim/rain.webp")
            xpos 0.5 ypos -1.0
        contains:
            get_image("anim/rain.webp")
            xpos -0.5 ypos -1.0
        contains:
            get_image("anim/rain.webp")
            xpos 0.5 ypos 0.0
        contains:
            get_image("anim/rain.webp")
            xpos -0.5 ypos 0.0
        contains:
            get_image("anim/rain.webp")
            xpos 0.5 ypos 1.0
        contains:
            get_image("anim/rain.webp")
            xpos -0.5 ypos 1.0
        contains:
            get_image("anim/rain.webp")
            xpos 0.5 ypos 2.0
        contains:
            get_image("anim/rain.webp")
            xpos -0.5 ypos 2.0
        block:
            yanchor 1.0
            linear 0.3 yanchor 0.0
            repeat

###ЛЕПЕСТКИ

    image lepestki:
        choice:
            get_image("anim/particles/lep/lep_1.webp")
        choice:
            get_image("anim/particles/lep/lep_2.webp")
        choice:
            get_image("anim/particles/lep/lep_3.webp")
        choice:
            get_image("anim/particles/lep/lep_4.webp")
        choice:
            get_image("anim/particles/lep/lep_5.webp")
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

###ПЫЛЬ ИЗ ДОКИ
    image dust1:
        get_image("anim/particles/dust/dust1.webp")
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
        get_image("anim/particles/dust/dust2.webp")
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
        get_image("anim/particles/dust/dust3.webp")
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
        get_image("anim/particles/dust/dust4.webp")
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

