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

    "Жопка"

    scene ts_bedroom
    show unblink
    pause 1

    call showpoem (poem_y1, img="yuri 3t") from _call_showpoem

    "Работает?"

    $ persistent.first_poem = False

    "Хуета"

    call showpoem (poem_test) from _call_showpoem_1

    "eojgfe"

    return