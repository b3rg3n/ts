# ХУЕТА ДЛЯ ТЕСТОВ
label testing_label_blya:

    python: # ОБНОВЛЯЕМ RPC
        try:
            rpc.update(state=glitchtext(12),details="Снова что-то мутит",large_image="logogovna",start=time.time())
        except AssertionError:
            pass

    #call showpoem (poem_y1, img="yuri 3t") from _call_showpoem

    window hide
    scene ts_class
    #show sayori 1a at t61
    #show monika 1a at t62
    #show yuri 1a at t63
    #show kaori 22a at t64
    #show natsuki 1a at t65
    #show hiroto 1a at t66

    show sayori 1a at t11:
        shader "example.gradient"
        u_gradient_left (1.0, 0.0, 0.0, 1.0)
        u_gradient_right (0.0, 0.0, 1.0, 1.0)

    "Так?"

    show ts_street_rain
    "Хуй"
    scene black
    show ts_school_gate_day_rain
    "хуй"
    scene black
    show ts_city_day_rain
    "елда"

    hide sayori

    show yuri 1a at Glitch(_fps=20., color_range1="c00a", color_range2="f00", glitch_strength=.5)

    "Хуй"

    hide yuri

    show natsuki 1a at Glitch(_fps=1000.)
    "Ускорим анимацию."
    hide natsuki
    show kaori 22a at Glitch(_fps=1000., glitch_strength=.3)
    "Усилим эффект."
    hide kaori
    show hiroto 1a at Glitch(_fps=1000., glitch_strength=.3, color_range1="#0a00", color_range2="0f0")

    "Пизда"

    hide hiroto

    pause 1
    scene ts_class at ts_blur_zadnika
    show zatemnenie_light
    with Dissolve(1.0)
    pause 1

    show chess1 at ts_chess_move_up
    pause 1

    $ TS.Screens(ts_showscreens)

    m "Пришло моё время..."

    show monika 1a onlayer front at t11

    "хуй"

    show ts_club at ts_coridor_glitch
    show monika 1a at t11
    show black zorder 5 at ts_black_glitch
    show blackout_exh
    show anim_exhausted

    $ TS.Screens(ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake))

    show m_rectstatic zorder 0

    m 1b "Хуй"

    m 2a "Пизда"

    return