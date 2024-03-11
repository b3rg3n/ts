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

    $ persistent.zastavka_skip = False

    return