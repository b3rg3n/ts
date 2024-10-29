#TRUE STORY MENU
#by @b3rg3n
#Since 2024
#ВЕСЬ ПИЗДЕЦ, ЧТО ПРОИСХОДИТ НА ЭКРАНЕ - ЗДЕСЯ)

label main_menu:

    $ ts_rpc_main_menu()

    stop sound fadeout 3
    stop music fadeout 3
    window hide

    python: #ГОПАЕМ ВРЕМЯ ИЗ СИСТЕМЫ
        from time import localtime, strftime
        t = strftime("%H:%M:%S", localtime())
        hour, minutes, sec = t.split(":")
        hour = int(hour)

    if persistent.badendmenu == True: #МЕНЮШКА ПОСЛЕ БЕД КОНЦОВКИ (ОДИНАКОВАЯ ДНЁМ И НОЧЬЮ)
        play music ts_killyourself fadein 5
        scene black
        show ts_menu_move_anim_bad_end
        show zatemnenie_light

    elif persistent.goodendmenu == True: #МЕНЮШКА ПОСЛЕ ГУД КОНЦОВКИ (ОДИНАКОВАЯ ДНЁМ И НОЧЬЮ)
        play music good_menu_ost fadein 5
        scene ts_menu_move_anim_good_end at ts_ustal_suka
        show zatemnenie_light
        $ TS.m(VHS())

    elif persistent.peredgoodendmenu == True: #МЕНЮШКА ПЕРЕД ГУД КОНЦОВКОЙ(ОДИНАКОВАЯ ДНЁМ И НОЧЬЮ)
        play music ts_gramatik fadein 5
        scene mon_piano_glitch_anim at ts_ustal_suka
        show zatemnenie_light

    elif persistent.peredbadendmenu == True: #МЕНЮШКА ПЕРЕД БЭД КОНЦОВКОЙ (ОДИНАКОВАЯ ДНЁМ И НОЧЬЮ)
        play music pered_bad_menu_ost fadein 5
        scene mon_piano_another_glitch_anim at ts_ustal_suka
        show zatemnenie_light

    elif persistent.carter3menu == True: #МЕНЮШКА КАРТЕРА 3
        if hour in [20,21,22,23,24,0,1,2,3,4,5,6]: #НОЧЬ
            play music bad_menu_ost fadein 5
            scene black
            show ts_menu_move_anim
            show ts_rain
            show zatemnenie_light
        elif True: #ДЕНЬ
            play music ts_mf_e fadein 5
            scene black
            show ts_menu_move_anim_three
            show zatemnenie_light

    elif persistent.carter2menu == True: #МЕНЮШКА КАРТЕРА 2
        if hour in [20,21,22,23,24,0,1,2,3,4,5,6]: #НОЧЬ
            play music ts_finalded fadein 5
            scene ts_menu_art3_night
            show dust1
            show dust2
            show dust3
            show dust4
            show zatemnenie_light
        elif True: #ДЕНЬ
            play music ts_tir fadein 5
            scene ts_menu_art_carter2_night
            show ts_rain
            show zatemnenie_light

    else: #МЕНЮШКА КАРТЕРА 1
        if hour in [20,21,22,23,24,0,1,2,3,4,5,6]: #НОЧЬ
            play music ts_bm fadein 5
            scene ts_menu_vid_night
            show zatemnenie_light
        elif True: #ДЕНЬ
            play music ts_pd fadein 5
            scene ts_menu_vid
            show zatemnenie_light

    with Fade(1.5, 1, 2)

    call screen main_menu #ВЫЗЫВАЕМ МЕНЮ

label glitch_main_menu_ending:
    $ persistent.badendmenuperedglitch = False
    $ persistent.badendmenuskipglitch = True
    play sound br_glitch
    show ts_menu_move_anim_bad_end as bg1 at Glitch(_fps=160, glitch_strength=1)
    $ TS.p(0.6)
    stop sound
    hide ts_menu_move_anim_bad_end as bg1 at Glitch(_fps=160, glitch_strength=1)
    call screen main_menu #ВЫЗЫВАЕМ МЕНЮ

label splashscreen:

    if not persistent.lan_chosen:

        scene black

        python:
            ui.imagebutton("mod_assets/source/images/gui/lang/russian_ground.png", "mod_assets/source/images/gui/lang/russian_hover.png", clicked = ui.returns("None"), align = (0.5, 0.45))

            ui.imagebutton("mod_assets/source/images/gui/lang/english_ground.png", "mod_assets/source/images/gui/lang/english_hover.png", clicked = ui.returns("english"), align = (0.5, 0.65))

            result = ui.interact()

            if result == "None":
                _preferences.language = None
                translation_new=translation_ru
                renpy.show("ru_hover", [lang_ru_hover])
                renpy.show("en_ground", [lang_en_ground])

            elif result == "english":
                _preferences.language = "english"
                translation_new=translation_en
                translate_names("english")
                #reload_names()
                renpy.show("ru_ground", [lang_ru_ground])
                renpy.show("en_hover", [lang_en_hover])

            persistent.lan_chosen = True

    python: # УСТАНОВКА ГРОМКОСТИ И ПРОВЕРКА НА СПЛЕШ | ОБНОВЛЯЕМ RPC

        if not renpy.android and not config.developer: # ПРОВЕРКА НА НАЛИЧИЕ ИГРОВЫХ АРХИВОВ
            for archive in ['audio','images','fonts']:
                if archive not in config.archives:
                    winerrorsuka()
                    renpy.quit()


        ts_rpc_splash()

        if not persistent.set_volumes:
            
            persistent.set_volumes = True
            
            ts_mm(.45)
            ts_ss(1.0)
            ts_aa(.65)
    if persistent.skip_splash is True:
        scene black
        show ts_anarchy
        with Dissolve(2)
        $ TS.p(0.5)
        hide ts_anarchy
        play sound slender1
        show anarchy_glitch_logo
        $ TS.p(0.8)
        stop sound
        hide anarchy_glitch_logo
        show ts_anarchy
        $ TS.p(0.5)
        scene black
        with Dissolve(2)
        return
    else:
        python:
            try:
                rpc.connect() # ПОДКЛЮЧЕНИЕ К ДС
            except DiscordNotFound:
                pass
            except ConnectionRefusedError:
                pass
            ts_rpc_main_menu()
        $ persistent.rpc_mode = True
        scene black
        show ts_anarchy
        with Dissolve(2)
        $ TS.p(0.5)
        hide ts_anarchy
        play sound slender1
        show anarchy_glitch_logo
        $ TS.p(0.8)
        stop sound
        hide anarchy_glitch_logo
        show ts_anarchy
        $ TS.p(0.5)
        scene black
        with Dissolve(2)
        jump spashcreen1

label spashcreen1:
    $ TS.p(1)
    play music ts_mosh fadein 2
    $ TS.p(1.5)
    scene ts_menu_vid_sunset
    show zatemnenie
    with dissolve4
    $ TS.p(1)
    show screen bergenchik_intro_ebat0
    $ TS.p(2)
    show screen bergenchik_intro_ebat1
    $ TS.p(2)
    show screen bergenchik_intro_ebat2
    $ TS.p(2)
    show screen bergenchik_intro_ebat3
    $ TS.p(2)
    show screen bergenchik_intro_ebat4
    $ TS.p(2)
    call screen skitsoglasenblya
    return

label splashscreen2:
    hide screen bergenchik_intro_ebat4
    hide screen bergenchik_intro_ebat3
    hide screen bergenchik_intro_ebat2
    hide screen bergenchik_intro_ebat1
    hide screen bergenchik_intro_ebat0
    show screen bergenchik_intro_ebat5
    $ TS.p(4)
    stop music fadeout 6
    hide screen bergenchik_intro_ebat5
    scene black
    with dissolve4
    $ TS.p(1)
    $ persistent.skip_splash = True
    return

label after_load: # ВОСКРЕШЕНИЕ RPC ПРИ ЗАГРУЗКЕ
    if persistent.rpclabel == "0":
        $ ts_rpc_carter0()
    elif persistent.rpclabel == "1":
        $ ts_rpc_carter1()
    elif persistent.rpclabel == "2":
        $ ts_rpc_carter2()
    elif persistent.rpclabel == "3":
        $ ts_rpc_carter3()
    elif persistent.rpclabel == "4":
        $ ts_rpc_carter4()
    elif persistent.rpclabel == "5":
        $ ts_rpc_carter5()
    elif persistent.rpclabel == "6":
        $ ts_rpc_carter6()
    elif persistent.rpclabel == "7":
        $ ts_rpc_carter7()
    elif persistent.rpclabel == "8":
        $ ts_rpc_carter8()
    elif persistent.rpclabel == "9":
        $ ts_rpc_carter9()
    elif persistent.rpclabel == "10":
        $ ts_rpc_carter10()
    elif persistent.rpclabel == "11":
        $ ts_rpc_carter11()
    elif persistent.rpclabel == "12":
        $ ts_rpc_carter12()
    elif persistent.rpclabel == "999":
        $ ts_rpc_credits()


screen skitsoglasenblya:

    modal True tag aw_r1
    textbutton translation_new["ts_splash_set14"] style "log_button" text_style "splash_button_link" yalign 0.785 xalign 0.35 at ts_preferences_anim:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action Quit(confirm=False)
    textbutton translation_new["ts_splash_set15"] style "log_button" text_style "splash_button_link" yalign 0.785 xalign 0.65 at ts_preferences_anim:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action Jump("splashscreen2")

screen bergenchik_intro_ebat0:
    text translation_new["ts_splash_set1"] style "settings_link" size 35 text_align 0.5 yalign 0.175 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim
    text translation_new["ts_splash_set2"] style "settings_link" size 35 text_align 0.5 yalign 0.225 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim

screen bergenchik_intro_ebat1:
    text translation_new["ts_splash_set3"] style "settings_link" size 35 text_align 0.5 yalign 0.275 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim
    text translation_new["ts_splash_set4"] style "settings_link" size 35 text_align 0.5 yalign 0.325 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim

screen bergenchik_intro_ebat2:
    text translation_new["ts_splash_set5"] style "settings_link" size 35 text_align 0.5 yalign 0.375 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim
    text translation_new["ts_splash_set6"] style "settings_link" size 35 text_align 0.5 yalign 0.425 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim

screen bergenchik_intro_ebat3:
    text translation_new["ts_splash_set7"] style "settings_link" size 35 text_align 0.5 yalign 0.475 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim
    text translation_new["ts_splash_set8"] style "settings_link" size 35 text_align 0.5 yalign 0.525 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim

screen bergenchik_intro_ebat4:
    text translation_new["ts_splash_set9"] style "settings_link" size 35 text_align 0.5 yalign 0.575 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim
    text translation_new["ts_splash_set10"] style "settings_link" size 35 text_align 0.5 yalign 0.625 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim
    text translation_new["ts_splash_set11"] style "settings_link" size 35 text_align 0.5 yalign 0.675 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim

screen bergenchik_intro_ebat5:
    text translation_new["ts_splash_set12"] style "settings_link" size 35 text_align 0.5 yalign 0.475 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim
    text translation_new["ts_splash_set13"] style "settings_link" size 35 text_align 0.5 yalign 0.525 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim
