# ANARCHY LIB
# НАБОР СКРИПТОВ, КОТОРЫЙ УПРОСТИТ ТЕБЕ ЖИЗНЬ:
# ИЗБАВИТ ОТ ЛИШНИХ БОЛЕЙ В АНАЛЬНОМ ОТВЕРСТИИ
# И ПОЗВОЛИТ СОКРАТИТЬ КОЛИЧЕСТВО КОДА 
# by @b3rg3n
# Since 2024

init -1199 python:
# ДОБАВЛЯЕМ ФИЧУ ГОПА АУДИО БЕЗ ДЕФАЙНА
# Т.Е. МОЖНО ПРОСТО ПРОПИСАТЬ В КОДЕ СЦЕНАРИЯ play music hueta (ЕСЛИ В ПАПКЕ ЕСТЬ ФАЙЛ HUETA.MP3(ИЛИ С ДРУГИМ ФОРМАТОМ, ЧТО УКАЗАНЫ НИЖЕ) - ОН ЗАРАБОТАЕТ БЕЗ ДЕФАЙНА)
    import os # НУЖНО ДЛЯ ГОПА ЮЗЕРНЕЙМА
    import getpass # ЭТО ТОЖЕ
    import datetime # НУЖНО ДЛЯ ГОПА ВРЕМЕНИ
    from os import path # ЭТО ДЛЯ ГОПА АУДИО

    modID = 'mod_assets/source/audio/' # ПУТЬ, ГДЕ У ТЕБЯ ЛЕЖАТ ЗВУКИ И МУЗОНЫ

    for file in renpy.list_files(): # ФУНКЦИЯ ГОПА АУДИО БЕЗ ДЕФАЙНА
        if modID in file:
            file_name = path.splitext(path.basename(file))[0]
            if file.endswith((".wav", ".mp2", ".mp3", ".ogg", ".opus")):
                globals()[file_name] = file

# ПЕРЕМЕННЫЕ ДЛЯ УКОРОТА ПУТИ ДЕФАЙНА
# МЕНЬШЕ ПОТРЕБЛЯЕТСЯ ПАМЯТИ = МЕНЬШЕ ПРОСАДОК
# ЮЗАТЬ ТАК = image perdun = ts_images + "sheeptune/ebanko.png" (полный путь сократился "mod_assets/source/images/sheeptune/ebanko.png")
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

# РЕГЕСТРИРУЕМ ДОП КАНАЛЫ
# ЛИШНИМ НЕ БУДЕТ
# ЮЗАТЬ ТАК = play sound4 peerdune
# З.Ы. - НЕНУЖНЫЕ МОЖЕШЬ ПРОСТО УБРАТЬ
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

    def volume(vol, chnl): # ФУНКЦИЯ РЕГУЛИРОВКИ ГРОМКОСТИ ОДНОЙ СТРОКОЙ КОДА ($ volume(0.2, sound))
        renpy.music.set_volume(vol, channel=chnl)

    def stop_music(): # ДОБАВЛЯЕМ НОВЫЕ КАНАЛЫ В СТОП МУЗОН (ДАБЫ ОНИ ТОЖЕ СТОПАЛИСЬ НАХ)
        for chnl in ("sound", "sound2", "sound3", "sound_loop", "sound_loop2", "sound_loop3", "ambience", "music", "music2"):
            renpy.music.stop(channel=chnl)

    def stop_sound(): # ДОБАВЛЯЕМ НОВЫЕ КАНАЛЫ В СТОП ЗВУКИ (АНАЛОГИЧНО ВЫШЕ)
        for chnl in ("sound", "sound2", "sound3", "sound_loop", "sound_loop2", "sound_loop3", "ambience", "ambience2"):
            renpy.sound.stop(channel=chnl)

    def get_pos(channel='music'): # ДОБАВЛЯЕМ ВЫЧЕТ ПОЗИЦИИ (ИСПОЛЬЗУЕТСЯ В ДОКИ МОДАХ ДЛЯ СИНХРОНА ХУЙНИ)
        pos = renpy.music.get_pos(channel=channel)
        if pos: return pos
        return 0

# ЗАКОСТЫЛИМ МЕТОД ПОДСЧЁТА ИГРОВОГО ВРЕМЕНИ
# УДАЛЯЕТСЯ ВМЕСТЕ С ПОСТОЯННЫМИ ДАННЫМИ

    persistent.game_last_time = datetime.datetime.now()
    if persistent.gametime is None:
        persistent.gametime = 0
    def show_gametime(st, at):
        t = datetime.datetime.now()
        dt = t - persistent.game_last_time
        persistent.game_last_time = t
        persistent.gametime += dt.total_seconds()
        minutes, seconds = divmod(int(persistent.gametime), 60)
        hours, minutes = divmod(minutes, 60)
        img = Text("{size=+15}{font=[cit_font]}%0*d:%0*d:%0*d{/font}{/size}" % (2, hours, 2, minutes, 2, seconds))
        return img, .1

# АХУЕННАЯ ФИШКА, КОТОРАЯ ПОЗВОЛИТ ТЕБЕ ЮЗАТЬ ATL НА РАЗНЫХ ОВЕРЛЕЯХ
# МЕТОД ВЗЯЛ У БРАТКА С НИКОМ @superrage
# ЮЗАТЬ ТАК = $ TS.Screens(ts_tryaska_hueta_ebanaya) Т.Е. В СКОБКАХ TRANSFORM, ПЕРЕД СКОБКАМИ - НУЖНЫЙ ОВЕРЛЕЙ
# ПРИ НЕОБХОДИМОСТИ МОЖЕШЬ ПРИСРАТЬ СВОЙ
init -15 python in TS:

    def Master(atl):
        renpy.show_layer_at(atl, layer='master')

    def Screens(atl):
        renpy.show_layer_at(atl, layer='screens')

    def Transient(atl):
        renpy.show_layer_at(atl, layer='transient')

    def Overlay(atl):
        renpy.show_layer_at(atl, layer='overlay')

    def Front(atl):
        renpy.show_layer_at(atl, layer='front')


init:
#ГОПАЕМ ЮЗЕРНАЙМ
    if renpy.android or renpy.ios: # ПРОВЕРКА НА КАЛОЗВОНЫ (В ПЕРЕМЕННУЮ МОЖЕШЬ ВПИСАТЬ СВОЙ ВАРИК ЮЗЕРА)
        $ user = "Игрок"
    if renpy.linux:
        $ user = getpass.getuser() # МЕТОД ГОПА НА ЛИНУКСЕ (ТРЕБУЕТ ТРЕТИЙ ПИТОН, Т.Е. РЕНДРИСТ 8 И НОВЕЕ)
    else:
        $ user = os.environ.get('username') # ДЕДОВСКИЙ МЕТОД ГОПА ЮЗЕРА НА ВИНДЕ

    image gametime = DynamicDisplayable(show_gametime) # ВЫВОД ЗАТРАЧЕННОГО ВРЕМЕНИ - ЮЗАТЬ ТАК = [gametime]