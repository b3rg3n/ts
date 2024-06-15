# ХУЕТА ДЛЯ ТЕСТОВ
label testing_label_blya:

    #$ persistent.sprite_time = "day"

    #$ persistent.sprite_time = "clodly"

    #$ persistent.sprite_time = "sunset"

    #$ persistent.sprite_time = "night"

    #$ persistent.uncolorize = "none"

    #$ persistent.uncolorize = "lite"

    #$ persistent.uncolorize = "full"
    scene black
    show ts_yrec_kill_nahui_suicide_blya at left
    show ts_sayori_zalagala_chereshnya:
        align (0.5, 0.15)
    show ts_maloletka_pozvonok_sloman_nahui at right
    $ persistent.uncolorize = "none"
    "ewfe"
    scene ts_club

    "fefke"
    $ persistent.ingame_pizda = False
    "офф"
    show layer screens at ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake)
    $ persistent.ingame_pizda = True
    "он"
    show layer screens at ts_null_transform
    $ persistent.ingame_pizda = False
    "офф"
##############
    show layer screens at ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake)

    play sound slender
    $ persistent.ingame_pizda = True
    show ts_club_glitch_pizdets zorder 4 at ts_coridor_glitch
    show black zorder 5 at ts_black_glitch
    show blackout_exh zorder 5
    show anim_exhausted zorder 5
    show m_rectstatic zorder 5
    show natsuki ghost3 zorder 6 at Glitch(_fps=1000.)

    pause 2.5

    stop sound

    $ persistent.ingame_pizda = False

    scene ts_club
    show natsuki 1a at i11

    "Ахуеть"
###############
    return