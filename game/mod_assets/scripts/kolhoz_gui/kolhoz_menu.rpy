#TRUE STORY MENU
#by @b3rg3n
#Since 2024
#ВЕСЬ ПИЗДЕЦ, ЧТО ПРОИСХОДИТ НА ЭКРАНЕ - ЗДЕСЯ)

label main_menu:

    if renpy.windows:
        python: # ОБНОВЛЯЕМ RPC
            rpc.update(state="Наслаждается",details="Просмотр главного меню",large_image="logogovna",start=time.time())

    stop sound fadeout 3
    stop music fadeout 3
    window hide
    python: #ГОПАЕМ ВРЕМЯ ИЗ СИСТЕМЫ
        from time import localtime, strftime
        t = strftime("%H:%M:%S", localtime())
        hour, min, sec = t.split(":")
        hour = int(hour)
    if persistent.carter2menu == True: #МЕНЮШКА КАРТЕРА 2
        if hour in [20,21,22,23,24,0,1,2,3,4,5,6]: #НОЧЬ
            play music ts_angel fadein 5
            scene ts_menu_art_carter2_night
            show ts_rain
            show zatemnenie_light
        elif True: #ДЕНЬ
            play music ts_ora fadein 5
            scene black
            show ts_menu_move_anim
            show ts_rain
            show zatemnenie_light
    else: #МЕНЮШКА КАРТЕРА 1
        if hour in [20,21,22,23,24,0,1,2,3,4,5,6]: #НОЧЬ
            play music ts_menu_night_ost fadein 5
            scene ts_menu_vid_night
            show zatemnenie_light
        elif True: #ДЕНЬ
            play music ts_wmm fadein 5
            scene ts_menu_vid
            show zatemnenie_light
    with Fade(1.5, 1, 2)
    call screen main_menu #ВЫЗЫВАЕМ МЕНЮ

label splashscreen:

    if renpy.windows:
        python: # ОБНОВЛЯЕМ RPC
            rpc.update(state="Запускается...",details="Просмотр заставки",large_image="logogovna",start=time.time())

    python: # УСТАНОВКА ГРОМКОСТИ И ПРОВЕРКА НА СПЛЕШ
        if not persistent.set_volumes:
            
            persistent.set_volumes = True
            
            _preferences.volumes['music'] = .45
            _preferences.volumes['sfx'] = 1.0
            _preferences.volumes['voice'] = .65
    if persistent.skip_splash is True:
        return
    else:
        jump spashcreen1

label spashcreen1:
    $ renpy.pause(1, hard=True)
    play music mosh1 fadein 2
    $ renpy.pause(1.5, hard=True)
    scene ts_menu_vid_sunset
#    scene ts_intro_3
#    show ts_rain
#    show ts_intro_31
    show zatemnenie
    with dissolve4
    $ renpy.pause(1, hard=True)
    show screen bergenchik_intro_ebat0 with awrain
    $ renpy.pause(4, hard=True)
    hide screen bergenchik_intro_ebat0
    show screen bergenchik_intro_ebat1
    with awrain
    $ renpy.pause(4, hard=True)
    hide screen bergenchik_intro_ebat1
    show screen bergenchik_intro_ebat2
    with awrain2
    $ renpy.pause(4, hard=True)
    hide screen bergenchik_intro_ebat2
    show screen bergenchik_intro_ebat3
    with awrain2
    $ renpy.pause(4, hard=True)
    hide screen bergenchik_intro_ebat3
    show screen bergenchik_intro_ebat4
    with awrain2
    $ renpy.pause(4, hard=True)
    hide screen bergenchik_intro_ebat4
    show screen bergenchik_intro_ebat5
    with awrain2
    call screen skitsoglasenblya with dissolve2
    return

label splashscreen2:
    hide screen bergenchik_intro_ebat5
    show screen bergenchik_intro_ebat6
    with awrain2
    $ renpy.pause(4, hard=True)
    stop music fadeout 6
    hide screen bergenchik_intro_ebat6
    scene black
    with dissolve4
    $ renpy.pause(1, hard=True)
    $ persistent.skip_splash = True
    return

screen ts_logo_shit:
    text "{size=+100}{font=[ts_font]}True Story{/font}{/size}" yalign 0.5 xalign 0.5 xpos 640 ypos 60 at chapter_anim

screen skitsoglasenblya:

    modal True tag aw_r1
    textbutton ("{size=+10}Выход{/size}") yalign 0.685 xalign 0.35:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action Quit(confirm=not main_menu)
    textbutton ("{size=+10}Продолжить{/size}") yalign 0.685 xalign 0.65:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action Jump("splashscreen2")

screen bergenchik_intro_ebat0:
    text "{size=+10}{font=[cit_font]}Запрещено для несовершеннолетних и{/font}{/size}" yalign 0.475 xalign 0.5
    text "{size=+10}{font=[cit_font]}для слишком впечатлительных особ.{/font}{/size}" yalign 0.525 xalign 0.5

screen bergenchik_intro_ebat1:
    text "{size=+10}{font=[cit_font]}Мод содержит в себе сцены насилия, употребления наркотиков, табака,{/font}{/size}" yalign 0.475 xalign 0.5
    text "{size=+10}{font=[cit_font]}алокголя, и прочие сцены сексуального характера.{/font}{/size}" yalign 0.525 xalign 0.5

screen bergenchik_intro_ebat2:
    text "{size=+10}{font=[cit_font]}Все подозрения на пропаганду идеологии, сектанства -{/font}{/size}" yalign 0.45 xalign 0.5
    text "{size=+10}{font=[cit_font]}являются лишь вашими домыслами. Авторы не занимаются{/font}{/size}" yalign 0.5 xalign 0.5
    text "{size=+10}{font=[cit_font]}пропагандой всего того, что вы решили <<додумать>>.{/font}{/size}" yalign 0.55 xalign 0.5

screen bergenchik_intro_ebat3:
    text "{size=+10}{font=[cit_font]}Яркие вспышки света и мелькающие изображения могут навредить{/font}{/size}" yalign 0.475 xalign 0.5
    text "{size=+10}{font=[cit_font]}людям с высокой светочувствительностью и страдающим эпилепсией.{/font}{/size}" yalign 0.525 xalign 0.5

screen bergenchik_intro_ebat4:
    text "{size=+10}{font=[cit_font]}Мод никак не связан с Team Salvato.{/font}{/size}" yalign 0.475 xalign 0.5
    text "{size=+10}{font=[cit_font]}Оригинальные файлы лежат на ddlc.moe{/font}{/size}" yalign 0.525 xalign 0.5

screen bergenchik_intro_ebat5:
    text "{size=+10}{font=[cit_font]}Ты всё ещё хочешь в это играть?{/font}{/size}" yalign 0.45 xalign 0.5
    text "{size=+10}{font=[cit_font]}Серьёзно?{/font}{/size}" yalign 0.5 xalign 0.5
    text "{size=+10}{font=[cit_font]}Не боишься <<сильно впечатлиться>>?{/font}{/size}" yalign 0.55 xalign 0.5

screen bergenchik_intro_ebat6:
    text "{size=+10}{font=[cit_font]}И не говори потом,{/font}{/size}" yalign 0.475 xalign 0.5
    text "{size=+10}{font=[cit_font]}что я тебя не предупреждала.{/font}{/size}" yalign 0.525 xalign 0.5
