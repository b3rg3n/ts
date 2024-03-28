# TRUE STORY PERSISTENT LIST CHECKER
# by @b3rg3n
# Since 2024

screen ts_check_persistent:

    add "mod_assets/source/images/anim/zatemnenie.webp"

    text "{font=[cit_font]}Состояние переменных:" yalign 0.1 xalign 0.5

    text "{font=[cit_font]}Количество баллов unluck - [unluck_ball]" yalign 0.2 xalign 0.5

    text "{font=[cit_font]}unluck = [unluck]" yalign 0.3 xalign 0.1
    text "{font=[cit_font]}unluck2 = [unluck2]" yalign 0.35 xalign 0.1
    text "{font=[cit_font]}unluck3 = [unluck3]" yalign 0.4 xalign 0.1
    text "{font=[cit_font]}unluck4 = [unluck4]" yalign 0.45 xalign 0.1
    text "{font=[cit_font]}unluck5 = [unluck5]" yalign 0.5 xalign 0.1
    text "{font=[cit_font]}unluck4_cooking = [unluck4_cooking]" yalign 0.55 xalign 0.1
    text "{font=[cit_font]}unluck4_reading = [unluck4_reading]" yalign 0.6 xalign 0.1
    text "{font=[cit_font]}unluck4_telek = [unluck4_telek]" yalign 0.65 xalign 0.1
    text "{font=[cit_font]}chess_tutor = [chess_tutor]" yalign 0.7 xalign 0.1
    text "{font=[cit_font]}act2_chess = [act2_chess]" yalign 0.75 xalign 0.1

    text "{font=[cit_font]}persistent.carter2menu = [persistent.carter2menu]" yalign 0.3 xalign 0.5
    text "{font=[cit_font]}persistent.carter3menu = [persistent.carter3menu]" yalign 0.35 xalign 0.5
    text "{font=[cit_font]}persistent.вadendmenu = [persistent.badendmenu]" yalign 0.4 xalign 0.5
    text "{font=[cit_font]}persistent.goodendmenu = [persistent.goodendmenu]" yalign 0.45 xalign 0.5
    text "{font=[cit_font]}persistent.firstmenushka = [persistent.firstmenushka]" yalign 0.5 xalign 0.5
    text "{font=[cit_font]}persistent.zastavka_skip = [persistent.zastavka_skip]" yalign 0.55 xalign 0.5
    text "{font=[cit_font]}persistent.skip_splash = [persistent.skip_splash]" yalign 0.6 xalign 0.5
    text "{font=[cit_font]}persistent.first_poem = [persistent.first_poem ]" yalign 0.65 xalign 0.5
    text "{font=[cit_font]}persistent.scenario_proshel_вlya = [persistent.scenario_proshel_blya]" yalign 0.7 xalign 0.5
    text "{font=[cit_font]}persistent.вadendmenuperedglitch = [persistent.badendmenuperedglitch]" yalign 0.75 xalign 0.5
    text "{font=[cit_font]}persistent.вadendmenuskipglitch = [persistent.badendmenuskipglitch]" yalign 0.8 xalign 0.5

    textbutton "Вернуться" yalign 0.9 xalign 0.5 action Return() activate_sound start_sound_suka hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")