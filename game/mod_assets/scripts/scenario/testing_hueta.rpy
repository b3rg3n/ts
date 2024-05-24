# ХУЕТА ДЛЯ ТЕСТОВ
label testing_label_blya:

    python: # ОБНОВЛЯЕМ RPC
        try:
            rpc.update(state=glitchtext(12),details="Снова что-то мутит",large_image="logogovna",start=time.time())
        except AssertionError:
            pass

    play music audio.t5_yrec_pizdec
    "1"
    play music audio.t6o
    "2"
    play music audio.t6s
    "3"
    play music audio.t10y
    "4"

    "1212"
    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"
    show blink
    pause 2
    play ambience rain_int fadein 2
    pause 1
    scene ts_class_rain_shader
    show ts_class_rain_ovr
    show unblink
    pause 1
    show layer screens at ts_showscreens
    "11"
    return

    scene ts_nebo_fon_bgshka_suka
    show ts_house_rain_ovr
    show ts_rain
    "тест"


    scene ts_nebo_fon_bgshka_suka
    show ts_shkola_rain_ovr
    show ts_rain
    "тест"

    scene ts_nebo_fon_bgshka_suka
    show ts_street_rain_ovr
    show ts_rain
    "тест"


    return

    scene ts_club
    show sayori 1a at t11
    show layer master at Static
    show layer screens at Static
    s "Ну что, Моника..."
    show sayori 1b at t11
    s "Пиздец тебе, да?"
    show sayori 1c at t11
    s "Косоёбит?"
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