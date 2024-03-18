# TRUE STORY TEXTBOX COLOR
# ГОПНУЛ ИЗ MND
# СПАСИБО, ВАСЯ, ЕБАТЬ
# by @b3rg3n & @gesundhelt
# Since 2024

init python:

    txcolorchange = True
    pps = 1
    status_color = "#fff"
    status_color_custom = "#fff"

    def ts_status():
        global status_color
        global status_color_custom
        if not txcolorchange or pps <= 0:
            status_color = status_color_custom or "#ffffff"
        elif pps == 1: # БЕЛЫЙ
            status_color = "#ffffff"
            status_color_custom = "#ffffff"
        elif pps == 2: # КРАСНЫЙ
            status_color = "#ff0000"
            status_color_custom = "#ffffff"
        elif pps == 3: # ЖЁЛТЫЙ
            status_color = "#fbff00"
            status_color_custom = "#ffffff"
        elif pps == 4: # ОРАНЖЕВЫЙ
            status_color = "#ff8800"
            status_color_custom = "#ffffff"

    while ts_status in config.window_overlay_functions:
        config.window_overlay_functions.remove(ts_status)
    config.window_overlay_functions.append(ts_status)
