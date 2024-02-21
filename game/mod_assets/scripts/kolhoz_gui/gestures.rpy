#TRUE STORY GESTURES
#by @b3rg3n
#Since 2024
define config.variants = ["phone", "tablet", "touch", "ios", None]

define config.gestures = { "n" : "game_menu",
                           "w" : "help",
                           "e" : "toggle_skip",
                           "s" : "hide_windows"}
init -1700 python:
    _game_menu_screen = "save"
