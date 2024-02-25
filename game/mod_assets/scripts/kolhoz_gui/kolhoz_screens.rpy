#TRUE STORY SCREENS
#by @b3rg3n
#Since 2024
init -1 python:
    renpy.music.register_channel("menu_zvuk", "sfx", False)

    main_font = "mod_assets/source/fonts/captureit.ttf"
    nvl_font = "mod_assets/source/fonts/nvl_font.ttf"
    header_font = "mod_assets/source/fonts/captureit.ttf"
    link_font = "mod_assets/source/fonts/captureit.ttf"
    info_font = "mod_assets/source/fonts/2.ttf"
    splash_font = "mod_assets/source/fonts/captureit.ttf"


    style.file_picker_text = Style(style.default)
    style.file_picker_text.antialias = True
    style.file_picker_text.font  = main_font
    style.file_picker_text.color = "#bdbdbd"
    style.file_picker_text.selected_color = "#ffffff"
    style.file_picker_text.hover_color = "#ffffff"
    style.file_picker_text.size = 17
    style.file_picker_text.drop_shadow=(2, 2)
    style.file_picker_text.drop_shadow_color = "#000"

    style.save_load_button = Style(style.button)
    style.save_load_button.background = get_image("images/gui/save_load/thumbnail_idle.webp")
    style.save_load_button.hover_background = get_image("images/gui/save_load/thumbnail_hover.webp")
    style.save_load_button.selected_background = get_image("images/gui/save_load/thumbnail_selected.webp")
    style.save_load_button.selected_hover_background = get_image("images/gui/save_load/thumbnail_selected.webp")
    style.save_load_button.selected_idle_background = get_image("images/gui/save_load/thumbnail_selected.webp")

    style.blank_button = Style(style.button)
    style.blank_button.background = "mod_assets/source/images/gui/none.webp"
    style.blank_button.hover_background = "mod_assets/source/images/gui/none.webp"
    style.blank_button.selected_background = "mod_assets/source/images/gui/none.webp"
    style.blank_button.selected_hover_background = "mod_assets/source/images/gui/none.webp"
    style.blank_button.selected_idle_background = "mod_assets/source/images/gui/none.webp"

    style.base_font = Style(style.default)
    style.base_font.font  = nvl_font
    style.base_font.size = 21
    style.base_font.line_spacing = 2

    style.settings_header = Style(style.base_font)
    style.settings_header.font  = header_font
    style.settings_header.size = 29
    style.settings_header.color = "#FFFFFF"
    style.settings_header.hover_color = "#FFFFFF"

    style.settings_text = Style(style.settings_header)
    style.settings_text.size = 29
    style.settings_text.selected_color = "#FF0000"
    style.settings_text.hover_color = "#FFFFFF"

    style.settings_link = Style(style.base_font)
    style.settings_link.font  = link_font
    style.settings_link.size = 45
    style.settings_link.kerning = 3
    style.settings_link.color = "#ffffff"
    style.settings_link.hover_color = "#ff0000"
    style.settings_link.selected_color = "#ffffff"
    style.settings_link.selected_idle_color = "#ffffff"
    style.settings_link.selected_hover_color = "#ff0000"
    style.settings_link.insensitive_color = "#ffffff"

    style.finger = Style(style.base_font)
    style.finger.font  = link_font
    style.finger.size = 15
    style.finger.kerning = 3
    style.finger.color = "#ffffff"
    style.finger.hover_color = "#ffffff"
    style.finger.selected_color = "#ffffff"
    style.finger.selected_idle_color = "#ffffff"
    style.finger.selected_hover_color = "#ffffff"
    style.finger.insensitive_color = "#ffffff"

    style.hyperlink_text = Style(style.settings_link)
    style.hyperlink_text.underline = True
    style.hyperlink_text.hover_color = "#0ff"
    style.hyperlink_text.idle_color = "#08f"

    style.music_link = Style(style.settings_link)
    style.music_link.insensitive_color = "#4f4f4f"
    style.music_link.selected_color = "#ffffff"

    style.sprite_menu = Style(style.settings_text)
    style.sprite_menu.size = 30
    style.sprite_menu.color = "#466123"
    style.sprite_menu.selected_color = "#466123"
    style.sprite_menu.hover_color = "#9dcd55"

    style.say_dialogue = Style(style.base_font)
    style.say_label = Style(style.base_font)
    style.say_label.size = 28
    style.say_label.drop_shadow=(2, 2)
    style.say_label.drop_shadow_color = "#000"

    style.chapter = Style(style.base_font)
    style.chapter.font  = header_font
    style.chapter.size = 80
    style.chapter.color = "#fff"

    style.chapter.outlines = [ (1, "#ffdd7d", 0, 0) ]

    style.daynum = Style(style.chapter)
    style.daynum.font  = header_font
    style.daynum.size = 30

    style.normal_day = Style(style.base_font)
    style.normal_day.color = "#ffdd7d"
    style.normal_day.drop_shadow=(2, 2)
    style.normal_day.drop_shadow_color = "#000"
    style.narrator_day = Style(style.normal_day)
    style.narrator_day.italic = False
    style.thoughts_day = Style(style.normal_day)
    style.thoughts_day.bold = False

    style.normal_sunset = Style(style.base_font)
    style.normal_sunset.color = "#ffdd7d"
    style.normal_sunset.drop_shadow=(2, 2)
    style.normal_sunset.drop_shadow_color = "#000"
    style.narrator_sunset = Style(style.normal_sunset)
    style.narrator_sunset.italic = False
    style.thoughts_sunset = Style(style.normal_sunset)
    style.thoughts_sunset.bold = False

    style.normal_night = Style(style.base_font)
    style.normal_night.color = "#ffdd7d"
    style.normal_night.drop_shadow=(2, 2)
    style.normal_night.drop_shadow_color = "#000"
    style.narrator_night = Style(style.normal_night)
    style.narrator_night.italic = False
    style.thoughts_night = Style(style.normal_night)
    style.thoughts_night.bold = False

    style.normal_prolog = Style(style.base_font)
    style.normal_prolog.color = "#ffdd7d"
    style.normal_prolog.drop_shadow=(2, 2)
    style.normal_prolog.drop_shadow_color = "#000"
    style.narrator_prolog = Style(style.normal_prolog)
    style.narrator_prolog.italic = False
    style.thoughts_prolog = Style(style.normal_prolog)
    style.thoughts_prolog.bold = False

    style.cards_button = Style(style.button)
    style.cards_button.font  = header_font
    style.cards_button.background = RoundRect("#000", False)
    style.cards_button.hover_background = RoundRect("#555", False)
    style.cards_button.insensitive_background = RoundRect("#404040", False)

    style.cards_button_text = Style(style.button_text)
    style.cards_button_text.color = "#FFF"
    style.cards_button_text.selected_color = "#ff0000"
    style.cards_button_text.insensitive_color = "#ffffff"

    style.log_button = Style(style.button)
    style.log_button.child = None
    style.log_button.focus_mask = None
    style.log_button.background  = None

    style.log_button_text = Style(style.normal_day)
    style.log_button_text.font  = main_font
    style.log_button_text.selected_color = "#115bc0"
    style.log_button_text.hover_color = "#115bc0"
    style.log_button_text.selected_color = "#b6ff00"
    style.log_button_text.hover_color = "#b6ff00"

    style.log_button_text_edit = Style(style.log_button_text)
    style.log_button_text_edit.size = 33

init -1 python:
    _main_menu_screen = "main_menu"
init -501 screen main_menu:

    modal True tag menu

    textbutton ("{size=+15}Сойти с ума{/size}") ypos 342 xpos 75:
        action Start()
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
    textbutton ("{size=+15}Вспомнить{/size}") ypos 392 xpos 75:
        action ShowMenu('load')
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
    textbutton ("{size=+15}Настройки{/size}") ypos 442 xpos 75:
        action ShowMenu('preferences')
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
    textbutton ("{size=+15}Сбежать{/size}") ypos 492 xpos 75:
        action ShowMenu('quit')
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
    text "{size=+10}{font=[cit_font]} RenPy ver. [renpy.version_only] | Mod ver. [config.version]{/font}{/size}" yalign 0.983 xalign 0.990

init -1 python:
    def force_quit():
        renpy.quit()

init -501 screen quit:

    modal True tag menu

    add get_image("images/anim/zatemnenie.webp")

    text translation_new["Quit_confirm"] style "settings_link" size 60 text_align 0.5 xalign 0.5 yalign 0.33 color "#FFFFFF" antialias True kerning 2

    textbutton translation_new["Yes"] text_size 70 style "log_button" text_style "settings_link" xalign 0.21 yalign 0.55 text_color "#FFFFFF" text_hover_color "#FF0000" action Quit(confirm=False) activate_sound start_sound_suka hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
    textbutton translation_new["No"] text_size 70 style "log_button" text_style "settings_link" xalign 0.75 yalign 0.55 text_color "#FFFFFF" text_hover_color "#FF0000" action Return() activate_sound start_sound_suka hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")

label _compat_confirm_quit:
    $ renpy.call_screen('quit')


init -1 python:
    _game_menu_screen = "game_menu_selector"
init -501 screen game_menu_selector:

    modal True tag menu
    add "mod_assets/source/images/gui/ebanoemenu/ingame_menu.webp"
    textbutton ("{size=+15}На Главную{/size}") ypos 342 xpos 75:
        action MainMenu()
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
    textbutton ("{size=+15}Запомнить{/size}") ypos 392 xpos 75:
        action ShowMenu('save')
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
    textbutton ("{size=+15}Вспомнить{/size}") ypos 442 xpos 75:
        action ShowMenu('load')
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
    textbutton ("{size=+15}Настройки{/size}") ypos 492 xpos 75:
        action ShowMenu('preferences')
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
    textbutton ("{size=+15}Сбежать{/size}") ypos 542 xpos 75:
        action ShowMenu('quit')
        activate_sound start_sound_suka
        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
    imagebutton ypos 0 xpos 0:
        auto "mod_assets/source/images/gui/ebanoemenu/nope_%s.webp"
        action Return()
    text "{font=[cit_font]}{size=+15}Сходишь с ума уже {image=gametime}{size=+15}{/font}" ypos 650 xpos 76

init -101 python:

    store.selected_slot = "_"
    persistent._file_page = 1


init 4 python:
    import renpy.store as store

    class FunctionCallback(Action):
        def __init__(self,function,*arguments):
            self.function=function
            self.arguments=arguments
        def __call__(self):
            return self.function(self.arguments)

    def on_load_callback(slot):
        try:
            if persistent.on_save_timeofday[slot]:
                persistent.timeofday = persistent.on_save_timeofday[slot][0]
                persistent.sprite_time = persistent.on_save_timeofday[slot][1]
                persistent.font_size = persistent.on_save_timeofday[slot][2]
                
                _preferences.volumes['music'] = persistent.on_save_timeofday[slot][3]
                _preferences.volumes['sfx'] = persistent.on_save_timeofday[slot][4]
                _preferences.volumes['voice'] = persistent.on_save_timeofday[slot][5]
        
        except:
            pass

    def on_save_callback(slot):
        if not persistent.on_save_timeofday:
            persistent.on_save_timeofday={}
        
        persistent.on_save_timeofday[slot] = (persistent.timeofday, persistent.sprite_time, persistent.font_size, _preferences.volumes['music'], _preferences.volumes['sfx'], _preferences.volumes['voice'])

    def do_rollback(cnt):
        if not d2_cardgame_block_rollback:
            k=cnt[0]
            renpy.rollback(True, k+1)


    config.thumbnail_width = 141
    config.thumbnail_height = 78

    style.file_picker_ss_window.xpos = 0
    style.file_picker_ss_window.ypos = 0

init -501 screen save:

    modal True tag menu

    window background get_image("images/anim/zatemnenie.webp") xmaximum 1280 ymaximum 720:

        textbutton translation_new["settings"] style "log_button" text_style "settings_link" xalign 0.02 yalign 0.08 action ShowMenu('preferences') activate_sound start_sound_suka hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        textbutton translation_new["LOAD"] style "log_button" text_style "settings_link" xalign 0.98 yalign 0.08 action ShowMenu('load') activate_sound start_sound_suka hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        hbox xalign 0.5 yalign 0.08:
            add get_image("images/gui/ebanoemenu/star.webp") yalign 0.65
            text " "+translation_new["SAVE"]+" " style "settings_link" yalign 0.5 color "#ffffff"
            add get_image("images/gui/ebanoemenu/star.webp") yalign 0.65
        textbutton translation_new["Back"] style "log_button" text_style "settings_link" xalign 0.015 yalign 0.92 action Return() activate_sound start_sound_suka hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")

        textbutton translation_new["Save_game"] style "log_button" text_style "settings_link" yalign 0.92 xalign 0.5 action (FunctionCallback(on_save_callback, selected_slot), FileSave(selected_slot)) activate_sound start_sound_suka hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        textbutton "{size=-12}{b}x{/b} {/size}"+translation_new["Delete"] style "log_button" text_style "settings_link" yalign 0.92 xalign 0.97 action FileDelete(selected_slot) activate_sound start_sound_suka hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")

        vbox xalign 0.023 yalign 0.5:
            grid 1 10:
                for i in range(0, 10):
                    if i == 0:
                        textbutton translation_new["Auto"] text_size 25 style "log_button" text_style "settings_link" action (FilePage("auto"), SetVariable("selected_slot", False)) activate_sound start_sound_suka hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
                    else:
                        textbutton str(i) text_size 25 right_padding 25 style "log_button" text_style "settings_link" action (FilePage(i), SetVariable("selected_slot", False)) activate_sound start_sound_suka hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")

        grid 4 3 xpos 0.13 ypos 0.2 xmaximum 0.81 ymaximum 0.65:
            transpose False
            xfill True
            yfill True
            for i in range(1, 13):

                fixed:
                    add FileScreenshot(i) xpos 7 ypos 7

                    button:
                        action SetVariable("selected_slot", i)
                        activate_sound start_sound_suka
                        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
                        xfill False
                        yfill False
                        style "save_load_button"
                        has fixed
                        text ( "%s." % i + FileTime(i, format=' %d.%m.%y, %H:%M', empty=" "+translation_new["Empty_slot"]) + "\n" +FileSaveName(i)) style "file_picker_text" xpos 10 ypos 10


init -1 python:
    _load_prompt = "load"
init -501 screen load:

    modal True tag menu

    window background get_image("images/anim/zatemnenie.webp") xmaximum 1280 ymaximum 720:

        textbutton translation_new["settings"] style "log_button" text_style "settings_link" xalign 0.02 yalign 0.08 action ShowMenu('preferences') activate_sound start_sound_suka hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        textbutton translation_new["SAVE"] style "log_button" text_style "settings_link" xalign 0.98 yalign 0.08 action ShowMenu('save') activate_sound start_sound_suka hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        hbox xalign 0.5 yalign 0.08:
            add get_image("images/gui/ebanoemenu/star.webp") yalign 0.65
            text " "+translation_new["LOAD"]+" " style "settings_link" yalign 0.5 color "#ffffff"
            add get_image("images/gui/ebanoemenu/star.webp") yalign 0.65
        textbutton translation_new["Back"] style "log_button" text_style "settings_link" xalign 0.015 yalign 0.92 action Return() activate_sound start_sound_suka hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        textbutton translation_new["Load_game"] style "log_button" text_style "settings_link" yalign 0.92 xalign 0.5 action (FunctionCallback(on_load_callback,selected_slot), FileLoad(selected_slot)) activate_sound start_sound_suka hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        textbutton "{size=-12}{b}x{/b} {/size}"+translation_new["Delete"] style "log_button" text_style "settings_link" yalign 0.92 xalign 0.97 action FileDelete(selected_slot) activate_sound start_sound_suka hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")

        vbox xalign 0.023 yalign 0.5:
            grid 1 10:
                for i in range(0, 10):
                    if i == 0:
                        textbutton translation_new["Auto"] text_size 25 style "log_button" text_style "settings_link" action (FilePage("auto"), SetVariable("selected_slot", False)) activate_sound start_sound_suka hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
                    else:
                        textbutton str(i) text_size 25 right_padding 25 style "log_button" text_style "settings_link" action (FilePage(i), SetVariable("selected_slot", False)) activate_sound start_sound_suka hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")

        grid 4 3 xpos 0.13 ypos 0.2 xmaximum 0.81 ymaximum 0.65:
            transpose False
            xfill True
            yfill True
            for i in range(1, 13):

                fixed:
                    add FileScreenshot(i) xpos 7 ypos 7

                    button:
                        action SetVariable("selected_slot", i)
                        activate_sound start_sound_suka
                        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
                        xfill False
                        yfill False
                        style "save_load_button"
                        has fixed
                        text ( "%s." % i + FileTime(i, format=' %d.%m.%y, %H:%M', empty=" "+translation_new["Empty_slot"]) + "\n" +FileSaveName(i)) style "file_picker_text" xpos 10 ypos 10

init -501 screen preferences:

    modal True tag menu

    $ bar_null = Frame(get_image("images/gui/ebanoemenu/bar_null.webp"),36,36)
    $ bar_full = Frame(get_image("images/gui/ebanoemenu/bar_full.webp"),36,36)

    window background get_image("images/anim/zatemnenie.webp") xmaximum 1280 ymaximum 720:

        textbutton translation_new["SAVE"] style "log_button" text_style "settings_link" xalign 0.02 yalign 0.08 action ShowMenu('save') activate_sound start_sound_suka hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        textbutton translation_new["LOAD"] style "log_button" text_style "settings_link" xalign 0.98 yalign 0.08 action ShowMenu('load') activate_sound start_sound_suka hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
        hbox xalign 0.5 yalign 0.08:
            add get_image("images/gui/ebanoemenu/star.webp") yalign 0.65
            text " "+translation_new["settings"]+" " style "settings_link" yalign 0.5 color "#ffffff"
            add get_image("images/gui/ebanoemenu/star.webp") yalign 0.65
        textbutton translation_new["Back"] style "log_button" text_style "settings_link" xalign 0.015 yalign 0.92 action Return() activate_sound start_sound_suka hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")

        side "c b r":
            area (0.25, 0.23, 0.51, 0.71)
            viewport id "preferences":
                mousewheel True
                draggable True
                scrollbars None

                has grid 1 16 xfill True spacing 15
                if renpy.android or renpy.ios:
                    text translation_new["Skip"] style "settings_header" xalign 0.5
                    grid 2 1 xfill True:

                        hbox xalign 0.5:
                            if _preferences.skip_unseen:
                                add get_image("images/gui/ebanoemenu/leaf.webp") ypos 0.12
                            else:
                                null width 22
                            textbutton translation_new["Skip_all"] style "log_button" text_style "settings_text" action Preference("skip", "all") activate_sound start_sound_suka hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")

                        hbox xalign 0.5:
                            if not _preferences.skip_unseen:
                                add get_image("images/gui/ebanoemenu/leaf.webp") ypos 0.12
                            else:
                                null width 22
                            textbutton translation_new["Skip_seen"] style "log_button" text_style "settings_text" action Preference("skip", "seen") activate_sound start_sound_suka hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")

                else:
                    text translation_new["Window_mode"] style "settings_header" xalign 0.5
                    grid 2 1 xfill True:

                        hbox xalign 0.5:
                            if _preferences.fullscreen:
                                add get_image("images/gui/ebanoemenu/leaf.webp") ypos 0.12
                            else:
                                null width 22
                            textbutton translation_new["Fullscreen"] style "log_button" text_style "settings_text" action Preference("display", "fullscreen") activate_sound start_sound_suka hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")

                        hbox xalign 0.5:
                            if not _preferences.fullscreen:
                                add get_image("images/gui/ebanoemenu/leaf.webp") ypos 0.12
                            else:
                                null width 22
                            textbutton translation_new["Window"] style "log_button" text_style "settings_text" action Preference("display", "window") activate_sound start_sound_suka hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")

                    text translation_new["Skip"] style "settings_header" xalign 0.5
                    grid 2 1 xfill True:

                        hbox xalign 0.5:
                            if _preferences.skip_unseen:
                                add get_image("images/gui/ebanoemenu/leaf.webp") ypos 0.12
                            else:
                                null width 22
                            textbutton translation_new["Skip_all"] style "log_button" text_style "settings_text" action Preference("skip", "all") activate_sound start_sound_suka hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")

                        hbox xalign 0.5:
                            if not _preferences.skip_unseen:
                                add get_image("images/gui/ebanoemenu/leaf.webp") ypos 0.12
                            else:
                                null width 22
                            textbutton translation_new["Skip_seen"] style "log_button" text_style "settings_text" action Preference("skip", "seen") activate_sound start_sound_suka hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")

                text translation_new["Volume"] style "settings_header" xalign 0.5

                grid 2 1 xfill True:
                    textbutton translation_new["Music_lower"] style "log_button" text_style "settings_text" action Play("sound", "mod_assets/source/audio/sfx/skitetksy_voice/ebanko.ogg") xpos 0.1 ypos -0.2
                    bar value Preference("music volume") left_bar bar_full right_bar bar_null thumb "mod_assets/source/images/gui/ebanoemenu/htumb.webp" hover_thumb "mod_assets/source/images/gui/ebanoemenu/htumb.webp" xmaximum 0.8 ymaximum 3 xpos -0.35

                grid 2 1 xfill True:
                    textbutton translation_new["Sound"] style "log_button" text_style "settings_text" action Play("sound", "mod_assets/source/audio/sfx/skitetksy_voice/ebanko.ogg") xpos 0.1 ypos -0.2
                    bar value Preference("sound volume") left_bar bar_full right_bar bar_null thumb "mod_assets/source/images/gui/ebanoemenu/htumb.webp" hover_thumb "mod_assets/source/images/gui/ebanoemenu/htumb.webp" xmaximum 0.8 ymaximum 3 xpos -0.35

                grid 2 1 xfill True:
                    textbutton translation_new["Ambience"] style "log_button" text_style "settings_text" action Play("sound", "mod_assets/source/audio/sfx/skitetksy_voice/ebanko.ogg") xpos 0.1 ypos -0.2
                    bar value Preference("voice volume") left_bar bar_full right_bar bar_null thumb "mod_assets/source/images/gui/ebanoemenu/htumb.webp" hover_thumb "mod_assets/source/images/gui/ebanoemenu/htumb.webp" xmaximum 0.8 ymaximum 3 xpos -0.35

                text translation_new["Text_speed"] style "settings_header" xalign 0.5
                bar value Preference("text speed") left_bar bar_full right_bar bar_null thumb "mod_assets/source/images/gui/ebanoemenu/htumb.webp" hover_thumb "mod_assets/source/images/gui/ebanoemenu/htumb.webp" xalign 0.5 xmaximum 0.8 ymaximum 3

                text translation_new["Font"] style "settings_header" xalign 0.5
                grid 2 1 xfill True:
                    hbox xalign 0.5:
                        if persistent.bazarbig == True:
                            add get_image("images/gui/ebanoemenu/leaf.webp") ypos 0.12
                        else:
                            null width 22
                        textbutton translation_new["Normal_font"] style "log_button" text_style "settings_text" action [SetField(persistent,'bazarbig', False)] activate_sound start_sound_suka hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")

                    hbox xalign 0.5:
                        if not persistent.bazarbig == False:
                            add get_image("images/gui/ebanoemenu/leaf.webp") ypos 0.12
                        else:
                            null width 22
                        textbutton translation_new["Big_font"] style "log_button" text_style "settings_text" action [SetField(persistent,'bazarbig', True)] activate_sound start_sound_suka hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")

                text translation_new["Cens_mode_set"] style "settings_header" xalign 0.5
                grid 2 1 xfill True:
                    hbox xalign 0.5:
                        if persistent.cens_mode == True:
                            add get_image("images/gui/ebanoemenu/leaf.webp") ypos 0.12
                        else:
                            null width 22
                        textbutton translation_new["Cens_mode_off"] style "log_button" text_style "settings_text" action [SetField(persistent,'cens_mode', False)] activate_sound start_sound_suka hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")

                    hbox xalign 0.5:
                        if not persistent.cens_mode == False:
                            add get_image("images/gui/ebanoemenu/leaf.webp") ypos 0.12
                        else:
                            null width 22
                        textbutton translation_new["Cens_mode_on"] style "log_button" text_style "settings_text" action [SetField(persistent,'cens_mode', True)] activate_sound start_sound_suka hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")


            bar value XScrollValue("preferences") left_bar "mod_assets/source/images/gui/none.webp" right_bar "mod_assets/source/images/gui/none.webp" thumb "mod_assets/source/images/gui/none.webp" hover_thumb "mod_assets/source/images/gui/none.webp"
            vbar value YScrollValue("preferences") bottom_bar "mod_assets/source/images/gui/none.webp" top_bar "mod_assets/source/images/gui/none.webp" thumb "mod_assets/source/images/gui/ebanoemenu/vthumb.webp" thumb_offset -12


init -501 screen choice(items):
    style_prefix "choice"

    modal True
    frame background Frame('mod_assets/source/images/gui/ec_nightmare.webp', 0, 0) xfill True yalign 0.5 bottom_padding 33 top_padding 33:
        $ l = len(items)
        grid 1 l:
            xalign 0.5
            for caption, action, chosen in items:
                if action and caption:
                    button:
                        background None
                        action action
                        activate_sound start_sound_suka
                        hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
                        text caption font 'mod_assets/source/fonts/captureit.ttf' size 35 hover_size 37 at ec_tr_choice
                        xalign 0.5


init -1 style choice_vbox is vbox
init -1 style choice_button is button
init -1 style choice_button_text is button_text

init -1 style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

init -1 style choice_button is default:
    properties gui.button_properties("choice_button")

init -1 style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


init -501 screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform -1 notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


init -1 style notify_frame is empty
init -1 style notify_text is gui_text

init -1 style notify_frame:
    ypos gui.notify_ypos

    background Frame("mod_assets/source/images/gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

init -1 style notify_text:
    properties gui.text_properties("notify")


init -1 style pref_vbox:
    variant "medium"
    xsize 450

init -501 screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0




init -1 style window:
    variant "small"
    background "mod_assets/source/images/gui/phone/textbox.png"

init -1 style radio_button:
    variant "small"
    foreground "mod_assets/source/images/gui/phone/button/radio_[prefix_]foreground.png"

init -1 style check_button:
    variant "small"
    foreground "mod_assets/source/images/gui/phone/button/check_[prefix_]foreground.png"

init -1 style nvl_window:
    variant "small"
    background "mod_assets/source/images/gui/phone/nvl.png"

init -1 style main_menu_frame:
    variant "small"
    background "mod_assets/source/images/gui/phone/overlay/main_menu.png"

init -1 style game_menu_outer_frame:
    variant "small"
    background "mod_assets/source/images/gui/phone/overlay/game_menu.png"

init -1 style game_menu_navigation_frame:
    variant "small"
    xsize 340

init -1 style game_menu_content_frame:
    variant "small"
    top_margin 0

init -1 style pref_vbox:
    variant "small"
    xsize 400

init -1 style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("mod_assets/source/images/gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("mod_assets/source/images/gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

init -1 style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("mod_assets/source/images/gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("mod_assets/source/images/gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

init -1 style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("mod_assets/source/images/gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("mod_assets/source/images/gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

init -1 style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("mod_assets/source/images/gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("mod_assets/source/images/gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

init -1 style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("mod_assets/source/images/gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "mod_assets/source/images/gui/phone/slider/horizontal_[prefix_]thumb.png"

init -1 style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("mod_assets/source/images/gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "mod_assets/source/images/gui/phone/slider/vertical_[prefix_]thumb.png"

init -1 style slider_vbox:
    variant "small"
    xsize None

init -1 style slider_slider:
    variant "small"
    xsize 600


init -501 screen confirm(message, yes_action, no_action):

    modal True

    zorder 200

    add get_image("images/gui/base.png")
    text _(message) text_align 0.5 yalign 0.36 xalign 0.5 color "#ffffff" font header_font size 60
    textbutton translation_new["Yes"] text_size 60 style "log_button" text_style "settings_link" yalign 0.65 xalign 0.3 action yes_action activate_sound start_sound_suka hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
    textbutton translation_new["Noo"] text_size 60 style "log_button" text_style "settings_link" yalign 0.65 xalign 0.7 action no_action activate_sound start_sound_suka hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")



init -1 style confirm_frame is gui_frame
init -1 style confirm_prompt is gui_prompt
init -1 style confirm_prompt_text is gui_prompt_text
init -1 style confirm_button is gui_medium_button
init -1 style confirm_button_text is gui_medium_button_text

init -1 style confirm_frame:
    background Frame([ "mod_assets/source/images/gui/confirm_frame.png", "mod_assets/source/images/gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

init -1 style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

init -1 style confirm_button:
    properties gui.button_properties("confirm_button")

init -1 style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


init -501 screen input(prompt):
    style_prefix "input"

    window:

        has vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

        text prompt style "input_prompt"
        input id "input"

init -1 style input_prompt is default

init -1 style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

init -1 style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width



init -501 screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        has hbox:
            spacing 6

        text _("Перематываю")

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


transform -1 delayed_blink(delay, cycle):
    alpha .5

    pause delay
    block:

        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


init -1 style skip_frame is empty
init -1 style skip_text is gui_text
init -1 style skip_triangle is skip_text

init -1 style skip_frame:
    ypos gui.skip_ypos
    background Frame("mod_assets/source/images/gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

init -1 style skip_text:
    size gui.notify_text_size

init -1 style skip_triangle:
    font "DejaVuSans.ttf"


init -1 python:
    config.character_id_prefixes.append('namebox')

init -1 style window is default
init -1 style say_label is default
init -1 style say_dialogue is default
init -1 style say_thought is say_dialogue

init -1 style namebox is default
init -1 style namebox_label is say_label


init -1 style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("mod_assets/source/images/gui/textbox.png", xalign=0.5, yalign=1.0)

init -1 style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("mod_assets/source/images/gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

init -1 style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

init -1 style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False


init -1 style default:
    properties gui.text_properties()
    language gui.language

init -1 style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

init -1 style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

init -1 style gui_text:
    properties gui.text_properties("interface")


init -1 style button:
    properties gui.button_properties("button")
    background "mod_assets/source/images/gui/button/[prefix_]background.png"

init -1 style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


init -1 style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

init -1 style prompt_text is gui_text:
    properties gui.text_properties("prompt")


init -1 style bar:
    ysize gui.bar_size
    left_bar Frame("mod_assets/source/images/gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("mod_assets/source/images/gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

init -1 style vbar:
    xsize gui.bar_size
    top_bar Frame("mod_assets/source/images/gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("mod_assets/source/images/gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

init -1 style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("mod_assets/source/images/gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("mod_assets/source/images/gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

init -1 style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("mod_assets/source/images/gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("mod_assets/source/images/gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

init -1 style slider:
    ysize gui.slider_size
    base_bar Frame("mod_assets/source/images/gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "mod_assets/source/images/gui/slider/horizontal_[prefix_]thumb.png"

init -1 style vslider:
    xsize gui.slider_size
    base_bar Frame("mod_assets/source/images/gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "mod_assets/source/images/gui/slider/vertical_[prefix_]thumb.png"


init -1 style frame:
    padding gui.frame_borders.padding
    background Frame("mod_assets/source/images/gui/frame.png", gui.frame_borders, tile=gui.frame_tile)


init -1002 python:
    translation=translation_ru
    translation_new=translation

    def merge_two_dicts(x, y):
        z = x.copy()
        z.update(y)
        return z
    translation_temp={}
    for i,k in translation.iteritems():
        translation_temp[i]={}
        translation_temp[i][_preferences.language]=k
    translation=merge_two_dicts(translation,translation_temp)

    def get_translation(string):
        renpy.log("%s" % string )
        return translation[string][_preferences.language]

init -1003 python:
    translation_ru = {
        "Quit_confirm" : "Уверен? Обратного пути не будет.",
        "Yes" : "Конечно",
        "No" : "Не особо",
        "Noo" : "Передумал",
        "settings" : "НАСТРОЙКИ",
        "LOAD" : "ВСПОМНИТЬ",
        "SAVE" : "ЗАПОМНИТЬ",
        "BACK" : "ВЕРНУТЬСЯ",
        "Back" : "Вернуться?",
        "Save_game" : "Запомнить?",
        "Delete" : "Забыть?",
        "Auto" : "Авто",
        "Empty_slot" : "Пусто",
        "Load_game" : "Вспомнить?",
        "Window_mode" : "Режим экрана",
        "Fullscreen" : "Во весь экран",
        "Window" : "В окне",
        "Skip" : "Пропускать",
        "Skip_all" : "Вообще всё",
        "Skip_seen" : "Что уже видел",
        "Volume" : "Громкость",
        "Music_lower" : "Музыка",
        "Sound" : "Звуки",
        "Ambience" : "Фон",
        "Text_speed" : "Скорость текста",
        "Font" : "Размер текстбокса",
        "Normal_font" : "Обычный",
        "Big_font" : "Большой",
        "Music_widget_set" : "Названия треков",
        "Music_widget_on" : "Включить",
        "Music_widget_off" : "Отключить",
        "Cens_mode_set" : "Антицензор",
        "Cens_mode_off" : "Отключить",
        "Cens_mode_on" : "Включить",

}


init -501 screen quick_menu():

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Назад") action Rollback()
            textbutton _("История") action ShowMenu('history')
            textbutton _("Пропуск") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Авто") action Preference("auto-forward", "toggle")
            textbutton _("Запомнить") action ShowMenu('save')
            textbutton _("Крутилки") action ShowMenu('preferences')


init -1 python:
    config.overlay_screens.append("quick_menu")

default -1 quick_menu = False

init -1 style quick_button is default
init -1 style quick_button_text is button_text

init -1 style quick_button:
    properties gui.button_properties("quick_button")

init -1 style quick_button_text:
    properties gui.button_text_properties("quick_button")

init -501 screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Узнать правду") action Start()

        else:

            textbutton _("История") action ShowMenu("history")

            textbutton _("Запомнить") action ShowMenu("save")

        textbutton _("Вспомнить") action ShowMenu("load")

        textbutton _("Крутилки") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("Завершить повтор") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Главное меню") action MainMenu()

        textbutton _("Об игре") action ShowMenu("about")

        textbutton _("Съебаться") action Quit(confirm=not main_menu)


init -1 style navigation_button is gui_button
init -1 style navigation_button_text is gui_button_text

init -1 style navigation_button_text:
    properties gui.button_text_properties("navigation_button")

init -501 screen main_menublya():
    tag menu


    add gui.main_menu_background

    frame:
        style "main_menu_frame"

    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


init -1 style main_menu_frame is empty
init -1 style main_menu_vbox is vbox
init -1 style main_menu_text is gui_text
init -1 style main_menu_title is main_menu_text
init -1 style main_menu_version is main_menu_text

init -1 style main_menu_frame:
    xsize 280
    yfill True

    background "mod_assets/source/images/gui/overlay/main_menu.png"

init -1 style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

init -1 style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

init -1 style main_menu_title:
    properties gui.text_properties("title")

init -1 style main_menu_version:
    properties gui.text_properties("version")

init -501 screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        has hbox


        frame:
            style "game_menu_navigation_frame"

        frame:
            style "game_menu_content_frame"

            if scroll == "viewport":

                viewport:
                    yinitial yinitial
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    has vbox
                    transclude

            elif scroll == "vpgrid":

                vpgrid:
                    cols 1
                    yinitial yinitial

                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    transclude

            else:

                transclude

    use navigation

    textbutton _("Вернуться"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


init -1 style game_menu_outer_frame is empty
init -1 style game_menu_navigation_frame is empty
init -1 style game_menu_content_frame is empty
init -1 style game_menu_viewport is gui_viewport
init -1 style game_menu_side is gui_side
init -1 style game_menu_scrollbar is gui_vscrollbar

init -1 style game_menu_label is gui_label
init -1 style game_menu_label_text is gui_label_text

init -1 style return_button is navigation_button
init -1 style return_button_text is navigation_button_text

init -1 style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "mod_assets/source/images/gui/overlay/game_menu.png"

init -1 style game_menu_navigation_frame:
    xsize 280
    yfill True

init -1 style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

init -1 style game_menu_viewport:
    xsize 920

init -1 style game_menu_vscrollbar:
    unscrollable gui.unscrollable

init -1 style game_menu_side:
    spacing 10

init -1 style game_menu_label:
    xpos 50
    ysize 120

init -1 style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

init -1 style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30


init -1 python:
    style.settings_link_edit = Style(style.settings_link)
    style.settings_link_edit.size = 30

init -501 screen mods():
    modal True tag menu

    $ bar_null = Frame(get_image("images/gui/ebanoemenu/bar_null.webp"),36,36)
    $ bar_full = Frame(get_image("images/gui/ebanoemenu/bar_full.webp"),36,36)

    window background get_image("images/anim/zatemnenie.webp") xmaximum 1920 ymaximum 1080:
        hbox xalign 0.5 yalign 0.08:
            add get_image("images/gui/ebanoemenu/star.webp") yalign 0.65
            text " "+translation_new["Mods"]+" " style "settings_link" yalign 0.5 color "#ffffff"
            add get_image("images/gui/ebanoemenu/star.webp") yalign 0.65
        textbutton translation_new["Back"]:
            style "log_button"
            text_style "settings_link"
            xalign 0.015 yalign 0.92
            activate_sound start_sound_suka
            hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
            action [Hide("mods"), Show("main_menu")]


        vbox:
            xalign -0.3
            yalign 0.2
            for lbl, name in sorted(mods.items()):
                textbutton name:
                    style "log_button"
                    text_style "settings_link_edit"
                    xpos 500 ypos 50
                    activate_sound start_sound_suka
                    hovered Play("menu_zvuk", "mod_assets/source/audio/sfx/gui/button_menu.ogg")
                    action Start(lbl)



init -502 screen help():

    predict False

    $ xmax = 1000
    $ xposition = 100

    $ history_text_size = 21
    $ history_name_size = 22

    if (persistent.bazarbig):
        $ history_text_size = 26
        $ history_name_size = 27
    else:
        $ history_text_size = 18
        $ history_name_size = 19




    style_prefix "history" tag menu

    window background Frame("mod_assets/source/images/gui/choice_box.png") left_padding 75 right_padding 75 bottom_padding 80 top_padding 80:


        has viewport id "history":
            draggable True
            mousewheel True
            scrollbars "vertical"
            yinitial 1.0

        vbox:

            for h in _history_list:

                if h.who:

                    text h.who:
                        font main_font
                        ypos 20
                        xpos xposition
                        xalign 0.0
                        size history_name_size
                        if "color" in h.who_args:
                            color h.who_args["color"]

                textbutton h.what text_style "normal_day" text_size history_text_size action RollbackToIdentifier(h.rollback_identifier) xpos xposition xmaximum xmax text_hover_color "#40e138"


init -2 style history_window is empty

init -2 style history_name is gui_label
init -2 style history_name_text is gui_label_text
init -2 style history_text is gui_text

init -2 style history_text is gui_text

init -2 style history_label is gui_label
init -2 style history_label_text is gui_label_text

init -2 style history_window:
    xfill True

init -2 style history_name

init -2 style history_name_text:

    xpos gui.history_text_xpos-2

init -2 style history_text:

    line_spacing 15

init -2 style history_label:
    xfill True

init -2 style history_label_text:
    xalign 0.5

init -2 style history_vscrollbar:
    xsize gui.scrollbar_size
    base_bar None
    xoffset -10 thumb "mod_assets/source/images/gui/ebanoemenu/vthumb.webp"

init -2 style history_button:
    focus_mask None



init -502 screen nvl(dialogue, items=None):

    $ timeofday = persistent.timeofday

    window background Frame("mod_assets/source/images/gui/choice_box.png",50,50) xfill True yfill True yalign 0.01 left_padding 0.01 right_padding 0.01 bottom_padding 0.2 top_padding 0.1:
        style "nvl_window"

        has vbox

        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

init -502 screen nvl_dialogue(dialogue):

    for who, what, who_id, what_id, window_id in dialogue:

        window:
            id window_id

            has hbox:
                spacing 10
            if (persistent.bazarbig):
                if who is not None:
                    text who id who_id size 33 font nvl_font
                text what id what_id size 32
            else:
                if who is not None:
                    text who id who_id size 27 font nvl_font
                text what id what_id size 26

define -2 config.nvl_list_length = 20

init -2 style say_label:
    properties gui.text_properties("name", accent=True)

init -2 style say_dialogue:
    properties gui.text_properties("dialogue")

init -2 style nvl_window is default
init -2 style nvl_entry is default

init -2 style nvl_label is say_label
init -2 style nvl_dialogue is say_dialogue

init -2 style nvl_button is button
init -2 style nvl_button_text is button_text

init -2 style nvl_window:
    xfill True
    yfill True

    background None
    padding gui.nvl_borders.padding

init -2 style nvl_entry:
    xfill True
    ysize gui.nvl_height

init -2 style nvl_label:


    ypos gui.nvl_name_ypos
    yanchor 0.0

    xalign -0.1

init -2 style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

init -2 style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

init -2 style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

init -2 style nvl_button_text:
    properties gui.button_text_properties("nvl_button")

init -4 python:

    def edgescroll_proportional(n):
        return

    config.locked = False 
    config.readback_buffer_length = 100 
    config.readback_full = True 
    config.readback_disallowed_tags = ["size"] 
    config.readback_choice_prefix = ">> "   
    config.locked = True


    class ReadbackADVCharacter(ADVCharacter):
        def do_done(self, who, what, multiple=None):
            self.add_history("adv", who, what, multiple=multiple)
            return

    class ReadbackNVLCharacter(NVLCharacter):
        def do_done(self, who, what):
            store_say(who, what)
            store.current_voice = ''
            return


    def say_wrapper(who, what, **kwargs):
        return

    readback_buffer = []
    current_line = None
    current_voice = None

    def store_say(who, what):
        
        say_color = " "
        try:
            say_color = '%02x%02x%02x'
        except:
            pass
        global readback_buffer, current_voice
        new_line = (who, preparse_say_for_store(what), current_voice, say_color)
        readback_buffer = readback_buffer + [new_line]
        readback_prune()

    def store_current_line(who, what):
        
        global current_line, current_voice
        current_line = (who, preparse_say_for_store(what), current_voice, " ")

    disallowed_tags_regexp = ""
    for tag in config.readback_disallowed_tags:
        if disallowed_tags_regexp != "":
            disallowed_tags_regexp += "|"
        disallowed_tags_regexp += "{"+tag+"=.*?}|{"+tag+"}|{/"+tag+"}"

    import re
    remove_tags_expr = re.compile(disallowed_tags_regexp)
    def preparse_say_for_store(input):
        
        global remove_tags_expr
        if input:
            return re.sub(remove_tags_expr, "", input)

    def readback_prune():
        global readback_buffer
        while len(readback_buffer) > config.readback_buffer_length:
            del readback_buffer[0]

    def readback_catcher():
        ui.add(renpy.Keymap(rollback=(SetVariable("yvalue", 1.0), ShowMenu("text_history"))))
        ui.add(renpy.Keymap(rollforward=ui.returns(None)))
