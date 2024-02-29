#TRUE STORY GESTURES
#by @b3rg3n
#Since 2024

define config.variants = ["phone", "tablet", "touch", "ios", None]

define config.gestures = { "n" : "game_menu", # СВАЙП ВВЕРХ - QUICK MENU
                           "w" : "help", # СВАЙП ВЛЕВО - ЭКРАН ИСТОРИИ
                           "e" : "toggle_skip", # СВАЙП ВПРАВО - СКИП
                           "s" : "hide_windows"} # СВАЙП ВНИЗ - СКРЫТЬ ИНТЕРФЕЙС
init -1700 python:
    _game_menu_screen = "save"
