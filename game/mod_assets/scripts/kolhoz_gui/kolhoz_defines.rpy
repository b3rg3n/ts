# TRUE STORY SCREENS DEFINES
# ТУТ НАХУЙ ЧЁРТ НОГУ СЛОМИТ
# НЕ ЛАЗИЙ СЮДА НАХУЙ
# by @b3rg3n
# Since 2024

init -2:
    $ ctc_pos = 0.995
    $ ctc_pos_nvl = 0.93
    image ctc_animation = Animation("mod_assets/source/images/gui/misc/ctc01.png", 0.15, "mod_assets/source/images/gui/misc/ctc02.png", 0.15, "mod_assets/source/images/gui/misc/ctc03.png", 0.15, "mod_assets/source/images/gui/misc/ctc04.png", 0.15, "mod_assets/source/images/gui/misc/ctc05.png", 0.15, "mod_assets/source/images/gui/misc/ctc06.png", 0.15, "mod_assets/source/images/gui/misc/ctc07.png", 0.15, "mod_assets/source/images/gui/misc/ctc08.png", 0.15, xpos=ctc_pos, ypos=0.99, xanchor=1.0, yanchor=1.0)
    image ctc_animation_nvl = Animation("mod_assets/source/images/gui/misc/ctc01.png", 0.15, "mod_assets/source/images/gui/misc/ctc02.png", 0.15, "mod_assets/source/images/gui/misc/ctc03.png", 0.15, "mod_assets/source/images/gui/misc/ctc04.png", 0.15, "mod_assets/source/images/gui/misc/ctc05.png", 0.15, "mod_assets/source/images/gui/misc/ctc06.png", 0.15, "mod_assets/source/images/gui/misc/ctc07.png", 0.15, "mod_assets/source/images/gui/misc/ctc08.png", 0.15, xpos=ctc_pos_nvl, ypos=0.94, xanchor=1.0, yanchor=1.0)

    $ std_set_for_preview = {}
    $ std_set = {}
    $ store.colors = {}
    $ store.names = {}
    $ store.names_list = []
    $ time_of_day = 'night'
    $ store.names_list.append('narrator')

init -4 python:

    def translate():
        if _preferences.language == "english":
            layout.ARE_YOU_SURE = "Are you sure? "
            layout.DELETE_SAVE = "Are you sure you want to delete this save? "
            layout.OVERWRITE_SAVE = "Are you sure you want to overwrite your save? "
            layout.LOADING = "Loading will lose unsaved progress.\nAre you sure you want to do this? "
            layout.QUIT = "Are you sure you want to quit? "
            layout.MAIN_MENU = "Are you sure you want to return to the main menu?\nThis will lose unsaved progress. "
            layout.SLOW_SKIP = "Are you sure you want to begin skipping? "
            layout.FAST_SKIP_UNSEEN = "Are you sure you want to skip to the next choice? "
            layout.FAST_SKIP_SEEN = "Are you sure you want to skip to unseen dialogue or the next choice? "
        else:
            layout.ARE_YOU_SURE = _("Уверен?")
            layout.DELETE_SAVE = _("Точно хочешь забыть?")
            layout.OVERWRITE_SAVE = _("Точно хочешь перезапомнить?")
            layout.LOADING = _("Если вспомнишь - забудешь, что видел после.\nУверен?")
            layout.QUIT = _("Так скоро тикаешь?")
            layout.MAIN_MENU = _("Вернуться на главную?\nЭабудешь всё, что видел.")
            layout.END_REPLAY = _("Остановить повтор?")
            layout.SLOW_SKIP = _("Промотать всё?")
            layout.FAST_SKIP_UNSEEN = _("Промотать всё до следующего выбора?")
            layout.FAST_SKIP_SEEN = _("Перейти на следующий выбор?")

init -2 python:
    gui.init(1280, 720)

    def translate_names(lang):
        for char in store.names.keys():
            gl = globals()
            gl[char+"_name"] = translation_new[char]

define -2 gui.accent_color = '#ffffff'
define -2 gui.idle_color = '#ffffff'
define -2 gui.idle_small_color = '#aaaaaa'
define -2 gui.hover_color = '#ff0000'
define -2 gui.selected_color = '#ff0000'
define -2 gui.insensitive_color = '#ffffff7f'
define -2 gui.muted_color = '#510000'
define -2 gui.hover_muted_color = '#7a0000'
define -2 gui.text_color = '#ffffff'
define -2 gui.interface_text_color = '#ffffff'

define -2 gui.text_font = "mod_assets/source/fonts/nvl_font.ttf"
define -2 gui.name_text_font = "mod_assets/source/fonts/nvl_font.ttf"
define -2 gui.interface_text_font = "mod_assets/source/fonts/2.ttf"

define -2 gui.text_size = 22
define -2 gui.name_text_size = 30
define -2 gui.interface_text_size = 22
define -2 gui.label_text_size = 24
define -2 gui.notify_text_size = 16
define -2 gui.title_text_size = 50

define -2 gui.main_menu_background = "mod_assets/source/images/gui/main_menu.png"
define -2 gui.game_menu_background = "mod_assets/source/images/gui/game_menu.png"

define -2 gui.textbox_height = 185
define -2 gui.textbox_yalign = 1.0
define -2 gui.name_xpos = 263
define -2 gui.name_ypos = 0
define -2 gui.name_xalign = 0.0
define -2 gui.namebox_width = None
define -2 gui.namebox_height = None
define -2 gui.namebox_borders = Borders(5, 5, 5, 5)
define -2 gui.namebox_tile = False
define -2 gui.dialogue_xpos = 268
define -2 gui.dialogue_ypos = 50
define -2 gui.dialogue_width = 744
define -2 gui.dialogue_text_xalign = 0.0

define -2 gui.button_width = None
define -2 gui.button_height = None
define -2 gui.button_borders = Borders(4, 4, 4, 4)
define -2 gui.button_tile = False
define -2 gui.button_text_font = gui.interface_text_font
define -2 gui.button_text_size = gui.interface_text_size
define -2 gui.button_text_idle_color = gui.idle_color
define -2 gui.button_text_hover_color = gui.hover_color
define -2 gui.button_text_selected_color = gui.selected_color
define -2 gui.button_text_insensitive_color = gui.insensitive_color
define -2 gui.button_text_xalign = 0.0

define -2 gui.radio_button_borders = Borders(18, 4, 4, 4)
define -2 gui.check_button_borders = Borders(18, 4, 4, 4)
define -2 gui.confirm_button_text_xalign = 0.5
define -2 gui.page_button_borders = Borders(10, 4, 10, 4)
define -2 gui.quick_button_borders = Borders(10, 4, 10, 0)
define -2 gui.quick_button_text_size = 14
define -2 gui.quick_button_text_idle_color = gui.idle_small_color
define -2 gui.quick_button_text_selected_color = gui.accent_color

define -2 gui.choice_button_width = 790
define -2 gui.choice_button_height = None
define -2 gui.choice_button_tile = False
define -2 gui.choice_button_borders = Borders(100, 5, 100, 5)
define -2 gui.choice_button_text_font = gui.text_font
define -2 gui.choice_button_text_size = gui.text_size
define -2 gui.choice_button_text_xalign = 0.5
define -2 gui.choice_button_text_idle_color = "#cccccc"
define -2 gui.choice_button_text_hover_color = "#ffffff"
define -2 gui.choice_button_text_insensitive_color = "#444444"

define -2 gui.slot_button_width = 276
define -2 gui.slot_button_height = 206
define -2 gui.slot_button_borders = Borders(10, 10, 10, 10)
define -2 gui.slot_button_text_size = 14
define -2 gui.slot_button_text_xalign = 0.5
define -2 gui.slot_button_text_idle_color = gui.idle_small_color
define -2 gui.slot_button_text_selected_idle_color = gui.selected_color
define -2 gui.slot_button_text_selected_hover_color = gui.hover_color

define -2 config.thumbnail_width = 256
define -2 config.thumbnail_height = 144
define -2 gui.file_slot_cols = 3
define -2 gui.file_slot_rows = 2

define -2 gui.navigation_xpos = 40
define -2 gui.skip_ypos = 10
define -2 gui.notify_ypos = 45
define -2 gui.choice_spacing = 22
define -2 gui.navigation_spacing = 4
define -2 gui.pref_spacing = 10
define -2 gui.pref_button_spacing = 0
define -2 gui.page_spacing = 0
define -2 gui.slot_spacing = 10
define -2 gui.main_menu_text_xalign = 1.0

define -2 gui.frame_borders = Borders(4, 4, 4, 4)
define -2 gui.confirm_frame_borders = Borders(40, 40, 40, 40)
define -2 gui.skip_frame_borders = Borders(16, 5, 50, 5)
define -2 gui.notify_frame_borders = Borders(16, 5, 40, 5)
define -2 gui.frame_tile = False

define -2 gui.bar_size = 25
define -2 gui.scrollbar_size = 12
define -2 gui.slider_size = 25
define -2 gui.bar_tile = False
define -2 gui.scrollbar_tile = False
define -2 gui.slider_tile = False
define -2 gui.bar_borders = Borders(4, 4, 4, 4)
define -2 gui.scrollbar_borders = Borders(4, 4, 4, 4)
define -2 gui.slider_borders = Borders(4, 4, 4, 4)
define -2 gui.vbar_borders = Borders(4, 4, 4, 4)
define -2 gui.vscrollbar_borders = Borders(4, 4, 4, 4)
define -2 gui.vslider_borders = Borders(4, 4, 4, 4)

define -2 gui.unscrollable = "hide"

define -2 gui.language = "unicode"

define -4 gui.nvl_borders = Borders(0, 10, 0, 20)
define -4 gui.nvl_list_length = 6
define -4 gui.nvl_height = 115
define -4 gui.nvl_spacing = 10
define -4 gui.nvl_name_xpos = 165
define -4 gui.nvl_name_ypos = 12
define -4 gui.nvl_name_width = 150
define -4 gui.nvl_name_xalign = 1.0
define -4 gui.nvl_text_xpos = 180
define -4 gui.nvl_text_ypos = 18
define -4 gui.nvl_text_width = 1350
define -4 gui.nvl_text_xalign = 0.0
define -4 gui.nvl_thought_xpos = 240
define -4 gui.nvl_thought_ypos = 0
define -4 gui.nvl_thought_width = 1170
define -4 gui.nvl_thought_xalign = 0.0
define -4 gui.nvl_button_xpos = 174
define -4 gui.nvl_button_xalign = 0.0


define -3 config.narrator_menu = True

define -4 config.history_length = 100

define -4 gui.history_height = 1050

define -4 gui.history_name_xpos = 0
define -4 gui.history_name_ypos = 0
define -4 gui.history_name_width = 0
define -4 gui.history_name_xalign = 0.0

define -4 gui.history_text_xpos = 250
define -4 gui.history_text_ypos = 0
define -4 gui.history_text_width = 1010
define -4 gui.history_text_xalign = 0.0

define -4 gui.nvl_borders = Borders(0, 15, 0, 30)

define -4 gui.nvl_height = None

define -4 gui.nvl_spacing = 8

define -4 gui.nvl_name_xpos = 645
define -4 gui.nvl_name_ypos = 8
define -4 gui.nvl_name_width = 225
define -4 gui.nvl_name_xalign = 1.0

define -4 gui.nvl_text_xpos = 15
define -4 gui.nvl_text_ypos = 12
define -4 gui.nvl_text_width = 1755
define -4 gui.nvl_text_xalign = 0.0

define -4 gui.nvl_thought_xpos = 360
define -4 gui.nvl_thought_ypos = 0
define -4 gui.nvl_thought_width = 1755
define -4 gui.nvl_thought_xalign = 0.0

define -4 gui.nvl_button_xpos = 675
define -4 gui.nvl_button_xalign = 0.0

init -3 style base_font is default
init -3 style base_font:
    font "mod_assets/source/fonts/2.ttf"
    size 19
    line_spacing 2
    color "#ffdd7d"
    drop_shadow (2, 2)
    drop_shadow_color "#000"

init -3 style normal_day is base_font
init -3 style narrator_day is base_font
init -3 style thoughts_day is base_font
init -3 style normal_sunset is base_font
init -3 style narrator_sunset is base_font
init -3 style thoughts_sunset is base_font
init -3 style normal_night is base_font
init -3 style narrator_night is base_font
init -3 style thoughts_night is base_font
init -3 style normal_prolog is base_font
init -3 style narrator_prolog is base_font
init -3 style thoughts_prolog is base_font
