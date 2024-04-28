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
    $ chess_tutor = False

    $ unluck_ball = 0 # ОБЩИЕ БАЛЛЫ АНЛАКА БЛЯ

    if config.developer: # МЕНЮШКА РАЗРАБОТЧИКА
        scene ts_razrab_menu with dissolve2
        $ TS.Screens(ts_showscreens)
        menu:
            "Выбор главы":
                $ TS.Screens(ts_null_transform)
                call screen scenario_start_change_chapter with dissolve2
                return
            "Тестовый label":
                $ TS.Screens(ts_null_transform)
                jump testing_label_blya
            "Смотреть титры":
                $ TS.Screens(ts_showscreens)
                menu:
                    "good":
                        $ TS.Screens(ts_null_transform)
                        jump good_credits_ts_label
                    "bad":
                        $ TS.Screens(ts_null_transform)
                        jump bad_credits_ts_label
            "Очистить переменные":
                $ persistent.zastavka_skip = False
                $ persistent.firstmenushka = True
                $ persistent.skip_splash = False
                $ persistent.first_poem = False
                $ persistent.scenario_proshel_blya = False
                $ persistent.badendmenuperedglitch = False
                $ persistent.badendmenuskipglitch = False
                $ persistent.carter2menu = False
                $ persistent.carter3menu = False
                $ persistent.badendmenu = False
                $ renpy.full_restart(transition=None, label="splashscreen")
            "Выбрать нужную менюшку":
                menu:
                    "Из первого акта":
                        $ persistent.carter2menu = False
                        $ persistent.carter3menu = False
                        $ persistent.badendmenu = False
                        $ persistent.badendmenuperedglitch = False
                        $ persistent.badendmenuskipglitch = False
                        $ persistent.goodendmenu = False
                        return
                    "Из второго акта":
                        $ persistent.carter2menu = True
                        $ persistent.carter3menu = False
                        $ persistent.badendmenu = False
                        $ persistent.badendmenuperedglitch = False
                        $ persistent.badendmenuskipglitch = False
                        $ persistent.goodendmenu = False
                        return
                    "Из третьего акта":
                        $ persistent.carter2menu = False
                        $ persistent.carter3menu = True
                        $ persistent.badendmenu = False
                        $ persistent.badendmenuperedglitch = False
                        $ persistent.badendmenuskipglitch = False
                        $ persistent.goodendmenu = False
                        return
                    "После плохой концовки":
                        $ persistent.badendmenuperedglitch = True
                        $ persistent.badendmenuskipglitch = False
                        $ persistent.badendmenu = True
                        $ persistent.carter2menu = False
                        $ persistent.carter3menu = False
                        $ persistent.goodendmenu = False
                        menu:
                            "1 фон":
                                $ persistent.badendbg = "1"
                                return
                            "2 фон":
                                $ persistent.badendbg = "2"
                                return
                            "3 фон":
                                $ persistent.badendbg = "0"
                                return
                    "После хорошей концовки":
                        $ persistent.badendmenuperedglitch = False
                        $ persistent.badendmenuskipglitch = False
                        $ persistent.badendmenu = False
                        $ persistent.carter2menu = False
                        $ persistent.carter3menu = False
                        $ persistent.goodendmenu = True
                        return
                    "Вернуться":
                        jump ts_start
            "Заменить рендер":
                show zatemnenie with dspr
                $ TS.Screens(ts_showscreens)
                call screen ts_render_changer
            "Обратно в меню":
                return

    if persistent.scenario_proshel_blya == True: # ПРОВЕРКА НА ПРОЙДЕННУЮ ИГРУ
        call screen scenario_start_change_chapter with dissolve2
        return
    else:
        scene black with dissolve2
        pause 2
        if _preferences.language == "english":
            jump ts_scenario_0_eng
        else:
            jump ts_scenario_0

screen scenario_start_change_chapter: # ВЫБОР ГЛАВЫ НАХ

    modal True tag ts_chng_two
    text "{size=+20}{font=[ts_main_font_hueta]}{color=#FF0000}Начнём сначала? Или выберешь главу?{/color}{/font}{/size}" yalign 0.1 xalign 0.5

    textbutton ("{size=+10}Начать с пролога{/size}") yalign 0.2 xalign 0.5:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action Jump("ts_chapter_prologue_changes")

    text "{size=+20}{font=[ts_main_font_hueta]}{color=#FF0000}Акт первый:{/color}{/font}{/size}" yalign 0.3 xalign 0.1

    textbutton ("{size=+10}Первая глава{/size}") yalign 0.4 xalign 0.1:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action Jump("ts_chapter_one_changes")

    textbutton ("{size=+10}Вторая глава{/size}") yalign 0.5 xalign 0.1:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action Jump("ts_chapter_two_changes")

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

    textbutton ("{size=+10}Вторая глава{/size}") yalign 0.5 xalign 0.5:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action Jump("ts_chapter_six_changes")

    text "{size=+20}{font=[ts_main_font_hueta]}{color=#FF0000}Акт третий:{/color}{/font}{/size}" yalign 0.3 xalign 0.9

label ts_chapter_prologue_changes:
    scene black with dissolve2
    pause 2
    jump ts_scenario_0

label ts_chapter_one_changes:
    scene black with dissolve2
    pause 2
    jump ts_scenario_1

label ts_chapter_two_changes:
    scene black with dissolve2
    pause 2
    jump ts_scenario_2

label ts_chapter_three_changes: # ВЫБОРЫ ПЕРЕД ТРЕТЬЕЙ ГЛАВОЙ
    show screen scenario_start_change_chapter_one with dissolve2
    pause 1
    hide screen scenario_start_change_chapter_one with dissolve2
    pause 2

    scene black with dissolve2
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

    scene black with dissolve2
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

    scene black with dissolve2
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


label ts_chapter_six_changes: # ВЫБОРЫ ПЕРЕД ШЕСТОЙ ГЛАВОЙ
    show screen scenario_start_change_chapter_one with dissolve2
    pause 1
    hide screen scenario_start_change_chapter_one with dissolve2
    pause 2

    scene black with dissolve2
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

    play sound fb
    scene ts_kitchen
    show hiroto 2r at i11
    show zatemnenie
    with flash

    menu:
        "Сказать правду":
            pass
        "Соврать":
            $ unluck5 = True
            $ unluck_ball += 1

    play sound fb
    scene ts_kitchen
    show hiroto 1e at i21
    show monika 1a at i22
    show zatemnenie
    with flash

    menu:
        "Играть в шахматы":
            $ act2_chess = True
            cm "Итак, я повторяю свой вопрос: ты хочешь обучиться игре в шахматы?"
            menu:
                "Да":
                    $ chess_tutor = True
                "Нет":
                    pass
        "Сразу пойти к себе":
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

    jump ts_scenario_6

screen scenario_start_change_chapter_one: # ВАРНИНГ ХУЙНИ
    text "{size=+15}{font=[ts_main_font_hueta]}Сделай нужные выборы.{/font}{/size}" yalign 0.5 xalign 0.5

screen scenario_start_change_chapter_one1: # ВАРНИНГ ХУЙНИ 2
    text "{size=+15}{font=[ts_main_font_hueta]}Направляемся в нужное место.{/font}{/size}" yalign 0.5 xalign 0.5
