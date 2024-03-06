# TRUE STORY MUSIC WIDGET
# by @b3rg3n & @salotor
# Since 2024

init -998 python:
    style.button_text_ts = Style(style.default)
    style.button_text_ts.color = "#c8ffff"
    style.button_text_ts.insensitive_color = "#c8c8c8"
    style.button_text_ts.selected_color = "#ffffc8"
    style.button_text_ts.text_align = 0.5
    style.button_text_ts.xalign = 0.5
    style.button_text_ts.yalign = 0.5
    style.button_text_ts.ypos = 10
    style.button_text_ts.xpadding = 6
    style.button_text_ts.size = 24

    style.button_ts = Style(style.default)
    style.button_ts.background = Frame(im.Twocolor(("mod_assets/source/images/gui/widgetovr.webp"), "#404040", "#404040"), 8, 8)    
    style.button_ts.hover_background = Frame(im.Twocolor(("mod_assets/source/images/gui/widgetovr.webp"), "#404040", "#404040"), 8, 8)    
    style.button_ts.insensitive_background = Frame(im.Twocolor(("mod_assets/source/images/gui/widgetovr.webp"), "#404040", "#404040"), 8, 8)    
    style.button_ts.xmargin = 1
    style.button_ts.xpadding = 6
    style.button_ts.ymargin = 1
    style.button_ts.ypadding = 1
    style.button_ts.ypos = 2

init -997 python:
    style.button_text_music_ts = Style(style.button_text_ts)
    style.button_text_music_ts.font = "mod_assets/source/fonts/1.ttf"
    style.button_text_music_ts.layout = "nobreak"

python early:
    def check_muzlo_ts(value):
        for k, v in music_list_ts.items():
            if v == value:
                return k
    def get_playing_ts(channel='music'):
        m = renpy.music.get_playing(channel=channel)
        if m is not None:
            m = parse_music(m)
        return m
    import re
    def parse_music(mus_string):
        return re.sub('<.*?>', '', str(mus_string))

    def widget_music_ts():
        if (not persistent.music_widget_ts):
            return
        else:
            
            m = get_playing_ts('music')
            
            
            ui.button(clicked=None, style="button_ts", xpos=0.40, xanchor=0.0, xminimum=133, ysize=27)    
            if m in music_list_ts.values():
                ui.text(check_muzlo_ts(m)[:50], style="button_text_music_ts")
            elif m == None:
                ui.text("%s" % "Нет музыки", style="button_text_music_ts")
            else:
                ui.text("%s" % "Оригинальный DDLC OST", style="button_text_music_ts")
    config.overlay_functions.append(widget_music_ts)
