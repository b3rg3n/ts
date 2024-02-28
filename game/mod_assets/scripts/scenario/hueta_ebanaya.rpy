label ts_start:
###ТУТ ПОКОЯЦЦА ПЕРЕМЕННЫЕ БЛЕАДЬ
    $ unluck = False
    $ unluck2 = False
    $ unluck3 = False
    $ unluck4 = False
    $ unluck4_telek = False
    $ unluck4_reading = False
    $ unluck4_cooking = False


    if persistent.scenario_proshel_blya == True:
        call screen scenario_start_change_chapter with dissolve2
        return
    else:
        jump ts_scenario_0

screen scenario_start_change_chapter:

    modal True tag ts_chng_one
    text "{size=+15}{font=[ts_main_font_hueta]}Начнём сначала? Или выберешь главу?{/font}{/size}" yalign 0.5 xalign 0.5
    textbutton ("{size=+10}Начать сначала{/size}") yalign 0.685 xalign 0.35:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action Jump("ts_scenario_0")

    textbutton ("{size=+10}Выбрать главу{/size}") yalign 0.685 xalign 0.65:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action Jump("ts_chapter_change")

label ts_chapter_change:
    call screen scenario_start_change_chapter1 with dissolve2

screen scenario_start_change_chapter1:

    modal True tag ts_chng_two
    text "{size=+15}{font=[ts_main_font_hueta]}Какую из?{/font}{/size}" yalign 0.3 xalign 0.5

    textbutton ("{size=+10}Пролог{/size}") yalign 0.485 xalign 0.5:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action Jump("ts_scenario_0")

    textbutton ("{size=+10}Первая{/size}") yalign 0.685 xalign 0.2:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action Jump("ts_scenario_1")

    textbutton ("{size=+10}Вторая{/size}") yalign 0.685 xalign 0.4:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action Jump("ts_scenario_2")

    textbutton ("{size=+10}Третья{/size}") yalign 0.685 xalign 0.6:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action Jump("ts_chapter_three_changes")

    textbutton ("{size=+10}Четвёртая{/size}") yalign 0.685 xalign 0.8:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action Jump("ts_chapter_four_changes")

    textbutton ("{size=+10}Пятая{/size}") yalign 0.885 xalign 0.5:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action Jump("ts_chapter_five_changes")

label ts_chapter_three_changes: # ВЫБОРЫ ПЕРЕД ТРЕТЬЕЙ ГЛАВОЙ
    show screen scenario_start_change_chapter_one with dissolve2
    pause 1
    hide screen scenario_start_change_chapter_one with dissolve2
    pause 2

    play sound fb
    scene ts_corridor
    show zatemnenie
    with flash

    menu:
        "Посмотреть в других классах":
            $ unluck = True
        "Идти вперёд":
            pass

    window hide
    play sound fb
    scene black
    with flash
    pause 2
    
    show screen scenario_start_change_chapter_one1 with dissolve2
    pause 1
    hide screen scenario_start_change_chapter_one1 with dissolve2
    pause 2

    jump ts_scenario_3

label ts_chapter_four_changes: # ВЫБОРЫ ПЕРЕД ЧЕТВЁРТОЙ ГЛАВОЙ
    show screen scenario_start_change_chapter_one with dissolve2
    pause 1
    hide screen scenario_start_change_chapter_one with dissolve2
    pause 2

    play sound fb
    scene ts_corridor
    show zatemnenie
    with flash

    menu:
        "Посмотреть в других классах":
            $ unluck = True
        "Идти вперёд":
            pass

    play sound fb
    scene ts_school_bathroom
    show zatemnenie
    with flash

    menu:
        "Искать дальше":
            $ unluck2 = True
        "Успокоиться и вернуться":
            pass

    play sound fb
    scene ts_kitchen
    show zatemnenie
    with flash

    menu:
        "Пожарить":
            $ unluck3 = True
        "Сварить":
            pass

    window hide
    play sound fb
    scene black
    with flash
    pause 2
    
    show screen scenario_start_change_chapter_one1 with dissolve2
    pause 1
    hide screen scenario_start_change_chapter_one1 with dissolve2
    pause 2

    jump ts_scenario_4

label ts_chapter_five_changes: # ВЫБОРЫ ПЕРЕД ПЯТОЙ ГЛАВОЙ
    show screen scenario_start_change_chapter_one with dissolve2
    pause 1
    hide screen scenario_start_change_chapter_one with dissolve2
    pause 2

    play sound fb
    scene ts_corridor
    show zatemnenie
    with flash

    menu:
        "Посмотреть в других классах":
            $ unluck = True
        "Идти вперёд":
            pass

    play sound fb
    scene ts_school_bathroom
    show zatemnenie
    with flash

    menu:
        "Искать дальше":
            $ unluck2 = True
        "Успокоиться и вернуться":
            pass

    play sound fb
    scene ts_kitchen
    show zatemnenie
    with flash

    menu:
        "Пожарить":
            $ unluck3 = True
        "Сварить":
            pass

    play sound fb
    scene ts_kitchen
    show zatemnenie
    with flash

    menu:
        "Выйти прямо сейчас":
            pass
        "Ещё немного посидеть":
            $ unluck4 = True
            menu:
                "Посмотреть телевизор":
                    $ unluck4_telek = True
                "Почитать":
                    $ unluck4_reading = True
                "Покашеварить":
                    $ unluck4_cooking = True

    window hide
    play sound fb
    scene black
    with flash
    pause 2
    
    show screen scenario_start_change_chapter_one1 with dissolve2
    pause 1
    hide screen scenario_start_change_chapter_one1 with dissolve2
    pause 2

    jump ts_scenario_5

screen scenario_start_change_chapter_one:
    text "{size=+15}{font=[ts_main_font_hueta]}Сделай нужные выборы.{/font}{/size}" yalign 0.5 xalign 0.5

screen scenario_start_change_chapter_one1:
    text "{size=+15}{font=[ts_main_font_hueta]}Направляемся в нужное место.{/font}{/size}" yalign 0.5 xalign 0.5
