# TRUE STORY TEXT SCREENS
# by @b3rg3n
# Since 2024

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
        "Quit_confirm" : "Уверен?",
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
        "Font" : "Размер текстбокса",
        "Normal_font" : "Обычный",
        "Big_font" : "Большой",
        "Music_widget_set" : "Названия треков",
        "Music_widget_on" : "Включить",
        "Music_widget_off" : "Отключить",
        "Cens_mode_set" : "Антицензор",
        "Cens_mode_off" : "Отключить",
        "Cens_mode_on" : "Включить",

}
