# ТУТ ПРОИСХОДИТ СТАРТ ИГРЫ БЛЯ
label start:

    show layer screens at ts_null_transform

    python: #ГОПАЕМ ВРЕМЯ ИЗ СИСТЕМЫ
        from time import localtime, strftime
        t = strftime("%H:%M:%S", localtime())
        hour, minutes, sec = t.split(":")
        hour = int(hour)

    if persistent.carter3menu == True: #МЕНЮШКА КАРТЕРА 3
        if hour in [20,21,22,23,24,0,1,2,3,4,5,6]: #НОЧЬ
            play sound br_glitch
            show ts_menu_move_anim as bg1 at Glitch(_fps=160, glitch_strength=1)
            pause 0.6
            stop sound
            hide ts_menu_move_anim as bg1 at Glitch(_fps=160, glitch_strength=1)
        elif True: #ДЕНЬ
            play sound br_glitch
            show ts_menu_move_anim_three as bg1 at Glitch(_fps=160, glitch_strength=1)
            pause 0.6
            stop sound
            hide ts_menu_move_anim_three as bg1 at Glitch(_fps=160, glitch_strength=1)

    elif persistent.carter2menu == True: #МЕНЮШКА КАРТЕРА 2
        if hour in [20,21,22,23,24,0,1,2,3,4,5,6]: #НОЧЬ
            play sound br_glitch
            show ts_menu_art_carter2_night as bg1 at Glitch(_fps=160, glitch_strength=1)
            pause 0.6
            stop sound
            hide ts_menu_art_carter2_night as bg1 at Glitch(_fps=160, glitch_strength=1)
        elif True: #ДЕНЬ
            play sound br_glitch
            show ts_menu_art3_night as bg1 at Glitch(_fps=160, glitch_strength=1)
            pause 0.6
            stop sound
            hide ts_menu_art3_night as bg1 at Glitch(_fps=160, glitch_strength=1)

    else: #МЕНЮШКА КАРТЕРА 1
        if hour in [20,21,22,23,24,0,1,2,3,4,5,6]: #НОЧЬ
            play sound br_glitch
            show ts_menu_vid_night as bg1 at Glitch(_fps=160, glitch_strength=1)
            pause 0.6
            stop sound
            hide ts_menu_vid_night as bg1 at Glitch(_fps=160, glitch_strength=1)
        elif True: #ДЕНЬ
            play sound br_glitch
            show ts_menu_vid as bg1 at Glitch(_fps=160, glitch_strength=1)
            pause 0.6
            stop sound
            hide ts_menu_vid as bg1 at Glitch(_fps=160, glitch_strength=1)

    stop sound fadeout 2
    stop music fadeout 2
    scene black with dissolve
    pause 0.5
    if persistent.zastavka_skip is True:
        jump ts_start
    else:
        play music ts_wnuk fadein 2
        scene ts_razrab_menu
        show zatemnenie_light
        with dissolve2
        show screen ts_start_shit_blya
        $ renpy.pause(3, hard=True)
        hide screen ts_start_shit_blya with dspr
        show screen ts_cens_changer
        $ renpy.pause(hard=True)

label ts_intro_settings1:
    hide screen ts_cens_changer with dspr
    show screen ts_widget_changer
    $ renpy.pause(hard=True)

label ts_intro_settings2:
    hide screen ts_widget_changer with dspr
    pause 1
    show layer screens at ts_showscreens
    brg "Тебя устраивает такой размер шрифта?{w} Или же..."
    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"
    show layer screens at ts_null_transform
    show screen ts_font_changer
    $ renpy.pause(hard=True)

label ts_intro_settings3:
    hide screen ts_font_changer with dspr
    show layer screens at ts_showscreens
    brg "А теперь?{w} Или ещё разок поменяем?"
    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"
    show layer screens at ts_showscreens
    menu:
        "Поменяем":
            show layer screens at ts_null_transform
            show screen ts_font_changer
            $ renpy.pause(hard=True)
        "Оставь этот":
            show layer screens at ts_showscreens
            brg "Хорошо."
            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"
            show layer screens at ts_null_transform
            jump ts_intro_settings4

label ts_intro_settings4:
    show screen ts_control_help_suka
    $ renpy.pause(hard=True)
    hide screen ts_control_help_suka with dspr
    pause 1
    show screen ts_set_end_shit_blya
    $ renpy.pause(3, hard=True)
    stop music fadeout 3
    hide screen ts_set_end_shit_blya with dspr
    pause 1
    $ persistent.zastavka_skip = True
    jump ts_start