# ХУЕТА ДЛЯ ТЕСТОВ
label testing_label_blya:

    python: # ОБНОВЛЯЕМ RPC
        ts_rpc_development()

    scene black
    window hide
    pause 1
    $ Chapter("True Story")
    $ Chapter("True Story")

    $ Chapter("Be available on october")
    $ Chapter("Be available on october")

    pause 1.0

    show layer screens at ts_showscreens

    show ts_credits_fedya_1 at ts_show_credits_videosos_fedya
    show ts_credits_cg_1 at ts_show_credits_videosos_cg

    #show screen ts_good_credits_scr_1
    #show screen ts_good_credits_scr_11

    show screen ts_good_credits_scr_3
    show screen ts_good_credits_scr_33

    pause

    scene white
    $ persistent.sprite_time = "day"
    show sayori 4z at t41
    show yuri 4f at t42
    show monika 1f at t43
    show natsuki 1e at t44
    show layer master at ts_trns_chromAbber
    "day"

    show screen poem(poem_peacedets)
    pause
    show screen poem(poem_y2)
    pause
    show screen poem(poem_su)
    pause
    show screen poem(poem_n2)




    $ persistent.sprite_time = "cloudly"
    "cloudly"
    $ persistent.sprite_time = "sunset"
    "sunset"
    $ persistent.sprite_time = "night"
    "night"


    $ persistent.uncolorize = "none"

    #$ persistent.uncolorize = "lite"

    #$ persistent.uncolorize = "full"


    show screen dialog("truestory.exe\n\nВ файлах скрипта обнаружена критическая ошибка. Попробуйте ещё раз.", ok_action=Return())

    return