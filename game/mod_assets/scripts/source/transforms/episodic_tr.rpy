# TRUE STORY TRANSFORMS
# by @b3rg3n & @superrage
# Since 2024

init:
### АНИМАЦИИ НЕ ДЛЯ СПРАЙТОВ БЛЯ
    transform ts_chess_move_up: # АНИМАЦИИ ДЛЯ ШАХМАТ
        xoffset 400 yoffset 300 alpha 0.0 subpixel True
        ease 0.6 yoffset 50 alpha 1.0

    transform camera_zoom: # ЗУМ
        ease 2.0 pos (-0.3, 0.0) zoom 1.50

    transform camera_zoom1: # ЕЩЁ ЗУМ
        ease 2.0 pos (-0.4, -0.4) zoom 1.90

    transform noise_alpha: # ПРОЗРАЧНОСТЬ
        alpha 0.25

    transform na10: # ЕЩЁ ПРОЗРАЧНОСТЬ
        alpha 0.10

    transform noisefade(t=0): # ПЛАВНОЕ ПОЯВЛЕНИЕ
        alpha 0.0
        t
        linear 5.0 alpha 0.40

    transform br_rotate(l, z, x, y): # ПОВОРОТ ДЛЯ ИКОНКИ ЗАГРУЗКИ
        parallel:
            zoom z xalign x yalign y rotate_pad True rotate 0
            linear l rotate 360
            repeat

    transform ec_tr_choice: # АНИМАЦИЯ МЕНЮ ВЫБОРА
        on hover:
            easein 0.1 yoffset -2
        on idle:
            easein 0.1 yoffset 2

    transform ts_razebal: # ВЛЕТЕЛ С РАЗБЕГУ НАХУЙ
        xalign 0.5 yalign 0.5
        parallel:
            ease 0.25 zoom 1.1
            ease 0.5 zoom 1.0
        parallel:
            ease 0.25 rotate -1.5
            ease 0.25 rotate 1.0
            ease 0.25 rotate 0.0

    transform ts_get_achievement: # АЧИВОЧКА
        pos (0.2, 0.8)
        anchor (0.5, 0.5)
        zoom 0.0
        ease 1.5 zoom 1.05
        ease 0.25 zoom 0.95
        ease 0.25 zoom 1.0
        pause 4.0
        ease 0.5 pos (-0.8, 0.85)
        ease 0.5 pos (-1.0, 0.85) alpha 0.0

    transform ts_running_fast: # БЫСТРЫЙ БЕГ
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

    transform ts_beg: # ПРОСТО БЕГ
        parallel:
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            ease 0.2 zoom 1.04 xpos 0.5 ypos 0.49
        parallel:
            ease 0.2 xpos 0.5 ypos 0.49
            ease 0.2 xpos 0.48 ypos 0.51
            ease 0.2 xpos 0.5 ypos 0.49
            ease 0.2 xpos 0.52 ypos 0.51
            repeat

    transform ts_heartattack(img): # ПЛЫВЁТ КАРТИНКА И НЕБОЛЬШИЕ ФЛЕШБЕКИ НА ФОНЕ С КРАСНЫМ ОВЕРЛЕЕМ
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

    transform ts_alko(img): # ТА ЖЕ ДРОЧЬ, ТОК БЕЗ ОВЕРЛЕЯ
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

    transform chapter_anim: # АНИМАЦИЯ ТЕКСТА НАЗВАНИЯ ГЛАВЫ
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

    python: # ЕГО ДЕФАЙНЫ
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

screen chapter(name): # ЭКРАН ЭТОЙ АНИМАЦИИ
    text name:
        style "chapter_text"
        at chapter_anim

transform lang_ru_ground: # АНИМАЦИЯ ЯЗЫКА ПРИ ПЕРВОМ ЗАПУСКЕ
    align (0.5, 0.45)
    ease 0.5 align (0.2, 0.45)
    linear 1.0 align (1.6, 0.45)

transform lang_ru_hover: # АНИМАЦИЯ ЯЗЫКА ПРИ ПЕРВОМ ЗАПУСКЕ
    align (0.5, 0.45)
    pause 1.5
    ease 1.0 align (0.5, 0.45)
    linear 1.5 zoom 1.5
    pause 1.5

transform lang_en_ground: # АНИМАЦИЯ ЯЗЫКА ПРИ ПЕРВОМ ЗАПУСКЕ
    align (0.5, 0.65)
    ease 0.5 align (0.2, 0.65)
    linear 1.0 align (1.6, 0.65)

transform lang_en_hover: # АНИМАЦИЯ ЯЗЫКА ПРИ ПЕРВОМ ЗАПУСКЕ
    align (0.5, 0.65)
    pause 1.5
    ease 1.0 align (0.5, 0.65)
    linear 1.5 zoom 1.5
    pause 1.5