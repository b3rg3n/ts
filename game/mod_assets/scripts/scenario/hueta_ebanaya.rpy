# ТУТ ЛЕЖИТ ФИЧА СКИПА ТЕКСТА ДО НУЖНОЙ ГЛАВЫ БЛЯ

label ts_start:
###ТУТ ПОКОЯТСЯ ПЕРЕМЕННЫЕ БЛЯТЬ
    $ unluck = False
    $ unluck2 = False
    $ unluck3 = False
    $ unluck4 = False
    $ unluck4_telek = False
    $ unluck4_reading = False
    $ unluck4_cooking = False
    $ act2_chess = False
    $ unluck5 = False

    $ unluck_ball = 0 # ОБЩИЕ БАЛЛЫ АНЛАКА БЛЯ

    if config.developer == True: # МЕНЮШКА РАЗРАБОТЧИКА
        menu:
            "Выбор главы":
                call screen scenario_start_change_chapter with dissolve2
                return
            "Тестовый label":
                jump testing_label_blya
            "Очистить переменные":
                $ persistent.zastavka_skip = False
                $ persistent.firstmenushka = True
                $ persistent.skip_splash = False
                $ persistent.first_poem = False
                $ persistent.scenario_proshel_blya = False
                return
            "Выбрать нужную менюшку":
                menu:
                    "Из первого акта":
                        $ persistent.carter2menu = False
                        $ persistent.carter3menu = False
                        return
                    "Из второго акта":
                        $ persistent.carter2menu = True
                        $ persistent.carter3menu = False
                        return
                    "Из третьего акта":
                        $ persistent.carter2menu = False
                        $ persistent.carter3menu = True
                        return
                    "Вернуться":
                        jump ts_start
            "Обратно в меню":
                return

    if persistent.scenario_proshel_blya == True: # ПРОВЕРКА НА ПРОЙДЕННУЮ ИГРУ
        call screen scenario_start_change_chapter with dissolve2
        return
    else:
        jump ts_scenario_0

screen scenario_start_change_chapter: # ВЫБОР ГЛАВЫ НАХ

    modal True tag ts_chng_two
    text "{size=+20}{font=[ts_main_font_hueta]}{color=#FF0000}Начнём сначала? Или выберешь главу?{/color}{/font}{/size}" yalign 0.1 xalign 0.5

    textbutton ("{size=+10}Начать с пролога{/size}") yalign 0.2 xalign 0.5:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action Jump("ts_scenario_0")

    text "{size=+20}{font=[ts_main_font_hueta]}{color=#FF0000}Акт первый:{/color}{/font}{/size}" yalign 0.3 xalign 0.1

    textbutton ("{size=+10}Первая глава{/size}") yalign 0.4 xalign 0.1:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action Jump("ts_scenario_1")

    textbutton ("{size=+10}Вторая глава{/size}") yalign 0.5 xalign 0.1:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action Jump("ts_scenario_2")

    textbutton ("{size=+10}Третья глава{/size}") yalign 0.6 xalign 0.1:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action Jump("ts_chapter_three_changes")

    textbutton ("{size=+10}Четвёртая глава{/size}") yalign 0.7 xalign 0.1:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action Jump("ts_chapter_four_changes")

    text "{size=+20}{font=[ts_main_font_hueta]}{color=#FF0000}Акт второй:{/color}{/font}{/size}" yalign 0.3 xalign 0.5

    textbutton ("{size=+10}Первая глава{/size}") yalign 0.4 xalign 0.5:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action Jump("ts_chapter_five_changes")

    text "{size=+20}{font=[ts_main_font_hueta]}{color=#FF0000}Акт третий:{/color}{/font}{/size}" yalign 0.3 xalign 0.9

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
            $ unluck_ball += 1
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
            $ unluck_ball += 1
        "Идти вперёд":
            pass

    play sound fb
    scene ts_school_bathroom
    show zatemnenie
    with flash

    menu:
        "Искать дальше":
            $ unluck2 = True
            $ unluck_ball += 1
        "Успокоиться и вернуться":
            pass

    play sound fb
    scene ts_kitchen
    show zatemnenie
    with flash

    menu:
        "Пожарить":
            $ unluck3 = True
            $ unluck_ball += 1
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
            $ unluck_ball += 1
        "Идти вперёд":
            pass

    play sound fb
    scene ts_school_bathroom
    show zatemnenie
    with flash

    menu:
        "Искать дальше":
            $ unluck2 = True
            $ unluck_ball += 1
        "Успокоиться и вернуться":
            pass

    play sound fb
    scene ts_kitchen
    show zatemnenie
    with flash

    menu:
        "Пожарить":
            $ unluck3 = True
            $ unluck_ball += 1
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
            $ unluck_ball += 1
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

screen scenario_start_change_chapter_one: # ВАРНИНГ ХУЙНИ
    text "{size=+15}{font=[ts_main_font_hueta]}Сделай нужные выборы.{/font}{/size}" yalign 0.5 xalign 0.5

screen scenario_start_change_chapter_one1: # ВАРНИНГ ХУЙНИ 2
    text "{size=+15}{font=[ts_main_font_hueta]}Направляемся в нужное место.{/font}{/size}" yalign 0.5 xalign 0.5
