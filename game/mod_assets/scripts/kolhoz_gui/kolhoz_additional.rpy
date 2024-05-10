# TRUE STORY ADDITIONAL SCREENS
# by @b3rg3n
# Since 2024

screen ts_start_shit_blya: #ПОЯСНЕНИЕ ХУЙНИ ТЕКСТ
    text "{size=+15}{font=[cit_font]}Проведём небольшую{/font}{/size}" yalign 0.475 xalign 0.5 at ts_preferences_anim
    text "{size=+15}{font=[cit_font]}настройку мода.{/font}{/size}" yalign 0.525 xalign 0.5 at ts_preferences_anim

screen ts_cens_changer: # АНТИЦЕНЗОР
    modal True tag aw_r2
    text "{size=+15}{font=[cit_font]}Убрать цензуру?{/font}{/size}" yalign 0.430 xalign 0.5 at ts_preferences_anim
    text "{size=+15}{font=[cit_font]}Если включить - в игре будет{/font}{/size}" yalign 0.480 xalign 0.5 at ts_preferences_anim
    text "{size=+15}{font=[cit_font]}присутствовать нецензурная лексика.{/font}{/size}" yalign 0.530 xalign 0.5 at ts_preferences_anim
    text "{size=+15}{font=[cit_font]}Можно изменить в любой момент игры.{/font}{/size}" yalign 0.580 xalign 0.5 at ts_preferences_anim
    textbutton ("{size=+15}Отключить{/size}") yalign 0.685 xalign 0.35 at ts_preferences_anim:
        activate_sound start_sound_suka
        hover_sound button_menu
        action (SetField(persistent, "cens_mode", False), Jump("ts_intro_settings1"))
    textbutton ("{size=+15}Включить{/size}") yalign 0.685 xalign 0.65 at ts_preferences_anim:
        activate_sound start_sound_suka
        hover_sound button_menu
        action (SetField(persistent, "cens_mode", True), Jump("ts_intro_settings1"))

screen ts_widget_changer: # ВИДЖЕТ ТРЕКОВ БЛЯ
    modal True tag aw_r2
    text "{size=+15}{font=[cit_font]}Включить вывод названий играющих треков?{/font}{/size}" yalign 0.430 xalign 0.5 at ts_preferences_anim
    text "{size=+15}{font=[cit_font]}Они будут показываться в меню быстрого доступа{/font}{/size}" yalign 0.480 xalign 0.5 at ts_preferences_anim
    if renpy.android or renpy.ios:
        text "{size=+15}{font=[cit_font]}которое вызывается свайпом вверх.{/font}{/size}" yalign 0.530 xalign 0.5 at ts_preferences_anim
    else:
        text "{size=+15}{font=[cit_font]}которое вызывается нажатием пкм.{/font}{/size}" yalign 0.530 xalign 0.5 at ts_preferences_anim
    text "{size=+15}{font=[cit_font]}Можно изменить в любой момент игры.{/font}{/size}" yalign 0.580 xalign 0.5 at ts_preferences_anim
    textbutton ("{size=+15}Отключить{/size}") yalign 0.685 xalign 0.35 at ts_preferences_anim:
        activate_sound start_sound_suka
        hover_sound button_menu
        action (SetField(persistent, "music_widget_ts", False), Jump("ts_intro_settings2"))
    textbutton ("{size=+15}Включить{/size}") yalign 0.685 xalign 0.65 at ts_preferences_anim:
        activate_sound start_sound_suka
        hover_sound button_menu
        action (SetField(persistent, "music_widget_ts", True), Jump("ts_intro_settings2"))

screen ts_font_changer: # РАЗМЕР ШРИФТА
    modal True tag aw_r4
    text "{size=+15}{font=[cit_font]}Увеличить размер шрифта?{/font}{/size}" yalign 0.475 xalign 0.5 at ts_preferences_anim
    text "{size=+15}{font=[cit_font]}Или - оставить стандартный?{/font}{/size}" yalign 0.525 xalign 0.5 at ts_preferences_anim
    textbutton ("{size=+15}Стандартный{/size}") yalign 0.685 xalign 0.35 at ts_preferences_anim:
        activate_sound start_sound_suka
        hover_sound button_menu
        action (SetField(persistent, "bazarbig", False), Jump("ts_intro_settings3"))
    textbutton ("{size=+15}Увеличенный{/size}") yalign 0.685 xalign 0.65 at ts_preferences_anim:
        activate_sound start_sound_suka
        hover_sound button_menu
        action (SetField(persistent, "bazarbig", True), Jump("ts_intro_settings3"))

screen ts_set_end_shit_blya: #ПОЯСНЕНИЕ ХУЙНИ ТЕКСТ
    text "{size=+15}{font=[cit_font]}Настройка завершена.{/font}{/size}" yalign 0.475 xalign 0.5 at ts_preferences_anim
    text "{size=+15}{font=[cit_font]}Переходим к истории.{/font}{/size}" yalign 0.525 xalign 0.5 at ts_preferences_anim

screen ts_render_changer: # ЗАМЕНА РЕНДЕРА ЁПТЫТЬ
    modal True tag aw_r2

    text "{size=+15}{font=[cit_font]}Выключить режим энергосбережения?{/font}{/size}" yalign 0.175 xalign 0.5 at ts_preferences_anim
    text "{size=+15}{font=[cit_font]}Возрастает нагрузка на ЦП (+FPS).{/font}{/size}" yalign 0.225 xalign 0.5 at ts_preferences_anim
    textbutton ("{size=+15}Включить{/size}") yalign 0.285 xalign 0.35 at ts_preferences_anim:
        activate_sound start_sound_suka
        hover_sound button_menu
        action (Preference("gl powersave", True), Jump("ts_render_reboot_suka"))
    textbutton ("{size=+15}Отключить{/size}") yalign 0.285 xalign 0.65 at ts_preferences_anim:
        activate_sound start_sound_suka
        hover_sound button_menu
        action (Preference("gl powersave", False), Jump("ts_render_reboot_suka"))

    text "{size=+15}{font=[cit_font]}Изменить рендер?{/font}{/size}" yalign 0.375 xalign 0.5 at ts_preferences_anim
    text "{size=+15}{font=[cit_font]}Работает только на винде.{/font}{/size}" yalign 0.425 xalign 0.5 at ts_preferences_anim
    textbutton ("{size=+15}Авто{/size}") yalign 0.485 xalign 0.30 at ts_preferences_anim:
        activate_sound start_sound_suka
        hover_sound button_menu
        action (_SetRenderer("auto"), Jump("ts_render_reboot_suka"))
    textbutton ("{size=+15}OpenGL{/size}") yalign 0.485 xalign 0.45 at ts_preferences_anim:
        activate_sound start_sound_suka
        hover_sound button_menu
        action (_SetRenderer("gl2"), Jump("ts_render_reboot_suka"))
    textbutton ("{size=+15}DirectX 11{/size}") yalign 0.485 xalign 0.65 at ts_preferences_anim:
        activate_sound start_sound_suka
        hover_sound button_menu
        action (_SetRenderer("angle2"), Jump("ts_render_reboot_suka"))

    text "{size=+15}{font=[cit_font]}Ограничитель кадров{/font}{/size}" yalign 0.575 xalign 0.5 at ts_preferences_anim
    text "{size=+15}{font=[cit_font]}Нагрузка на ЦП возрастает конкретно{/font}{/size}" yalign 0.625 xalign 0.5 at ts_preferences_anim
    textbutton ("{size=+15}Гц Монитора{/size}") yalign 0.685 xalign 0.05 at ts_preferences_anim:
        activate_sound start_sound_suka
        hover_sound button_menu
        action (Preference("gl framerate", None), Jump("ts_render_reboot_suka"))
    textbutton ("{size=+15}360 FPS{/size}") yalign 0.685 xalign 0.30 at ts_preferences_anim:
        activate_sound start_sound_suka
        hover_sound button_menu
        action (Preference("gl framerate", 360), Jump("ts_render_reboot_suka"))
    textbutton ("{size=+15}144 FPS{/size}") yalign 0.685 xalign 0.45 at ts_preferences_anim:
        activate_sound start_sound_suka
        hover_sound button_menu
        action (Preference("gl framerate", 144), Jump("ts_render_reboot_suka"))
    textbutton ("{size=+15}120 FPS{/size}") yalign 0.685 xalign 0.60 at ts_preferences_anim:
        activate_sound start_sound_suka
        hover_sound button_menu
        action (Preference("gl framerate", 120), Jump("ts_render_reboot_suka"))
    textbutton ("{size=+15}60 FPS{/size}") yalign 0.685 xalign 0.75 at ts_preferences_anim:
        activate_sound start_sound_suka
        hover_sound button_menu
        action (Preference("gl framerate", 60), Jump("ts_render_reboot_suka"))
    textbutton ("{size=+15}30 FPS{/size}") yalign 0.685 xalign 0.90 at ts_preferences_anim:
        activate_sound start_sound_suka
        hover_sound button_menu
        action (Preference("gl framerate", 30), Jump("ts_render_reboot_suka"))

    text "{size=+15}{font=[cit_font]}Включить разрыв кадров?{/font}{/size}" yalign 0.775 xalign 0.5 at ts_preferences_anim
    text "{size=+15}{font=[cit_font]}Пропуск кадров, если ЦП не вывозит.{/font}{/size}" yalign 0.825 xalign 0.5 at ts_preferences_anim
    textbutton ("{size=+15}Включить{/size}") yalign 0.885 xalign 0.35 at ts_preferences_anim:
        activate_sound start_sound_suka
        hover_sound button_menu
        action (Preference("gl tearing", True), Jump("ts_render_reboot_suka"))
    textbutton ("{size=+15}Отключить{/size}") yalign 0.885 xalign 0.65 at ts_preferences_anim:
        activate_sound start_sound_suka
        hover_sound button_menu
        action (Preference("gl tearing", False), Jump("ts_render_reboot_suka"))

label ts_render_reboot_suka:
    $ renpy.quit(relaunch=True)

screen ts_credits_list_suka: # ЭКРАН РАЗРАБОВ СУКА
    modal True tag menu
    add ts_anim + "zatemnenie.webp"

    text translation_new["ts_crd_scr10"] style "settings_link" size 75 text_align 0.5 yalign 0.030 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim

    textbutton translation_new["ts_crd_mishlent"] style "log_button" text_style "settings_link" yalign 0.2 xalign 0.5 at ts_preferences_anim:
        activate_sound start_sound_suka
        hover_sound button_menu
        hovered [Show("ts_bergen_credit_info")]
        unhovered Hide("ts_bergen_credit_info")
        if _preferences.language == "english":
            action OpenURL("https://www.reddit.com/user/iamnineoneone/")
        else:
            action OpenURL("https://vk.com/b3rg3n")

    textbutton translation_new["ts_crd_vladick"] style "log_button" text_style "settings_link" yalign 0.4 xalign 0.5 at ts_preferences_anim:
        activate_sound start_sound_suka
        hover_sound button_menu
        hovered [Show("ts_mad_credit_info")]
        unhovered Hide("ts_mad_credit_info")
        if _preferences.language == "english":
            action OpenURL("https://www.reddit.com/user/Neljas/")
        else:
            action OpenURL("https://vk.com/maddiethemad")

    textbutton translation_new["ts_crd_scr9"] style "log_button" text_style "settings_link" yalign 0.6 xalign 0.270 at ts_preferences_anim:
        activate_sound start_sound_suka
        hover_sound button_menu
        hovered [Show("ts_vk_credit_info")]
        unhovered Hide("ts_vk_credit_info")
        action OpenURL("https://vk.com/teamanarkhisty")

    text "{size=+70}{font=[cit_font]}|{/font}{/size}" yalign 0.6 xalign 0.5 at ts_preferences_anim

    textbutton translation_new["ts_crd_scr8"] style "log_button" text_style "settings_link" yalign 0.6 xalign 0.8 at ts_preferences_anim:
        activate_sound start_sound_suka
        hover_sound button_menu
        hovered [Show("ts_ds_credit_info")]
        unhovered Hide("ts_ds_credit_info")
        action OpenURL("https://discord.com/invite/8B3eKkU37q")

    textbutton translation_new["Back"] style "log_button" text_style "settings_link" yalign 0.8 xalign 0.5 at ts_preferences_anim:
        activate_sound start_sound_suka
        hover_sound button_menu
        action [Hide("ts_credits_list_suka"), Show("main_menu")]

screen ts_bergen_credit_info:
    text translation_new["ts_crd_scr1"] style "settings_link" size 50 text_align 0.5 yalign 0.920 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim
    text translation_new["ts_crd_scr2"] style "settings_link" size 50 text_align 0.5 yalign 0.980 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim

screen ts_mad_credit_info:
    text translation_new["ts_crd_scr3"] style "settings_link" size 50 text_align 0.5 yalign 0.920 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim
    text translation_new["ts_crd_scr2"] style "settings_link" size 50 text_align 0.5 yalign 0.980 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim

screen ts_vk_credit_info:
    text translation_new["ts_crd_scr4"] style "settings_link" size 50 text_align 0.5 yalign 0.920 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim
    text translation_new["ts_crd_scr5"] style "settings_link" size 50 text_align 0.5 yalign 0.980 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim

screen ts_ds_credit_info:
    text translation_new["ts_crd_scr6"] style "settings_link" size 50 text_align 0.5 yalign 0.920 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim
    text translation_new["ts_crd_scr7"] style "settings_link" size 50 text_align 0.5 yalign 0.980 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim
