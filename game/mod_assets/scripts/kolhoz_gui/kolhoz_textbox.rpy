# TRUE STORY TEXTBOX
# by @b3rg3n
# Since 2024

screen say(who, what):
    style_prefix "say"

    if (persistent.bazarbig):
        if (persistent.ingame_pizda):
            imagebutton:
                auto (ts_gui + "dialogue_box/big/glitch/backward_%s.webp")
                xpos 25
                ypos 583
                activate_sound button_error
                hovered Play("menu_zvuk", ts_sfx + "gui/button_menu.ogg")
                action NullAction()
            add "ts_textbox_big_zalagal":
                xpos 116
                ypos 544
            imagebutton:
                auto (ts_gui + "dialogue_box/big/glitch/hide_%s.webp")
                xpos 1008
                ypos 554
                activate_sound button_error
                hovered Play("menu_zvuk", ts_sfx + "gui/button_menu.ogg")
                action NullAction()
            imagebutton:
                auto (ts_gui + "dialogue_box/big/glitch/save_%s.webp")
                xpos 1048
                ypos 554
                activate_sound button_error
                hovered Play("menu_zvuk", ts_sfx + "gui/button_menu.ogg")
                action NullAction()
            imagebutton:
                auto (ts_gui + "dialogue_box/big/glitch/menu_%s.webp")
                xpos 1087
                ypos 554
                activate_sound button_error
                hovered Play("menu_zvuk", ts_sfx + "gui/button_menu.ogg")
                action NullAction()
            imagebutton:
                auto (ts_gui + "dialogue_box/big/glitch/load_%s.webp")
                xpos 1125
                ypos 554
                activate_sound button_error
                hovered Play("menu_zvuk", ts_sfx + "gui/button_menu.ogg")
                action NullAction()
            if not config.skipping:
                imagebutton:
                    auto (ts_gui + "dialogue_box/big/glitch/forward_%s.webp")
                    xpos 1179
                    ypos 583
                    activate_sound button_error
                    hovered Play("menu_zvuk", ts_sfx + "gui/button_menu.ogg")
                    action NullAction()
            else:
                imagebutton:
                    auto (ts_gui + "dialogue_box/big/fast_forward_%s.webp")
                    xpos 1179
                    ypos 583
                    activate_sound button_error
                    hovered Play("menu_zvuk", ts_sfx + "gui/button_menu.ogg")
                    action NullAction()
            text what:
                id "what"
                xpos 129
                ypos 576
                xmaximum 1027
                size 27
                line_spacing 1
            if who:
                text who:
                    id "who"
                    xpos 129
                    ypos 562
                    size 27
                    line_spacing 1
        else:
            imagebutton:
                auto (ts_gui + "dialogue_box/big/backward_%s.webp")
                xpos 25
                ypos 583
                activate_sound start_sound_suka
                hovered Play("menu_zvuk", ts_sfx + "gui/button_menu.ogg")
                action ShowMenu("help")
            add ts_gui + "dialogue_box/big/dialogue_box_large.webp":
                xpos 116
                ypos 544
            imagebutton:
                auto (ts_gui + "dialogue_box/big/hide_%s.webp")
                xpos 1008
                ypos 554
                activate_sound start_sound_suka
                hovered Play("menu_zvuk", ts_sfx + "gui/button_menu.ogg")
                action HideInterface()
            imagebutton:
                auto (ts_gui + "dialogue_box/big/save_%s.webp")
                xpos 1048
                ypos 554
                activate_sound start_sound_suka
                hovered Play("menu_zvuk", ts_sfx + "gui/button_menu.ogg")
                action ShowMenu('save')
            imagebutton:
                auto (ts_gui + "dialogue_box/big/menu_%s.webp")
                xpos 1087
                ypos 554
                activate_sound start_sound_suka
                hovered Play("menu_zvuk", ts_sfx + "gui/button_menu.ogg")
                action ShowMenu('preferences')
            imagebutton:
                auto (ts_gui + "dialogue_box/big/load_%s.webp")
                xpos 1125
                ypos 554
                activate_sound start_sound_suka
                hovered Play("menu_zvuk", ts_sfx + "gui/button_menu.ogg")
                action ShowMenu('load')
            if not config.skipping:
                imagebutton:
                    auto (ts_gui + "dialogue_box/big/forward_%s.webp")
                    xpos 1179
                    ypos 583
                    activate_sound start_sound_suka
                    hovered Play("menu_zvuk", ts_sfx + "gui/button_menu.ogg")
                    action Skip()
            else:
                imagebutton:
                    auto (ts_gui + "dialogue_box/big/fast_forward_%s.webp")
                    xpos 1179
                    ypos 583
                    activate_sound start_sound_suka
                    hovered Play("menu_zvuk", ts_sfx + "gui/button_menu.ogg")
                    action Skip()
            text what:
                id "what"
                xpos 129
                ypos 576
                xmaximum 1027
                size 27
                line_spacing 1
            if who:
                text who:
                    id "who"
                    xpos 129
                    ypos 562
                    size 27
                    line_spacing 1
    else:
        if (persistent.ingame_pizda):
            imagebutton:
                auto (ts_gui + "dialogue_box/backward_%s.webp")
                xpos 25
                ypos 616
                activate_sound button_error
                hovered Play("menu_zvuk", ts_sfx + "gui/button_menu.ogg")
                action NullAction()
            add ts_gui + "dialogue_box/dialogue_box_large_pizda.webp":
                xpos 116
                ypos 577
            imagebutton:
                auto (ts_gui + "dialogue_box/hide_%s.webp")
                xpos 1008
                ypos 584
                activate_sound button_error
                hovered Play("menu_zvuk", ts_sfx + "gui/button_menu.ogg")
                action NullAction()
            imagebutton:
                auto (ts_gui + "dialogue_box/save_%s.webp")
                xpos 1048
                ypos 584
                activate_sound button_error
                hovered Play("menu_zvuk", ts_sfx + "gui/button_menu.ogg")
                action NullAction()
            imagebutton:
                auto (ts_gui + "dialogue_box/menu_%s.webp")
                xpos 1087
                ypos 584
                activate_sound button_error
                hovered Play("menu_zvuk", ts_sfx + "gui/button_menu.ogg")
                action NullAction()
            imagebutton:
                auto (ts_gui + "dialogue_box/load_%s.webp")
                xpos 1125
                ypos 584
                activate_sound button_error
                hovered Play("menu_zvuk", ts_sfx + "gui/button_menu.ogg")
                action NullAction()
            if not config.skipping:
                imagebutton:
                    auto (ts_gui + "dialogue_box/forward_%s.webp")
                    xpos 1179
                    ypos 616
                    activate_sound button_error
                    hovered Play("menu_zvuk", ts_sfx + "gui/button_menu.ogg")
                    action NullAction()
            else:
                imagebutton:
                    auto (ts_gui + "dialogue_box/fast_forward_%s.webp")
                    xpos 1179
                    ypos 616
                    activate_sound button_error
                    hovered Play("menu_zvuk", ts_sfx + "gui/button_menu.ogg")
                    action NullAction()
            text what:
                id "what"
                xpos 129
                ypos 609
                xmaximum 1027
                size 23
                line_spacing 1
            if who:
                text who:
                    id "who"
                    xpos 129
                    ypos 595
                    size 23
                    line_spacing 1
        else:
            imagebutton:
                auto (ts_gui + "dialogue_box/backward_%s.webp")
                xpos 25
                ypos 616
                activate_sound start_sound_suka
                hovered Play("menu_zvuk", ts_sfx + "gui/button_menu.ogg")
                action ShowMenu("help")
            add ts_gui + "dialogue_box/dialogue_box_large.webp":
                xpos 116
                ypos 577
            imagebutton:
                auto (ts_gui + "dialogue_box/hide_%s.webp")
                xpos 1008
                ypos 584
                activate_sound start_sound_suka
                hovered Play("menu_zvuk", ts_sfx + "gui/button_menu.ogg")
                action HideInterface()
            imagebutton:
                auto (ts_gui + "dialogue_box/save_%s.webp")
                xpos 1048
                ypos 584
                activate_sound start_sound_suka
                hovered Play("menu_zvuk", ts_sfx + "gui/button_menu.ogg")
                action ShowMenu('save')
            imagebutton:
                auto (ts_gui + "dialogue_box/menu_%s.webp")
                xpos 1087
                ypos 584
                activate_sound start_sound_suka
                hovered Play("menu_zvuk", ts_sfx + "gui/button_menu.ogg")
                action ShowMenu('preferences')
            imagebutton:
                auto (ts_gui + "dialogue_box/load_%s.webp")
                xpos 1125
                ypos 584
                activate_sound start_sound_suka
                hovered Play("menu_zvuk", ts_sfx + "gui/button_menu.ogg")
                action ShowMenu('load')
            if not config.skipping:
                imagebutton:
                    auto (ts_gui + "dialogue_box/forward_%s.webp")
                    xpos 1179
                    ypos 616
                    activate_sound start_sound_suka
                    hovered Play("menu_zvuk", ts_sfx + "gui/button_menu.ogg")
                    action Skip()
            else:
                imagebutton:
                    auto (ts_gui + "dialogue_box/fast_forward_%s.webp")
                    xpos 1179
                    ypos 616
                    activate_sound start_sound_suka
                    hovered Play("menu_zvuk", ts_sfx + "gui/button_menu.ogg")
                    action Skip()
            text what:
                id "what"
                xpos 129
                ypos 609
                xmaximum 1027
                size 23
                line_spacing 1
            if who:
                text who:
                    id "who"
                    xpos 129
                    ypos 595
                    size 23
                    line_spacing 1

    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0
