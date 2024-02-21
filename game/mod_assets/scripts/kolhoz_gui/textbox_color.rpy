#SR TEXTBOX COLOR & ROUTE NAME
#by @b3rg3n & @gesundheit
#Since 2023
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
        elif pps == 1: #Белый
            status_name = "Skitetsky Remaster"
            status_color = "#ffffff"
            status_color_custom = "#ffffff"
        elif pps == 11: #Белый
            status_name = "JOZEF Remaster"
            status_color = "#ffffff"
            status_color_custom = "#ffffff"

    while mnd_status in config.window_overlay_functions:
        config.window_overlay_functions.remove(mnd_status)
    config.window_overlay_functions.append(mnd_status)
