screen sr_start_shit_blya: #ПОЯСНЕНИЕ ХУЙНИ ТЕКСТ
    text "{size=+15}{font=[cit_font]}Проведём небольшую{/font}{/size}" yalign 0.475 xalign 0.5
    text "{size=+15}{font=[cit_font]}настройку мода.{/font}{/size}" yalign 0.525 xalign 0.5

screen sr_cens_changer: # АНТИЦЕНЗОР
    modal True tag aw_r2
    text "{size=+15}{font=[cit_font]}Включить антицензор?{/font}{/size}" yalign 0.475 xalign 0.5
    text "{size=+15}{font=[cit_font]}Можно изменить в любой момент игры.{/font}{/size}" yalign 0.525 xalign 0.5
    textbutton ("{size=+15}Отключить{/size}") yalign 0.685 xalign 0.35:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action (SetField(persistent, "cens_mode", False), Jump("sr_intro_settings1"))
    textbutton ("{size=+15}Включить{/size}") yalign 0.685 xalign 0.65:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action (SetField(persistent, "cens_mode", True), Jump("sr_intro_settings1"))

screen sr_font_changer: # РАЗМЕР ШРИФТА
    modal True tag aw_r4
    text "{size=+15}{font=[cit_font]}Увеличить размер шрифта?{/font}{/size}" yalign 0.475 xalign 0.5
    text "{size=+15}{font=[cit_font]}Или - оставить как есть?{/font}{/size}" yalign 0.525 xalign 0.5
    textbutton ("{size=+15}Оставить{/size}") yalign 0.685 xalign 0.35:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action (SetField(persistent, "bazarbig", False), Jump("sr_intro_settings3"))
    textbutton ("{size=+15}Сделать больше{/size}") yalign 0.685 xalign 0.65:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action (SetField(persistent, "bazarbig", True), Jump("sr_intro_settings3"))

screen sr_set_end_shit_blya: #ПОЯСНЕНИЕ ХУЙНИ ТЕКСТ
    text "{size=+15}{font=[cit_font]}Настройка завершена.{/font}{/size}" yalign 0.475 xalign 0.5
    text "{size=+15}{font=[cit_font]}Переходим к истории.{/font}{/size}" yalign 0.525 xalign 0.5

label start: # ТУТ НАЧИНАЕТСЯ ПИЗДЕЦ
    play sound aw_knife_slash_1
    python: #ГОПАЕМ ВРЕМЯ ИЗ СИСТЕМЫ
        from time import localtime, strftime
        t = strftime("%H:%M:%S", localtime())
        hour, min, sec = t.split(":")
        hour = int(hour)
    if persistent.carter2menu == True: #МЕНЮШКА КАРТЕРА 2
        if hour in [20,21,22,23,24,0,1,2,3,4,5,6]: #НОЧЬ
            scene ts_menu_art_carter2_night
            show ts_rain
            show zatemnenie_light
        elif True: #ДЕНЬ
            scene black
            show ts_menu_move_anim
            show ts_rain
            show zatemnenie_light
    else: #МЕНЮШКА КАРТЕРА 1
        if hour in [20,21,22,23,24,0,1,2,3,4,5,6]: #НОЧЬ
            scene ts_menu_vid_night
            show zatemnenie_light
        elif True: #ДЕНЬ
            scene ts_menu_vid
            show zatemnenie_light
    show altbloodanim
    pause 0.6
    play sound aw_knife_slash_2
    show bloodanim
    pause 0.3
    stop sound fadeout 2
    stop music fadeout 2
    scene black with dissolve2
    pause 0.5
    if persistent.zastavka_skip is True:
        jump ts_start
    else:
        show screen sr_start_shit_blya with awrain
        $ renpy.pause(3, hard=True)
        hide screen sr_start_shit_blya
        show screen sr_cens_changer
        with awrain
        $ renpy.pause(hard=True)

label sr_intro_settings1:
    hide screen sr_cens_changer
    show screen sr_font_changer
    with awrain
    $ renpy.pause(hard=True)

label sr_intro_settings3:
    hide screen sr_font_changer
    show screen sr_set_end_shit_blya
    with awrain
    $ renpy.pause(3, hard=True)
    hide screen sr_set_end_shit_blya with dissolve
    pause 1
    $ persistent.zastavka_skip = True
    jump ts_start