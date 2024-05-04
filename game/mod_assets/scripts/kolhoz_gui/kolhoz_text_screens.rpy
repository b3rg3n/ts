# TRUE STORY TEXT SCREENS
# by @b3rg3n
# Since 2024

init -1001 python:
    if _preferences.language == "english":
        translation=translation_en
    else:
        translation=translation_ru

    translation_new=translation


init python:
    def translation_init():
        if _preferences.language == "english":
            translation=translation_en
        else:
            translation=translation_ru
        
        translation_new=translation

init -1002 python:
    translation=translation_ru
    translation_new=translation

    def merge_two_dicts(x, y):
        z = x.copy()
        z.update(y)
        return z
    translation_temp={}
    for i,k in translation.iteritems():
        translation_temp[i]={}
        translation_temp[i][_preferences.language]=k
    translation=merge_two_dicts(translation,translation_temp)

    def get_translation(string):
        renpy.log("%s" % string )
        return translation[string][_preferences.language]

init -1003 python:
    translation_ru = {
        "Quit_confirm" : "Ты хочешь уйти,\nтак и недослушав\nмою историю?",
        "Quit_confirm_bad" : "Ты решил оставить\nвсё как есть?\nСовесть не замучает?",
        "Quit_confirm_good" : "Спасибо за уделённое время.\nВозвращайся скорее.\nНе заставляй меня скучать!",
        "Yes_quit_good" : "Скоро вернусь",
        "No_quit_good" : "Я остаюсь",
        "Yes_quit_bad" : "Прости. Прощай",
        "No_quit_bad" : "Я останусь",
        "Yes_quit" : "Вернусь позже",
        "No_quit" : "Я останусь",
        "Yes" : "Конечно",
        "No" : "Не особо",
        "Noo" : "Передумал",
        "settings" : "НАСТРОЙКИ",
        "LOAD" : "ВСПОМНИТЬ",
        "SAVE" : "ЗАПОМНИТЬ",
        "BACK" : "ВЕРНУТЬСЯ",
        "Back" : "Вернуться?",
        "Save_game" : "Запомнить?",
        "Delete" : "Забыть?",
        "Auto" : "Авто",
        "Empty_slot" : "Пусто",
        "Load_game" : "Вспомнить?",
        "Window_mode" : "Режим экрана",
        "Window_no_change" : "Нельзя изменить тут",
        "Fullscreen" : "Во весь экран",
        "Window" : "В окне",
        "Skip" : "Пропускать",
        "Skip_all" : "Вообще всё",
        "Skip_seen" : "Что уже видел",
        "Volume" : "Громкость",
        "Music_lower" : "Музыка",
        "Sound" : "Звуки",
        "Ambience" : "Фон",
        "Text_speed" : "Скорость текста",
        "Font" : "Размер шрифта",
        "Normal_font" : "Стандартный",
        "Big_font" : "Увеличенный",
        "Music_widget_set" : "Названия треков",
        "Music_widget_on" : "Включить",
        "Music_widget_off" : "Отключить",
        "Cens_mode_set" : "Без цензуры",
        "Cens_mode_off" : "Отключить",
        "Cens_mode_on" : "Включить",
        "Language" : "Язык",
        "Russian" : "Русский",
        "English" : "Английский",

}

    translation_en = {
        "Quit_confirm" : "Ты хочешь уйти,\nтак и недослушав\nмою историю?",
        "Quit_confirm_bad" : "Ты решил оставить\nвсё как есть?\nСовесть не замучает?",
        "Quit_confirm_good" : "Спасибо за уделённое время.\nВозвращайся скорее.\nНе заставляй меня скучать!",
        "Yes_quit_good" : "Скоро вернусь",
        "No_quit_good" : "Я остаюсь",
        "Yes_quit_bad" : "Прости. Прощай",
        "No_quit_bad" : "Я останусь",
        "Yes_quit" : "Вернусь позже",
        "No_quit" : "Я останусь",
        "Yes" : "Yes ",
        "No" : "Nope ",
        "Noo" : "Cancel ",
        "settings" : "SETTINGS ",
        "LOAD" : "recall ",
        "SAVE" : "REMEMBER ",
        "BACK" : "BACK ",
        "Back" : "Back? ",
        "Save_game" : "Save? ",
        "Delete" : "Delete? ",
        "Auto" : "Auto ",
        "Empty_slot" : "Empty ",
        "Load_game" : "REMEMBER? ",
        "Window_mode" : "Window mode",
        "Window_no_change" : "Нельзя изменить тут",
        "Fullscreen" : "Fullscreen ",
        "Window" : "Windowed",
        "Skip" : "Skip",
        "Skip_all" : "All",
        "Skip_seen" : "Seen",
        "Volume" : "Volume ",
        "Music_lower" : "Music",
        "Sound" : "Sounds",
        "Ambience" : "Ambience ",
        "Text_speed" : "Text Speed",
        "Font" : "Font Size",
        "Normal_font" : "Standart",
        "Big_font" : "Biggest",
        "Music_widget_set" : "Music Widget",
        "Music_widget_on" : "On  ",
        "Music_widget_off" : "Off ",
        "Cens_mode_set" : "Without cens",
        "Cens_mode_off" : "Off  ",
        "Cens_mode_on" : "On ",
        "Language" : "Language",
        "Russian" : "Russian",
        "English" : "English",

}
