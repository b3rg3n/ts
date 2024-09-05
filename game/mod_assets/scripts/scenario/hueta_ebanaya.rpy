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
    $ unluck6 = False
    $ unluck7 = False

    $ unluck_ball = 0 # ОБЩИЕ БАЛЛЫ АНЛАКА БЛЯ

    if config.developer: # МЕНЮШКА РАЗРАБОТЧИКА
        scene ts_razrab_menu with dissolve2
        menu:
            "Выбор главы":
                call screen scenario_start_change_chapter with wipeleft
                return
            "Тестовый label":
                jump testing_label_blya
            "Смотреть титры":
                menu:
                    "good":
                        jump good_credits_ts_label
                    "bad":
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
                $ persistent.peredbadendmenu = False
                $ persistent.peredgoodendmenu = False
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
                        $ persistent.peredbadendmenu = False
                        $ persistent.peredgoodendmenu = False
                        return
                    "Из второго акта":
                        $ persistent.carter2menu = True
                        $ persistent.carter3menu = False
                        $ persistent.badendmenu = False
                        $ persistent.badendmenuperedglitch = False
                        $ persistent.badendmenuskipglitch = False
                        $ persistent.goodendmenu = False
                        $ persistent.peredbadendmenu = False
                        $ persistent.peredgoodendmenu = False
                        return
                    "Из третьего акта":
                        $ persistent.carter2menu = False
                        $ persistent.carter3menu = True
                        $ persistent.badendmenu = False
                        $ persistent.badendmenuperedglitch = False
                        $ persistent.badendmenuskipglitch = False
                        $ persistent.goodendmenu = False
                        $ persistent.peredbadendmenu = False
                        $ persistent.peredgoodendmenu = False
                        return
                    "Перед гуд концовкой":
                        $ persistent.carter2menu = False
                        $ persistent.carter3menu = False
                        $ persistent.badendmenu = False
                        $ persistent.badendmenuperedglitch = False
                        $ persistent.badendmenuskipglitch = False
                        $ persistent.goodendmenu = False
                        $ persistent.peredbadendmenu = False
                        $ persistent.peredgoodendmenu = True
                        return
                    "Перед бэд концовкой":
                        $ persistent.carter2menu = False
                        $ persistent.carter3menu = False
                        $ persistent.badendmenu = False
                        $ persistent.badendmenuperedglitch = False
                        $ persistent.badendmenuskipglitch = False
                        $ persistent.goodendmenu = False
                        $ persistent.peredbadendmenu = True
                        $ persistent.peredgoodendmenu = False
                        return
                    "После плохой концовки":
                        $ persistent.badendmenuperedglitch = True
                        $ persistent.badendmenuskipglitch = False
                        $ persistent.badendmenu = True
                        $ persistent.carter2menu = False
                        $ persistent.carter3menu = False
                        $ persistent.goodendmenu = False
                        $ persistent.peredbadendmenu = False
                        $ persistent.peredgoodendmenu = False
                        return
                    "После хорошей концовки":
                        $ persistent.badendmenuperedglitch = False
                        $ persistent.badendmenuskipglitch = False
                        $ persistent.badendmenu = False
                        $ persistent.carter2menu = False
                        $ persistent.carter3menu = False
                        $ persistent.goodendmenu = True
                        $ persistent.peredbadendmenu = False
                        $ persistent.peredgoodendmenu = False
                        return
                    "Вернуться":
                        jump ts_start
            #"Оффнуть печку":
            #    python:
            #        offpc()
            #"Ебануть синий экран":
            #    python:
            #        bsod()
            "Обратно в меню":
                return

    if persistent.scenario_proshel_blya == True: # ПРОВЕРКА НА ПРОЙДЕННУЮ ИГРУ
        call screen scenario_start_change_chapter with wipeleft
        return
    else:
        scene black with dissolve2
        pause 2
        jump ts_scenario_0

screen scenario_start_change_chapter: # ВЫБОР ГЛАВЫ НАХ

    modal True tag ts_chng_two
    if _preferences.language == "english":
        text translation_new["ts_govno_text1"] style "settings_link" size 60 text_align 0.5 yalign 0.1 xalign 0.5 color "#FF0000" antialias True kerning 2 at ts_preferences_anim
    else:
        text translation_new["ts_govno_text1"] style "settings_link" size 75 text_align 0.5 yalign 0.1 xalign 0.5 color "#FF0000" antialias True kerning 2 at ts_preferences_anim

    textbutton translation_new["ts_govno_text2"] style "log_button" text_style "change_chapter_suka" yalign 0.2 xalign 0.5 at ts_preferences_anim:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action Jump("ts_chapter_prologue_changes")

    text translation_new["ts_govno_text3"] style "settings_link" size 75 text_align 0.5 yalign 0.3 xalign 0.1 color "#FF0000" antialias True kerning 2 at ts_preferences_anim

    textbutton translation_new["ts_govno_text4"] style "log_button" text_style "change_chapter_suka" yalign 0.4 xalign 0.1 at ts_preferences_anim:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action Jump("ts_chapter_one_changes")

    textbutton translation_new["ts_govno_text5"] style "log_button" text_style "change_chapter_suka" yalign 0.5 xalign 0.1 at ts_preferences_anim:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action Jump("ts_chapter_two_changes")

    textbutton translation_new["ts_govno_text6"] style "log_button" text_style "change_chapter_suka" yalign 0.6 xalign 0.1 at ts_preferences_anim:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action Jump("ts_chapter_three_changes")

    textbutton translation_new["ts_govno_text7"] style "log_button" text_style "change_chapter_suka" yalign 0.7 xalign 0.1 at ts_preferences_anim:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action Jump("ts_chapter_four_changes")

    text translation_new["ts_govno_text8"] style "settings_link" size 75 text_align 0.5 yalign 0.3 xalign 0.5 color "#FF0000" antialias True kerning 2 at ts_preferences_anim

    textbutton translation_new["ts_govno_text4"] style "log_button" text_style "change_chapter_suka" yalign 0.4 xalign 0.5 at ts_preferences_anim:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action Jump("ts_chapter_five_changes")

    textbutton translation_new["ts_govno_text5"] style "log_button" text_style "change_chapter_suka" yalign 0.5 xalign 0.5 at ts_preferences_anim:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action Jump("ts_chapter_six_changes")

    textbutton translation_new["ts_govno_text6"] style "log_button" text_style "change_chapter_suka" yalign 0.6 xalign 0.5 at ts_preferences_anim:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action Jump("ts_chapter_seven_changes")

    textbutton translation_new["ts_govno_text7"] style "log_button" text_style "change_chapter_suka" yalign 0.7 xalign 0.5 at ts_preferences_anim:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action Jump("ts_chapter_eight_changes")

    text translation_new["ts_govno_text9"] style "settings_link" size 75 text_align 0.5 yalign 0.3 xalign 0.9 color "#FF0000" antialias True kerning 2 at ts_preferences_anim

    textbutton translation_new["ts_govno_text4"] style "log_button" text_style "change_chapter_suka" yalign 0.4 xalign 0.9 at ts_preferences_anim:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action Jump("ts_chapter_nine_changes")

    textbutton translation_new["ts_govno_text5"] style "log_button" text_style "change_chapter_suka" yalign 0.5 xalign 0.9 at ts_preferences_anim:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action Jump("ts_chapter_ten_changes")

    textbutton translation_new["ts_govno_text6"] style "log_button" text_style "change_chapter_suka" yalign 0.6 xalign 0.9 at ts_preferences_anim:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action Jump("ts_chapter_12_changes")

    text translation_new["ts_govno_text228"] style "settings_link" size 75 text_align 0.5 yalign 0.8 xalign 0.5 color "#FF0000" antialias True kerning 2 at ts_preferences_anim

    textbutton translation_new["ts_govno_text229"] style "log_button" text_style "change_chapter_suka" yalign 0.9 xalign 0.25 at ts_preferences_anim:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action Jump("ts_chapter_good_end_changes")

    textbutton translation_new["ts_govno_text230"] style "log_button" text_style "change_chapter_suka" yalign 0.9 xalign 0.75 at ts_preferences_anim:
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        action Jump("ts_chapter_bad_end_changes")

label ts_chapter_prologue_changes:
    scene black with dissolve2
    pause 2
    jump ts_scenario_0

label ts_chapter_good_end_changes:
    scene black with dissolve2
    pause 2
    jump ts_good_ending_blya

label ts_chapter_bad_end_changes:
    scene black with dissolve2
    pause 2
    jump ts_bad_ending_blya

label ts_chapter_one_changes:
    scene black with dissolve2
    pause 2
    jump ts_scenario_1

label ts_chapter_two_changes:
    scene black with dissolve2
    pause 2
    jump ts_scenario_2

label ts_chapter_three_changes: # ВЫБОРЫ ПЕРЕД ТРЕТЬЕЙ ГЛАВОЙ
    show screen scenario_start_change_chapter_one
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
    
    show screen scenario_start_change_chapter_one1
    pause 1
    hide screen scenario_start_change_chapter_one1 with dissolve2
    pause 2

    jump ts_scenario_3

label ts_chapter_four_changes: # ВЫБОРЫ ПЕРЕД ЧЕТВЁРТОЙ ГЛАВОЙ
    show screen scenario_start_change_chapter_one
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
    
    show screen scenario_start_change_chapter_one1
    pause 1
    hide screen scenario_start_change_chapter_one1 with dissolve2
    pause 2

    jump ts_scenario_4

label ts_chapter_five_changes: # ВЫБОРЫ ПЕРЕД ПЯТОЙ ГЛАВОЙ
    show screen scenario_start_change_chapter_one
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

    show screen scenario_start_change_chapter_one1
    pause 1
    hide screen scenario_start_change_chapter_one1 with dissolve2
    pause 2

    jump ts_scenario_5


label ts_chapter_six_changes: # ВЫБОРЫ ПЕРЕД ШЕСТОЙ ГЛАВОЙ
    show screen scenario_start_change_chapter_one
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

    show screen scenario_start_change_chapter_one1
    pause 1
    hide screen scenario_start_change_chapter_one1 with dissolve2
    pause 2

    jump ts_scenario_6

label ts_chapter_seven_changes: # ВЫБОРЫ ПЕРЕД СЕДЬМОЙ ГЛАВОЙ
    show screen scenario_start_change_chapter_one
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

    show screen scenario_start_change_chapter_one1
    pause 1
    hide screen scenario_start_change_chapter_one1 with dissolve2
    pause 2

    jump ts_scenario_7

label ts_chapter_eight_changes: # ВЫБОРЫ ПЕРЕД ВОСЬМОЙ ГЛАВОЙ
    show screen scenario_start_change_chapter_one
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

    play sound fb
    scene ts_darkbed
    show zatemnenie
    with flash

    menu:
        "Лечь спать дальше":
            $ unluck6 = True
        "Встать пораньше":
            pass

    window hide
    play sound fb
    scene black
    with flash
    pause 2

    show screen scenario_start_change_chapter_one1
    pause 1
    hide screen scenario_start_change_chapter_one1 with dissolve2
    pause 2

    jump ts_scenario_8

label ts_chapter_nine_changes:
    show screen scenario_start_change_chapter_one
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

    play sound fb
    scene ts_darkbed
    show zatemnenie
    with flash

    menu:
        "Лечь спать дальше":
            $ unluck6 = True
        "Встать пораньше":
            pass

    window hide
    play sound fb
    scene black
    with flash
    pause 2

    show screen scenario_start_change_chapter_one1
    pause 1
    hide screen scenario_start_change_chapter_one1 with dissolve2
    pause 2

    jump ts_scenario_9

label ts_chapter_ten_changes:
    show screen scenario_start_change_chapter_one
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

    play sound fb
    scene ts_darkbed
    show zatemnenie
    with flash

    menu:
        "Лечь спать дальше":
            $ unluck6 = True
        "Встать пораньше":
            pass

    window hide
    play sound fb
    scene black
    with flash
    pause 2

    menu:
        "Первая часть":
            show screen scenario_start_change_chapter_one1
            pause 1
            hide screen scenario_start_change_chapter_one1 with dissolve2
            pause 2
            jump ts_scenario_10
        "Вторая часть":
            show screen scenario_start_change_chapter_one1
            pause 1
            hide screen scenario_start_change_chapter_one1 with dissolve2
            pause 2
            jump ts_scenario_11

label ts_chapter_12_changes:
    show screen scenario_start_change_chapter_one
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

    play sound fb
    scene ts_darkbed
    show zatemnenie
    with flash

    menu:
        "Лечь спать дальше":
            $ unluck6 = True
        "Встать пораньше":
            pass

    window hide
    play sound fb
    scene black
    with flash
    pause 2

    show screen scenario_start_change_chapter_one1
    pause 1
    hide screen scenario_start_change_chapter_one1 with dissolve2
    pause 2
    jump ts_scenario_12


screen scenario_start_change_chapter_one: # ВАРНИНГ ХУЙНИ
    text translation_new["ts_govno_text10"] style "ebanko_ingame" size 75 text_align 0.5 yalign 0.5 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim

screen scenario_start_change_chapter_one1: # ВАРНИНГ ХУЙНИ 2
    text translation_new["ts_govno_text11"] style "ebanko_ingame" size 75 text_align 0.5 yalign 0.5 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim
