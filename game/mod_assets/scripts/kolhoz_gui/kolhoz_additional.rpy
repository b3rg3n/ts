# TRUE STORY ADDITIONAL SCREENS
# by @b3rg3n
# Since 2024

screen ts_start_shit_blya: #ПОЯСНЕНИЕ ХУЙНИ ТЕКСТ
    text translation_new["ts_intro_set14"] style "settings_link" size 50 text_align 0.5 yalign 0.465 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim
    text translation_new["ts_intro_set15"] style "settings_link" size 50 text_align 0.5 yalign 0.545 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim

screen ts_cens_changer: # АНТИЦЕНЗОР
    modal True tag aw_r2

    text translation_new["ts_intro_set10"] style "settings_link" size 50 text_align 0.5 yalign 0.230 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim
    text translation_new["ts_intro_set11"] style "settings_link" size 50 text_align 0.5 yalign 0.320 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim
    text translation_new["ts_intro_set12"] style "settings_link" size 50 text_align 0.5 yalign 0.410 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim
    text translation_new["ts_intro_set13"] style "settings_link" size 50 text_align 0.5 yalign 0.500 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim

    textbutton translation_new["Cens_mode_off"] style "log_button" text_style "settings_link" yalign 0.685 xalign 0.35 at ts_preferences_anim:
        activate_sound start_sound_suka
        hover_sound button_menu
        action (SetField(persistent, "cens_mode", False), Jump("ts_intro_settings1"))

    textbutton translation_new["Cens_mode_on"] style "log_button" text_style "settings_link" yalign 0.685 xalign 0.65 at ts_preferences_anim:
        activate_sound start_sound_suka
        hover_sound button_menu
        action (SetField(persistent, "cens_mode", True), Jump("ts_intro_settings1"))

screen ts_widget_changer: # ВИДЖЕТ ТРЕКОВ БЛЯ
    modal True tag aw_r2

    text translation_new["ts_intro_set5"] style "settings_link" size 50 text_align 0.5 yalign 0.230 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim
    text translation_new["ts_intro_set6"] style "settings_link" size 50 text_align 0.5 yalign 0.320 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim

    if renpy.android or renpy.ios:
        text translation_new["ts_intro_set7"] style "settings_link" size 50 text_align 0.5 yalign 0.410 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim
    else:
        text translation_new["ts_intro_set8"] style "settings_link" size 50 text_align 0.5 yalign 0.410 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim

    text translation_new["ts_intro_set9"] style "settings_link" size 50 text_align 0.5 yalign 0.500 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim


    textbutton translation_new["Cens_mode_off"] style "log_button" text_style "settings_link" yalign 0.685 xalign 0.3 at ts_preferences_anim:
        activate_sound start_sound_suka
        hover_sound button_menu
        action (SetField(persistent, "music_widget_ts", False), Jump("ts_intro_settings2"))

    textbutton translation_new["Cens_mode_on"] style "log_button" text_style "settings_link" yalign 0.685 xalign 0.7 at ts_preferences_anim:
        activate_sound start_sound_suka
        hover_sound button_menu
        action (SetField(persistent, "music_widget_ts", True), Jump("ts_intro_settings2"))

screen ts_font_changer: # РАЗМЕР ШРИФТА
    modal True tag aw_r4

    text translation_new["ts_intro_set3"] style "settings_link" size 50 text_align 0.5 yalign 0.465 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim
    text translation_new["ts_intro_set4"] style "settings_link" size 50 text_align 0.5 yalign 0.545 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim


    textbutton translation_new["Normal_font"] style "log_button" text_style "settings_link" yalign 0.685 xalign 0.3 at ts_preferences_anim:
        activate_sound start_sound_suka
        hover_sound button_menu
        action (SetField(persistent, "bazarbig", False), Jump("ts_intro_settings3"))

    textbutton translation_new["Big_font"] style "log_button" text_style "settings_link" yalign 0.685 xalign 0.7 at ts_preferences_anim:
        activate_sound start_sound_suka
        hover_sound button_menu
        action (SetField(persistent, "bazarbig", True), Jump("ts_intro_settings3"))

screen ts_set_end_shit_blya: #ПОЯСНЕНИЕ ХУЙНИ ТЕКСТ
    text translation_new["ts_intro_set1"] style "settings_link" size 50 text_align 0.5 yalign 0.465 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim
    text translation_new["ts_intro_set2"] style "settings_link" size 50 text_align 0.5 yalign 0.545 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim

screen ts_dop_list_suka: # ЭКРАН ДОП ХУЙНИ СУКА
    modal True tag menu
    add ts_anim + "zatemnenie.webp"

    text translation_new["ts_dop_set1"] style "settings_link" size 75 text_align 0.5 yalign 0.030 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim

    textbutton translation_new["ts_dop_set2"] style "log_button" text_style "settings_link" yalign 0.2 xalign 0.5 at ts_preferences_anim:
        activate_sound start_sound_suka
        hover_sound button_menu
        action ShowMenu('ts_credits_list_suka')

    textbutton translation_new["ts_dop_set3"] style "log_button" text_style "settings_link" yalign 0.4 xalign 0.5 at ts_preferences_anim:
        activate_sound start_sound_suka
        hover_sound button_menu
        action ShowMenu("music_room", mr=music_room)

    textbutton translation_new["ts_dop_set4"] style "log_button" text_style "settings_link" yalign 0.6 xalign 0.5 at ts_preferences_anim:
        activate_sound start_sound_suka
        hover_sound button_menu
        action ShowMenu('gallery')#NullAction()

    textbutton translation_new["Back"] style "log_button" text_style "settings_link" yalign 0.8 xalign 0.5 at ts_preferences_anim:
        activate_sound start_sound_suka
        hover_sound button_menu
        action Return()

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
        action Return()

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

screen ts_font_info:
    text translation_new["ts_font_info1"] style "settings_link" size 30 text_align 0.5 yalign 0.7 xalign 0.93 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim

screen ts_lang_info:
    if _preferences.language == "english":
        text translation_new["ts_lang_info1"] style "settings_link" size 30 text_align 0.5 yalign 0.7 xalign 0.845 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim
    else:
        text translation_new["ts_lang_info1"] style "settings_link" size 30 text_align 0.5 yalign 0.7 xalign 0.83 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim

screen ts_powersave_info:
    text translation_new["ts_powersave_info1"] style "settings_link" size 30 text_align 0.5 yalign 0.7 xalign 0.93 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim

screen ts_tearing_info:
    text translation_new["ts_tearing_info1"] style "settings_link" size 30 text_align 0.5 yalign 0.7 xalign 0.93 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim

screen ts_rpc_info_sooqa:
    if _preferences.language == "english":
        text translation_new["ts_dicord_rpc_info1"] style "settings_link" size 30 text_align 0.5 yalign 0.7 xalign 0.88 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim
    else:
        text translation_new["ts_dicord_rpc_info1"] style "settings_link" size 30 text_align 0.5 yalign 0.7 xalign 0.93 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim

screen ts_window_info:
    if _preferences.language == "english":
        text translation_new["ts_window_info1"] style "settings_link" size 30 text_align 0.5 yalign 0.7 xalign 0.88 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim
    else:
        text translation_new["ts_window_info1"] style "settings_link" size 30 text_align 0.5 yalign 0.7 xalign 0.93 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim

screen ts_skip_info:
    if renpy.android or renpy.ios:
        text translation_new["ts_skip_info11"] style "settings_link" size 30 text_align 0.5 yalign 0.7 xalign 0.88 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim
    else:
        text translation_new["ts_skip_info1"] style "settings_link" size 30 text_align 0.5 yalign 0.7 xalign 0.88 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim

screen ts_anticens_info:
    text translation_new["ts_anticens_info1"] style "settings_link" size 30 text_align 0.5 yalign 0.7 xalign 0.93 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim

screen ts_muzzon_info:
    if renpy.android or renpy.ios:
        text translation_new["ts_muzzon_info1"] style "settings_link" size 30 text_align 0.5 yalign 0.7 xalign 0.93 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim
    else:
        text translation_new["ts_muzzon_info2"] style "settings_link" size 30 text_align 0.5 yalign 0.7 xalign 0.93 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim

screen ts_control_help_suka:
    if renpy.android:
        text translation_new["ts_ctr_help1"] style "settings_link" size 50 text_align 0.5 yalign 0.400 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim
        text translation_new["ts_ctr_help2"] style "settings_link" size 50 text_align 0.5 yalign 0.475 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim
        text translation_new["ts_ctr_help3"] style "settings_link" size 50 text_align 0.5 yalign 0.550 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim
        text translation_new["ts_ctr_help4"] style "settings_link" size 50 text_align 0.5 yalign 0.625 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim
    else:
        text translation_new["ts_ctr_help5"] style "settings_link" size 40 text_align 0.5 yalign 0.400 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim
        text translation_new["ts_ctr_help6"] style "settings_link" size 40 text_align 0.5 yalign 0.475 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim
        text translation_new["ts_ctr_help7"] style "settings_link" size 40 text_align 0.5 yalign 0.550 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim
        text translation_new["ts_ctr_help8"] style "settings_link" size 40 text_align 0.5 yalign 0.625 xalign 0.5 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim
    textbutton translation_new["ts_understand"] style "log_button" text_style "settings_link" yalign 0.8 xalign 0.5 at ts_preferences_anim:
        activate_sound start_sound_suka
        hover_sound button_menu
        action Return()