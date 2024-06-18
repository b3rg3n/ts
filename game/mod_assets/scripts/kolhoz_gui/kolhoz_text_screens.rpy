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
        "LOAD" : "Выбери воспоминание",
        "SAVE" : "Что будешь запоминать?",
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
        "Skippinghueta" : "Перематываю",
        "fix_hueta_energy" : "Энергосбережение",
        "fix_hueta_tearing" : "Разрыв кадров",
        "BG" : "Фоны",
        "CG" : "Арты",

        "ts_powersave_info1" : "Настройка режима энергосбережения RenPy.\nОтключите, если наблюдаете лаги эффектов.\nВозрастает нагрузка на ЦП\n(и нагрев, соответственно).",
        "ts_tearing_info1" : "Настройка разрыва кадров RenPy.\nВключите, если ваш процессор не вывозит рендер\nсцены и наблюдаются лаги переходов.\nИспользовать с осторожностью.",
        "ts_anticens_info1" : "Убрать цензуру?\nЕсли включить - в игре будет\nприсутствовать нецензурная лексика.\nМожно изменить в любой момент игры.",
        "ts_muzzon_info1" : "Включить вывод названий играющих треков?\nОни будут показываться в меню быстрого доступа\nкоторое вызывается свайпом вверх.\nМожно изменить в любой момент игры.",
        "ts_muzzon_info2" : "Включить вывод названий играющих треков?\nОни будут показываться в меню быстрого доступа\nкоторое вызывается нажатием ПКМ.\nМожно изменить в любой момент игры.",

        "ts_crd_scr1" : "Код, эффекты, интерфейс, визуал, порт, тестирование.",
        "ts_crd_scr2" : "Нажми на кнопку чтобы открыть ВК.",
        "ts_crd_scr3" : "Сценарий, редактура, перевод на английский.",
        "ts_crd_scr4" : "Тут можно обратиться за техподдержкой",
        "ts_crd_scr5" : "и посмотреть остальные наши моды/переводы.",
        "ts_crd_scr6" : "Тут можно пообщаться с участниками сообщества",
        "ts_crd_scr7" : "и просто хорошо провести время.",
        "ts_crd_scr8" : "Сервер Discord",
        "ts_crd_vladick" : "Maddie, The Mad",
        "ts_crd_mishlent" : "BERGEN",
        "ts_crd_scr9" : "Группа в ВК",
        "ts_crd_scr10" : "Разработчики мода",

        "ts_intro_set1" : "Переходим к истории.",
        "ts_intro_set2" : "Настройка завершена.",
        "ts_intro_set3" : "Увеличить размер шрифта?",
        "ts_intro_set4" : "Или - оставить стандартный?",
        "ts_intro_set5" : "Включить вывод названий играющих треков?",
        "ts_intro_set6" : "Они будут показываться в меню быстрого доступа",
        "ts_intro_set7" : "которое вызывается свайпом вверх.",
        "ts_intro_set8" : "которое вызывается нажатием пкм.",
        "ts_intro_set9" : "Можно изменить в любой момент игры.",
        "ts_intro_set10" : "Убрать цензуру?",
        "ts_intro_set11" : "Если включить - в игре будет",
        "ts_intro_set12" : "присутствовать нецензурная лексика.",
        "ts_intro_set13" : "Можно изменить в любой момент игры.",
        "ts_intro_set14" : "Проведём небольшую",
        "ts_intro_set15" : "настройку мода.",

        "ts_dop_set1" : "Дополнительно",
        "ts_dop_set2" : "Ссылки",
        "ts_dop_set3" : "Саундтрек",
        "ts_dop_set4" : "Галерея",

        "ts_splash_set1" : "Запрещено для несовершеннолетних и",
        "ts_splash_set2" : "для слишком впечатлительных особ.",
        "ts_splash_set3" : "Яркие вспышки света и мелькающие изображения могут навредить",
        "ts_splash_set4" : "людям с высокой светочувствительностью и страдающим эпилепсией.",
        "ts_splash_set5" : "Права на использованные в моде материалы",
        "ts_splash_set6" : "принадлежат их авторам.",
        "ts_splash_set7" : "Мод никак не связан с Team Salvato.",
        "ts_splash_set8" : "Оригинальные файлы лежат на ddlc.moe",
        "ts_splash_set9" : "Ты всё ещё хочешь в это играть?",
        "ts_splash_set10" : "Серьёзно?",
        "ts_splash_set11" : "Не боишься <<сильно впечатлиться>>?",
        "ts_splash_set12" : "И не говори потом,",
        "ts_splash_set13" : "что я тебя не предупреждала.",
        "ts_splash_set14" : "Выход",
        "ts_splash_set15" : "Продолжить",

        "ts_menu_set1" : "True Story",
        "ts_menu_set2" : "Воскреснуть",
        "ts_menu_set3" : "Теперь",
        "ts_menu_set4" : "Ещё разок?",
        "ts_menu_set5" : "Сойти с ума",
        "ts_menu_set6" : "Все",
        "ts_menu_set7" : "Будут",
        "ts_menu_set8" : "Счастливы",
        "ts_menu_set9" : "Вспомнить",
        "ts_menu_set10" : "Настройки",
        "ts_menu_set11" : "Дополнительно",
        "ts_menu_set12" : "Сбежать",
        "ts_menu_set13" : "Ты доволен результатом?",
        "ts_menu_set14" : "Режим разработчика",
        "ts_menu_set15" : "Это всё - твоя вина.",
        "ts_menu_set16" : "На главную",
        "ts_menu_set17" : "Запомнить",
        "ts_menu_set18" : "Сходишь с ума уже",
        "ts_menu_set19" : "ТЫ ДОЛЖНА УМЕРЕТЬ",

        "ts_menu_mus1" : "Сейчас ничего не играет",
        "ts_menu_mus2" : "Список треков",

        "ts_credits_ending1" : "Идея:",
        "ts_credits_ending2" : "Сценарий:",
        "ts_credits_ending3" : "Визуал:",

        "ts_govno_text1" : "Начнём сначала? Или выберешь главу?",
        "ts_govno_text2" : "Начать с пролога",
        "ts_govno_text3" : "Акт первый:",
        "ts_govno_text4" : "Первая глава",
        "ts_govno_text5" : "Вторая глава",
        "ts_govno_text6" : "Третья глава",
        "ts_govno_text7" : "Четвёртая глава",
        "ts_govno_text8" : "Акт второй:",
        "ts_govno_text9" : "Акт третий:",
        "ts_govno_text10" : "Сделай нужные выборы.",
        "ts_govno_text11" : "Направляемся в нужное место."

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
        "Yes" : "Конечно",
        "No" : "Не особо",
        "Noo" : "Передумал",
        "settings" : "НАСТРОЙКИ",
        "LOAD" : "Выбери воспоминание",
        "SAVE" : "Что будешь запоминать?",
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
        "Skippinghueta" : "Перематываю",
        "fix_hueta_energy" : "Энергосбережение",
        "fix_hueta_tearing" : "Разрыв кадров",



        "ts_crd_scr1" : "Код, эффекты, интерфейс, визуал, порт, тестирование.",
        "ts_crd_scr2" : "Нажми на кнопку чтобы открыть ВК.",
        "ts_crd_scr3" : "Сценарий, редактура, перевод на английский.",
        "ts_crd_scr4" : "Тут можно обратиться за техподдержкой",
        "ts_crd_scr5" : "и посмотреть остальные наши моды/переводы.",
        "ts_crd_scr6" : "Тут можно пообщаться с участниками сообщества",
        "ts_crd_scr7" : "и просто хорошо провести время.",
        "ts_crd_scr8" : "Сервер Discord",
        "ts_crd_vladick" : "Maddie, The Mad",
        "ts_crd_mishlent" : "BERGEN",
        "ts_crd_scr9" : "Группа в ВК",
        "ts_crd_scr10" : "Разработчики мода",

        "ts_intro_set1" : "Переходим к истории.",
        "ts_intro_set2" : "Настройка завершена.",
        "ts_intro_set3" : "Увеличить размер шрифта?",
        "ts_intro_set4" : "Или - оставить стандартный?",
        "ts_intro_set5" : "Включить вывод названий играющих треков?",
        "ts_intro_set6" : "Они будут показываться в меню быстрого доступа",
        "ts_intro_set7" : "которое вызывается свайпом вверх.",
        "ts_intro_set8" : "которое вызывается нажатием пкм.",
        "ts_intro_set9" : "Можно изменить в любой момент игры.",
        "ts_intro_set10" : "Убрать цензуру?",
        "ts_intro_set11" : "Если включить - в игре будет",
        "ts_intro_set12" : "присутствовать нецензурная лексика.",
        "ts_intro_set13" : "Можно изменить в любой момент игры.",
        "ts_intro_set14" : "Проведём небольшую",
        "ts_intro_set15" : "настройку мода.",

        "ts_splash_set1" : "Запрещено для несовершеннолетних и",
        "ts_splash_set2" : "для слишком впечатлительных особ.",
        "ts_splash_set3" : "Яркие вспышки света и мелькающие изображения могут навредить",
        "ts_splash_set4" : "людям с высокой светочувствительностью и страдающим эпилепсией.",
        "ts_splash_set5" : "Права на использованные в моде материалы",
        "ts_splash_set6" : "принадлежат их авторам.",
        "ts_splash_set7" : "Мод никак не связан с Team Salvato.",
        "ts_splash_set8" : "Оригинальные файлы лежат на ddlc.moe",
        "ts_splash_set9" : "Ты всё ещё хочешь в это играть?",
        "ts_splash_set10" : "Серьёзно?",
        "ts_splash_set11" : "Не боишься <<сильно впечатлиться>>?",
        "ts_splash_set12" : "И не говори потом,",
        "ts_splash_set13" : "что я тебя не предупреждала.",
        "ts_splash_set14" : "Выход",
        "ts_splash_set15" : "Продолжить",

        "ts_menu_set1" : "True Story",
        "ts_menu_set2" : "Воскреснуть",
        "ts_menu_set3" : "Теперь",
        "ts_menu_set4" : "Ещё разок?",
        "ts_menu_set5" : "Сойти с ума",
        "ts_menu_set6" : "Все",
        "ts_menu_set7" : "Будут",
        "ts_menu_set8" : "Счастливы",
        "ts_menu_set9" : "Вспомнить",
        "ts_menu_set10" : "Настройки",
        "ts_menu_set11" : "Разработчики",
        "ts_menu_set12" : "Сбежать",
        "ts_menu_set13" : "Ты доволен результатом?",
        "ts_menu_set14" : "Режим разработчика",
        "ts_menu_set15" : "Это всё - твоя вина.",
        "ts_menu_set16" : "На главную",
        "ts_menu_set17" : "Запомнить",
        "ts_menu_set18" : "Сходишь с ума уже",
        "ts_menu_set19" : "YOU WILL DIE",

        "ts_credits_ending1" : "Идея:",
        "ts_credits_ending2" : "Сценарий:",
        "ts_credits_ending3" : "Визуал:",

        "ts_govno_text1" : "Начнём сначала? Или выберешь главу?",
        "ts_govno_text2" : "Начать с пролога",
        "ts_govno_text3" : "Акт первый:",
        "ts_govno_text4" : "Первая глава",
        "ts_govno_text5" : "Вторая глава",
        "ts_govno_text6" : "Третья глава",
        "ts_govno_text7" : "Четвёртая глава",
        "ts_govno_text8" : "Акт второй:",
        "ts_govno_text9" : "Акт третий:",
        "ts_govno_text10" : "Сделай нужные выборы.",
        "ts_govno_text11" : "Направляемся в нужное место."

}
