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

    scene ts_bedroom
    show unblink
    pause 1

    return