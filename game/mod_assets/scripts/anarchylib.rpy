# ANARCHY LIB
# НАБОР СКРИПТОВ, КОТОРЫЙ УПРОСТИТ ТЕБЕ ЖИЗНЬ:
# ИЗБАВИТ ОТ ЛИШНИХ БОЛЕЙ В АНАЛЬНОМ ОТВЕРСТИИ
# И ПОЗВОЛИТ СОКРАТИТЬ КОЛИЧЕСТВО КОДА 
# by @b3rg3n
# Since 2024

init -1199 python:
# ДОБАВЛЯЕМ ФИЧУ ГОПА АУДИО БЕЗ ДЕФАЙНА
# Т.Е. МОЖНО ПРОСТО ПРОПИСАТЬ В КОДЕ СЦЕНАРИЯ play music hueta (ЕСЛИ В ПАПКЕ ЕСТЬ ФАЙЛ HUETA.MP3(ИЛИ С ДРУГИМ ФОРМАТОМ, ЧТО УКАЗАНЫ НИЖЕ) - ОН ЗАРАБОТАЕТ БЕЗ ДЕФАЙНА)
    import math # НУЖНО ДЛЯ ЭФФЕКТОВ ОРИГА ДОКИ
    import os # НУЖНО ДЛЯ ГОПА ЮЗЕРНЕЙМА
    import getpass # ЭТО ТОЖЕ (работает только на 3 питоне)
    import datetime # НУЖНО ДЛЯ ГОПА ВРЕМЕНИ
    from os import path # ЭТО ДЛЯ ГОПА АУДИО
    import random # НУЖНО ДЛЯ ГЛИТЧТЕКСТА

# ПЕРЕМЕННЫЕ ДЛЯ УКОРОТА ПУТИ ДЕФАЙНА
# МЕНЬШЕ ПОТРЕБЛЯЕТСЯ ПАМЯТИ = МЕНЬШЕ ПРОСАДОК
# ЮЗАТЬ ТАК = image perdun = ts_images + "sheeptune/ebanko.png" (полный путь сократился "mod_assets/source/images/sheeptune/ebanko.png")
    ts_source = "mod_assets/source/"

    ts_fonts = ts_source + "fonts/"

    ts_audio = ts_source + "audio/"
    ts_muzzon = ts_audio + "ost/"
    ts_sfx = ts_audio + "sfx/"

    ts_images = ts_source + "images/"
    ts_spr = ts_images + "spr/"
    ts_bg = ts_images + "bg/"
    ts_cg = ts_images + "cg/"
    ts_anim = ts_images + "anim/"
    ts_gui = ts_images + "gui/"
    ts_gl_bg_path = ts_bg + "glitch/"

    ts_mr = ts_gui + "music_room/art/"

    ts_natsuki_pt = ts_spr + "natsuki/"
    ts_bug_pt = ts_spr + "bug/"
    ts_elena_pt = ts_spr + "elena/"
    ts_himari_pt = ts_spr + "himari/"
    ts_hime_pt = ts_spr + "hime/"
    ts_hiroto_pt = ts_spr + "hiroto/"
    ts_kotonoha_pt = ts_spr + "kotonoha/"
    ts_momika_pt = ts_spr + "momika/"
    ts_monika_pt = ts_spr + "monika/"
    ts_yuri_pt = ts_spr + "yuri/"
    ts_sayori_pt = ts_spr + "sayori/"

    ts_videosos = ts_source + "videosos/"
    ts_telek = ts_videosos + "bg/telek/"

    for file in renpy.list_files(): # ФУНКЦИЯ ГОПА АУДИО БЕЗ ДЕФАЙНА
        if ts_audio in file:
            file_name = path.splitext(path.basename(file))[0]
            if file.endswith((".wav", ".mp2", ".mp3", ".ogg", ".opus")):
                globals()[file_name] = file

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
        img = Text("{size=35}{font=[cit_font]}%0*d:%0*d:%0*d{/font}{/size}" % (2, hours, 2, minutes, 2, seconds))
        return img, .1

init python:
# РЕГЕСТРИРУЕМ ДОП КАНАЛЫ
# ЛИШНИМ НЕ БУДЕТ
# ЮЗАТЬ ТАК = play sound4 peerdune
# З.Ы. - НЕНУЖНЫЕ МОЖЕШЬ ПРОСТО УБРАТЬ
    renpy.music.register_channel("sound", "sfx", False)
    renpy.music.register_channel("sound2", "sfx", False)
    renpy.music.register_channel("sound3", "sfx", False)
    renpy.music.register_channel("sound4", "sfx", False)
    renpy.music.register_channel("sound_loop", "sfx", True)
    renpy.music.register_channel("sound_loop2", "voice", True)
    renpy.music.register_channel("sound_loop3", "voice", True)
    renpy.music.register_channel("ambience", "voice", True)
    renpy.music.register_channel("ambience2", "voice", False)
    renpy.music.register_channel("music2", "music", False)

init python:

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

init python: # ОТДЕЛЬНЫЙ, Т.К. С ОСТАЛЬНЫМИ ЧЁТ НЕ ДЕФАЙНИТ БЛЯ
# ФИЧА С ГЛИТЧТЕКСТОМ
# ВЗЯТО ИЗ ОРИГА ДОКИ (@danslvato)
# ЮЗАТЬ ТАК = $ glitch_hueta_text = glitchtext(12) з.ы - 12 это кол-во символов хуйни (потом [glitch_hueta_text])
    nonunicode = "¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽž"

    def glitchtext(length):
        output = ""
        for x in range(length):
            output += random.choice(nonunicode)
        return output

init:
# ДЕФОЛТНЫЕ ЗНАЧЕНИЯ ПЕРЕМЕННЫХ ДЛЯ ОБЕСЦЕВЕТА И ВРЕМЕНИ СПРАЙТА
    default persistent.sprite_time = 'day'
    default persistent.uncolorize = 'none'
#ГОПАЕМ ЮЗЕРНАЙМ
    if renpy.android or renpy.ios: # ПРОВЕРКА НА КАЛОЗВОНЫ (В ПЕРЕМЕННУЮ МОЖЕШЬ ВПИСАТЬ СВОЙ ВАРИК ЮЗЕРА)
        $ user = "Игрок"
    elif renpy.linux:
        $ user = getpass.getuser() # МЕТОД ГОПА НА ЛИНУКСЕ (ТРЕБУЕТ ТРЕТИЙ ПИТОН, Т.Е. РЕНДРИСТ 8 И НОВЕЕ)
    else:
        $ user = os.environ.get('username') # ДЕДОВСКИЙ МЕТОД ГОПА ЮЗЕРА НА ВИНДЕ

    image gametime = DynamicDisplayable(show_gametime) # ВЫВОД ЗАТРАЧЕННОГО ВРЕМЕНИ - ЮЗАТЬ ТАК = [gametime]

###ТРАНЗИТЫ (ИЗ НАЗВАНИЙ ПОНЯТНО, ЧТО ЭТО ЗА ТРАНЗИТЫ БЛЯ)
    define flash = Fade(.25, 0, .75, color="#fff")
    define flash_red = Fade(1, 0, 1, color="#e11")
    define dspr = Dissolve(.2)
    define dissolve2 = Dissolve(2.0)
    define dissolve3 = Dissolve(3.0)
    define dissolve4 = Dissolve(4)