# TRUE STORY ENGINE FUNCTIONS
# by @b3rg3n
# Since 2024

init -1199 python:
    from os import path
    modID = 'mod_assets/source/audio/'

    for file in renpy.list_files(): # ФУНКЦИЯ ГОПА АУДИО БЕЗ ДЕФАЙНА
        if modID in file:
            file_name = path.splitext(path.basename(file))[0]
            if file.endswith((".wav", ".mp2", ".mp3", ".ogg", ".opus")):
                globals()[file_name] = file

    # ПЕРЕМЕННЫЕ ДЛЯ УКОРОТА ПУТИ ДЕФАЙНА
    ts_source = "mod_assets/source/"
    ts_images = ts_source + "images/"
    ts_spr = ts_images + "spr/"
    ts_bg = ts_images + "bg/"
    ts_cg = ts_images + "cg/"
    ts_anim = ts_images + "anim/"
    ts_fonts = ts_source + "fonts/"
    ts_videosos = ts_source + "videosos/"
    ts_muzzon = ts_source + "audio/ost/"
    ts_sfx = ts_source + "audio/sfx/"
    ts_gui = ts_images + "gui/"

init -1001 python:
# РЕГЕСТРИРУЕМ ДОП КАНАЛЫ
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

    def volume(vol, chnl): # ФУНКЦИЯ РЕГУЛИРОВКИ ГРОМКОСТИ ОДНОЙ СТРОКОЙ КОДА
        renpy.music.set_volume(vol, channel=chnl)

    def stop_music(): # ДОБАВЛЯЕМ НОВЫЕ КАНАЛЫ В СТОП МУЗОН
        for chnl in ("sound", "sound2", "sound3", "sound_loop", "sound_loop2", "sound_loop3", "ambience", "music", "music2"):
            renpy.music.stop(channel=chnl)

    def stop_sound(): # ДОБАВЛЯЕМ НОВЫЕ КАНАЛЫ В СТОП ЗВУКИ
        for chnl in ("sound", "sound2", "sound3", "sound_loop", "sound_loop2", "sound_loop3", "ambience", "ambience2"):
            renpy.sound.stop(channel=chnl)

    def get_pos(channel='music'): # ДОБАВЛЯЕМ ВЫЧЕТ ПОЗИЦИИ
        pos = renpy.music.get_pos(channel=channel)
        if pos: return pos
        return 0