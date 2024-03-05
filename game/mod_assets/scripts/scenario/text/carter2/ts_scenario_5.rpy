label ts_scenario_5:
    $ save_name = "Всё же хорошо?"

    $ persistent.carter2menu = True
    $ persistent.carter3menu = False

    play sound chp
    $ Chapter("АКТ ВТОРОЙ")
    $ Chapter("АКТ ВТОРОЙ")
    $ Chapter("Глава пятая")
    $ Chapter("Глава пятая")
    $ Chapter("Всё же хорошо?")
    stop sound fadeout 7
    $ Chapter("Всё же хорошо?")

    scene ts_bedroom
    show unblink
    pause 1

    return