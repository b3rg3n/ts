# TRUE STORY GLITCH STUFF
# by @b3rg3n
# Since 2024
init:
#BG's
    image ts_l51 = ts_bg + "glitch/l51.webp"
    image ts_l52 = ts_bg + "glitch/l52.webp"
    image ts_l53 = ts_bg + "glitch/l53.webp"

    image ts_l5_glitch_pizdets:
        "ts_l51"
        0.03 # Задержка
        "ts_l53"
        0.03 # Задержка
        "ts_l52"
        0.03 # Задержка
        "ts_l51"
        0.03 # Задержка
        "ts_l53"
        0.03 # Задержка
        repeat # Не убирать

    image ts_club1 = ts_bg + "glitch/club1.webp"
    image ts_club2 = ts_bg + "glitch/club2.webp"
    image ts_club3 = ts_bg + "glitch/club3.webp"

    image ts_club_glitch_pizdets:
        "ts_club1"
        0.03 # Задержка
        "ts_club3"
        0.03 # Задержка
        "ts_club2"
        0.03 # Задержка
        "ts_club1"
        0.03 # Задержка
        "ts_club3"
        0.03 # Задержка
        repeat # Не убирать

    image ts_kitchen1 = ts_bg + "glitch/kitchen1.webp"
    image ts_kitchen2 = ts_bg + "glitch/kitchen2.webp"
    image ts_kitchen3 = ts_bg + "glitch/kitchen3.webp"

    image ts_kitchen_glitch_pizdets:
        "ts_kitchen1"
        0.03 # Задержка
        "ts_kitchen3"
        0.03 # Задержка
        "ts_kitchen2"
        0.03 # Задержка
        "ts_kitchen1"
        0.03 # Задержка
        "ts_kitchen3"
        0.03 # Задержка
        repeat # Не убирать

    image ts_sayori_bedroom_glitch_pizdets:
        ts_bg + "glitch/sayori_bedroom1.webp"
        0.03 # Задержка
        ts_bg + "glitch/sayori_bedroom3.webp"
        0.03 # Задержка
        ts_bg + "glitch/sayori_bedroom2.webp"
        0.03 # Задержка
        ts_bg + "glitch/sayori_bedroom1.webp"
        0.03 # Задержка
        ts_bg + "glitch/sayori_bedroom3.webp"
        0.03 # Задержка
        repeat # Не убирать

    image ts_residental_glitch_pizdets:
        ts_bg + "glitch/residential1.webp"
        0.03 # Задержка
        ts_bg + "glitch/residential3.webp"
        0.03 # Задержка
        ts_bg + "glitch/residential2.webp"
        0.03 # Задержка
        ts_bg + "glitch/residential1.webp"
        0.03 # Задержка
        ts_bg + "glitch/residential3.webp"
        0.03 # Задержка
        repeat # Не убирать

    image ts_sayori_zalagala_blyadina:
        ts_sayori_pt + "glitch/3b1.webp"
        0.03 # Задержка
        ts_sayori_pt + "glitch/3b3.webp"
        0.03 # Задержка
        ts_sayori_pt + "glitch/3b2.webp"
        0.03 # Задержка
        ts_sayori_pt + "glitch/3b1.webp"
        0.03 # Задержка
        ts_sayori_pt + "glitch/3b3.webp"
        0.03 # Задержка
        repeat # Не убирать

    image ts_natsuki_zalagala_blyadina:
        ts_natsuki_pt + "glitch/ghost3_1.webp"
        0.03 # Задержка
        ts_natsuki_pt + "glitch/ghost3_3.webp"
        0.03 # Задержка
        ts_natsuki_pt + "glitch/ghost3_2.webp"
        0.03 # Задержка
        ts_natsuki_pt + "glitch/ghost3_1.webp"
        0.03 # Задержка
        ts_natsuki_pt + "glitch/ghost3_3.webp"
        0.03 # Задержка
        repeat # Не убирать

    image ts_yuri_zalagala_blyadina:
        ts_yuri_pt + "glitch/za.webp"
        0.03 # Задержка
        ts_yuri_pt + "glitch/zb.webp"
        0.03 # Задержка
        ts_yuri_pt + "glitch/zc.webp"
        0.03 # Задержка
        ts_yuri_pt + "glitch/zd.webp"
        0.03 # Задержка
        repeat # Не убирать

    image ts_hiroto_zalagal:
        ts_hiroto_pt + "glitch/b1.webp"
        0.03 # Задержка
        ts_hiroto_pt + "glitch/b3.webp"
        0.03 # Задержка
        ts_hiroto_pt + "glitch/b2.webp"
        0.03 # Задержка
        ts_hiroto_pt + "glitch/b1.webp"
        0.03 # Задержка
        ts_hiroto_pt + "glitch/b3.webp"
        0.03 # Задержка
        repeat # Не убирать

    image ts_yrec_kill_nahui_suicide_blya:
        ts_yuri_pt + "stab/glitch/1.webp"
        0.3
        parallel:
            ts_yuri_pt + "stab/glitch/2.webp"
            0.25
            ts_yuri_pt + "stab/glitch/3.webp"
            0.1
            repeat

    image ts_maloletka_pozvonok_sloman_nahui:
        ts_natsuki_pt + "glitch/1.webp"
        0.3
        parallel:
            ts_natsuki_pt + "glitch/2.webp"
            0.1
            ts_natsuki_pt + "glitch/3.webp"
            0.05
            repeat

    image ts_sayori_zalagala_chereshnya:
        ts_sayori_pt + "glitch/noface1.webp"
        0.03 # Задержка
        ts_sayori_pt + "glitch/noface1b.webp"
        0.03 # Задержка
        ts_sayori_pt + "glitch/noface2.webp"
        0.03 # Задержка
        ts_sayori_pt + "glitch/noface1.webp"
        0.03 # Задержка
        ts_sayori_pt + "glitch/noface1b.webp"
        0.03 # Задержка
        repeat # Не убирать

    image ts_textbox_big_zalagal:
        ts_gui + "dialogue_box/big/glitch/pizda1.webp"
        0.03 # Задержка
        ts_gui + "dialogue_box/big/glitch/pizda2.webp"
        0.03 # Задержка
        ts_gui + "dialogue_box/big/glitch/pizda3.webp"
        0.03 # Задержка
        ts_gui + "dialogue_box/big/glitch/pizda4.webp"
        0.03 # Задержка
        ts_gui + "dialogue_box/big/glitch/pizda5.webp"
        0.03 # Задержка
        ts_gui + "dialogue_box/big/glitch/pizda6.webp"
        0.03 # Задержка
        repeat # Не убирать
