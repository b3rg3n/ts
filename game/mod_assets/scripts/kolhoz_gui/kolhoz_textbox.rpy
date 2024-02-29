# TRUE STORY TEXTBOX
# by @b3rg3n
# Since 2024

screen say(who, what):
    style_prefix "say"
    if (persistent.bazarbig):
        if showstatus and pps > 0:
            add im.MatrixColor("mod_assets/source/images/gui/dialogue_box/big/status.webp", im.matrix.colorize("#000", status_color)):
                xpos 690
                ypos 550
            text status_name:
                xpos 735
                ypos 552
                size 17
        imagebutton:
            idle im.MatrixColor("mod_assets/source/images/gui/dialogue_box/big/backward_idle.webp", im.matrix.colorize("#000", status_color))
            hover im.MatrixColor("mod_assets/source/images/gui/dialogue_box/big/backward_hover.webp", im.matrix.colorize("#000", status_color))
            xpos 25
            ypos 583
            action ShowMenu("help")
        add im.MatrixColor("mod_assets/source/images/gui/dialogue_box/big/dialogue_box_large.webp", im.matrix.colorize("#000", status_color)):
            xpos 116
            ypos 544
        imagebutton:
            idle im.MatrixColor("mod_assets/source/images/gui/dialogue_box/big/hide_idle.webp", im.matrix.colorize("#000", status_color))
            hover im.MatrixColor("mod_assets/source/images/gui/dialogue_box/big/hide_hover.webp", im.matrix.colorize("#000", status_color))
            xpos 1005
            ypos 556
            action HideInterface()
        imagebutton:
            idle im.MatrixColor("mod_assets/source/images/gui/dialogue_box/big/save_idle.webp", im.matrix.colorize("#000", status_color))
            hover im.MatrixColor("mod_assets/source/images/gui/dialogue_box/big/save_hover.webp", im.matrix.colorize("#000", status_color))
            xpos 1045
            ypos 556
            action ShowMenu('save')
        imagebutton:
            idle im.MatrixColor("mod_assets/source/images/gui/dialogue_box/big/menu_idle.webp", im.matrix.colorize("#000", status_color))
            hover im.MatrixColor("mod_assets/source/images/gui/dialogue_box/big/menu_hover.webp", im.matrix.colorize("#000", status_color))
            xpos 1084
            ypos 556
            action ShowMenu('preferences')
        imagebutton:
            idle im.MatrixColor("mod_assets/source/images/gui/dialogue_box/big/load_idle.webp", im.matrix.colorize("#000", status_color))
            hover im.MatrixColor("mod_assets/source/images/gui/dialogue_box/big/load_hover.webp", im.matrix.colorize("#000", status_color))
            xpos 1122
            ypos 556
            action ShowMenu('load')
        if not config.skipping:
            imagebutton:
                idle im.MatrixColor("mod_assets/source/images/gui/dialogue_box/big/forward_idle.webp", im.matrix.colorize("#000", status_color))
                hover im.MatrixColor("mod_assets/source/images/gui/dialogue_box/big/forward_hover.webp", im.matrix.colorize("#000", status_color))
                xpos 1179
                ypos 583
                action Skip()
        else:
            imagebutton:
                idle im.MatrixColor("mod_assets/source/images/gui/dialogue_box/big/fast_forward_idle.webp", im.matrix.colorize("#000", status_color))
                hover im.MatrixColor("mod_assets/source/images/gui/dialogue_box/big/fast_forward_hover.webp", im.matrix.colorize("#000", status_color))
                xpos 1179
                ypos 583
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
        if showstatus and pps > 0:
            add im.MatrixColor("mod_assets/source/images/gui/dialogue_box/status.webp", im.matrix.colorize("#000", status_color)):
                xpos 736
                ypos 581
            text status_name:
                xpos 775
                ypos 583
                size 13
        imagebutton:
            idle im.MatrixColor("mod_assets/source/images/gui/dialogue_box/backward_idle.webp", im.matrix.colorize("#000", status_color))
            hover im.MatrixColor("mod_assets/source/images/gui/dialogue_box/backward_hover.webp", im.matrix.colorize("#000", status_color))
            xpos 25
            ypos 616
            action ShowMenu("help")
        add im.MatrixColor("mod_assets/source/images/gui/dialogue_box/dialogue_box_large.webp", im.matrix.colorize("#000", status_color)):
            xpos 116
            ypos 577
        imagebutton:
            idle im.MatrixColor("mod_assets/source/images/gui/dialogue_box/hide_idle.webp", im.matrix.colorize("#000", status_color))
            hover im.MatrixColor("mod_assets/source/images/gui/dialogue_box/hide_hover.webp", im.matrix.colorize("#000", status_color))
            xpos 1005
            ypos 589
            action HideInterface()
        imagebutton:
            idle im.MatrixColor("mod_assets/source/images/gui/dialogue_box/save_idle.webp", im.matrix.colorize("#000", status_color))
            hover im.MatrixColor("mod_assets/source/images/gui/dialogue_box/save_hover.webp", im.matrix.colorize("#000", status_color))
            xpos 1045
            ypos 589
            action ShowMenu('save')
        imagebutton:
            idle im.MatrixColor("mod_assets/source/images/gui/dialogue_box/menu_idle.webp", im.matrix.colorize("#000", status_color))
            hover im.MatrixColor("mod_assets/source/images/gui/dialogue_box/menu_hover.webp", im.matrix.colorize("#000", status_color))
            xpos 1084
            ypos 589
            action ShowMenu('preferences')
        imagebutton:
            idle im.MatrixColor("mod_assets/source/images/gui/dialogue_box/load_idle.webp", im.matrix.colorize("#000", status_color))
            hover im.MatrixColor("mod_assets/source/images/gui/dialogue_box/load_hover.webp", im.matrix.colorize("#000", status_color))
            xpos 1122
            ypos 589
            action ShowMenu('load')
        if not config.skipping:
            imagebutton:
                idle im.MatrixColor("mod_assets/source/images/gui/dialogue_box/forward_idle.webp", im.matrix.colorize("#000", status_color))
                hover im.MatrixColor("mod_assets/source/images/gui/dialogue_box/forward_hover.webp", im.matrix.colorize("#000", status_color))
                xpos 1179
                ypos 616
                action Skip()
        else:
            imagebutton:
                idle im.MatrixColor("mod_assets/source/images/gui/dialogue_box/fast_forward_idle.webp", im.matrix.colorize("#000", status_color))
                hover im.MatrixColor("mod_assets/source/images/gui/dialogue_box/fast_forward_hover.webp", im.matrix.colorize("#000", status_color))
                xpos 1179
                ypos 616
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