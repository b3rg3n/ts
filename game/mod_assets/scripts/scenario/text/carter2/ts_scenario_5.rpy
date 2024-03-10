label ts_scenario_5:
    $ save_name = "Всё же хорошо?"

    $ persistent.carter2menu = False
    $ persistent.carter3menu = True

    play sound chp2
    $ Chapter("АКТ ВТОРОЙ")
    $ Chapter("АКТ ВТОРОЙ")
    $ Chapter("Глава первая")
    $ Chapter("Глава первая")
    $ Chapter("Всё же хорошо?")
    stop sound fadeout 7
    $ Chapter("Всё же хорошо?")

    "Жопка"

    scene ts_bedroom
    show unblink
    pause 1

    call showpoem (poem_y1, img="yuri 3t") from _call_showpoem

    "Работает?"

    $ TS.Screens(ts_hidescreens)

    pause 1

    show sayori 1a at tss22

    pause 1

    show sayori 1a at thide
    hide sayori

    pause 1

    $ TS.Screens(ts_showscreens)

    pause 1

    show ts_club at ts_coridor_glitch
    show black zorder 5 at ts_black_glitch
    show m_rectstatic zorder 0

    $ TS.Screens(ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake))

    show m_rectstatic zorder 0

    "Хуй"

    "Пизда"
    return