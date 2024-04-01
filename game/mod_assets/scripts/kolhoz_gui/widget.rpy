# TRUE STORY MUSIC WIDGET
# by @b3rg3n & @salotor
# Since 2024

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
            globals()['track_checker_blya'] = "empty"
            return
        else:
            
            m = get_playing_ts('music')
            
            
            if m in music_list_ts.values():
                globals()['track_checker_blya'] = check_muzlo_ts(m)[:50]
            elif m == None:
                globals()['track_checker_blya'] = "Нет музыки"
            else:
                globals()['track_checker_blya'] = "Не прописано название трека"
    config.overlay_functions.append(widget_music_ts)

init:
    default track_checker_blya = "empty"