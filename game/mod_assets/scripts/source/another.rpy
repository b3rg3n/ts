# TRUE STORY ANOTHER
# by @b3rg3n
# Since 2024

init -1000 python:

    import os.path

    def get_image(file):
        return "mod_assets/source/%s" % file

init -1199 python:
    from os import path
    mod_prefix = False
    if mod_prefix:
        mod_prefix = '_' + mod_prefix
    else:
        mod_prefix = ''
    modID = 'mod_assets/source/'

    for file in renpy.list_files():
        if modID in file:
            file_name = path.splitext(path.basename(file))[0] + mod_prefix
            if file.endswith((".wav", ".mp2", ".mp3", ".ogg", ".opus")):
                globals()[file_name] = file


init -1001 python:

    renpy.music.register_channel("sound", "sfx", False)
    renpy.music.register_channel("sound2", "sfx", False)
    renpy.music.register_channel("sound3", "sfx", False)
    renpy.music.register_channel("sound4", "sfx", False)
    renpy.music.register_channel("sound_loop", "voice", True)
    renpy.music.register_channel("sound_loop2", "voice", True)
    renpy.music.register_channel("sound_loop3", "voice", True)
    renpy.music.register_channel("ambience", "voice", True)
    renpy.music.register_channel("ambience2", "voice", False)
    renpy.music.register_channel("music2", "music", False)

    def volume(vol, chnl):
        renpy.music.set_volume(vol, channel=chnl)

    def stop_music():
        for chnl in ("sound", "sound2", "sound3", "sound_loop", "sound_loop2", "sound_loop3", "ambience", "music"):
            renpy.music.stop(channel=chnl)

    def stop_sound():
        for chnl in ("sound", "sound2", "sound3", "sound_loop", "sound_loop2", "sound_loop3", "ambience"):
            renpy.sound.stop(channel=chnl)

    def reload_names():
        global store
        for x in store.names_list:
            char_define(x)

init:
#ГОПАЕМ ЮЗЕРНАЙМ
    if renpy.android or renpy.ios:
        $ user = "Игрок"
    else:
        $ user = os.environ.get('username')

    image ru_ground = "mod_assets/source/images/gui/lang/russian_ground.png"
    image ru_hover = "mod_assets/source/images/gui/lang/russian_hover.png"

    image en_ground = "mod_assets/source/images/gui/lang/english_ground.png"
    image en_hover = "mod_assets/source/images/gui/lang/english_hover.png"