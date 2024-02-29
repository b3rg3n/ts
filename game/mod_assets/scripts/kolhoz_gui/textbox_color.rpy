# TRUE STORY TEXTBOX COLOR
# ГОПНУЛ ИЗ MND
# СПАСИБО, ВАСЯ, ЕБАТЬ
# by @b3rg3n & @gesundhelt
# Since 2024

init python:

    showstatus = False
    pps = 1
    status_name = ""
    status_color = "#fff"
    status_color_custom = "#fff"
    def mnd_status():
        global status_name
        global status_color
        global status_color_custom
        if not showstatus or pps <= 0:
            status_name = ""
            status_color = status_color_custom or "#ffffff"
        elif pps == 1: # БЕЛЫЙ
            status_name = " "
            status_color = "#ffffff"
            status_color_custom = "#ffffff"
        elif pps == 2: # КРАСНЫЙ
            status_name = " "
            status_color = "#ff0000"
            status_color_custom = "#ffffff"
        elif pps == 3: # ЖЁЛТЫЙ
            status_name = " "
            status_color = "#fbff00"
            status_color_custom = "#ffffff"
        elif pps == 4: # ОРАНЖЕВЫЙ
            status_name = " "
            status_color = "#ff8800"
            status_color_custom = "#ffffff"
        elif pps == 5: # ФИОЛЕТОВЫЙ
            status_name = " "
            status_color = "#ff00c8"
            status_color_custom = "#ffffff"
        elif pps == 6: # СИНИЙ
            status_name = " "
            status_color = "#2600ff"
            status_color_custom = "#ffffff"

    while mnd_status in config.window_overlay_functions:
        config.window_overlay_functions.remove(mnd_status)
    config.window_overlay_functions.append(mnd_status)
