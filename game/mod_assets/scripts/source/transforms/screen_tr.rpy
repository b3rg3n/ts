# TRUE STORY SCREEN TRANSFORMS
# by @b3rg3n & @superrage
# Since 2024

transform ts_hidescreens_fast:
    #xpos 0.0 ypos 0.0 alpha 1.0 subpixel True
    #ease 0.1 xpos 1.0 ypos 0.5 alpha 0.0
    xpos 0.0 ypos 0.0 alpha 1.0 subpixel True
    ease 0.1 xpos 0.0 ypos 0.2 alpha 0.0

transform ts_showscreens_fast:
    #xpos -1.0 ypos 0.5 alpha 0.0 subpixel True
    #ease 0.1 xpos 0.0 ypos 0.0 alpha 1.0
    ypos 0.2 alpha 0.0 subpixel True
    ease 0.1 ypos 0.0 alpha 1.0

transform ts_hidescreens:
    #xpos 0.0 ypos 0.0 alpha 1.0 subpixel True
    #ease 1.0 xpos 1.0 ypos 0.5 alpha 0.0
    xpos 0.0 ypos 0.0 alpha 1.0 subpixel True
    ease 1.0 xpos 0.0 ypos 0.2 alpha 0.0

transform ts_showscreens:
    #xpos -1.0 ypos 0.5 alpha 0.0 subpixel True
    #ease 1.0 xpos 0.0 ypos 0.0 alpha 1.0
    ypos 0.2 alpha 0.0 subpixel True
    ease 1.0 ypos 0.0 alpha 1.0

transform ts_showscreens_nvl:
    ypos 0.2 alpha 0.0 subpixel True
    ease 1.0 ypos 0.0 alpha 1.0

transform ts_hidescreens_nvl:
    xpos 0.0 ypos 0.0 alpha 1.0 subpixel True
    ease 1.0 xpos 0.0 ypos 0.2 alpha 0.0

transform ts_hide_credits_videosos:
    xpos 0.2 ypos 0.4 alpha 1.0 subpixel True
    ease 1.0 xpos 0.2 ypos 0.2 alpha 0.0

transform ts_show_credits_videosos:
    xpos 0.2 ypos 0.2 alpha 0.0 subpixel True
    ease 1.0 xpos 0.2 ypos 0.4 alpha 1.0

transform ts_show_credits_videosos_fedya:
    xpos 0.125 ypos 0.01 alpha 0.0 subpixel True
    ease 1.0 xpos 0.125 ypos 0.2 alpha 1.0

transform ts_show_credits_videosos_cg:
    xpos 0.8 ypos 0.01 alpha 0.0 subpixel True
    ease 1.0 xpos 0.8 ypos 0.2 alpha 1.0

transform ts_hide_credits_videosos_fedya:
    xpos 0.125 ypos 0.2 alpha 1.0 subpixel True
    ease 1.0 xpos 0.125 ypos 0.01 alpha 0.0

transform ts_hide_credits_videosos_cg:
    xpos 0.8 ypos 0.2 alpha 1.0 subpixel True
    ease 1.0 xpos 0.8 ypos 0.01 alpha 0.0

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

transform ts_shake2(t1=ts_null_transform, t2=ts_null_transform, t3=ts_null_transform, t4=ts_null_transform, t5=ts_null_transform, t6=ts_null_transform):
    shader "MakeVisualNovels.AnimatedAberration"
    u_aberrationAmount(25.0)
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

transform ts_preferences_anim: # АНИМАЦИЯ МЕНЮ НАСТРОЕК
    zoom 0.4 alpha 0
    ease 0.5 zoom 1.0 alpha 1
    on hover:
        easein 0.1 yoffset -2
    on idle:
        easein 0.1 yoffset 2

transform ts_preferences_anim_lite: # АНИМАЦИЯ МЕНЮ НАСТРОЕК БЕЗ СПАВНА ИЗ ВОЗДУХА
    on hover:
        easein 0.1 yoffset -2
    on idle:
        easein 0.1 yoffset 2