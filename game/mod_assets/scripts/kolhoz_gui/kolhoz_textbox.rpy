# TRUE STORY TEXTBOX
# by @b3rg3n
# Since 2024

screen say(who, what):
    style_prefix "say"

    if (persistent.bazarbig):
        if (persistent.ingame_pizda):
            add "ts_textbox_big_zalagal":
                xpos -5
                ypos 544
            imagebutton:
                auto (ts_gui + "dialogue_box/big/glitch/backward_%s.webp")
                xpos 25
                ypos 583
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
                    auto (ts_gui + "dialogue_box/big/glitch/fast_forward_%s.webp")
                    xpos 1179
                    ypos 583
                    activate_sound button_error
                    hovered Play("menu_zvuk", ts_sfx + "gui/button_menu.ogg")
                    action NullAction()
            text what:
                id "what"
                xpos 129
                ypos 586
                xmaximum 1040
                size 27
                line_spacing 1
            if who:
                text who:
                    id "who"

                    ypos 562
                    size 27
                    line_spacing 1
        else:
            add ts_gui + "dialogue_box/big/dialogue_box_large.webp":
                xpos -5
                ypos 544
            imagebutton:
                auto (ts_gui + "dialogue_box/big/backward_%s.webp")
                xpos 25
                ypos 583
                activate_sound start_sound_suka
                hovered Play("menu_zvuk", ts_sfx + "gui/button_menu.ogg")
                action ShowMenu("help")

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
                ypos 586
                xmaximum 1040
                size 27
                line_spacing 1
            if who:
                text who:
                    id "who"
                    #xpos 129
                    ypos 562
                    size 27
                    line_spacing 1
    else:
        if (persistent.ingame_pizda):
            add "ts_textbox_big_zalagal_min":
                xpos -5
                ypos 577
            imagebutton:
                auto (ts_gui + "dialogue_box/glitch/backward_%s.webp")
                xpos 25
                ypos 616
                activate_sound button_error
                hovered Play("menu_zvuk", ts_sfx + "gui/button_menu.ogg")
                action NullAction()

            if not config.skipping:
                imagebutton:
                    auto (ts_gui + "dialogue_box/glitch/forward_%s.webp")
                    xpos 1179
                    ypos 616
                    activate_sound button_error
                    hovered Play("menu_zvuk", ts_sfx + "gui/button_menu.ogg")
                    action NullAction()
            else:
                imagebutton:
                    auto (ts_gui + "dialogue_box/glitch/fast_forward_%s.webp")
                    xpos 1179
                    ypos 616
                    activate_sound button_error
                    hovered Play("menu_zvuk", ts_sfx + "gui/button_menu.ogg")
                    action NullAction()
            text what:
                id "what"
                xpos 129
                ypos 619
                xmaximum 1040
                size 23
                line_spacing 1
            if who:
                text who:
                    id "who"

                    ypos 595
                    size 23
                    line_spacing 1
        else:
            add ts_gui + "dialogue_box/dialogue_box_large.webp":
                xpos -5
                ypos 577
            imagebutton:
                auto (ts_gui + "dialogue_box/backward_%s.webp")
                xpos 25
                ypos 616
                activate_sound start_sound_suka
                hovered Play("menu_zvuk", ts_sfx + "gui/button_menu.ogg")
                action ShowMenu("help")

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
                ypos 619
                xmaximum 1040
                size 23
                line_spacing 1
            if who:
                text who:
                    id "who"

                    ypos 595
                    size 23
                    line_spacing 1

    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

screen dialog(message, ok_action):

    modal True
    zorder 200
    style_prefix "confirm"
    add "mod_assets/source/images/gui/confirm.png"

    frame:

        vbox:
            xalign 1.0
            yalign 1.0
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("OK") activate_sound start_sound_suka hover_sound button_menu action ok_action

style confirm_prompt is gui_prompt