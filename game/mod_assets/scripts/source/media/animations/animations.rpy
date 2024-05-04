# TRUE STORY ANIMATIONS
# by @b3rg3n
# Since 2024

init:
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

    image ts_menu_move_anim_bad_end1:
        contains:
            ts_images + "intro/menu/monikill1.webp" #with Fade(1.5, 1, 2)
            zoom 1.0 xalign 0.0 yalign 0.6 alpha 0.0
            parallel:
                ease 0.2 alpha 1.0
            parallel:
                linear 15.0 xalign 1.0 yalign 0.4
            ts_images + "intro/menu/monikill1.webp"
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

###ЛЕПЕСТКИ

    image lepestki:
        choice:
            ts_anim + "particles/lep/lep_1.webp"
        choice:
            ts_anim + "particles/lep/lep_2.webp"
        choice:
            ts_anim + "particles/lep/lep_3.webp"
        choice:
            ts_anim + "particles/lep/lep_4.webp"
        choice:
            ts_anim + "particles/lep/lep_5.webp"
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

