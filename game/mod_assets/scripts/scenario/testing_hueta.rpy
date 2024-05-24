# ХУЕТА ДЛЯ ТЕСТОВ
label testing_label_blya:

    python: # ОБНОВЛЯЕМ RPC
        try:
            rpc.update(state=glitchtext(12),details="Снова что-то мутит",large_image="logogovna",start=time.time())
        except AssertionError:
            pass

    #$ persistent.sprite_time = "day"

    #$ persistent.sprite_time = "clodly"

    #$ persistent.sprite_time = "sunset"

    #$ persistent.sprite_time = "night"

    #$ persistent.uncolorize = "none"

    #$ persistent.uncolorize = "lite"

    #$ persistent.uncolorize = "full"

    scene ts_club
    $ persistent.uncolorize = "none"
    "без"
    $ persistent.uncolorize = "lite"
    "лёгкое"
    $ persistent.uncolorize = "full"
    "полное"
    $ persistent.sprite_time = "day"
    show elena a at t11
    "день"
    $ persistent.sprite_time = "cloudly"
    "облачно"
    $ persistent.sprite_time = "sunset"
    "вечер"
    $ persistent.sprite_time = "night"
    "ночь"

    return
##############
    show layer screens at ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake)

    play sound slender

    show ts_club_glitch_pizdets zorder 4 at ts_coridor_glitch
    show black zorder 5 at ts_black_glitch
    show blackout_exh zorder 5
    show anim_exhausted zorder 5
    show m_rectstatic zorder 5
    show natsuki_demon_glitch_pizdets zorder 6 at Glitch(_fps=1000.)

    pause 2.5

    stop sound

    scene ts_club
    show natsuki 1a at i11

    "Ахуеть"
###############
    return