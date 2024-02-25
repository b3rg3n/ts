#SR MUSIC WIDGET
#by @b3rg3n & @salotor
#Since 2023
init -1000 python:
    nonsteam_7dl = False
    if nonsteam_7dl == True:
        default_7dl_path = 'mod_assets/source/'
        default_7dl_path_length = 18
    else:
        default_7dl_path = 'mod_assets/source/'
        default_7dl_path_length = 13

init -999 python:
    def get_image_7dl(file):
        return default_7dl_path+"images/gui/%s" % (file)

init -998 python:
    style.button_text_7dl = Style(style.default)
    style.button_text_7dl.color = "#c8ffff"
    style.button_text_7dl.insensitive_color = "#c8c8c8"
    style.button_text_7dl.selected_color = "#ffffc8"
    style.button_text_7dl.text_align = 0.5
    style.button_text_7dl.xalign = 0.5
    style.button_text_7dl.yalign = 0.5
    style.button_text_7dl.ypos = 10
    style.button_text_7dl.xpadding = 6
    style.button_text_7dl.size = 24

    style.button_7dl = Style(style.default)
    style.button_7dl.background = Frame(im.Twocolor(get_image_7dl("rr6g.webp"), "#404040", "#404040"), 8, 8)    
    style.button_7dl.hover_background = Frame(im.Twocolor(get_image_7dl("rr6g.webp"), "#404040", "#404040"), 8, 8)    
    style.button_7dl.insensitive_background = Frame(im.Twocolor(get_image_7dl("rr6g.webp"), "#404040", "#404040"), 8, 8)    
    style.button_7dl.xmargin = 1
    style.button_7dl.xpadding = 6
    style.button_7dl.ymargin = 1
    style.button_7dl.ypadding = 1
    style.button_7dl.ypos = 2

init -997 python:
    style.button_text_music_7dl = Style(style.button_text_7dl)
    style.button_text_music_7dl.font = "mod_assets/source/fonts/1.ttf"
    style.button_text_music_7dl.layout = "nobreak"

python early:
    def check_muzlo_7dl(value):
        for k, v in music_list_ts.items():
            if v == value:
                return k
    def get_playing_7dl(channel='music'):
        m = renpy.music.get_playing(channel=channel)
        if m is not None:
            m = parse_music(m)
        return m
    import re
    def parse_music(mus_string):
        return re.sub('<.*?>', '', str(mus_string))

    def widget_music_7dl():
        if (not persistent.music_widget_7dl):
            return
        else:
            
            m = get_playing_7dl('music')
            
            
            ui.button(clicked=None, style="button_7dl", xpos=0.40, xanchor=0.0, xminimum=133, ysize=27)    
            if m in music_list_ts.values():
                ui.text(check_muzlo_7dl(m)[:50], style="button_text_music_7dl")
            elif m == None:
                ui.text("%s" % "Нет музыки", style="button_text_music_7dl")
            else:
                ui.text("%s" % "Не прописано название", style="button_text_music_7dl")
    config.overlay_functions.append(widget_music_7dl)
