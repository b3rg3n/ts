label ts_scenario_12:

    $ TS.b()

    python: # ОБНОВЛЯЕМ RPC
        ts_rpc_carter11()

    $ persistent.rpclabel = "11"
    $ persistent.sprite_time = "day"
    $ persistent.carter2menu = False
    $ persistent.carter3menu = True
    $ persistent.badendmenuperedglitch = False
    $ persistent.badendmenuskipglitch = False
    $ persistent.badendmenu = False
    $ persistent.goodendmenu = False
    $ persistent.peredbadendmenu = False
    $ persistent.peredgoodendmenu = False

    if _preferences.language == "english":
        $ save_name = "More of the same"
    else:
        $ save_name = "Порочный круг"


    scene black

    play sound chp
    if _preferences.language == "english":
        $ Chapter("ACT THREE")
        $ Chapter("ACT THREE")
        $ Chapter("chapter three")
        $ Chapter("chapter three")
        $ Chapter("More of the same")
        stop sound fadeout 7
        $ Chapter("More of the same")
    else:
        $ Chapter("АКТ ТРЕТИЙ")
        $ Chapter("АКТ ТРЕТИЙ")
        $ Chapter("Глава третья")
        $ Chapter("Глава третья")
        $ Chapter("Порочный круг")
        stop sound fadeout 7
        $ Chapter("Порочный круг")

    $ TS.p(2)

    $ TS.s(ts_showscreens)

    $ persistent.uncolorize = "full"

    play sound nfy
    if _preferences.language == "english":
        $ renpy.notify("Third cycle")
    else:
        $ renpy.notify("Цикл третий")

    s "{size=-6}..ика!{/size}"
    s "{size=-4}Моника!{/size}"
    s "Моника, просыпайся уже!" with hpunch
    "Опять всё заново..."
    s "Вставай давай, пьянь малолетняя!"
    m "..."

    play music ts_cr_cof fadein 2
    scene ts_sayori_bedroom
    show sayori 4pi at t11
    show unblink
    "Передо мной предстала... уже до боли знакомая картина..."
    "Сайори в пижаме в её спальне."
    em "В той самой, в которой ты её и повесила, кстати."
    "«Да не я её повесила... она... сама как-то...»"
    em "Сама связала петлю, сама откинула стул, и сама себя повесила?"
    $ TS.s(vpunch)
    em "Хватит сказки рассказывать!"
    em "И вообще, не забывай, по какому поводу ты в начале каждого цикла просыпаешься в спальне у Сайори, а не у себя."
    "Ах да, точно..."
    m "С-Сайори..."
    show sayori 2pg at t11
    m "П-прости, пожалуйста, за это недоразумение..."
    m "А... Ф-фестиваль же только через неделю, да?"
    show sayori 2ph at f11
    s "Ну... да, а что?"
    show sayori 3pg at t11
    m "Да ничего... просто с похмелья вспомнилось, ради чего это всё затевалось, хе-хе..."
    show sayori 2pk at t11
    m "Ну... Всё? Я протрезвела, сейчас уже всё нормально – можно я теперь домой уже пойду? Папа там уже наверняка заждался, все больницы и морги обзвонил..."
    show sayori 3pn at f11
    s "..."
    s 2pl "Да, конечно..."
    s 2pc "Только тихо, родители ещё спят..."
    s 3pm "А хотя подожди!"
    extend 2px " Хочешь, я с тобой пройдусь? "
    if not renpy.android:
        window hide
        $ TS.m(ts_trns_dream)
        play sound ts_glitch5
        $ TS.p(1)
        $ TS.m()
        stop sound
        $ TS.s(ts_showscreens_fast)
    extend "Мне всё равно в магазин также надо, как раз по пути!"
    show sayori 2pa at t11
    m "А... д-да нет, у меня дом в другой стороне находится..."
    show sayori 2pk at f11
    stop music fadeout 3
    s "Эх-х-х..."
    extend 2px " Ну ладно, тогда до понедельника!"
    show sayori 2pa at t11
    m "Да, до понедельника..."
    hide sayori
    "После этих слов мы разошлись каждая своей дорогой: Сайори – в магазин, а я... думать."
    play music ts_brandon fadein 3

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound chasiki fadein 1
    scene ts_residential
    with ts_lap
    stop sound fadeout 1

    $ TS.s(ts_showscreens)
    "Вместо того, чтобы сразу пойти домой, я решаю зайти в дом... Миры."
    "Я так и не поняла, от чего она умерла."
    show monika 1r at f11
    em "Даже если ты вломишься в пустой, {i}чужой{/i} дом, понятнее тебе не станет."
    show monika 1q at t11
    m "Без тебя знаю. Но я чувствую, как меня тянет к этому дому."
    
    play sound chasiki fadein 1
    scene ts_sayori_house
    with ts_lap
    stop sound fadeout 1
    
    "Я нервно хихикаю, замечая, как все дома в этом районе, по всей видимости, совершенно одинаковы."
    "Ведь дом Сайори {b}точно такой же{/b}."
    "Однако зайти внутрь я так и не решаюсь, и вместо этого просто решаю стоять снаружи."
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"
    $ TS.p(5)
    $ TS.s(ts_showscreens)
    "Прошло пять минут."
    show monika 2i at f11
    em "Ну, повспоминала? Предалась ностальгии? Всё, пойдём уже отсюда, всё равно дверь изнутри тебе никто не откроет."
    show monika 2h at t11
    m "Да... Но всё равно, как будто мама Миры вот-вот скажет: «А Мира на тренировке задерживается, но если хочешь, проходи»."
    m "Славные были деньки... Которые так бесславно кончились... Теперь уже навсегда..."
    show monika 2i at f11
    em "Да, да, было всё здорово и классно у вас, но потом у вас всё перестало быть здорово и классно – пойдём отсюда, тебе всё равно никто не ответит, а так ты просто и дальше будешь стоять и тупить."
    show monika 2h at t11
    m "Ладно..."
    "Я окидываю взглядом пустующий дом Миры один последний раз на этой неделе и медленно возвращаюсь домой."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound chasiki fadein 1
    scene ts_kitchen
    show hiroto 1z1 at f11
    with ts_lap
    stop sound fadeout 1

    play sound nfy
    if _preferences.language == "english":
        $ renpy.notify("Third cycle")
    else:
        $ renpy.notify("Цикл третий")


    $ TS.s(ts_showscreens)

    ts_ft "Ну привет, гулёна!"
    show hiroto 1j at t11
    m "Да-да, пап, и тебе доброе утро, прости, я вчера напилась сильно, друзья меня до дома Сайори дотащили, но сейчас со мной всё нормально, жива, здорова, в общем, да..."
    m "Кстати, а где у нас шахматы? Что-то поиграть так захотелось..."
    show hiroto 1k at t11
    "От услышанного папа буквально потерял дар речи."
    show hiroto 1e at t11
    "Однако он быстро собрался с собой и лишь сказал:"
    show hiroto 1c at f11
    ts_ft "Сразу признаёшь вину?"
    ts_ft "Ну да ладно, я и ругать-то тебя не собирался. "
    extend 1u "Как будто сам таким по молодости не был..."
    ts_ft 1c "А шахматы у нас..."
    ts_ft 1x "Э-э-э..."
    show hiroto 1x at t11
    m "А шахматы у нас в гостиной. Со всеми фигурами на месте."
    show hiroto 1z at f11
    ts_ft "Откуда ты?..{w=0.6}{nw}"
    show hiroto 1a1 at t11
    m "Подумала и угадала."
    "Пап, лучше не задавай лишних вопросов..."
    "Иначе если бы ты всё-таки задал эти вопросы, не факт, что я сама смогу на них ответить..."
    show hiroto 1y at f11
    ts_ft "Так а с кем ты играть-то будешь?"
    ts_ft 1x "Потому что я вот что-то не очень хочу.{w=0.8} {size=-8}После только что увиденного...{/size}{w=0.5}{nw}"
    show hiroto 1a1 at t11
    m "О, за это не переживай, я просто шахматные задачки всякие порешаю."
    m "У нас как раз одна книжечка с задачами завалялась... Вот как раз с неё и буду решать."
    stop music fadeout 4
    show hiroto 1b1 at t11
    "Папа лишь молча кивнул, {w=0.6}{nw}"
    show hiroto 1b1 at cright with move
    hide hiroto
    extend "а затем ушёл по своим делам."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound chasiki fadein 1
    scene ts_bedroom
    show monika 1bo at f11
    with ts_lap
    stop sound fadeout 1

    $ TS.s(ts_showscreens)

    play music ts_ytm_c fadein 2
    "Решать задачки было той ещё скукой."
    "Это же просто задачки из разряда тренировочного лагеря, где враги картонные и неподвижно стоят на месте, а в реальной игре такие ситуации вряд ли произойдут."
    show monika 4bs at t11
    with linearblur
    "Поэтому спустя пару однотипных задачек на вилки я просто решаю попросить Аки поиграть со мной."
    "Хотя бы отточу навыки в реальных боевых условиях, так сказать."
    show monika 3bs at f11
    em "Ч-что? Со мной? Но я же не умею..."
    show monika 3bs at t11
    m "Умеешь. Как ты там сама много раз говорила? «Я – это твоё подсознание, я буквально часть тебя»?"
    show monika 2bn at f11
    em "То, что я – это часть тебя, не обязательно означает, что эта часть тебя так же хорошо играет в шахматы..."
    show monika 2bo at t11
    m "О-о-о, сначала ты две недели называешь меня бездарностью во всех возможных вариациях, а теперь ты мне льстишь?"
    show monika 2bi at f11
    em "И до сих пор считаю, что ты бездарность."
    em 2bp "Но просто... я никогда раньше не умела играть в шахматы... И я не уверена, что я из тех частей твоего мозга, которая ответственна за умение играть в шахматы..."
    show monika 2bo at t11
    m "Ну, не попробуешь – не узнаешь, верно?"
    show monika 2bq at f11
    em "..."
    em 2bi "Ладно. Сыграем. Но только одну партию."
    show monika 2bh at t11
    m "А я большего и не прошу. Одну так одну."
    show monika 2br at f11
    em "И на что я только подписываюсь..."
    show monika 2bq at t11
    m "На игру со мной, очевидно же."
    show monika 2bi at f11
    em "Расставляй уже. Я буду играть чёрными тогда."
    show monika 2bh at t11
    m "Ну... ладно?"
    "Я молча заканчиваю расставлять фигуры. Игра началась."
    "Ну, поехали..."

    play sound psy_fast_3
    scene black
    with memglitch
    stop sound
    if chess_tutor == True:
        python:
            _preferences.volumes['music'] = 0.0
        play sound psy_fast_3
        scene black with memglitchbolee
        stop sound

        show momika 1n at f11
        cm "Кхе-кхе..."
        show momika 3l at f11
        cm "Привет ещё раз!"
        show momika 2b at f11
        cm "Давно не виделись, не так ли? Уже много времени прошло, ты уже даже и забыл, наверное, что я вообще-то тоже есть в этом моде."
        menu:
            "Да, давненько.":
                pass
        show momika 2l at f11
        cm "Ну, ты уже, наверное, устал от всего этого хоррора в Третьем Акте."
        show momika 1n at f11
        cm "Или какой там акт вообще сценарист сейчас пишет..."
        show momika 2b at f11
        cm "В общем, неважно! Сейчас будет сцена с шахматами между Моникой и Аки, и я обещаю, что за всё это время не будет ни одного скримера."
        cm "А я, как и в прошлый раз, буду помогать тебе осваивать основы!"
        show momika 4g at f11
        cm "Или ты уже не хочешь, чтобы я тебе помогала?"
        menu:
            "Нет, что ты, конечно, хочу!":
                pass
            "Разумеется, хочу.":
                pass
            "Нет, я хочу учиться и дальше.":
                pass
        show momika 2l at f11
        cm "Фух... Ну вот и славненько!"
        show momika 3d at f11
        cm "Только прими к сведению, что я рассказала б{u}{b}о{/u}{/b}льшую часть из того, что я хотела, ещё в прошлый раз, поэтому на этот раз новых знаний будет поменьше."
        show momika 2k at f11
        cm "В любом случае, если игра тебе понравится, ничего не мешает тебе попрактиковаться и без меня!"
        show momika 2b at f11
        cm "Будь то игра с друзьями, в местном шахматном клубе, по сети, или даже со своей шизофренией, как Моника!"
        cm "А на шахматных ресурсах вроде {a=https://chess.com}этого{/a} или {a=https://lichess.org}этого{/a}, помимо самой игры, тебе будет доступен и курс новичка, в котором ты глубже втянешься в игру!"
        cm "Там и задачки есть, и их сотни, тысячи, сотни тысяч, и всё это абсолютно бесплатно!"
        show momika 1n at f11
        cm 1n "Главное – {b}решать{/b} эти задачки, а не как Моника..."
        show monika 2br at f41
        show momika 2o at t44
        em "Ты можешь заткнуться хотя бы на пять минут?"
        show monika 2bv at t41
        show momika 2p at f44
        cm "Ой, да ладно, я и так всего полтора раза за весь мод появляюсь, а тут ещё ты меня гонишь..."
        show monika 2bv at t41
        show momika 2n at f44
        cm "В-в общем, ладно, наслаждайся игрой."
        show monika 2bv at t41
        show momika 3b at f44
        cm "Кстати, эта игра списана с игры реального человека, сценариста этого мода!"
        show monika 2bi at f41
        show momika 1f at t44
        em "Да поняли мы уже, поняли, дай мне просто поиграть с этой бездарностью, и всё, чего ты всё оттягиваешь этот момент?"
        show monika 2bh at t41
        show momika 2f at f44
        cm "..."
        show monika 2bh at t41
        show momika 1p at f44
        cm "Ладно..."

        play sound psy_fast_3
        scene ts_bedroom
        with memglitchbolee
        stop sound
        python:
            _preferences.volumes['music'] = .65

    show monika 2bh at t41
    "Шоу начинается..."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    show atc3_chess1 at ts_chess_move_up

    $ TS.s(ts_showscreens)

    "Ещё с детства я всегда играла e4, потому что в детстве я играла только с папой, а он игрок агрессивный, и сам начинает с пешки е."
    if chess_tutor == True:
        show momika 2b at f44
        cm "Есть три основных типа дебютов: открытые, полуоткрытые и закрытые."
        cm "Открытые – это дебюты, которые начинаются с ходов 1. е4 е5. Полуоткрытые – это дебюты, в которых белые ходят е4, но чёрные не отвечают им е5, вместо этого играя другой ход."
        show momika 2d at f44
        cm "Закрытые же дебюты начинаются с ходов 1. d4 d5."
        cm "Некоторые теоретики также относят полузакрытые (такие, в которых белые играют d4, но чёрные не отвечают d5) и фланговые (в которых первым ходом играется любая другая не центральная пешка) дебюты в отдельные категории."
        cm "Однако другие шахматные теоретики так не считают, и включают полузакрытые и фланговые дебюты в подкатегории закрытых."
        show momika 3k at f44
        cm "А поскольку в моде не было и не будет ни одной игры в закрытых дебютах, мы тоже будем считать, что все дебюты, которые начинаются не с хода 1. е4 – закрытые."
        show momika at thide
        hide momika
    show monika 2bo at t41
    $ TS.p(0.4)
    show monika 2bh at t41

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    show atc3_chess1 at ts_chess_move_down
    $ TS.p(0.5)
    hide atc3_chess1 with dissolve

    show atc3_chess2 at ts_chess_move_up
    $ TS.p(1)
    $ TS.s(ts_showscreens)

    "Первый ход у Аки точно такой же, как и у папы. Но я-то знаю, что собирается она играть совсем иначе, чем просто выпускать ферзя как можно раньше."
    "Я же продолжаю гнуть свою линию и выставляю вторую центральную пешку."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    show atc3_chess2 at ts_chess_move_down
    $ TS.p(0.5)
    hide atc3_chess2 with dissolve

    show atc3_chess3 at ts_chess_move_up
    $ TS.p(1)
    $ TS.s(ts_showscreens)

    "Аки без раздумий тоже ходит второй центральной пешкой."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    show atc3_chess3 at ts_chess_move_down
    $ TS.p(0.5)
    hide atc3_chess3 with dissolve

    show atc3_chess4 at ts_chess_move_up
    $ TS.p(1)
    $ TS.s(ts_showscreens)

    "Старая добрая «Французская защита». Конечно, всю теорию я не помню, но первые пару ходов я знаю, как дважды два."
    "Я бью пешку, не тратя ни секунды на размышления."
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    show atc3_chess4 at ts_chess_move_down
    $ TS.p(0.5)
    hide atc3_chess4 with dissolve

    show atc3_chess5 at ts_chess_move_up
    $ TS.p(1)
    $ TS.s(ts_showscreens)
    "Аки бьёт пешку в ответ."
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    show atc3_chess5 at ts_chess_move_down
    $ TS.p(0.5)
    hide atc3_chess5 with dissolve

    show atc3_chess6 at ts_chess_move_up
    $ TS.p(1)
    $ TS.s(ts_showscreens)
    show monika 2bd at f41
    em "Слушай, а мы стих писать на этот раз будем?"
    show monika 2bc at t41
    m "А кому не всё равно на этот стих? Девочки в клубе так ни разу и не спросили, что же я там такого написала, это скорее как предлог того, что нам вообще надо стихи писать."
    m "А даже если и спросят – я этот стих уже наизусть помню, поэтому за пару минут вечером напишу, а девочкам скажу, что стих дома, и что я {i}обязательно{/i} принесу его на следующее собрание."
    show monika 2bd at f41
    em "Ладно..."
    show monika 2bc at t41
    "С этим разговором о стихе я совсем отвлеклась от игры."
    "...а что там дальше?"
    "Ну, наверное, стандартное развитие..."
    "Я просто вывожу коня."
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    show atc3_chess6 at ts_chess_move_down
    $ TS.p(0.5)
    hide atc3_chess6 with dissolve

    show atc3_chess7 at ts_chess_move_up
    $ TS.p(1)
    $ TS.s(ts_showscreens)
    "Аки безэмоционально выводит того же коня."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    show atc3_chess7 at ts_chess_move_down
    $ TS.p(0.5)
    hide atc3_chess7 with dissolve

    show atc3_chess8 at ts_chess_move_up
    $ TS.p(1)
    $ TS.s(ts_showscreens)

    "Так, дальше... Дальше, наверное, выводить слона и делать рокировку..."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    show atc3_chess8 at ts_chess_move_down
    $ TS.p(0.5)
    hide atc3_chess8 with dissolve

    show atc3_chess9 at ts_chess_move_up
    $ TS.p(1)
    $ TS.s(ts_showscreens)

    if chess_tutor == True:
        show momika 2g at f44
        cm "Ладьи очень прямолинейные и неповоротливые, так их ещё и зажали в углах доски..."
        show momika 3d at f44
        cm "Что нужно сделать для того, чтобы они вступали в игру чуть раньше?"
        show momika 3b at f44
        cm "Правильно, рокировка."
        show momika 2d at f44
        cm "Рокировка – это специальный ход короля и одной из ладей, который, по сути, ломает все правила шахмат."
        show momika 3d at f44
        cm "Тут тебе и король, который ходит сразу на две клетки вместо одной, и в принципе игрок ходит сразу двумя фигурами..."
        cm "И по итогу король ходит на две клетки, а ладья становится сразу за королём, образуя своеобразный замок из пешек и ладьи."
        show momika 3i at f44
        cm "Но у такой хитрости есть ряд ограничений."
        show momika 2d at f44
        cm "Во-первых, до рокировки нельзя делать ходов ни королём, ни ладьёй, с которой король хочет рокироваться."
        show momika 4d at f44
        cm "Даже если какая-то из фигур походит, а затем вернётся на своё изначальное место, право на рокировку теряется."
        show momika 2d at f44
        cm "Во-вторых, рокироваться нельзя, если королю объявлен шах. Рокироваться, чтобы уйти от шаха, тоже нельзя."
        cm "И наконец, при рокировке король не должен быть под шахом ни в одной из клеток, применяемых при рокировке."
        show momika 2n at f44
        cm "Ну и ещё в турнирных играх и при игре на онлайн-ресурсах король должен ходить первым. Если первой походит ладья, то это просто будет считаться обычным ходом ладьи, а право на рокировку потеряется..."
        show momika at thide
        hide momika
    "Аки, в свою очередь, выводит второго коня."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    show atc3_chess9 at ts_chess_move_down
    $ TS.p(0.5)
    hide atc3_chess9 with dissolve

    show atc3_chess10 at ts_chess_move_up
    $ TS.p(1)
    $ TS.s(ts_showscreens)

    "Так... Что я там говорила? Рокировку буду делать?"
    "...Нет, рокировка подождёт. Я же белым цветом всё-таки играю, у меня право первого хода, мне атаковать надо и побеждать!"
    "Я с ухмылкой вывожу второго коня."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    show atc3_chess10 at ts_chess_move_down
    $ TS.p(0.5)
    hide atc3_chess10 with dissolve

    show atc3_chess11 at ts_chess_move_up
    $ TS.p(1)
    $ TS.s(ts_showscreens)

    "Аки выводит вперёд ещё одну фигуру. На этот раз слона."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    show atc3_chess11 at ts_chess_move_down
    $ TS.p(0.5)
    hide atc3_chess11 with dissolve

    show atc3_chess12 at ts_chess_move_up
    $ TS.p(1)
    $ TS.s(ts_showscreens)

    "Новых ходов на развитие без риска я сделать больше не смогу."
    "Нет, есть ещё второй слон, однако это будет означать потерю темпа – Аки сделает рокировку первой, и фактически чёрными играть уже буду я."
    "Нужно срочно рокироваться, пока не началось."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    show atc3_chess12 at ts_chess_move_down
    $ TS.p(0.5)
    hide atc3_chess12 with dissolve

    show atc3_chess13 at ts_chess_move_up
    $ TS.p(1)
    $ TS.s(ts_showscreens)

    "Аки без лишних размышлений отвечает мне такой же рокировкой."
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    show atc3_chess13 at ts_chess_move_down
    $ TS.p(0.5)
    hide atc3_chess13 with dissolve

    show atc3_chess14 at ts_chess_move_up
    $ TS.p(1)
    $ TS.s(ts_showscreens)
    if chess_tutor == True:
        show momika 2b at t44
        cm "Собственно, ты увидел рокировку в действии."
        show momika 2d at f44
        cm "Кстати, существует два типа рокировок: короткая и длинная. Короткая делается на королевском фланге, а длинная – на ферзевом."
        cm "Исходя из названия, короткая делается проще, потому что тебе нужно вывести всего две фигуры, и можно рокироваться уже на четвёртом ходу."
        show momika 4d at f44
        cm "Однако в некоторых дебютах предпочтительнее всё же длинная рокировка, потому что задействованы все фигуры с ферзевого фланга."
        show momika 2d at f44
        cm "А если оба игрока рокируются в разные стороны, то это обычно означает драку не на жизнь, а на смерть. "
        show momika 3l at f44
        extend "В шахматах, конечно же. В жизни шахматисты очень миролюбивые."
        show momika 3b at f44
        cm "Ладно, не буду тебе мешать, продолжай смотреть игру!"
        show momika at thide
        hide momika
    "..."
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    scene ts_bedroom
    with ts_paint

    show atc3_chess15 at ts_chess_move_up
    $ TS.p(1)
    $ TS.s(ts_showscreens)

    show monika 2bo at t41
    with linearblur
    "Прошло ещё несколько ходов."
    "У нас с Аки произошёл первый размен фигурами: Аки отдала своего слона за моего коня, в связи с чем открывается окно возможностей для атаки на беззащитную пешку."
    show monika 2bq at t41
    $ TS.p(0.8)
    show monika 2bh at t41

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    show atc3_chess15 at ts_chess_move_down
    $ TS.p(0.5)
    hide atc3_chess15 with dissolve

    show atc3_chess16 at ts_chess_move_up
    $ TS.p(1)
    $ TS.s(ts_showscreens)

    "Аки как ни в чём ни бывало развивает ферзя."
    "Превосходно. Всё согласно моему плану..."
    "Вот только чем бить первым? Или скорее, кто мне нужен меньше?"
    "После некоторых размышлений я бью пешку конём."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    show atc3_chess16 at ts_chess_move_down
    $ TS.p(0.5)
    hide atc3_chess16 with dissolve

    show atc3_chess17 at ts_chess_move_up
    $ TS.p(1)
    $ TS.s(ts_showscreens)

    show monika 3bs at t41
    $ TS.p(0.8)
    show monika 1bz at t41
    $ TS.p(0.4)
    show monika 1bf at t41
    "Аки, осознав, что она зевнула пешку, от безысходности бьёт моего коня своим."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    show atc3_chess17 at ts_chess_move_down
    $ TS.p(0.5)
    hide atc3_chess17 with dissolve

    show atc3_chess18 at ts_chess_move_up
    $ TS.p(1)
    $ TS.s(ts_showscreens)

    "Я со злой, но безобидной ухмылкой тут же бью коня своим слоном."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    show atc3_chess18 at ts_chess_move_down
    $ TS.p(0.5)
    hide atc3_chess18 with dissolve

    show atc3_chess19 at ts_chess_move_up
    $ TS.p(1)
    $ TS.s(ts_showscreens)

    show monika 2bp at f41
    em "Да не очень-то мне эта пешка и нужна была..."
    show monika 2bo at t41
    m "Ага, охотно верю..."
    show monika 2bi at f41
    em "Игра ещё не окончена..."
    show monika 1bq at t41
    m "Ну, с этим соглашусь."
    "И откуда только в Аки проснулся такой азарт? Мы же не на корову играем всё-таки, да и сама она говорила, что играть не умеет."
    "Хотя, учитывая то, как именно она играет, играет она на примерно том же уровне, что и я сама."
    "Это и не удивительно... Я уже так удивлялась за прошедшие две недели, что внезапное умение Аки играть в шахматы – это наименьшее из всех зол."
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    scene ts_bedroom
    with ts_pixel

    show atc3_chess23 at ts_chess_move_up
    $ TS.p(1)
    $ TS.s(ts_showscreens)

    show monika 1bz at t41
    with linearblur
    "Да, Аки сказала, что игра ещё не окончена."
    "Однако когда у тебя в эндшпиле целой ладьи не хватает вдобавок к лишней пешке – это уже чересчур."
    "Последние несколько ходов Аки просто бездумно водит фигуры туда-сюда."
    "Впрочем, я тоже не намного осмысленнее это делаю."
    "Ну то есть, да, у меня лишняя ладья – как с этой лишней ладьёй выиграть теперь?"
    "Попробую-ка я сдвоить их. Сначала я подвожу одну ладью к другой..."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    show atc3_chess23 at ts_chess_move_down
    $ TS.p(0.5)
    hide atc3_chess23 with dissolve

    show atc3_chess24 at ts_chess_move_up
    $ TS.p(1)
    $ TS.s(ts_showscreens)

    show monika 1bz at t41
    $ TS.p(0.5)
    show monika 1bo at t41
    "Аки же тем временем от безысходности просто двигает очередную пешку на одну клетку."
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    show atc3_chess24 at ts_chess_move_down
    $ TS.p(0.5)
    hide atc3_chess24 with dissolve

    show atc3_chess25 at ts_chess_move_up
    $ TS.p(1)
    $ TS.s(ts_showscreens)
    "А затем я ставлю ладью на вторую горизонталь, чтобы на следующем ходу обе ладьи были на одной вертикали."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    show atc3_chess25 at ts_chess_move_down
    $ TS.p(0.5)
    hide atc3_chess25 with dissolve

    show atc3_chess26 at ts_chess_move_up
    $ TS.p(1)
    $ TS.s(ts_showscreens)

    "Однако вместо того, чтобы играть дальше, Аки просто..."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    show atc3_chess26 at ts_chess_move_down
    $ TS.p(0.5)
    hide atc3_chess26 with dissolve

    $ TS.s(ts_showscreens)

    stop music fadeout 3
    show monika 1bz at t41
    $ TS.p(0.5)
    show monika 1bv at t41
    $ TS.p(0.5)
    show monika 2bzc at t41
    $ TS.p(0.3)
    "...начинает плакать?"
    show monika 2bzb at f41
    em "Всё, ладно, я сдаюсь. Довольна?"
    show monika 2bzc at t41
    "Мне так и хочется подерзить ей, отомстить ей за две недели гноблений и унижений, но я просто... не могу так сделать."
    "Я же выше этого."
    play music ts_brandon fadein 2
    m "Да не расстраивайся ты так, не на корову же играли."
    show monika 2bza at f41
    em "Я должна была выиграть, понимаешь?"
    em 2bzb "Чтобы в очередной раз показать тебе, что ты бездарность!"
    show monika 2bzc at t41
    m "Ну, не настолько я и бездарность, раз хоть у кого-то смогла выиграть..."
    m "То есть, я хотела сказать, что играли мы до последнего момента на равных..."
    show monika 2bza at f41
    em "Это ничего не меняет!"
    show monika 2bzc at t41
    m "А вот и меняет! Ты же сама полчаса назад говорила, что не уверена, умеешь ли ты играть в принципе."
    m "А для первой игры в шахматы ты сыграла очень даже неплохо."
    show monika 2bw at t41
    $ TS.p(2)
    show monika 1bo at t41
    $ TS.p(1.5)
    "Аки мешкается, стоит ли мне грубить и дальше, или же просто принять это и жить дальше."
    show monika 2bp at f41
    em "Ладно, наверное, ты тоже иногда бываешь права..."
    show monika 2bm at t41
    $ persistent.sprite_time = "day"
    m "Ну вот видишь, хорошо то, что хорошо заканчивается."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"
    #$ persistent.sprite_time = "cloudly"
    #play ambience rain_int fadein 3
    #play sound chasiki fadein 1
    #if renpy.android:
    #    scene ts_club_rain_vedro
    #    show ts_rain
    #else:
    #    scene ts_club_rain_shader
    #show ts_club_rain_ovr
    scene ts_club
    show yuri 1g at t31
    show sayori 2y at t32
    show natsuki 1t at t33
    with ts_lap
    stop sound fadeout 1
    $ TS.s(ts_showscreens)

    play sound nfy
    if _preferences.language == "english":
        $ renpy.notify("Third cycle")
    else:
        $ renpy.notify("Цикл третий")

    m "Итак, ребята! Все закончили со стихотворениями?"
    show yuri 1j at t31
    show sayori 2l at t32
    show natsuki 1t at t33
    "Девочки согласно закивали."
    m "А теперь к делам насущным."
    show yuri 1e at t31
    show sayori 3b at t32
    show natsuki 1za at t33
    m "Это последнее собрание перед фестивалем, и..."
    "Чёрт, я уже в третий раз прошу их с тем, чтобы они помогли клубу, а мне всё ещё неловко просить их о том, чтобы они что-то сделали, по сути, для меня."
    if unluck7 == True:
        "После прошлой среды, как мне казалось, Литературный клуб перестанет существовать как таковой, потому что Юри в тот злополучный день буквально вышла из себя."
        "Однако на следующий день я уже по инерции пришла в клуб."
        "И каково же было моё удивление, когда все собрались как ни в чём ни бывало!"
        "Уж не знаю, сон ли это, или моя больная фантазия, или всё вместе, но следующее собрание мы провели как самое обычное, без каких-либо казусов."
        "Даже я изо всех сил старалась вести себя как обычно."
        "Но в общем, да, в прошлую пятницу я тоже просила их о том же самом: о том, чтобы «Литературный клуб проявил себя с лучшей стороны»."
    m "И... на фестивале нужно проявить себя с лучшей стороны, так что каждой из вас необходимо... поработать на благо клуба."
    m "Впереди ещё все выходные, так что времени у вас будет предостаточно."
    m "Нацуки, ты можешь—{w=0.8}{nw}"
    show natsuki 1y at f33
    n "О, я и так прекрасно знаю, что я могу!"
    n 1z "Кексы! Пока что никто не жаловался, и не думаю, что кто-то пожалуется, ведь будет работать профессионал!"
    show sayori 3n at t32
    show natsuki 1z at t33
    "При упоминании кексов Сайори активизировалась. Разве что не облизнулась."
    "Я решаю перехватить инициативу, пока у неё слюни не потекли."
    show sayori 2o at t32
    m "Так, Сайори, теперь ты."
    m "Ты же у нас рисуешь хорошо, так ведь?"
    show sayori 2l at f32
    s "Не настолько уж и хорошо, так, просто иногда рисую от нечего делать..."
    show sayori 2k at t32
    m "Ну, а нам и не нужно очередное произведение искусства. Просто нарисуй несколько листовок и буклетиков, распечатай их побольше, и на этом всё. Думаешь, справишься?"
    show sayori 2h at f32
    s "Да, с этим справлюсь."
    show sayori 2k at t32
    m "Ну и на десерт – Юри."
    show yuri 1f at f31
    y "Да, что тебе нужно?"
    show yuri 1e at t31
    m "У тебя, так сказать, очень экзотический почерк."
    "В прошлые разы я говорила про красивый почерк, но это не нравилось Нацуки. Сейчас же я говорю гораздо нейтральнее."
    "Вот что ни говори, но я всё-таки учусь на ошибках."
    em "Ты и есть одна большая ошибка..."
    m "Что я там говорила? Ах да, экзотический почерк. А мероприятие у нас не абы какое, а литературное."
    m "Поэтому ты могла бы красиво написать всякие красивые слова."
    m "И к тому же, ты могла бы задать этому мероприятию соответствующую..."
    show yuri 2y6 at t31
    m "{cps=15}Атмосферу.{/cps}"
    show yuri 2y6 at f31
    y "Атмосферу, говоришь?"

    $ persistent.ingame_pizda = True

    python:
        _preferences.volumes['sfx'] = 1.0
        _preferences.volumes['music'] = .0

    play sound2 ts_smeh_pizdec

    $ TS.s(ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake))

    play sound ts_glitch_music14
    scene ts_club:
        align(0.5, 0.5) zoom 1.0
        ease 0.1 align(0.2, 0.5) zoom 2.0
        ease 0.1 align(0.8, 0.2) zoom 3.0
        ease 0.1 align(0.3, 0.7) zoom 2.5
        ease 0.1 align(0.4, 0.9) zoom 4.0
        ease 0.1 align(0.5, 0.5) zoom 1.0
        repeat
    show yuri 3y3:
        align(0.5, 0.5) zoom 1.0
        ease 0.1 align(0.1, 0.2) zoom 2.0
        parallel:
            ease 0.02 align(0.8, 0.2) zoom 3.0
            ease 0.02 align(0.4, 0.4) zoom 4.0
            ease 0.02 align(0.9, 0.6) zoom 5.0
            ease 0.02 align(0.8, 0.2) zoom 3.0
            repeat

    y "{cps=10}{b}Я ПРОСТО ОБОЖАЮ АТМОСФЕРНЫЕ МЕРОПРИЯТИЯ!{/b}{/cps}"
    y "{cps=15}{b}НАСТОЛЬКО ОБОЖАЮ, ЧТО ГОТОВА УМЕРЕТЬ ЗА НИХ!{/b}{/cps}"

    stop sound2
    stop sound

    $ TS.s()

    $ persistent.ingame_pizda = False

    #if renpy.android:
    #    scene ts_club_rain_vedro
    #    show ts_rain
    #else:
    #    scene ts_club_rain_shader
    #show ts_club_rain_ovr
    scene ts_club
    show sayori 2k at i32
    show natsuki 1z at i33

    show yuri 3y3 at i31
    with flash
    $ TS.p(1)
    play sound yurikill
    $ TS.p(1.43)
    show yuri stab_1
    $ TS.p(0.75)
    show yuri stab_2
    show blood:
        pos (210,485)
    $ TS.p(1.25)
    show yuri stab_3
    $ TS.p(0.75)
    show yuri stab_2
    show blood:
        pos (210,485)
    show yuri stab_4 with ImageDissolve("mod_assets/source/images/spr/yuri/stab/4_wipe.webp", 0.25)
    $ TS.p(1.25)
    show yuri stab_5
    $ TS.p(0.7)
    show yuri stab_6:
        2.55
        easeout_cubic 0.5 yoffset 300
    show blood as blood2:
        pos (235,335)
    $ TS.p(2.55)
    hide blood
    hide blood2
    $ TS.p(0.25)
    play sound fall
    $ TS.p(0.25)
    python:
        _preferences.volumes['sfx'] = .65
        _preferences.volumes['music'] = .45
    show sayori 4p at h32
    show natsuki scream at h33
    $ TS.s(ts_showscreens_fast)
    "Мы втроём смотрим на уже бездыханную Юри."
    show natsuki 1zb at f33
    n "Кажется, меня..."
    show natsuki 1zb at h33
    $ TS.p(0.7)
    show natsuki 1zb at h33
    $ TS.p(1)
    show natsuki vomit at h33
    $ TS.p(1.5)
    play sound sfx_body_bump
    show yuri stab_6 at ts_punch2()
    show natsuki at lhide
    hide natsuki
    play sound2 door_break
    "Нацуки выметается прочь из кабинета."
    show sayori 4w at f32
    s "А ты что смотришь? Помоги ей!"
    show sayori 4w at t32
    m "Во-первых, ей уже больше ничего не поможет. А во-вторых, уже завтра всё вернётся в изначальную точку."
    show sayori 4w at f32
    s "Что значит «завтра всё вернётся в изначальную точку»? Моника, твоя подруга умерла на твоих и наших глазах, а тебе всё равно?!"
    show sayori 4w at t32
    m "Сайори..."
    show sayori 2u at t32
    m "Что, если я скажу тебе, что всё происходящее – нереально, и что я это всё уже в третий раз вижу?"
    m "Нет, конечно, конкретно это я тоже вижу впервые, но в целом – да, одна и та же неделя повторяется уже три раза..."
    show sayori 3v at f32
    s "Я отвечу, что ты совсем из ума выжила."
    s 4w "Как ты не понимаешь? Юри только что зарезалась до смерти, а тебе хоть бы что!"
    show sayori 4w at t32
    m "Иногда мне тоже кажется, что я совсем спятила..."
    em "И далеко не тебе одной."
    show sayori 3u at t32
    stop music fadeout 5
    m "Но поверь мне, завтра всё будет точно так же, как и в прошлую субботу. Ты ничего из всего произошедшего за эту неделю даже помнить не будешь."
    m "А я, пожалуй, пойду. Время уже позднее, а мы и так уже засиделись."
    m "И да, насчёт этого..."
    "Я показываю на уже начавшую разлагаться Юри."
    $ persistent.sprite_time = "cloudly"
    m "И да, насчёт этого...{fast} Тоже не переживай. Всё восстановится.{w=2} Во всех смыслах этого слова."
    stop ambience fadeout 3
    play music ts_cr_cof

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    $ persistent.sprite_time = "day"
    play sound chasiki fadein 1
    scene ts_hotel_rec
    with ts_lap
    stop sound fadeout 1

    $ TS.s(ts_showscreens)
    
    play sound nfy
    if _preferences.language == "english":
        $ renpy.notify("Fifth cycle")
    else:
        $ renpy.notify("Цикл пятый")

    if _preferences.language == "english":
        $ misc_name = "Receptionist"
    else:
        $ misc_name = "Администратор"
    show harumi 2ch at f11
    misc "Добрый день, девушка. Добро пожаловать в нашу гостиницу. Меня зовут Сайка."
    if _preferences.language == "english":
        $ misc_name = "Saika"
    else:
        $ misc_name = "Сайка"
    misc 1cp "А я вас что-то раньше здесь не видела..."
    show harumi 1cl at t11
    m "Да, я... впервые в этом городе, так, проездом на недельку..."
    "Я ещё только учусь оборачивать цикличность всего здесь происходящего в свою пользу."
    "И первой пробой пера станет как раз наш местный отель и эта высокомерная кляча в роли администратора, которая мне даже в глаза не смотрит."
    "Заодно и выясню, можно ли здесь вообще что-либо оборачивать в свою пользу, или оно всё только пугать меня будет."
    show harumi 1cn at f11
    misc "Как-то вы... слишком молодо выглядите."
    misc "Вам хотя бы восемнадцать есть?"
    show harumi 1cm at t11
    m "Да, конечно."
    "Я без раздумий показываю ей свой паспорт, доказывая этой клуше, что я уже совершеннолетняя."
    "Я как-то не подумала, что все цифры в паспорте тоже могут запутаться, как и время на телефоне и все контакты на нём..."
    show harumi 2cl at t11
    "Однако она только улыбнулась, как будто увидев там что-то очень приятное."
    show harumi 1cp at f11
    misc "Да, это совсем другое дело..."
    misc 2ch "Чем я могу помочь?"
    show harumi 1cj at t11
    "В первую очередь ты сможешь помочь тем, чтобы наконец-то посмотреть на {i}меня{/i}, а не куда-то вдаль."
    m "Мне нужен самый дорогой номер в этом отеле на одну неделю."
    show harumi 2cn at f11
    misc "Ну вы же понимаете, что это очень дорого вам обойдётся?"
    show harumi 2cm at t11
    m "Понимаю, да. У меня просто..."
    "Я слегка понижаю голос."
    show harumi 1cy at t11
    m "{size=-6}Очень богатые родители...{/size}"
    "Что? Я же даже не вру. Ну разве что совсем чуть-чуть."
    "Но о достатке родителей я говорю {s}относительно{/s} честно."
    show harumi 2cx at f11
    misc "{size=-6}Так бы сразу и сказали...{/size}"
    misc 2ch "Значит, на неделю?"
    show harumi 2cj at t11
    m "Да. До следующей субботы. С оплатой по факту проживания."
    "Я одариваю её самой лучезарной улыбкой, которую только могу сделать."
    "Впрочем, что-то мне подсказывает, что на словах про богатых родителей эта меркантильная мымра готова была бы лично прислуживать мне всю неделю, только чтобы ей чаевых побольше дали."
    show harumi 2ch at f11
    misc "Да-да, конечно, всё ради наших любимых клиентов."
    $ TS.p(3)
    misc 2ce "Всё, готово. Ваш номер 444."
    misc 2ch "Хотите, чтобы я помогла вам донести вещи?"
    show harumi 2cj at t11
    "Меркантильная клуня. Иначе и не скажешь."
    m "Да нет, спасибо... у меня и вещей-то нет..."
    "Хорошо, что она не задалась вопросом, почему у меня нет вещей, если я, по идее, впервые в этом городе..."
    "По-видимому, она слишком озабочена своей собственной выгодой и тем, чтобы {b}так старательно не смотреть мне в глаза{/b}."
    show harumi 1cp at f11
    misc "Ладно..."
    misc 2ch "Если вам что-нибудь ещё будет нужно, можете смело обращаться ко мне по любому поводу!"
    show harumi 2cj at t11
    m "Несомненно..."
    show harumi 1ce at f11
    misc "Если что, лифт находится в той стороне..."
    show harumi 1ca at t11
    m "Ага, да, спасибо..."
    show harumi 1ca at cright with move
    hide harumi
    stop music fadeout 7
    "Ну, с почином меня, так сказать."
    "Теперь я в лучшем номере в отеле на другом конце города, а папа..."
    "А что папа? Забудет всё на следующей неделе, как и обычно. Да и все остальные тоже забудут всё."
    "В том числе и эта клуша."
    "Я же фактически выбила себе неделю в люксовом номере задаром."
    em "Ты, главное, не переусердствуй так..."
    m "А что такого будет? Всё равно к следующей субботе всё откатится до изначального состояния."

    play music ts_mots fadein 3

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound chasiki fadein 1
    scene ts_class
    with ts_lap
    stop sound fadeout 1

    $ TS.s(ts_showscreens)

    play sound nfy
    if _preferences.language == "english":
        $ renpy.notify("Tenth cycle")
    else:
        $ renpy.notify("Цикл десятый")

    "С каждым новым циклом я стала чувствовать себя всё вольготнее."
    "Последние пару циклов я иногда приходила в школу голышом. Благо хоть в эти дни было солнечно и в целом достаточно тепло, чтобы я просто не замёрзла."
    "Но что странно, так это то, что никто даже и бровью не повёл, что Моника, местная звезда школы, пришла в школу абсолютно нагой."
    "Ну ничего, я думаю, что это можно исправить."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    scene black with ts_paint
    $ TS.p(1)

    show ts_cor_split_animated
    show ts_of_split_animated
    $ TS.p(0.99)

    $ TS.s(ts_showscreens)

    if _preferences.language == "english":
        $ misc_name = "Raddan"
    else:
        $ misc_name = "Раддан"
    show daisuke 1ba at t44
    "Ага. Вот он. Сидит и кофе пьёт. Думает, какая же у него отличная работа."
    "Я без стука вламываюсь в дверь."

    play sound door_break
    scene ts_office
    show daisuke 1ba at t11
    $ TS.m(ts_razebal)
    "На лице директора ни один мускул не дрогнул."
    "Ни из-за того, что это как минимум неприлично и чересчур фамильярно так расхаживать, ни из-за того, что перед ним так-то красивая молодая девушка стоит."
    show daisuke 1bb at f11
    misc "Да, мисс Ида, здравствуйте. Вы что-то хотели?"
    show daisuke 1bh at t11
    $ currentpos = get_pos()
    play music "<from " + str(currentpos) + " loop 10.893>mod_assets/source/audio/ost/ts_emots.ogg"
    "Вместо ответа я просто залезаю к нему на стол и начинаю танцевать... танец не из самых пристойных, не забывая при этом отсвечивать всеми своими прелестями."
    "Благо, что они у меня хотя бы есть..."
    $ persistent.ingame_pizda = False
    "Спустя где-то минуту я наконец говорю максимально томным голосом."

    $ persistent.ingame_pizda = True
    $ TS.s(ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake))
    $ TS.m(ts_shluha_melkaya)
    show ts_psihuet3 zorder 3:
        alpha 0.5

    m "Господин Раддан, я уже очень давно хотела вам сказать..."
    m "Каждую ночь я засыпаю, думая только о вас..."
    m "Каждую ночь я убаюкиваю себя всякими... похотливыми мыслями..."
    $ gtextsuka = glitchtext(24)
    m "И даже ублажаю себя дезодорантом, думая, что это ваш [gtextsuka]."
    m "Скажу прямо: мы взрослые люди, и даже такое мелочное препятствие, как субординация, не помешает мне представить, чтобы вы ухватили меня за [gtextsuka]..."
    m "А затем [gtextsuka] меня во все [gtextsuka], пока мы оба не [gtextsuka]."
    m "А после этого я буду выкрикивать ваше имя, чтобы вся школа слышала..."
    m "Я хочу вас, господин Раддан."
    m "Разве не изумительно это звучит?"
    m "Скажите мне, господин Раддан, скажите мне только одно: «Да, я тоже хочу тебя, Моника»..."
    stop music
    $ persistent.ingame_pizda = False
    hide ts_psihuet3
    $ TS.s()
    $ TS.m()
    show daisuke 2bf at f11
    misc "Мисс Ида, вы мешаете мне работать."
    show daisuke 2bh at t11
    "Тьфу ты. Не сработало."
    "Что же, остаётся только один вариант..."
    show daisuke 2bg at h11
    "Я медленно залезаю к нему под стол и начинаю{w=0.44}{nw}"
    play music ts_first_day_of_sun fadein 1
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound chasiki fadein 1
    scene ts_club
    show sayori 3r at f11
    with ts_lap
    stop sound fadeout 1

    $ TS.s(ts_showscreens)
    
    play sound nfy
    if _preferences.language == "english":
        $ renpy.notify("Fifteenth cycle")
    else:
        $ renpy.notify("Цикл пятнадцатый")    

    s "Очень здорово, Моника, мне очень понравилось!"
    show sayori 3q at t11
    "А тем временем идёт третий месяц этого ада."
    "Вся эта предсказуемость мне уже изрядно поднадоела..."
    "Я уже почти два месяца не ночевала дома, а вместо этого сразу после того, как я говорю с Сайори и иду к дому Миры, в котором мне, естественно, никто не открывает, сразу же направляюсь в отель."
    "Плохо то, что это единственный отель в городе. Но хорошо то, что каждый раз меня приветствует одна и та же меркантильная клуша."
    "Я уже заученным текстом говорю о том, что мне нужен номер на неделю, и администратор каждый раз направляет меня в один и тот же номер."
    "Хоть бы в разных номерах давали пожить!{w=1} Хотя, с другой стороны, есть большая вероятность, что это их единственный люксовый номер во всём отеле..."
    "Но сейчас мы не об администраторе говорим, который за все эти разы так и не удосужился посмотреть мне прямо в глаза, а с Сайори беседуем."
    "И на этот эпизод у меня припасено одно... приспособление."
    "Очень тонкое... и очень острое... приспособление."
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"
    scene ts_club
    show yuri 3y7 at t21
    show natsuki 2o at t22
    with pushleft
    $ TS.p(2.5)
    $ TS.s(ts_showscreens)
    "Отлично. Они в очередной раз горячо спорят о том, какой стиль литературы лучше."
    "Никто и не заметит, если через пару минут этих стилей литературы станет... на один меньше."
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"
    scene ts_club
    show sayori 3q at t11
    with pushright
    $ TS.s(ts_showscreens)
    stop music fadeout 3
    "Я возвращаюсь к Сайори со злобной ухмылкой на лице."
    show sayori 2n at t11
    $ TS.p(1.23)
    $ TS.s(ts_showscreens_fast)
    show sayori 3l at f11
    s "М-Моника, а ты ч-чего так ухмыляешься?.."
    show sayori 3l at t11
    m "Да просто... надоело мне это всё..."
    m "И поскольку именно ты мой вице-президент, пожалуй, начну с тебя."

    show sayori 3k at t11
    $ TS.p(0.6)
    show sayori 4z at h11
    $ TS.p(0.15)
    play music ts_inferno
    stop ambience
    play sound aw_axe_hit
    $ TS.m(ts_glazkam_pizda_anim)
    show sayori glazkam_pizda at h11
    $ TS.p(1)
    play sound aw_axe_hit_1
    $ TS.m(ts_glazkam_pizda_anim)
    show sayori glazkam_pizda1 at h11
    $ TS.p(0.3)
    play sound2 sfx_body_bump
    show sayori glazkam_pizda1 at ts_punch()
    $ TS.s(ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake))
    "Резким движением я протыкаю Сайори один глаз. Ещё спустя момент Сайори лишилась и второго раза."
    hide sayori
    "Она даже закричать не успела."
    "Да, это мерзко. Да, это всё ещё моя подруга. Да, хоть это и сон, но по факту я уже убийца..."
    "Но а как ещё мне развлекаться, если я за три с лишним месяца одного и того же уже все легальные способы веселья перепробовала?"
    show monika 2p at f11
    with linearblur
    em "И ты же на этом не остановишься, я правильно полагаю?"
    show monika 2o at t11
    m "Очень правильно полагаешь."
    "Адреналин буквально кипит, а моё неровное дыхание, наверное, слышит вся школа."
    m "{size=+15}{b}СЛЫШИТЕ? СЛЕДУЮЩЕЙ СУББОТЫ НИКОГДА НЕ НАСТУПИТ!{/b}{/size}" with vpunch

    play sound chasiki fadein 1
    scene ts_club
    show natsuki 2y at f11
    with ts_lap
    stop sound fadeout 1
    
    play sound nfy
    if _preferences.language == "english":
        $ renpy.notify("Twenty fifth cycle")
    else:
        $ renpy.notify("Цикл двадцать пятый")

    n "Ну так, средне. Могло быть и лучше."
    show natsuki 2y at t11
    "Ах ты выскочка малолетняя..."
    show natsuki 2z at f11
    n "Смотри и учись, как работают настоящие профессионалы."
    show natsuki 2z at t11
    "Она протягивает мне свой стих."
    show natsuki 2zb at h11
    "Однако вместо этого я просто кромсаю его."
    show natsuki 2m at f11
    n "М-Моника, ты ч-чего? Если ты так на мнение о стихе обиделась, то прости..."
    n "Но м-мне ещё и другим девочкам его показывать..."
    show natsuki 2n at t11
    m "Не покажешь. Ты уже больше ничего в своей жизни не покажешь."
    show natsuki 2zb at t11
    if persistent.cens_mode == True:
        m "Иди сюда, сучара."
    else:
        m "Иди сюда, мелкая."
    $ TS.p(1.3)
    show natsuki scream at h11
    show natsuki screamnohead at h11
    show natscreamhead at h111
    $ TS.p(1)
    show natscreamhead at t111
    play sound2 scream_normal
    play sound bones_breaking
    $ TS.p(1)
    stop sound2 fadeout 1
    show natscreamhead at ts_punch1()
    show natsuki screamnohead at ts_punch()
    $ TS.p(0.2)
    play sound sfx_body_bump
    $ TS.p(1)
    show sayori 4z at h21
    show yuri 3y2 at h22
    m "А вы что смотрите? Собрание окончено! И все собрания до конца недели отменяются!"
    show yuri 3y2 at h22
    m "Ты следующая на очереди."

    play sound chasiki fadein 1
    scene ts_club
    show yuri 1j at f11
    with ts_lap
    stop sound fadeout 1
    
    play sound nfy
    if _preferences.language == "english":
        $ renpy.notify("Fortieth cycle")
    else:
        $ renpy.notify("Цикл сороковой")

    y "Ну, стихотворение хорошее, но у меня есть несколько советов."
    y 1k "Во-первых,{w=0.7}{nw}"
    show yuri 2p at h11
    if persistent.cens_mode == True:
        m "Так, всё, с меня хватит этого высокомерного пиздежа."
    else:
        m "Так, всё, довольно этого высокомерного трёпа."
    show yuri 2o at t11
    m "Резаться любишь, да?"
    show yuri 2y2 at h11
    "Ну посмотрим, как долго ты протянешь с отрезанными конечностями..."
    window hide
    $ TS.m(ts_knife_pizda_anim)
    play sound aw_knife_slash_2
    show yuri 2y2 at ts_punch()
    show ts_bloodanim zorder 3
    play sound3 scream_normal
    play sound2 sfx_body_bump
    $ TS.p(1)
    $ TS.m(ts_knife_pizda_anim)
    play sound aw_knife_slash_2
    show ts_altbloodanim zorder 3
    $ TS.p(1)
    $ TS.m(ts_knife_pizda_anim)
    play sound aw_knife_slash_2
    show sayori 4z at t31
    show natsuki scream at f33
    m "О-хо-хо, девочки, смотрите, сколько у неё порезов на руках!"
    m "Я сделала ещё один, ты же не против?"
    window hide
    play sound fb
    scene yrec_sdoh_nahui with flash

    $ TS.m(ts_knife_pizda_anim)
    play sound aw_knife_slash_2

    show ts_bloodanim zorder 3
    play sound2 sfx_body_bump
    $ TS.p(1)
    $ TS.m(ts_knife_pizda_anim)
    play sound aw_axe_hit
    show ts_altbloodanim zorder 3
    $ TS.p(1)
    $ TS.m(ts_knife_pizda_anim)
    play sound aw_axe_hit_1
    $ TS.p(1)
    stop music
    $ TS.b()
    play sound ts_glitch4
    scene ts_club
    with memglitchbolee
    stop sound
    $ TS.s(ts_showscreens)
    
    play sound nfy
    if _preferences.language == "english":
        $ renpy.notify("One hundredth cycle")
    else:
        $ renpy.notify("Цикл сотый")

    "Очередная неделя, очередное тупое однообразное собрание клуба..."
    "В последние несколько циклов я вообще на эти собрания не ходила, вместо этого занимаясь более полезными делами."
    "Впрочем..."
    play music ts_truth fadein 1
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"
    
    scene mon_piano_another_glitch_anim at ts_ustal_suka
    with ed_night_dis

    $ TS.s(ts_showscreens)


    "А какие полезные дела у меня ещё могут быть?"
    "Всё, что я хотела сделать, я сделала ещё много месяцев назад."
    "Всё, чего я при иных обстоятельствах никогда бы не хотела делать, я сделала сразу после этого."
    "Я десятки раз насиловала и убивала каждую из девочек. Иногда даже нескольких сразу. А иногда и вообще всех троих."
    "Я выкалывала им глаза, четвертовала их, отрезала все конечности..."
    "Пару раз я даже отрезала грудь Юри и примеряла её на себя – теперь-то будет знать..."
    "Я пускала газ в клубную комнату, я сбрасывала их с крыши школы, я их поджигала, я сшивала Юри и Нацуки, чтобы они были поистине {b}неразлучной{/b} парочкой..."
    "Иногда я применяла поистине средневековые методы пыток."
    "Например, я растягивала Нацуки, чтобы она «стала более длинной», или наоборот, отрезала пару костей у Юри, чтобы она «стала чуть короче»..."
    "Мой Литературный клуб стал посольством Холокоста."
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"
    $ TS.p(1)
    $ TS.s(ts_showscreens)
    
    play sound nfy
    if _preferences.language == "english":
        $ renpy.notify("Excessive drinking is harmful to your health")
    else:
        $ renpy.notify("Чрезмерное употребление алкоголем вредно для вашего здоровья")
    
    "Также я начала пить. Намного сильнее, чем оба родителя вместе взятые."
    "Каждый вечер я возвращаюсь из школы с новой бутылкой вина."
    "Иногда я пью с самого утра, и уже в школу прихожу вдрызг пьяной."
    "Когда мне показалось, что вина уже недостаточно, я перешла на более крепкие напитки."
    "Водка, коньяк, самогон, абсент... Пару раз я даже чистый спирт пила, и запивала кипятком."
    "Продолжалось это пару часов в день, а после этого я уже была полумёртвой. И так каждый день."
    
    play sound nfy
    if _preferences.language == "english":
        $ renpy.notify("Smoking is also harmful and dangerous to your health")
    else:
        $ renpy.notify("Курение также вредно и опасно для вашего здоровья")
    
    "Я начала курить. Сначала это была пара сигареток в день, затем пачка, две, и по нарастающей."
    "Каждую новую неделю у меня была новая марка сигарет."
    "Поначалу я думала, что одного блока на неделю должно быть вполне достаточно, однако со временем я поняла, что даже целого блока на жалкие семь дней мне не хватает."
    
    play sound nfy
    if _preferences.language == "english":
        $ renpy.notify("Drugs are even more harmful and dangerous to your health. Don't even think of smoking and shooting up stuff")
    else:
        $ renpy.notify("Наркотики – это ещё более вредно и опасно для вашего здоровья. Даже не вздумайте курить и колоться")
    
    "Вместе с этим я начала пробовать наркотики. Сначала лёгкая травка, а затем кокаин, героин, синтетика..."
    "К концу недели я уже скорее не молодая красивая девушка, а сорокалетняя баба с метровым целлюлитом."
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"
    $ TS.p(1)
    $ TS.s(ts_showscreens)
    "Но кажется, что эти циклы будто насмехаются надо мной."
    "Каждый раз, когда я придумываю новый изощрённый способ убийства Юри, Сайори или Нацуки..."
    "Каждый раз, когда я покупаю всё более крепкий алкогольный напиток..."
    "Каждый раз, как я уродую себя новыми сигаретами или наркотиками..."
    "Всё в итоге просто откатывается до изначального состояния."
    "Я так больше не могу!"
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"
    $ TS.p(2)
    $ TS.s(ts_showscreens)
    "Хотя постойте..."
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"
    $ TS.p(1)
    $ TS.s(ts_showscreens)
    "Вместо того, чтобы убивать девочек и продолжать мучения, которые растягиваются на целую неделю..."
    "Можно же сразу начать с себя, и тогда мучения резко закончатся."
    "А быть может, то я и проснусь сразу же."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound2 pageflip
    scene ts_closet
    with wipeleft_scene

    $ TS.s(ts_showscreens)

    "Надеюсь, в кладовой есть верёвка..."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    $ TS.m(ts_verevka_vzyal)
    $ TS.p(2)

    $ TS.s(ts_showscreens)

    "Ага, вот она!"
    "Мне, конечно, очень не хочется этого делать..."
    "Но если это способ выбраться из этой кошмарной «Недели Сурка», то я просто должна."
    "...и как только Юри так легко себя убила?"
    "Я уже не говорю о том, что десятки раз её убивала я..."
    "Я стою перед трудным выбором. Убить себя, чтобы никто не мучился, или сдаться перед чёртовым инстинктом самосохранения."
    "Впрочем... это же просто сон, верно?"
    "Поэтому я натягиваю петлю через голову и забираюсь на стул повыше."
    "Надеюсь, петля выдержит..."
    play sound bodyfall_final
    play sound_loop ts_udushie
    scene ts_mon_povesilas
    $ TS.m(ts_trans_povesilas_mon_maloletka_konchennaya)
    "Возможно... так... проснусь..."
    stop sound_loop
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound chasiki fadein 1
    scene black
    with ts_lap
    stop sound fadeout 1

    play sound nfy
    if _preferences.language == "english":
        $ renpy.notify("One hundred fiftieth cycle")
    else:
        $ renpy.notify("Цикл сто пятидесятый")

    $ TS.s(ts_showscreens)
    "А может... так?"
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    show ts_knife_suicide at ts_hidescreens_fast

    play sound aw_knife_slash_2
    $ TS.p(0.25)
    show ts_knife_suicide at ts_showscreens_fast
    show ts_bloodanim
    $ TS.p(0.25)
    show ts_knife_suicide at ts_hidescreens_fast
    play sound aw_knife_slash_1
    $ TS.p(0.25)
    show ts_knife_suicide at ts_showscreens_fast
    show ts_altbloodanim
    $ TS.p(0.25)
    show ts_knife_suicide at ts_hidescreens_fast
    play sound aw_knife_slash_2
    $ TS.p(0.25)
    show ts_knife_suicide at ts_showscreens_fast
    $ TS.p(0.25)
    show ts_knife_suicide at ts_hidescreens_fast
    play sound aw_knife_slash_2
    $ TS.p(0.25)
    show ts_knife_suicide at ts_showscreens_fast
    $ TS.p(0.25)
    play sound fb
    scene ts_menu_move_anim_bad_end
    with flash
    $ TS.p(2)
    play sound chasiki fadein 1
    scene black
    with ts_lap
    stop sound fadeout 1

    play sound nfy
    if _preferences.language == "english":
        $ renpy.notify("One hundred seventy sixth cycle")
    else:
        $ renpy.notify("Цикл сто семьдесят шестой")

    $ TS.s(ts_showscreens)
    "Или... так?"
    window hide
    play sound ts_introshoot
    scene ts_sky_fon at ts_padenie_s_krishi_suka
    $ TS.p(4)
    stop music
    scene black
    play sound sfx_body_bump
    $ TS.p(1)

    $ TS.s(ts_showscreens)

    play sound nfy
    if _preferences.language == "english":
        $ renpy.notify("Two hundredth cycle")
    else:
        $ renpy.notify("Цикл двухсотый")

    show monika 2p at f11
    with linearblur
    em "Сколько это ещё будет продолжаться?"
    show monika 2o at t11
    m "А я не знаю, это ты мне скажи."
    m "Кто из нас двоих всемогущее создание, ты или я?"
    show monika 3r at f11
    play music ts_mk fadein 2
    em "Я всего лишь твоё подсознание, и я знаю не сильно больше твоего."
    em 2n "Возможно, я знаю {i}самую малость{/i} больше..."
    show monika 2p at f11 with dissolve_cg
    em "Но всё равно эта разница очень несущественна..."
    show monika 2o at t11 with dissolve_cg
    m "Тогда почему?.."
    show monika 2d at f11
    em "Почему что?"
    show monika 1f at t11
    m "Почему я не могу выбраться из этой проклятой недели? Почему я не могу проснуться?"
    m "Я уже всё перепробовала! Я убивала всех своих друзей самыми изощрёнными способами, я убивала себя бессчётное количество раз..."
    m "А оно всё опять по новой... Я уже не могу так больше!"
    show monika 2r at f11
    em "Я уже говорила тебе, что ты самое настоящее животное?"
    show monika 2q at t11
    m "Вроде говорила... а вроде не говорила... не помню..."
    show monika 2i at f11
    em "В любом случае, скажу ещё раз: ты животное."
    em "Ты уже не человек, ты настоящий зверь. И говорю я это отнюдь не в хорошем смысле."
    em "Ты же понимаешь, что ты просто поехавшая?"
    em "Про убийства какие-то рассказываешь, про газ в клубе, про сшивание Юри и Нацуки..."
    em "Про водку какую-то, абсент, траву, сигареты..."
    em "Одна история изощрённее другой."
    show monika 2h at t11
    m "Ну а что мне ещё делать, если я уже всё сделала всё мыслимое и немыслимое?"
    show monika 2i at f11
    em "А ты не думала, что, вместо того, чтобы убивать, насиловать милых девочек, пить, курить и колоться, ты могла бы заняться чем-нибудь полезным?"
    em 5b "Ты могла бы снова научиться играть на пианино, выучить иностранный язык, и даже не один, могла бы всерьёз заняться шахматами, ты могла бы заняться биологией, в конце-то концов!"
    em 5c "Но нет, у тебя «мыслимое и немыслимое» заключается только в способах убийства этих девочек или в способах обхитрить эту курицу в отеле!"
    show monika 5c at t11
    m "Я... как-то... не подумала..."
    show monika 5b at f11
    em "Да ты вообще думать не умеешь, как я погляжу..."
    em 2r "Ладно, повторяю для особо тупых бездарностей один раз: сон закончится, когда ты встретишь... очень необычного человека."
    show monika 2q at t11
    m "К-какого человека?"
    show monika 5b at f11
    em "Я и так тебе уже достаточно жирно намекнула на способ окончания сна в принципе. Разжёвывать для тебя я не собираюсь."
    show monika 5c at t11
    m "Скажи хоть, мужчина это или женщина?"
    show monika 2i at f11
    em "Не скажу. Скажу лишь, что этого человека ты {b}очень{/b} хорошо знаешь."
    em "Всё, у меня нет времени на дальнейшие разговоры."
    hide monika with linearblur
    m "П-подожди! А к-как же{w=1}{nw}"
    $ persistent.ingame_pizda = True

    python:
        _preferences.volumes['sfx'] = 1.0

    play sound2 ts_smeh_pizdec

    $ TS.s(ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake))

    play music ts_glitch_music13
    scene ts_closet_glitches_balya:
        align(0.5, 0.5) zoom 1.0
        ease 0.1 align(0.2, 0.5) zoom 2.0
        ease 0.1 align(0.8, 0.2) zoom 3.0
        ease 0.1 align(0.3, 0.7) zoom 2.5
        ease 0.1 align(0.4, 0.9) zoom 4.0
        ease 0.1 align(0.5, 0.5) zoom 1.0
        repeat
    show ts_maloletka_pozvonok_sloman_nahui:
        align(0.5, 0.5) zoom 1.0
        ease 0.1 align(0.1, 0.2) zoom 2.0
        parallel:
            ease 0.02 align(0.8, 0.2) zoom 3.0
            ease 0.02 align(0.4, 0.4) zoom 4.0
            ease 0.02 align(0.9, 0.6) zoom 5.0
            ease 0.02 align(0.8, 0.2) zoom 3.0
            repeat

    $ gtextsuka = glitchtext(42)
    $ gtextsuka = glitchtext(24)
    n "[gtextsuka]{w=0.33}{nw}"
    $ gtextsuka = glitchtext(24)
    $ gtextsuka1 = glitchtext(48)
    n "[gtextsuka][gtextsuka1]{w=0.33}{nw}"
    $ gtextsuka = glitchtext(36)
    n "[gtextsuka]{w=0.33}{nw}"
    $ gtextsuka = glitchtext(24)
    $ gtextsuka1 = glitchtext(12)
    $ gtextsuka2 = glitchtext(23)
    $ gtextsuka3 = glitchtext(4)
    n "[gtextsuka][gtextsuka1][gtextsuka2][gtextsuka3]{w=0.33}{nw}"

    play sound2 ts_flashback
    scene ts_kitchen_psyhodelic_pizdec_glitch:
        align(0.5, 0.5) zoom 1.0
        ease 0.1 align(0.2, 0.5) zoom 2.0
        ease 0.1 align(0.8, 0.2) zoom 3.0
        ease 0.1 align(0.3, 0.7) zoom 2.5
        ease 0.1 align(0.4, 0.9) zoom 4.0
        ease 0.1 align(0.5, 0.5) zoom 1.0
        repeat
    show ts_hiroto_psyhodelic_pizdoc_eblet:
        align(0.5, 0.5) zoom 1.0
        ease 0.1 align(0.1, 0.2) zoom 2.0
        parallel:
            ease 0.02 align(0.8, 0.2) zoom 3.0
            ease 0.02 align(0.4, 0.4) zoom 4.0
            ease 0.02 align(0.9, 0.6) zoom 5.0
            ease 0.02 align(0.8, 0.2) zoom 3.0
            repeat

    $ gtextsuka = glitchtext(24)
    ts_ft "[gtextsuka]{w=0.33}{nw}"
    $ gtextsuka = glitchtext(24)
    $ gtextsuka1 = glitchtext(48)
    ts_ft "[gtextsuka][gtextsuka1]{w=0.33}{nw}"
    $ gtextsuka = glitchtext(36)
    ts_ft "[gtextsuka]{w=0.33}{nw}"
    $ gtextsuka = glitchtext(24)
    $ gtextsuka1 = glitchtext(12)
    $ gtextsuka2 = glitchtext(23)
    $ gtextsuka3 = glitchtext(4)
    ts_ft "[gtextsuka][gtextsuka1][gtextsuka2][gtextsuka3]{w=0.33}{nw}"

    play sound2 ts_smeh_pizdec
    scene nat_pizdos:
        align(0.5, 0.5) zoom 1.0
        ease 0.1 align(0.2, 0.5) zoom 2.0
        ease 0.1 align(0.8, 0.2) zoom 3.0
        ease 0.1 align(0.3, 0.7) zoom 2.5
        ease 0.1 align(0.4, 0.9) zoom 4.0
        ease 0.1 align(0.5, 0.5) zoom 1.0
        repeat
    show n_cg1b228:
        align(0.5, 0.5) zoom 1.0
        ease 0.1 align(0.1, 0.2) zoom 2.0
        parallel:
            ease 0.02 align(0.8, 0.2) zoom 3.0
            ease 0.02 align(0.4, 0.4) zoom 4.0
            ease 0.02 align(0.9, 0.6) zoom 5.0
            ease 0.02 align(0.8, 0.2) zoom 3.0
            repeat

    $ gtextsuka = glitchtext(24)
    n "[gtextsuka]{w=0.33}{nw}"
    $ gtextsuka = glitchtext(24)
    $ gtextsuka1 = glitchtext(48)
    n "[gtextsuka][gtextsuka1]{w=0.33}{nw}"
    $ gtextsuka = glitchtext(36)
    n "[gtextsuka]{w=0.33}{nw}"
    $ gtextsuka = glitchtext(24)
    $ gtextsuka1 = glitchtext(12)
    $ gtextsuka2 = glitchtext(23)
    $ gtextsuka3 = glitchtext(4)
    n "[gtextsuka][gtextsuka1][gtextsuka2][gtextsuka3]{w=0.33}{nw}"

    $ gtextsuka = glitchtext(42)
    m "[gtextsuka]{nw}"

    stop sound2
    stop music

    $ TS.s()

    $ persistent.ingame_pizda = False

    python:
        _preferences.volumes['sfx'] = .65
        _preferences.volumes['music'] = .45

    play sound nfy
    if _preferences.language == "english":
        $ renpy.notify("??? cycle")
    else:
        $ renpy.notify("Цикл ???")

    $ TS.b()
    $ persistent.uncolorize = "none"
    window hide
    play sound fb
    scene black with flash
    $ TS.s(ts_showscreens)
    s "{size=-6}..ика!{/size}"
    s "{size=-4}Моника!{/size}"
    s "Моника, просыпайся уже!" with hpunch
    play sound ts_glitch2
    s "Вставай давай, пьянь малолетняя!" with vpunch
    stop sound
    "Опять всё заново..."
    window hide
    play sound fb
    scene ts_sayori_bedroom
    show sayori 4pi at t11
    with flash
    $ TS.s(ts_showscreens)
    "Уже в который раз передо мной предстаёт всё та же Сайори во всё той же пижаме во всё той же комнате со всё тем же выражением лица."
    "Как же это всё мне уже надоело..."
    m "И тебе привет, Сайори."
    m "Всё, сейчас я протрезвела, со мной всё нормально, пойду уже домой, а то папа волнуется..."
    show sayori 3ph at f11
    s "Моника, п-постой!..{w=0.3}{nw}"
    show sayori 3pg at t11
    m "Сайори, нет времени ждать, фестиваль уже через неделю, просто выпусти меня, и я пойду..."
    show sayori 3ph at f11
    s "Ладно, ладно, хорошо... "
    extend 2pl "Только потише, а то родители спят ещё..."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play music ts_alt fadein 2

    play sound chasiki fadein 1
    scene ts_residential
    with ts_lap
    stop sound fadeout 1

    $ TS.s(ts_showscreens)

    show monika 2p at f11
    with linearblur
    em "Ты уже в тысячный раз ходишь к ней. Буквально."
    show monika 2o at t11
    m "Я ещё с первого раза всё поняла. Но почему-то каждый раз, как я выхожу из дома Сайори, что-то тянет меня сюда..."
    show monika 2q at t11
    "Я в очередной подхожу к дому Миры."
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_sayori_house
    with wipeleft_scene

    $ TS.s(ts_showscreens)

    "Подходя к дому, я с удивлением обнаруживаю, что на этот раз дверь не заперта."
    "Странно, очень странно..."
    k "Кого там принесло ещё?"
    "Сердце буквально замерло."
    "Пусть мы очень давно не общались, этот голос я узнаю из тысячи."
    show kuninobu 2h3 at ln11
    "Мира..."
    m "М-Мира, это я, М-Моника..."
    show kuninobu 1e at t11
    m "Я так давно тебя не видела..."
    "Я невольно начинаю плакать."
    "Да, пусть мы и не стали друзьями навсегда, а наоборот, со временем лишь отдалялись друг от друга..."
    "Она всё равно моя самая старая и самая первая подруга."
    show kuninobu 2e2 at t11
    "Я падаю на неё и начинаю рыдать что есть сил."
    show kuninobu 3e4 at f11
    k "Моника, да тише ты, не надо так резко..."
    show kuninobu 2e5 at t11
    "Мы медленно отпускаем друг друга из объятий."
    "Только сейчас я заметила, что Мира одета в школьную форму."
    show kuninobu 1f1 at t11
    "Я решаю спросить её об этом."
    show kuninobu 3b at f11
    k "Так я как раз по дороге из школы и умерла!"
    k 2j "Разрыв сердца. Две минуты, и меня уже не стало."
    k "Теперь я просто... странствую."
    show kuninobu 2i at t11
    m "Выглядишь как-то... чересчур оптимистично как для того, кто умер в... с-сколько тебе там лет было?"
    show kuninobu 2ff at f11
    k "Да сейчас уже и не вспомню..."
    k 2d "Но уже после того, как тебя в другой класс перевели."
    show kuninobu 2a at t11
    "Теперь понятно, почему я совершенно ничего не слышала о ней с тех самых пор..."
    show kuninobu 3e4 at f11
    k "Нет, конечно, похоронили меня не в школьной форме, а со всеми почестями, как полагается..."
    k 2d "Но для простоты и удобства я {i}блуждаю{/i} именно в ней."
    show kuninobu 2f1 at t11
    "Всё это слишком сложно для понимания..."
    m "А... Почему я тебя вообще вижу? Ты же сама говорила, что... умерла уже..."
    show kuninobu 3z at f11
    stop music fadeout 7
    k "Ах, это..."
    k 2s1 "Так ты же спишь. Всё это – не по-настоящему."
    k 1p "Нет, то, что я умерла – это так и было, я умерла на самом деле..."
    k 2f "Но этот наш разговор, который у нас только что был – этого на самом деле никогда не было."
    k "Как не было и вообще всего этого, всех этих циклов, всей этой дури, всех этих ужасов..."
    show kuninobu 1f1 at t11
    m "От-ткуда т-ты...{w=1}{nw}"
    show kuninobu 2o1 at f11
    $ persistent.ingame_pizda = False
    k "Всё это знаю? Так это всё тебе только снится."
    play sound2 ts_smeh_pizdec fadein 2
    show ts_glaza_k with Dissolve(4)
    $ persistent.ingame_pizda = True

    python:
        _preferences.volumes['sfx'] = 1.0

    $ TS.s(ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake))
    show black zorder 5 at ts_black_glitch
    k "Проснись, Моника... Меня уже не вернуть, но хотя бы ты поживи ещё."
    show blackout_exh zorder 5
    k "{cps=10}Проснись, Моника...{/cps}{nw}"
    show anim_exhausted zorder 5
    k "{cps=4}Проснись!{/cps}{nw}"
    show m_rectstatic zorder 5
    k "{cps=2}ПРОСНИСЬ!{/cps}" with vpunch
    window hide
    $ TS.m(ts_padenie_ebalon_vniz_suka)
    $ TS.p(1)
    play sound sfx_body_bump
    scene black
    $ persistent.ingame_pizda = False
    $ TS.s()
    $ TS.p(2)
    $ TS.b()
    if unluck_ball >= 5:
        jump ts_bad_ending_blya
    elif unluck_ball < 5:
        jump ts_good_ending_blya