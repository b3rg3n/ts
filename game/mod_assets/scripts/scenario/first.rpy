# ТУТ ПРОИСХОДИТ СТАРТ ИГРЫ БЛЯ

screen ts_start_shit_blya: #ПОЯСНЕНИЕ ХУЙНИ ТЕКСТ
    text "{size=+15}{font=[cit_font]}Проведём небольшую{/font}{/size}" yalign 0.475 xalign 0.5
    text "{size=+15}{font=[cit_font]}настройку мода.{/font}{/size}" yalign 0.525 xalign 0.5

screen ts_cens_changer: # АНТИЦЕНЗОР
    modal True tag aw_r2
    text "{size=+15}{font=[cit_font]}Убрать цензуру?{/font}{/size}" yalign 0.430 xalign 0.5
    text "{size=+15}{font=[cit_font]}Если включить - в игре будет{/font}{/size}" yalign 0.480 xalign 0.5
    text "{size=+15}{font=[cit_font]}присутствовать нецензурная лексика.{/font}{/size}" yalign 0.530 xalign 0.5
    text "{size=+15}{font=[cit_font]}Можно изменить в любой момент игры.{/font}{/size}" yalign 0.580 xalign 0.5
    textbutton ("{size=+15}Отключить{/size}") yalign 0.685 xalign 0.35:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action (SetField(persistent, "cens_mode", False), Jump("ts_intro_settings1"))
    textbutton ("{size=+15}Включить{/size}") yalign 0.685 xalign 0.65:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action (SetField(persistent, "cens_mode", True), Jump("ts_intro_settings1"))

screen ts_widget_changer: # ВИДЖЕТ ТРЕКОВ БЛЯ
    modal True tag aw_r2
    text "{size=+15}{font=[cit_font]}Включить вывод названий играющих треков?{/font}{/size}" yalign 0.430 xalign 0.5
    text "{size=+15}{font=[cit_font]}Они будут показываться в меню быстрого доступа{/font}{/size}" yalign 0.480 xalign 0.5
    if renpy.android or renpy.ios:
        text "{size=+15}{font=[cit_font]}которое вызывается свайпом вверх.{/font}{/size}" yalign 0.530 xalign 0.5
    else:
        text "{size=+15}{font=[cit_font]}которое вызывается нажатием пкм.{/font}{/size}" yalign 0.530 xalign 0.5
    text "{size=+15}{font=[cit_font]}Можно изменить в любой момент игры.{/font}{/size}" yalign 0.580 xalign 0.5
    textbutton ("{size=+15}Отключить{/size}") yalign 0.685 xalign 0.35:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action (SetField(persistent, "music_widget_ts", False), Jump("ts_intro_settings2"))
    textbutton ("{size=+15}Включить{/size}") yalign 0.685 xalign 0.65:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action (SetField(persistent, "music_widget_ts", True), Jump("ts_intro_settings2"))

screen ts_font_changer: # РАЗМЕР ШРИФТА
    modal True tag aw_r4
    text "{size=+15}{font=[cit_font]}Увеличить размер шрифта?{/font}{/size}" yalign 0.475 xalign 0.5
    text "{size=+15}{font=[cit_font]}Или - оставить стандартный?{/font}{/size}" yalign 0.525 xalign 0.5
    textbutton ("{size=+15}Стандартный{/size}") yalign 0.685 xalign 0.35:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action (SetField(persistent, "bazarbig", False), Jump("ts_intro_settings3"))
    textbutton ("{size=+15}Увеличенный{/size}") yalign 0.685 xalign 0.65:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action (SetField(persistent, "bazarbig", True), Jump("ts_intro_settings3"))

screen ts_set_end_shit_blya: #ПОЯСНЕНИЕ ХУЙНИ ТЕКСТ
    text "{size=+15}{font=[cit_font]}Настройка завершена.{/font}{/size}" yalign 0.475 xalign 0.5
    text "{size=+15}{font=[cit_font]}Переходим к истории.{/font}{/size}" yalign 0.525 xalign 0.5

screen ts_render_changer: # ЗАМЕНА РЕНДЕРА ЁПТЫТЬ
    modal True tag aw_r2

    text "{size=+15}{font=[cit_font]}Выключить режим энергосбережения?{/font}{/size}" yalign 0.175 xalign 0.5
    text "{size=+15}{font=[cit_font]}Возрастает нагрузка на ЦП (+FPS).{/font}{/size}" yalign 0.225 xalign 0.5
    textbutton ("{size=+15}Включить{/size}") yalign 0.285 xalign 0.35:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action (Preference("gl powersave", True), Jump("ts_render_reboot_suka"))
    textbutton ("{size=+15}Отключить{/size}") yalign 0.285 xalign 0.65:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action (Preference("gl powersave", False), Jump("ts_render_reboot_suka"))

    text "{size=+15}{font=[cit_font]}Изменить рендер?{/font}{/size}" yalign 0.375 xalign 0.5
    text "{size=+15}{font=[cit_font]}Работает только на винде.{/font}{/size}" yalign 0.425 xalign 0.5
    textbutton ("{size=+15}Авто{/size}") yalign 0.485 xalign 0.30:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action (_SetRenderer("auto"), Jump("ts_render_reboot_suka"))
    textbutton ("{size=+15}OpenGL{/size}") yalign 0.485 xalign 0.45:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action (_SetRenderer("gl2"), Jump("ts_render_reboot_suka"))
    textbutton ("{size=+15}DirectX 11{/size}") yalign 0.485 xalign 0.65:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action (_SetRenderer("angle2"), Jump("ts_render_reboot_suka"))

    text "{size=+15}{font=[cit_font]}Ограничитель кадров{/font}{/size}" yalign 0.575 xalign 0.5
    text "{size=+15}{font=[cit_font]}Нагрузка на ЦП возрастает конкретно{/font}{/size}" yalign 0.625 xalign 0.5
    textbutton ("{size=+15}Гц Монитора{/size}") yalign 0.685 xalign 0.05:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action (Preference("gl framerate", None), Jump("ts_render_reboot_suka"))
    textbutton ("{size=+15}360 FPS{/size}") yalign 0.685 xalign 0.30:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action (Preference("gl framerate", 360), Jump("ts_render_reboot_suka"))
    textbutton ("{size=+15}144 FPS{/size}") yalign 0.685 xalign 0.45:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action (Preference("gl framerate", 144), Jump("ts_render_reboot_suka"))
    textbutton ("{size=+15}120 FPS{/size}") yalign 0.685 xalign 0.60:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action (Preference("gl framerate", 120), Jump("ts_render_reboot_suka"))
    textbutton ("{size=+15}60 FPS{/size}") yalign 0.685 xalign 0.75:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action (Preference("gl framerate", 60), Jump("ts_render_reboot_suka"))
    textbutton ("{size=+15}30 FPS{/size}") yalign 0.685 xalign 0.90:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action (Preference("gl framerate", 30), Jump("ts_render_reboot_suka"))

    text "{size=+15}{font=[cit_font]}Включить разрыв кадров?{/font}{/size}" yalign 0.775 xalign 0.5
    text "{size=+15}{font=[cit_font]}Пропуск кадров, если ЦП не вывозит.{/font}{/size}" yalign 0.825 xalign 0.5
    textbutton ("{size=+15}Включить{/size}") yalign 0.885 xalign 0.35:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action (Preference("gl tearing", True), Jump("ts_render_reboot_suka"))
    textbutton ("{size=+15}Отключить{/size}") yalign 0.885 xalign 0.65:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action (Preference("gl tearing", False), Jump("ts_render_reboot_suka"))

label ts_render_reboot_suka:
    $ renpy.quit(relaunch=True)

label start: # ТУТ НАЧИНАЕТСЯ ПИЗДЕЦ

    $ TS.Screens(ts_null_transform)

    python: #ГОПАЕМ ВРЕМЯ ИЗ СИСТЕМЫ
        from time import localtime, strftime
        t = strftime("%H:%M:%S", localtime())
        hour, min, sec = t.split(":")
        hour = int(hour)

    if persistent.carter3menu == True: #МЕНЮШКА КАРТЕРА 3
        if hour in [20,21,22,23,24,0,1,2,3,4,5,6]: #НОЧЬ
            play sound br_glitch
            show ts_menu_move_anim as bg1 at br_glitches(_fps=160, glitch_strength=1)
            pause 0.6
            stop sound
            hide ts_menu_move_anim as bg1 at br_glitches(_fps=160, glitch_strength=1)
        elif True: #ДЕНЬ
            play sound br_glitch
            show ts_menu_move_anim_three as bg1 at br_glitches(_fps=160, glitch_strength=1)
            pause 0.6
            stop sound
            hide ts_menu_move_anim_three as bg1 at br_glitches(_fps=160, glitch_strength=1)

    elif persistent.carter2menu == True: #МЕНЮШКА КАРТЕРА 2
        if hour in [20,21,22,23,24,0,1,2,3,4,5,6]: #НОЧЬ
            play sound br_glitch
            show ts_menu_art_carter2_night as bg1 at br_glitches(_fps=160, glitch_strength=1)
            pause 0.6
            stop sound
            hide ts_menu_art_carter2_night as bg1 at br_glitches(_fps=160, glitch_strength=1)
        elif True: #ДЕНЬ
            play sound br_glitch
            show ts_menu_art3_night as bg1 at br_glitches(_fps=160, glitch_strength=1)
            pause 0.6
            stop sound
            hide ts_menu_art3_night as bg1 at br_glitches(_fps=160, glitch_strength=1)

    else: #МЕНЮШКА КАРТЕРА 1
        if hour in [20,21,22,23,24,0,1,2,3,4,5,6]: #НОЧЬ
            play sound br_glitch
            show ts_menu_vid_night as bg1 at br_glitches(_fps=160, glitch_strength=1)
            pause 0.6
            stop sound
            hide ts_menu_vid_night as bg1 at br_glitches(_fps=160, glitch_strength=1)
        elif True: #ДЕНЬ
            play sound br_glitch
            show ts_menu_vid as bg1 at br_glitches(_fps=160, glitch_strength=1)
            pause 0.6
            stop sound
            hide ts_menu_vid as bg1 at br_glitches(_fps=160, glitch_strength=1)

    stop sound fadeout 2
    stop music fadeout 2
    scene black with dissolve
    pause 0.5
    if persistent.zastavka_skip is True:
        jump ts_start
    else:
        play music ts_wnuk fadein 2
        scene ts_razrab_menu
        with dissolve2
        show screen ts_start_shit_blya with awrain
        $ renpy.pause(3, hard=True)
        hide screen ts_start_shit_blya
        show screen ts_cens_changer
        with awrain
        $ renpy.pause(hard=True)

label ts_intro_settings1:
    hide screen ts_cens_changer
    show screen ts_widget_changer
    with awrain
    $ renpy.pause(hard=True)

label ts_intro_settings2:
    hide screen ts_widget_changer with awrain
    pause 1
    $ TS.Screens(ts_showscreens)
    brg "Тебя устраивает такой размер шрифта?{w} Или же..."
    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"
    $ TS.Screens(ts_null_transform)
    show screen ts_font_changer with awrain
    $ renpy.pause(hard=True)

label ts_intro_settings3:
    hide screen ts_font_changer with awrain
    $ TS.Screens(ts_showscreens)
    brg "А теперь?{w} Или ещё разок поменяем?"
    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"
    $ TS.Screens(ts_showscreens)
    menu:
        "Поменяем":
            $ TS.Screens(ts_null_transform)
            show screen ts_font_changer with awrain
            $ renpy.pause(hard=True)
        "Оставь этот":
            $ TS.Screens(ts_showscreens)
            brg "Хорошо."
            $ TS.Screens(ts_hidescreens)
            " {w=1.0}{nw}"
            $ TS.Screens(ts_null_transform)
            jump ts_intro_settings4

label ts_intro_settings4:
    show screen ts_set_end_shit_blya with awrain
    $ renpy.pause(3, hard=True)
    stop music fadeout 3
    hide screen ts_set_end_shit_blya with dissolve
    pause 1
    $ persistent.zastavka_skip = True
    jump ts_start