label ts_scenario_10:

    $ TS.b()

    python: # ОБНОВЛЯЕМ RPC
        ts_rpc_carter10()

    $ persistent.rpclabel = "10"

    $ persistent.carter2menu = False
    $ persistent.carter3menu = True
    $ persistent.badendmenuperedglitch = False
    $ persistent.badendmenuskipglitch = False
    $ persistent.badendmenu = False
    $ persistent.goodendmenu = False
    $ persistent.peredbadendmenu = False
    $ persistent.peredgoodendmenu = False

    if _preferences.language == "english":
        $ save_name = "Descent to madness"
    else:
        $ save_name = "Спуск в безумие"

    play sound chp
    if _preferences.language == "english":
        $ Chapter("ACT THREE")
        $ Chapter("ACT THREE")
        $ Chapter("chapter two")
        $ Chapter("chapter two")
        $ Chapter("Descent to madness")
        stop sound fadeout 7
        $ Chapter("Descent to madness")
    else:
        $ Chapter("АКТ ТРЕТИЙ")
        $ Chapter("АКТ ТРЕТИЙ")
        $ Chapter("Глава вторая")
        $ Chapter("Глава вторая")
        $ Chapter("Спуск в безумие")
        stop sound fadeout 7
        $ Chapter("Спуск в безумие")

    $ persistent.uncolorize = "lite"

    play music ts_pb_sn fadein 2
    play sound ts_alarm fadein 2

    $ TS.p(2)

    scene ts_bedroom
    show unblink
    $ TS.m(ts_vstavai_shashlik)
    $ TS.p(3)
    play sound svet_on
    $ TS.p(1.5)

    $ TS.s(ts_showscreens)

    "Ух-х-х..."
    "На часах до боли привычные семь утра."
    stop sound fadeout 2
    "Начинаем новую... старую неделю."
    "Остаток выходных я провела с папой и максимально делала вид, что ничего сверхъестественного не произошло."
    "Папа, кажется, делал то же самое. Или он просто посчитал, что это просто такие последствия от похмелья..."
    "В любом случае, мы оба сделали вид, что это были самые обычные выходные."
    "Хотя изнутри меня всё терзало чувство, что это всё как-то... неправильно. Очень неправильно."
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_bathroom
    with wipeleft_scene


    $ TS.m(ts_clean_eblet)
    $ TS.p(2)
    play sound open_water_sink
    $ TS.p(0.5)
    stop sound
    play sound_loop water_sink_stream
    $ TS.p(1)
    play sound water_splash
    $ TS.p(1.6)
    stop sound_loop
    play sound close_water_sink
    $ TS.p(0.5)

    $ TS.s(ts_showscreens)

    "Нет, серьёзно, почему так? Почему никто ничего не помнит?"
    show monika 1bd at f11
    em "Я же тебе уже неоднократно говорила, что никто ничего не помнит, потому что этого в принципе никогда не происходило."
    show monika 1bf at t11
    m "Но я же помню! Значит, всё-таки происходило!"
    show monika 2bd at f11
    em "Об этом я тоже говорила. Ты помнишь, и я помню, потому что это всё просто твой сон."
    show monika 2bc at t11
    m "Но мне же снились сны! Как это вообще может быть, сон во сне?"
    show monika 2bi at f11
    em "Значит, это были очень детализированные сны."
    show monika 2bh at t11
    m "Но...{w=0.7}{nw}"
    show monika 2bi at f11
    em "Не задавай глупых вопросов. Лучше умывайся и чисть зубы, ты что-то задерживаешься, а тебе вообще-то ещё завтрак готовить."
    show monika 2bh at t11
    m "Но!..{w=0.44} Ладно, ладно, умываюсь уже..."
    show monika 3bk at f11
    em "Вот так-то лучше!"
    show monika 3bj at t11
    m "Хмф."
    show monika 1bc at t11
    "Я умываюсь и чищу зубы под синхронное молчание нас обеих."
    m "Бр-р-р..."
    "Я никогда так и не привыкну к холодной воде."
    "Почему я не могу просто умываться водой той же температуры, в которой я купаюсь?"
    show monika 1bd at f11
    em "Это уже к тебе вопросы. Но, насколько я знаю, папа твой всегда тебя поддержит, если ты захочешь попробовать что-то новое."
    show monika 1bc at t11
    m "Знаешь, что? А ты права. Вот спущусь на кухню, и сходу задам этот вопрос папе."
    show monika 3bl at f11
    em "Моя маленькая бездарность растёт не по дням, а по часам..."
    em 2bn "Слова не маленькой девочки, но взрослой самостоятельной женщины..."
    show monika 2bm at t11
    m "Да, решено: спущусь, спрошу у папы, а там будь что будет..."
    "С этими словами я заканчиваю свой утренний моцион и спускаюсь на кухню, чтобы приготовить завтрак."
    stop music fadeout 3
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_kitchen
    with wipeleft_scene

    $ TS.s(ts_showscreens)
    "Хм-м-м..."
    "Что я там готовила в прошлый понедельник?"
    "Хлопья с молоком и кофе, да."
    "Однако, учитывая прошлые ошибки и сопутствующий нагоняй от папы, на этот раз я решаю приготовить более питательный завтрак."
    play music ts_pb_stsg fadein 2
    "...что-то я гречку давно не готовила."
    if unluck4_cooking == True:
        "Да, пусть никто ничего и не помнит, но зато помню я."
        "И я точно помню, что гречку я ела в последний раз в позапрошлую пятницу."
    "Я наливаю воду в кастрюлю и ставлю её кипятиться."
    "Спустя пару минут на кухню спускается и папа."
    show hiroto 1a at t11
    m "О, доброе утро, пап."
    show hiroto 1g at f11
    ts_ft "Доброе утро, дорогая."
    show hiroto 1f at t11
    $ persistent.ingame_pizda = False
    m "Что-то ты сегодня поздновато."
    show hiroto 1y at f11

    ts_ft "А, да это так, пустяки.{w=0.05}{nw}"
    $ TS.s(ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake))

    $ persistent.ingame_pizda = True
    python:
        _preferences.volumes['music'] = 0.0
        _preferences.volumes['sfx'] = 1.0
    play sound ts_glitch_music1
    play sound2 ts_smeh_pizdec
    scene ts_kitchen_psyhodelic_pizdec_glitch
    show black zorder 5 at ts_black_glitch
    show blackout_exh zorder 5
    show anim_exhausted zorder 5
    show m_rectstatic zorder 5
    show ts_hiroto_psyhodelic_pizdoc zorder 6 at ip11
    extend " Думал о том, как бы мне убить тебя и спрятать тело."
    #show hiroto 1s at t11
    m "Ч-что, п-прости?"

    $ TS.s()

    $ persistent.ingame_pizda = False
    stop sound
    stop sound2
    scene ts_kitchen
    python:
        _preferences.volumes['music'] = .45
        _preferences.volumes['sfx'] = .65
    show hiroto 1t at f11
    ts_ft "Говорю, просто долго встать не мог."
    show hiroto 1s at t11
    $ persistent.ingame_pizda = False
    m "На тебя это не очень похоже."
    show hiroto 2y at f11
    ts_ft "Ну-у-у, {w=0.05}{nw}"

    $ TS.s(ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake))

    $ persistent.ingame_pizda = True
    python:
        _preferences.volumes['music'] = 0.0
        _preferences.volumes['sfx'] = 1.0
    play sound ts_glitch_music5
    play sound2 ts_smeh_pizdec
    scene ts_kitchen_psyhodelic_pizdec_glitch
    show black zorder 5 at ts_black_glitch
    show blackout_exh zorder 5
    show anim_exhausted zorder 5
    show m_rectstatic zorder 5
    show ts_hiroto_psyhodelic_pizdoc_eye zorder 6 at ipp11
    extend "убивать всех своих подруг и на тебя не похоже, но ты же это сделала. Чем я хуже?"
    #show hiroto 1r at t11
    m "Ч-ч-что?"
    $ TS.s()

    $ persistent.ingame_pizda = False
    stop sound
    stop sound2
    scene ts_kitchen
    python:
        _preferences.volumes['music'] = .45
        _preferences.volumes['sfx'] = .65
    show hiroto 1b at f11
    ts_ft "Я говорю, ладно уж, с одного раза хуже не сделается."
    show hiroto 1a at t11
    m "Я в-вот т-того же мнения б-была до н-недавнего в-времени..."
    "А ещё я до недавнего времени была уверена в том, что уж собственные родители меня пугать не будут."
    "А теперь мне даже в собственном доме неспокойно."
    "Что дальше? Мне будет страшно в собственной постели? Я буду бояться собственной тени?"
    em "Технически, я и есть твоя тень, и ты же меня особо не боишься, даже огрызаешься иногда."
    "«Ой, вот только тебя мне и не хватало!»"
    em "Всё, всё, ухожу..."
    show hiroto 1b at f11
    ts_ft "Ладно, что у нас на завтрак?"
    show hiroto 1a at t11
    m "Н-ну, я п-поставила гречку в-вариться, а затем будут х-хлопья с молоком и кофе..."
    show hiroto 1b at f11
    $ persistent.ingame_pizda = False
    ts_ft "О, гречка – это замечательно."
    stop music
    $ TS.s(ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake))

    $ persistent.ingame_pizda = True
    python:
        _preferences.volumes['music'] = 0.0
        _preferences.volumes['sfx'] = 1.0
    play sound ts_glitch_music2
    play sound2 ts_smeh_pizdec
    scene ts_kitchen_psyhodelic_pizdec_glitch
    show black zorder 5 at ts_black_glitch
    show blackout_exh zorder 5
    show anim_exhausted zorder 5
    show m_rectstatic zorder 5
    #show ts_hiroto_psyhodelic_pizdoc_eblet zorder 6 at ippp11
    show ts_hiroto_psyhodelic_pizdoc_eblet zorder 6:
        align(0.5, 0.5) zoom 1.0
        ease 0.1 align(0.1, 0.2) zoom 2.0
        parallel:
            ease 0.02 align(0.8, 0.2) zoom 3.0
            ease 0.02 align(0.4, 0.4) zoom 4.0
            ease 0.02 align(0.9, 0.6) zoom 5.0
            ease 0.02 align(0.8, 0.2) zoom 3.0
            repeat

    ts_ft "К гарниру в виде гречки хорошо бы подошли твои фаршированные глазные яблоки."
    ts_ft "Можно ещё твои запечёные уши, но это так, для следующего раза."
    $ TS.s()

    $ persistent.ingame_pizda = False
    stop sound
    stop sound2
    scene ts_kitchen
    python:
        _preferences.volumes['music'] = .45
        _preferences.volumes['sfx'] = .65
    
    play music ts_heaven fadein 1
    show hiroto 1b1 at t11
    "Видя моё крайне перепуганное лицо, папа и сам заволновался."
    show hiroto 2h at f11
    ts_ft "М-Моника, с тобой всё хорошо?"
    show hiroto 1j at t11
    m "Со мной? Всё хорошо, просто отлично, превосходно!"
    "Я издаю нервный смешок, чтобы дополнительно убедить папу, что со мной всё нормально."
    "Хотя внутри я вся кричу от того, что всё {b}не{/b} нормально, и мне бы скорее хотелось утопиться, чем проводить ещё хоть минуту в этом доме."
    if unluck6 == False:
        "Тем более, что я как раз на прошлой неделе видела обрыв у моря, с которого так хорошо было бы прыгать вниз..."
    em "Эй, вообще-то, я тоже здесь!"
    show hiroto 1z at f11
    stop music fadeout 3
    ts_ft "Н-ну хорошо, если ты так говоришь..."
    show hiroto 1b1 at t11
    "Ну хоть одна вселенская постоянная здесь присутстсует: вне зависимости от того, насколько плохой кошмар мне снится, папу всегда очень легко убедить."
    play music ts_solution fadein 2
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_kitchen
    with wipeleft_scene

    $ TS.s(ts_showscreens)
    show hiroto 1b1 at i11
    "Я съедаю гречку, хлопья и кофе олимпийскими темпами и говорю папе:"
    m "Л-ладно, пап, д-до в-вечера!"
    show hiroto 2h at f11
    ts_ft "М-Моника, подожди!.."
    hide hiroto
    "Но я его уже не слушаю, а вместо этого так же быстро выбегаю на улицу."
    stop music fadeout 4
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_house
    with wipeleft_scene

    play sound pageflip
    scene ts_seaside_road_morning
    with wipeleft_scene

    $ TS.s(ts_showscreens)
    play music ts_ios fadein 2
    "Я убегаю подальше от этого проклятого дома. Хоть куда-нибудь, лишь бы не находиться в одном доме с ним."
    show monika 2i at f11
    em "Ты же понимаешь, что от всех не спрячешься?"
    em 3i "А если и спрячешься, то тебя найдут мёртвой через пару дней, потому что такая бездарность, как ты, совершенно не приспособлена к жизни в диких условиях."
    em "Я же говорила тебе, и причём неоднократно, что это просто кошмар. Очень реалистичный, но всё же просто кошмар. Это всё не по-настоящему."
    show monika 2h at t11
    m "Ага... поговори мне тут... ты же и сама видела, что безумный папа, который хотел оторвать мне глаза и уши, был очень даже настоящим!"
    show monika 1r at f11
    em "Ты не только бездарность, ты ещё и глупая..."
    em 2i "Я тебе в тысячный раз повторяю: всё происходившее с тобой за эти десять дней – это просто сон. Три из них – это просто кошмарный сон."
    show monika 2h at t11
    m "Значит, если это просто сон... я же могу ущипнуть себя, и сон закончится..."
    show monika 2g at f11
    em "Подо{w=0.2}{nw}"
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"
    show monika 2f at t11
    play sound mon_ahh
    with vpunch
    $ TS.p(1)
    $ TS.s(ts_showscreens)
    m "Видишь? Ты до сих пор здесь, а папа и все мои друзья до сих пор безумны и кровожадны. Значит, не сплю!"
    show monika 1p at f11
    stop music fadeout 7
    em "Не спишь, ага, конечно..."
    em 2n "Просто... когда придёшь в школу, постарайся вести себя естественно."
    em 2p "Я понимаю, что поначалу это будет довольно сложно, но просто веди себя точно так же, как и на прошлой неделе..."
    show monika 1m at t11
    m "Ладно... уговорила..."
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"
    play sound ts_glitch6
    scene black with memglitchstr
    stop sound
    $ TS.p(1)
    play sound ts_glitch2
    scene ts_class with memglitchstr
    stop music fadeout 2
    play ambience clock_stena
    $ TS.s(ts_showscreens)
    "Мои подозрения в очередной раз подтвердились, когда я пришла в школу."
    "Одноклассники говорили на те же темы, что и в прошлый понедельник, а на уроке биологии учитель объяснял ту же тему, что и в прошлый раз."
    "Слово в слово."
    "Иногда, когда учитель делает паузы (тоже, кстати, в одних и тех же местах, что и в прошлый раз), я про себя сама договаривала конец фразы."
    "То же самое повторилось и на всех остальных уроках."
    "Если Аки всё-таки права, и неделя циклично повторяется один в один, то через пару таких циклов я сама могу провести все лекции на этой неделе."
    "Наконец, время выдвигаться в клуб."
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    stop ambience
    play sound pageflip
    scene ts_corridor
    with wipeleft_scene

    play sound pageflip
    scene ts_club
    with wipeleft_scene

    $ TS.s(ts_showscreens)
    "Хм-м-м..."
    "В клуб я снова пришла первой."
    "Или?.."
    "Если неделя повторяется точь в точь, то..."
    "Я решаю проверить кладовку."
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_closet
    show natsuki 1s at i11
    with wipeleft_scene

    $ TS.s(ts_showscreens)

    "Точно. Нацуки опять пришла и зарылась в кладовой."
    "По-моему, она зарылась в кладовой, потому что она решила поискать {i}ту самую{/i} мангу."
    "Как же она там называлась? «Ванильные Дамы» или как-то так? Вроде да."
    "Я решаю слегка подшутить над ней."
    m "Тык."

    show natsuki scream at hf11
    $ TS.s(vpunch)
    $ persistent.ingame_pizda = False
    play sound stol_udar
    n "{font=[pizdec_font]}А-А-А-А-А-А-А-А-А!{/font}"
    $ TS.s(ts_hidescreens_fast)
    " {w=0.1}{nw}"
    $ TS.p(1.3)
    $ TS.s(ts_showscreens_fast)
    n 1l "А, вот и ты, {w=0.05}{nw}"

    $ persistent.ingame_pizda = True

    python:
        _preferences.volumes['sfx'] = 1.0
        _preferences.volumes['music'] = .0

    play sound2 ts_smeh_pizdec

    $ TS.s(ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake))

    play sound ts_glitch_music8
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
    extend "[gtextsuka]"

    stop sound2
    stop sound

    $ TS.s()

    $ persistent.ingame_pizda = False

    scene ts_closet

    python:
        _preferences.volumes['sfx'] = .65
        _preferences.volumes['music'] = .45

    show natsuki 1j at t11
    play music ts_sh_true fadein 2
    m "А, да, п-привет, Нацуки..."
    m "П-похоже, что ты первая п-пришла..."
    show natsuki 1k at f11
    n "А, да я сама пришла только пару минут назад."
    show natsuki 1za at t11
    "Кажется, Нацуки совсем не знакома с понятием эмпатии."
    "Впрочем, мне же лучше – меньше вопросов о том, всё ли со мной нормально, и что со мной не так."
    show natsuki 1c at f11
    n "Я думала какую-то новую мангу почитать, ну, знаешь... "
    extend 2l "Чтобы прям {w=0.01}{nw}"
    play sound psy_fast_1
    extend "необычное!"
    show natsuki 2a at t11
    show natsuki mouth at t11
    show n_moving_mouth
    n "Сетчатый канифас слепозрения по линии жизни Анат ректипетальностью безукоризненно предложил склеромаляцию заржавшему католикосу."
    show natsuki 1a at t11
    hide n_moving_mouth
    $ gtextsuka = glitchtext(15)
    n 2k "Честно говоря, я эту мангу уже когда-то начинала читать, ещё аж лет в [gtextsuka], но тогда она мне показалась слишком скучной."
    n 2l "Но теперь я заметно повзрослела, и, думаю, в этот раз я её осилю!"
    show natsuki 1j at t11
    "В руках она держит уже знакомый мне первый том «Ванильных Девочек»."
    "Надо бы, кстати, запомнить уже название."
    "Хоть я и уже читала её, но уже всё забыла, так что мы с Нацуки сейчас на равных."
    show natsuki 2g at t11
    "Видя мою задумчивость, Нацуки тут же решает перейти в атаку."
    show natsuki 2e at f11
    n "Что? Думаешь, что это по-детски?"
    n 1h "Сама-то как думаешь, почему я тогда так её и не дочитала?"
    show natsuki 1i at t11
    m "Д-да что ты, в-вовсе нет, это с-совсем не то, что я имела в виду!.."
    m "К-конечно, это н-не по-детски..."
    "Хотя в иной ситуации я бы ответила совсем иначе."
    show natsuki 1k at f11
    n "Ну тогда..."
    n 1l "Хочешь, вместе почитаем?"
    show natsuki 1j at t11
    m "Да, к-конечно, почитаем..."
    show natsuki 2d at t11
    "Увидев и услышав, что я «разделяю её увлечение мангой», не заставляя меня, Нацуки просияла."
    n 4z "Ура!"
    n 2l "Может, теперь-то я пойму её!"
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound psy_fast_3
    scene n_cg1_bg
    show n_cg1_base
    show dust1
    show dust2
    show dust3
    show dust4
    with memglitchbolee
    stop sound
    $ TS.s(ts_showscreens)
    n "Знаешь..."
    n "Как-то даже непривычно читать мангу... вместе с кем-то ещё."

    play sound psy_fast_1
    scene n_cg1_bg
    show n_cg1_base
    show n_cg1_exp2
    show dust1
    show dust2
    show dust3
    show dust4
    with memglitch
    stop sound
    n "Все мои друзья насмехаются надо мной из-за одного только названия!"
    n "А манга, вообще-то, может рассказывать истории не хуже классических произведений, которые все обожают!"
    "Пока что она повторяет всё слово в слово."
    "Но по классике, неожиданность может начаться в самый непредсказуемый момент."
    em "И не говори..."
    m "Э-э-э... да."
    play sound psy_fast_1
    scene n_cg1_bg
    show n_cg1_base
    show n_cg1_exp1
    show dust1
    show dust2
    show dust3
    show dust4
    with memglitch
    stop sound
    n "Ну вот видишь! Хоть кто-то со мной согласен!"
    m "Д-давай уже начнём..."
    "А то эта излишняя предсказуемость меня пугает. Когда же всё пойдёт к чертям?"
    em "Сама же говорила, в самый непредсказуемый момент!"
    "«Вот только твоих подколов мне не хватало...»"

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene n_cg1_bg
    show n_cg1_base
    show n_cg1_exp4
    show dust1
    show dust2
    show dust3
    show dust4
    with wipeleft_scene

    $ TS.s(ts_showscreens)
    "Мы читаем мангу уже некоторое время."
    "...а точнее, читаю мангу уже одна только я."
    "Нацуки же просто... уснула."
    "Видимо, она настолько восторгалась моей самоотдачей, что я сама предложила почитать мангу, открыть мангу и прочее по мелочи, что не выдержала и просто уснула от радости и восторга."
    "Кажется, она как-то упоминала, что её отец плохо её кормит?"
    "Или не упоминала?.."
    "В любом случае, мне это очень не нравится..."
    m "Н-Нацуки..."
    play sound psy_fast_3
    scene n_cg1_bg
    show n_cg1_base
    show n_cg1_exp5
    show dust1
    show dust2
    show dust3
    show dust4
    with memglitch
    stop sound
    n "А, что такое?.."
    $ persistent.ingame_pizda = False
    m "С добрым утром. Ты уже минут пятнадцать дремаешь."
    n "А... Да я просто {w=0.01}{nw}"

    play sound ts_glitch_music10

    scene nat_pizdos
    show n_cg1b228

    $ persistent.ingame_pizda = True

    python:
        _preferences.volumes['sfx'] = 1.0
        _preferences.volumes['music'] = .0

    play sound2 ts_smeh_pizdec

    $ TS.s(ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake))

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

    $ persistent.ingame_pizda = False
    stop sound
    stop sound2
    $ TS.s()

    python:
        _preferences.volumes['sfx'] = .65
        _preferences.volumes['music'] = .45

    play sound psy_fast_3
    scene n_cg1_bg
    show n_cg1_base
    show n_cg1_exp5
    show dust1
    show dust2
    show dust3
    show dust4
    with memglitch
    stop sound

    $ TS.p(1.5)
    $ TS.s(ts_showscreens_fast)
    m "Ч-что?"
    play sound psy_fast_1
    scene n_cg1_bg
    show n_cg1_base
    show n_cg1_exp2
    show dust1
    show dust2
    show dust3
    show dust4
    with memglitch
    stop sound
    n "Ничего уже! Давай дальше читать."
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene n_cg1_bg
    show n_cg1_base
    show dust1
    show dust2
    show dust3
    show dust4
    with wipeleft_scene

    $ TS.s(ts_showscreens)
    "Мы продолжили читать."
    "Вкупе с тем, что я уже знаю, что произойдёт на этих страницах, я читаю более вдумчиво и внимательно."
    em "Ты что, и книжки свои в детстве по несколько раз перечитывала, чтобы хоть что-то понять?"
    "«Слушай, отстань уже, а?»"
    "Нацуки, кажется, тоже заинтересована мангой, как будто она читает её впервые."
    "Впрочем, сколько лет уже прошло с того, как она, по её словам, в последний раз читала это произведение? Лет восемь? Деcять?"
    "В любом случае, очень давно."
    "А ещё она, по её же словам, так и не дочитала эту мангу до конца."
    "Так что почти все детали уже стёрлись из её памяти."
    em "Точно так же, как «стёрлась её память обо всех событиях за всю неделю»?"
    "«Просто дай мне спокойно почитать!»"

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound ts_glitch4
    scene ts_club
    show dust1
    show dust2
    show dust3
    show dust4
    show natsuki 1k at f11
    with memglitchbolee

    $ TS.s(ts_showscreens)

    n "Ну, для первого раза достаточно."
    n 1l "Итак, что тебе понравилось? Кто тебе понравился?"
    show natsuki 1j at t11
    "За исключением пары моментов, которые в конце концов даже особого значения не имеют, Нацуки задаёт одни и те же вопросы."
    m "Ну-у-у, понравилась общая рисовка и стиль повествования, а ещё мне понравилась..."
    "Как же её там зовут?"
    m "Минори."
    stop music fadeout 7
    show natsuki 2l at f11
    n "Правда? Мне тоже больше всех Минори нравится!"
    n "Это потому, что она вся такая неуклюжая, да?"
    show natsuki 1j at t11
    m "Да. Неуклюжая, неловкая, и всё такое."
    m "Нацуки, позв—{w=0.05}{nw}"
    show natsuki 2l at f11
    n 2l "Именно! А ещё...{w=1}{nw}"
    "Нацуки, похоже, совсем меня не слышит."
    "Она слишком увлеклась мангой, а особенно тем, что хоть кто-то разделяет её увлечения, что она даже остальных не слышит."
    window hide
    play sound stuk
    with vpunch
    $ TS.p(2)
    play sound door_open
    $ TS.p(1)
    show yuri 1a at ln31
    show sayori 1a at ln32
    show natsuki 1a at t33
    $ TS.p(1.5)
    hide yuri
    hide sayori
    hide natsuki

    python:
        _preferences.volumes['sfx'] = 1.0
        _preferences.volumes['music'] = .0

    scene ts_club_glitch_pizdets

    play sound psy_fast_2

    show ts_yrec_kill_nahui_suicide_blya at left
    show ts_sayori_zalagala_chereshnya:
        align (0.5, 0.15)
    show ts_maloletka_pozvonok_sloman_nahui at right

    $ TS.p(2)

    stop sound

    python:
        _preferences.volumes['sfx'] = .65
        _preferences.volumes['music'] = .45

    scene ts_club
    show dust1
    show dust2
    show dust3
    show dust4

    show yuri 1a at i31
    show sayori 1a at i32
    show natsuki 1a at i33

    "Да и остальные уже пришли, поэтому диалога о возможном разрезе пространственно-временного континуума уже точно не будет."

    play music ts_holly_roller fadein 2

    $ gtextsuka = glitchtext(6)
    $ gtextsuka1 = glitchtext(3)
    $ gtextsuka2 = glitchtext(7)

    show sayori 2x at f32
    s 2x "Привет, [gtextsuka]! Привет, [gtextsuka1]!"
    play sound psy_fast_1
    $ TS.s(vpunch)
    s "[gtextsuka2]"
    show yuri 1b at f31
    show sayori 1a at t32
    $ gtextsuka = glitchtext(5)
    play sound psy_fast_3
    $ TS.s(vpunch)

    $ persistent.ingame_pizda = False
    y "Всем [gtextsuka]."
    show yuri 1a at t31
    show sayori 1a at t32
    show natsuki 2h at f33
    n "Что, даже не {w=0.01}{nw}"

    $ persistent.ingame_pizda = True

    python:
        _preferences.volumes['sfx'] = 1.0
        _preferences.volumes['music'] = .0

    scene ts_club_glitch_pizdets:
        align(0.5, 0.5) zoom 1.0
        ease 0.1 align(0.2, 0.5) zoom 2.0
        ease 0.1 align(0.8, 0.2) zoom 3.0
        ease 0.1 align(0.3, 0.7) zoom 2.5
        ease 0.1 align(0.4, 0.9) zoom 4.0
        ease 0.1 align(0.5, 0.5) zoom 1.0
        repeat

    play sound psy_fast_2
    play sound2 ts_glitch_music3

    show ts_yuri_zalagala_blyadina:
        align(0.15, 0.35)
        ease 0.5 align(0.9, 0.01)
        ease 0.5 align(0.15, 0.35)
        repeat
    show ts_sayori_zalagala_chereshnya:
        align(0.5, 0.15)
        ease 0.5 align(0.1, 0.6)
        ease 0.5 align(0.5, 0.15)
        repeat
    show ts_natsuki_zalagala_blyadina:
        align(0.9, 0.5)
        ease 0.5 align(0.3, 0.1)
        ease 0.5 align(0.9, 0.5)
        repeat

    $ TS.s(ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake))

    n "{font=[pizdec_font]}Что, даже не {fast}расчлените Монику и не принесёте её обрубки в жертву богам?{/font}"

    stop sound
    stop sound2
    $ persistent.ingame_pizda = False

    $ TS.s()
    python:
        _preferences.volumes['sfx'] = .65
        _preferences.volumes['music'] = .45

    scene ts_club
    show dust1
    show dust2
    show dust3
    show dust4

    show yuri 1a at i31
    show sayori 1a at i32
    show natsuki 1a at i33

    n 2w "Девочки, я в вас разочарована..."
    show sayori 3h at f32
    show natsuki 2x at t33
    $ persistent.ingame_pizda = False
    s "Да брось, Нацуки!"
    s 2h "Монике и так стыдно за {w=0.01}{nw}"

    $ persistent.ingame_pizda = True
    scene ts_sayori_bedroom

    $ TS.s(ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake))

    $ TS.m(VHS())

    show s_kill_bg_zoom zorder 1
    show s_kill_bg2_zoom zorder 1
    show s_kill_zoom zorder 3
    show s_kill2_zoom zorder 3
    show s_kill as s_kill_zoom_trans zorder 3:
        truecenter
        alpha 0.5
        zoom 2.0 xalign 0.5 yalign 0.05
        TS.p(0.5)
        dizzy(1, 1.0)
    show overlay aw_memory_back_1 zorder 4

    extend "то, что она хотела нас всех убить самыми изощрёнными способами и даже не раскаяться в содеянном, {w=0.01}{nw}"
    extend "а тут ещё ты накручиваешь её."
    $ TS.s()
    $ persistent.ingame_pizda = False

    scene ts_club
    show dust1
    show dust2
    show dust3
    show dust4

    show yuri 1a at i31
    show sayori 2f at i32
    show natsuki 2x at i33

    "Внешне я остаюсь спокойной и даже особо не нервничаю, хотя внутри мне хочется убежать из этого проклятого места."
    m "Д-да ладно, Сайори, я и н-не обижаюсь уже..."

    scene ts_club with linearblurbolee

    em "А помнишь, как я в прошлый понедельник говорила о том, что накрутила бы её шею градусов на двести?"
    "«Теперь помню... И зачем только об этом вспомнила?»"
    em "Да брось, весело же будет! Если они пугают тебя, то ничего не мешает тебе напугать их!"
    "Я представляю это действие..."
    $ TS.s(ts_hidescreens_fast)
    " {w=0.1}{nw}"
    play sound fb
    $ TS.m(VHS())
    show natsuki 1za at t11
    with flash
    $ TS.p(2)
    show natsuki 2zb at t11
    $ TS.s(ts_showscreens_fast)
    if persistent.cens_mode == True:
        m "Иди сюда, сучара."
    else:
        m "Иди сюда, мелкая."
    $ TS.s(ts_hidescreens_fast)
    " {w=0.1}{nw}"
    $ TS.p(1.3)
    show natsuki screamnohead at h11
    show natscreamhead at h111
    $ TS.p(1)
    show natscreamhead at t111
    play sound2 scream_normal
    play sound bones_breaking
    $ TS.p(1)#3
    stop sound2 fadeout 1
    #hide natscreamhead
    #hide natsuki screamnohead
    show natscreamhead at ts_punch1()
    show natsuki screamnohead at ts_punch()
    $ TS.p(0.2)
    play sound sfx_body_bump
    $ TS.p(1)

    play sound fb
    scene ts_club
    show dust1
    show dust2
    show dust3
    show dust4
    show yuri 1a at t31
    show sayori 1a at t32
    show natsuki 1a at t33
    with flash
    $ TS.s(ts_showscreens_fast)
    "«Нет, это уже слишком!»"
    show yuri 2t at f31
    show sayori 2f at t32
    show natsuki 2o at t33
    stop music
    play music ts_s_stuff fadein 1
    y "Моника? Ты опять {w=0.01}{nw}"
    hide dust1
    hide dust2
    hide dust3
    hide dust4
    if not renpy.android:
        $ TS.m(StillAberate(25.0))
        $ TS.s(StillAberate(25.0))

    python:
        currentpos = get_pos()
        startpos = currentpos - 0.2
        if startpos < 0: startpos = 0
        track = "<from " + str(startpos) + " to " + str(currentpos) + ">mod_assets/source/audio/ost/ts_s_stuff.ogg"
        renpy.music.play(track, loop=True)

    $ gtextsuka = glitchtext(123)
    y "[gtextsuka]{nw}"
    $ gtextsuka = glitchtext(280)
    y "[gtextsuka]{nw}"
    $ gtextsuka = glitchtext(221)
    y "[gtextsuka]{nw}"
    play sound psy_fast_1
    show dust1
    show dust2
    show dust3
    show dust4
    $ TS.m()
    $ TS.s()
    with memglitch
    stop sound
    play music ts_s_stuff fadein 2
    show yuri 2t at f31
    show sayori 2f at t32
    show natsuki 2o at t33
    y "Моника? Ты опять{fast} отключилась..."
    show yuri 2zg at t31
    m "А... Да это ничего, просто..."
    "Спокойно... Это всё только в моей голове..."
    "На самом деле ничего ужасного не было..."
    "Они ведут себя как обычно..."
    m "{i}Кхе-кхе...{/i}"
    show yuri 2e at t31
    show sayori 2b at t32
    show natsuki 2za at t33
    m "И-итак, ребята!.."
    m "К-как вы уже знаете, каждый год в середине н-ноября в школе проводится ф-фестиваль клубов."
    m "П-поэтому..."
    em "Ближе к теме уже."
    show yuri 1g at t31
    show sayori 1k at t32
    show natsuki 1i at t33
    m "Поэтому нам нужно придумать хоть какие-то новые клубные активности помимо того, что мы недавно прочитали..."
    "Я надеюсь, временная линия не полетит ко всем чертям только из-за того, что в этот раз я сказала «новые»..."
    show yuri 1j at f31
    y "{size=-10}Ты хотела сказать, только что прочитали...{/size}"
    show yuri 1i at t31
    "Нет, Юри, {i}недавно{/i} прочитали. Она просто этого не помнит, потому что в её понимании я говорю это впервые."
    "В любом случае, я решаю не давить на неё, и вместо этого просто продолжаю."
    em "Ты об эффекте бабочки не слышала никогда?"
    m "Так вот, недавно у меня появилось вдохновение... и я написала стих!"
    m "И я подумала: а ведь писать стихи легче, чем кажется!"
    em "Проще. Видимо, всё-таки не слышала..."
    m "Поэтому, вот вам и новая активность: напишите стих, чтобы к следующему собранию мы все смогли обсудить его друг с другом."
    if not renpy.android:
        $ TS.m(StillAberate(25.0))
        $ TS.s(StillAberate(25.0))
    $ glitchhuetenblya = glitchtext(24)
    python:
        _preferences.volumes['music'] = 0.0
    m "[glitchhuetenblya]{nw}"
    python:
        _preferences.volumes['music'] = .45
    $ TS.m()
    $ TS.s()
    show yuri 4c at s31
    show sayori 1e at s32
    show natsuki 1u at s33
    em "Нет, ну ты смотри, сама меняет слова в совершенно случайных местах, и сама же потом жалуется на то, что все ведут себя неадекватно!"
    em "Вот что: меня нет. Сама разбирайся, но моей помощи не жди."
    m "...и чтобы вы не подумали, что я вас как-то ущемляю – я сяду писать стихотворение вместе с вами!"
    m "Помните, в стихе не обязательно должна быть замудрённая рифма – её ведь вообще может не быть!"
    m "В конце концов, главное в стихе – не рифма. И даже не слог и не размер."
    show yuri 1q at s31
    "Последнее предложение я сказала, косясь на Юри. Судя по её выражению лица, она намёк поняла."
    m "Мне не нужно, чтобы вы с первого раза написали новый шедевр литературы. Просто пару четверостиший или несколько строк, связанных одной темой."
    show yuri 1i at t31
    show sayori 2y at t32
    show natsuki 1s at t33
    "На этот раз я убедила их гораздо быстрее."
    "Ну хоть сегодня этот «эффект бабочки» сыграл мне на руку."
    show yuri 1g at f31
    y "Н-ну... "
    extend 1j "Д-допустим, ты права..."
    show yuri 1i at t31
    show sayori 2l at f32
    s "Н-ну что же... Д-давай... попробуем..."
    show sayori 2l at t32
    show natsuki 2k at f33
    n 2k "Ну давай попробуем написать стишки."
    show natsuki 2za at t33
    "Они отвечают точно так же, как и на прошлой неделе. С теми же словами, интонациями, даже паузами."
    stop music fadeout 7
    "Если бы Аки не сказала мне заранее, что эта неделя циклично повторяется, я бы сама сказала, что у меня очень сильное чувство дежавю."
    "Честно говоря, внутри мне до сих пор страшно. Но внешне я остаюсь спокойной, даже какая-то имитация уверенности появилась."
    "Как будто это та же Моника, что и в прошлый понедельник."
    m "Тогда... пишем стихи!"
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"
    play music ts_alx_ewbf fadein 1
    scene ts_notebook with linearblurbolee
    $ TS.s(ts_showscreens)
    "Так-так-так... что там у меня в прошлый раз было? Про дыру в стене?"
    show monika 2d at f11
    em "Да, что-то вроде того."
    show monika 2c at t11
    "Ну тогда приступаем. Главное, правильные знаки препинания проставить, потому что слова я помню довольно отчётливо."
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_notebook
    with wipeleft_scene

    $ TS.s(ts_showscreens)
    "Спустя пару минут стих уже почти написан."
    "Чтобы сделать вид, что я придумываю что-то новое, я наигранно прикусываю губу пару раз, томно вздыхаю и смотрю на других девочек."
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"
    scene ts_club
    show dust1
    show dust2
    show dust3
    show dust4
    with linearblurbolee
    show yuri 1g at ln11
    $ TS.p(0.75)

    $ TS.p(0.5)

    show yuri 1g at ron11
    $ TS.p(0.75)
    hide yuri

    show sayori 2o at ln11
    $ TS.p(0.75)

    $ TS.p(0.5)

    show sayori 2o at ron11
    $ TS.p(0.75)
    hide sayori

    show natsuki 1s at ln11
    $ TS.p(0.75)

    $ TS.p(0.5)

    show natsuki 1s at ron11
    $ TS.p(0.75)
    hide natsuki
    scene ts_notebook with linearblurbolee
    $ TS.s(ts_showscreens)

    "Девочки тоже натужно пытаются выжать из себя хоть что-то."
    "Но их ручки тоже двигаются. Следовательно, первая часть плана уже выполнена."
    show monika 1p at f11
    em "Подожди, у нас был какой-то план?"
    show monika 1o at t11
    "«Ну как же, ты же сама сказала вести себя естественно, разве не это и был твой план?»"
    show monika 2r at f11
    em "Я тебе уже говорила, что ты тупая?"
    em "Мой план состоял в том, чтобы ты просто не пугалась всего, как маленький котёнок."
    em 3i "Но нет же, ты устроила самодеятельность, и теперь все девочки по твоей воле пишут стихи."
    show monika 3h at t11
    "«Ну-у-у, это своего рода тоже часть плана... Пока они пишут стихи, они меня не трогают, а значит, и пугать меня они тоже не будут.»"
    show monika 2n at f11
    em "Н-н-ну ладно, признаю, ты быстро учишься..."
    show monika 2m at t11
    "«Вот-вот.»"
    "«Ладно, что-то я с тобой заговорилась, Сайори и Нацуки уже даже стих быстрее меня написали.»"
    "Я тоже дописываю и перечитываю стих."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    scene ts_notebook with dissolve:
        blur 9.0

    $ TS.s(ts_showscreens)

    if not persistent.first_poem:
        $ persistent.first_poem = True
        show expression "mod_assets/source/images/gui/poem_dismiss.webp" as poem_dismiss:
            xpos 1050 ypos 590

    play sound pageflip

    if _preferences.language == "english":
        show screen poem(poem_m21_eng)
    else:
        show screen poem(poem_m21)


    pause

    play sound pageflip
    $ TS.s(ts_hidescreens)
    $ TS.p(1)
    hide screen poem
    hide poem_dismiss

    scene ts_notebook with dissolve

    $ TS.s(ts_showscreens)
        
    "Написано вроде как точно так же, как и в прошлый раз."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"
    scene ts_club
    show dust1
    show dust2
    show dust3
    show dust4
    show yuri 2l at t31
    show sayori 4s at t32
    show natsuki 1y at t33
    with linearblurbolee
    $ TS.s(ts_showscreens)
    "Кажется, Юри ещё нужно будет минут пять, прежде чем она тоже закончит."
    m "Итак, ребята!"
    m "Юри ещё нужно немного времени на то, чтобы закончить стих."
    m "И после того, как она закончит, можем расходиться."
    show yuri 2f at f31
    y "Я тоже закончила."
    show yuri 2e at t31
    m "Вот и отлично."
    m "Так, ладно, время уже позднее, поделиться друг с другом стихами на этом собрании мы не успеем... но всегда же есть следующее!"
    $ persistent.ingame_pizda = False
    m "До завтра, девочки!"

    python:
        _preferences.volumes['sfx'] = 1.0
        _preferences.volumes['music'] = .0

    play sound2 ts_glitch_music4

    $ TS.s(ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake))

    $ persistent.ingame_pizda = True
    play sound crack
    scene ts_club_glitch_pizdets
    show ts_yrec_kill_nahui_suicide_blya at left
    show ts_sayori_zalagala_blyadina at t32
    show ts_maloletka_pozvonok_sloman_nahui at right

    $ gtextsuka = glitchtext(24)
    $ gtextsuka1 = glitchtext(96)
    $ m_name = gtextsuka
    m "[gtextsuka1]{nw}"

    stop sound
    stop sound2

    $ TS.s()

    $ persistent.ingame_pizda = False

    play sound psy_fast_3
    scene ts_club
    show yuri 3d at h31
    show sayori 4s at h32
    show natsuki 1y at h33
    with memglitchbolee
    stop sound
    python:
        _preferences.volumes['sfx'] = .65
        _preferences.volumes['music'] = .45
    if _preferences.language == "english":
        $ m_name = "Everyone"
    else:
        $ m_name = "Все вместе"
    m "Пока, Моника!{fast}"

    stop music fadeout 7

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"
    play sound door_open
    show yuri 3d at lon31
    $ TS.p(1)
    hide yuri
    show sayori 4s at lon32
    $ TS.p(1)
    hide sayori
    $ TS.s(ts_showscreens_fast)
    if _preferences.language == "english":
        $ m_name = "Monika"
    else:
        $ m_name = "Моника"
    m "Нацуки, подо—{w=0.15}{nw}"
    $ TS.s(ts_hidescreens_fast)
    " {w=0.1}{nw}"
    play sound door_open
    show natsuki 1y at lon33
    $ TS.p(1)
    hide natsuki
    $ TS.s(ts_showscreens)
    "Однако Нацуки уже испарилась в мгновение ока."
    "Я не знаю почему, но мне кажется, что именно Нацуки из них троих кажется мне наиболее здравомыслящей."
    "Наверное, это потому, что она единственная из всех троих, чей корень зла – это не она сама."
    window hide
    scene ts_club_glitch_pizdets
    python:
        _preferences.volumes['sfx'] = 1.0
    play sound scream_pereponkam_pizda
    show monika g1 at t1111
    $ TS.p(1.25)
    stop sound
    scene ts_club
    python:
        _preferences.volumes['sfx'] = .65
    show monika 2k at f11
    $ TS.s(ts_showscreens_fast)
    em "Да как будто ты сама мисс Перфекционизм, и у тебя никаких таких проблем не существует!"
    show monika 2j at t11
    m "Я такого не говорила!"
    show monika 1n at f11
    em "Не говорила, не говорила..."
    em 3b "Но думала об этом!"
    show monika 3a at t11
    m "Так думаешь только ты."
    show monika 2i at f11
    em "Бу-бу-бу..."
    em 2d "Так что, кстати, куда мы сейчас? Домой?"
    show monika 2c at t11
    m "Твою мать, я совсем забыла о папе!"
    show monika 2l at f11
    em "Что, сейчас он уже не кажется таким кровожадным? Думаешь, что быстрее умрёшь от расчленения, чем от холода и голода?"
    em 3b "Говорю же, он—{w=0.2}{nw}"
    show monika 3a at t11
    m "Он такой же, как и всегда, а у меня просто воображение разыгралось, знаю, знаю, не гуди."
    $ persistent.sprite_time = "day"
    m "Ладно уж, домой так домой."

    play music ts_first_day_of_sun

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_corridor
    with wipeleft_scene

    $ TS.p(2)

    play sound pageflip
    scene ts_l5
    with wipeleft_scene

    $ TS.p(2)

    play sound pageflip
    scene ts_school_gate_evening
    with wipeleft_scene

    $ TS.p(2)

    play sound pageflip
    scene ts_street_late
    with wipeleft_scene

    $ persistent.sprite_time = "sunset"

    $ TS.s(ts_showscreens)
    "Несмотря на всю мою напускную уверенность, до дома я всё равно шла в час по чайной ложке."
    "Да, Аки убеждала меня, что с папой всё нормально, и это я просто сбрендила. Я ей вроде как даже поверила, но..."
    "...внутри меня до сих пор терзают сомнения."
    "А что, если это не моя шизофрения, а новая реальность?"
    show monika 1r at f11
    with linearblur
    em "Да говорю же, не реальность это, а просто сон. Просто твои бредни."
    if unluck_ball >= 5:
        em "Или, может, это просто твоя кома, твои отрывочные воспоминания одного и того же..."
    show monika 1r at t11
    m "Ну, возможно! Но я всё равно слегка побаиваюсь..."
    show monika 2i at f11
    em "Чего ты вообще боишься? Это твой дом, это твои родители..."
    em 3d "Вот до этой субботы – какими они вообще были?"
    show monika 2o at t11
    m "Я думала, что {b}моё подсознание{/b} такие простые вещи про {b}меня же{/b} спрашивать не должно..."
    m "Но вообще – ну, они заботливые, любящие, понимающие, поддерживающие меня во всех начинаниях..."
    show monika 2m at t11
    m "Да, у нас были и есть некоторые разногласия по теме учёбы... но а у кого их не было?"
    show monika 2d at f11
    em "Ладно, не продолжай, я поняла."
    em 2i "И ты хочешь сказать мне, что за последние три дня всё твоё представление о родителях перевернулось с ног на голову?"
    show monika 2h at t11
    m "Ну, не настолько кардинально... но я всё равно побаиваюсь папу..."
    show monika 2f at t11
    m "Что, если как-то раз он доведёт дело с отрезанием ушей или выкалыванием глаз до конца?.."
    show monika 3y at f11
    em "Не переживай, не доведёт. Это же просто сон, это всё не по-настоящему."
    em 2b "А если он хоть притронется к тебе – всегда же можно просто проснуться и забыть это всё, как страшный сон. Который, по сути, страшным сном и является."
    show monika 1e at t11
    m "Ну... ладно, возможно, ты и права..."
    show monika 4l at f11
    em "Ну ещё бы я была не права."
    em 2b "Перестань так бояться папу. Как говорится, обещать – не значит жениться."
    em 2y "Пусть он говорит что угодно, до реальных действий это так и не дойдёт."
    show monika 2e at t11
    m "Ладно уж..."
    "После этих слов я прибавила шаг, и через пару минут уже была у дома."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_house_monika_evening
    with wipeleft_scene

    $ TS.s(ts_showscreens)

    "Ну, с Богом..."
    $ persistent.sprite_time = "sunset"
    "Я медленно открываю дверь..."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_vhod_nolight
    with wipeleft_scene_long

    $ TS.p(2)

    play sound svet_on
    scene ts_vhod_night
    with flash

    $ TS.p(2)

    play sound pageflip
    scene ts_living_room_night
    with wipeleft_scene


    $ TS.s(ts_showscreens)
    $ persistent.sprite_time = "day"
    m "Папа? Я дома..."
    $ persistent.ingame_pizda = False
    "И как только я оборачиваюсь, я замечаю, что папа тоже только пришёл."
    stop music

    play sound_loop ts_glitch_music6
    $ persistent.ingame_pizda = True
    python:
        _preferences.volumes['sfx'] = 1.0
    show ts_living_room_night zorder 4 at ts_coridor_glitch
    show black zorder 5 at ts_black_glitch
    show blackout_exh zorder 5
    show anim_exhausted zorder 5
    show m_rectstatic zorder 5
    show hiroto 1b zorder 6 at Glitch(_fps=1000.)

    $ TS.s(ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake))

    $ gtextsuka = glitchtext(80)
    ts_ft "Здáрова [gtextsuka]. Как житие молодое{w=1.5}{nw}"

    $ TS.s()

    stop sound_loop
    $ persistent.ingame_pizda = False
    scene ts_living_room_night
    python:
        _preferences.volumes['sfx'] = 0.65
        _history_list = []

    play music ts_top_sound_blya fadein 2
    show hiroto 1b at f11
    ts_ft "Привет, Моника. Как день прошёл?"
    show hiroto 1a at t11
    "Спокойно... Это всего лишь сон... Очень страшный и очень больной, но это просто сон..."
    "С другой стороны, у папы тоже память, как у золотой рыбки, и то, что произошло утром, он к вечеру уже и забыл."
    "Хотя, он как-то говорил мне, что за работой в опеке ты настолько загружен всеми мелочами, что порой забываешь даже собственное имя."
    "Поэтому здесь ничего сверхъестественного нет."
    m "П-привет, пап..."
    m "День прошёл, ну... как обычно. Школа, клуб, домой..."
    show hiroto 1h at f11
    ts_ft "Понятно..."
    ts_ft "Ты просто так резко убежала, что я подумал, что этот ваш фестиваль уже сегодня..."
    show hiroto 1j at t11
    "ДА ОН И ДОЛЖЕН БЫЛ БЫТЬ СЕГОДНЯ, НУ КАК ЖЕ ВЫ НЕ ПОЙМЁТЕ?!"
    "Но вслух я этого не говорю, иначе действительно упекут в психлечебницу, и тогда я точно фестиваль пропущу."
    "Но с какой-то стороны, папа-таки обратил внимание на моё странное поведение сегодня утром."
    "Видимо, поторопилась я с выводами насчёт памяти моего отца."
    em "Да уж повнимательнее некоторых будет..."
    show hiroto 1f at f11
    m "А, да это... просто, вот, да, фестиваль же скоро, и я вот переживаю, нервничаю, в общем, хочу, чтобы всё прошло по высшему разряду."
    m "Поэтому и сорвалась вот с утра..."
    show hiroto 1g at f11
    ts_ft "Моника, да ничего страшного, нет ничего ужасного в том, что ты переживаешь за собственное мероприятие."
    show hiroto 1f at t11
    "В том, что я переживаю, ужасного действительно ничего нет."
    "Но ужасно то, как папа сегодня вёл себя с самого утра..."
    show hiroto 1c at f11
    ts_ft "Кстати, а когда у вас это самое мероприятие будет?"
    show hiroto 1a at t11
    "Я уже и сама не знаю, когда оно будет..."
    "Теперь уже, возможно, никогда..."
    "Но для простоты и душевного спокойствия нас обоих я решаю немного подыграть ему."
    m "Через неделю."
    show hiroto 1b at f11
    ts_ft "Тогда у меня для тебя отличные новости!"
    ts_ft "Но сначала надо покушать. Или ты уже?"
    show hiroto 1e at t11
    m "Нет, я сама только пару минут назад пришла, решила немного отдохнуть."
    show hiroto 1g at f11
    ts_ft "Ты хоть в школе ела?"
    show hiroto 1j at t11
    m "Ну-у-у... да."
    show hiroto 2g at f11
    ts_ft "Ну славненько тогда."
    show hiroto 1v at f11
    $ persistent.ingame_pizda = False
    ts_ft "Та-а-ак... "
    extend 1b "Моника, ты будешь {w=0.01}{nw}"
    play sound ts_glitch_music7
    $ persistent.ingame_pizda = True
    python:
        _preferences.volumes['sfx'] = 1.0
        _preferences.volumes['music'] = 0.0

    show ts_living_room_night zorder 4 at ts_coridor_glitch
    show black zorder 5 at ts_black_glitch
    show blackout_exh zorder 5
    show anim_exhausted zorder 5
    show m_rectstatic zorder 5
    show hiroto 1b zorder 6 at Glitch(_fps=1000.)
    $ TS.s(ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake))

    extend "жареные Ģ̵͉͎͎̙̟͎̟̭͍͐̏̒́L̴̛̛̪̳̠͔͑̊͐̾̀͑̕͝Ḁ̵̧̞̲̳̖͎͓̳̣̩̓̽͌̒̔͋̄͊́͑̕̚͝ͅZ̶̡̢̧̢̪̥̦̣̲̠̳͎͖͍̪̖͚̚À̸̛̛̪̪̝͕̞̮̭̒͌͆͊̈̍̀͂̀̈͘̕͝ всех твоих новых подруг?"

    show hiroto 1e zorder 6 at Glitch(_fps=1000.)
    m "Ч-что?"
    $ TS.s()
    scene ts_living_room_night
    stop sound
    $ persistent.ingame_pizda = False
    python:
        _preferences.volumes['sfx'] = 0.65
        _preferences.volumes['music'] = 0.45

    show hiroto 1b at f11
    stop music fadeout 5
    ts_ft "Я говорю, картошку жареную будешь?"
    show hiroto 1a at t11
    m "Д-да, конечно..."
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_kitchen
    with wipeleft_scene

    play music ts_lmr_menu fadein 1

    $ TS.s(ts_showscreens)

    "Спустя десять минут картошка уже начищена, порезана, пожарена и рассыпана по двум тарелкам."
    show hiroto 1b at f11
    ts_ft "Приятного аппетита, Моника."
    show hiroto 1a at t11
    $ persistent.ingame_pizda = False
    m "Спасибо, пап. Взаимно."

    play sound ts_glitch_music11
    $ persistent.ingame_pizda = True
    python:
        _preferences.volumes['sfx'] = 1.0
        _preferences.volumes['music'] = 0.0

    show ts_kitchen zorder 4 at ts_coridor_glitch
    show black zorder 5 at ts_black_glitch
    show blackout_exh zorder 5
    show anim_exhausted zorder 5
    show m_rectstatic zorder 5
    show hiroto 1a zorder 6 at Glitch(_fps=1000.)
    $ TS.s(ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake))

    ts_ft "Я надеюсь, ты умрёшь в страшных муках."
    ts_ft "Никто даже не заплачет на твоих похоронах."
    ts_ft "Если там вообще будет что хоронить."

    stop sound

    $ persistent.ingame_pizda = False
    python:
        _preferences.volumes['sfx'] = .65
        _preferences.volumes['music'] = .45
    $ TS.s()

    scene ts_kitchen
    show hiroto 1a at i11

    "Я уже даже и бровью не веду."
    "Да, признаю, поначалу мне было очень страшно."
    "Но сейчас это уже приелось."
    "После того, как мы съели примерно половину, папа наконец-то спрашивает."
    show hiroto 1b at f11
    ts_ft "Как там, кстати, в клубе дела?"
    show hiroto 1a at t11
    m "Знаешь... вполне неплохо..."
    m "У нас с д-девочками появилась новая активность. Мы теперь не только обсуждаем книги, но и с-стихи пишем. А завтра мы будем ими обмениваться."
    m "Я думаю сделать это п-постоянной клубной активностью."
    show hiroto 1c at f11
    ts_ft "Постоянной?"
    ts_ft 1h "Моника, написание стихов – это процесс творческий. А творческий процесс – это в первую очередь вдохновение, которое может как прийти, так и нет."
    ts_ft 1c "То, что сегодня все справились – это хорошо. Но завтра могут справиться не все. А ещё через пару дней вдохновения может не найтись вообще ни у кого."
    show hiroto 1e at t11
    "На этой неделе папа хоть и не использовал те же слова, но суть осталась примерно той же."
    "Впрочем, у меня уже заранее был заготовлен ответ."
    m "Ну, сегодня справились все. А завтра будет завтра. Тем более, завтра у них ещё весь вечер будет, чтобы написать стихотворение."
    m "Да и к тому же, даже если стих, который они написали в клубе, кому-то не понравится, у них будет ещё весь вечер, чтобы отредактировать или даже полностью переписать его."
    show hiroto 1h at f11
    ts_ft "Ну-у-у... "
    extend 1g "Ладно, убедила."
    show hiroto 1f at t11
    m "Ну вот и поговорили."
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_kitchen
    show hiroto 1f at t11
    with wipeleft_scene

    $ TS.s(ts_showscreens)

    "Закончив ужинать, я говорю папе."
    m "Ну так что там у тебя за отличные новости такие?"
    show hiroto 1c at f11
    ts_ft "А, да, новости."
    ts_ft 1b "Говоришь, фестиваль у тебя на следующей неделе будет?"
    show hiroto 1a at t11
    "Слышать про фестиваль, который «будет на следующей неделе», невероятно больно. Но виду я не подаю."
    m "Да, пап..."
    show hiroto 1c at f11
    ts_ft "Ну так вот..."
    $ gtextsuka = glitchtext(24)
    hide hiroto
    show ts_hiroto_psyhodelic_pizdoc1 at t11
    ts_ft "Я сегодня звонил [gtextsuka]..."
    hide ts_hiroto_psyhodelic_pizdoc1
    show hiroto 1b at i11
    ts_ft 1b "В общем, можешь и сама её набрать, это именно она преподнесла нам такие хорошие новости."
    show hiroto 1a at t11
    "Я так и не поняла, кому именно он звонил, но из контекста могу догадаться, что звонил он моей маме."
    m "Ладно..."
    m "Ну, я звоню?"
    show hiroto 1b at f11
    ts_ft "Ну, набирай."
    show hiroto 1a at t11
    "Я достаю телефон и..."
    stop music fadeout 3
    $ TS.s(ts_hidescreens_fast)
    " {w=0.1}{nw}"
    $ TS.p(3)
    $ TS.s(ts_showscreens_fast)
    "Да не может этого быть..."
    "Я до этого момента особо телефоном не пользовалась, поэтому и не замечала..."
    "Но когда дело дошло до того, чтобы самой набирать кого-то, я буквально побледнела от ужаса."
    "Привычный русский язык, который был у меня на телефоне до этой субботы, заменился какими-то бессвязными и беспорядочными символами." #ГЛИЧТЕКСТ ЕСЛИ ПО ПРОСТОМУ, НО У НАС ЖЕ ЛИТЕРАТУРНОЕ ПРОИЗВЕДЕНИЕ ЕБАТЬ КОПАТЬ
    if unluck_ball > 0:
        show hiroto 1j at t11
        "Кое-как дойдя до списка контактов, перебрав где-то четыре контакта, ни один из которых не был мамой, я наконец-то добралась до контакта мамы."
        show hiroto 1h at f11
        ts_ft "Моника, с тобой всё хорошо?"
        show hiroto 1j at t11
        m "Да, пап, просто прекрасно..."
        m "Дай я только... доберусь... до мамы..."
        show hiroto 1h at f11
        ts_ft "Ладно... не буду тебе мешать..."
        show hiroto 1e at t11
    elif unluck_ball == 0:
        "Кое-как дойдя до списка контактов, я очень удачно нашла контакт мамы с первого раза."
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"
    play sound mobila_gudok
    $ TS.p(3)
    play sound psy_fast_1
    scene black with memglitch
    stop sound
    $ TS.p(1)

    show ts_host_split_animated
    show ts_kuh_split_animated

    $ TS.p(0.99)

    show minami 1bzf at ln31
    show hiroto 1b1 at rn33
    $ TS.p(1)
    show n_cg1b1337
    $ gtextsuka1 = glitchtext(24)
    $ ts_mt_name = "[gtextsuka]"
    $ TS.s(ts_showscreens)
    $ ts_ft_name = "[gtextsuka1]"


    ts_mt "[gtextsuka]{w=1.5}{nw}"
    hide n_cg1b1337

    $ ts_mt_name = "µ¶МÅ МºĦŇĶŅ"
    show minami 1bd at f31
    play music ts_icra fadein 2
    ts_mt "Алло?"
    show minami 1bc at f31
    "Спокойно... Всего лишь сон... Странный и страшный, но это всего лишь сон..."
    m "П-привет, мам..."
    show minami 2bk at f31
    ts_mt "Моника! Я так рада тебя слышать!"
    show minami 2bj at t31
    show hiroto 1b at f33
    ts_ft "Привет ещё раз, дорогая."
    show minami 1bzf at f31
    show hiroto 1a at t33
    ts_mt "Привет, [gtextsuka]."
    $ ts_ft_name = "П̶̢̛̛̛̙͇͕͓̠̲̲͚͔̜͔̟̪̂̅̉̄͊̿͋́̀̚͝ͅͅа̸̧̧̨͍͎̼̲̱̫̟̼̺̱͚͙̤̻̓̇͊̓̈͌̾̄̏̚п̷̨̮̝̠̻̞̯̼̈́͒͑̑͂͘͜а̷͓̪̳̖̳͈̱͎͔̱͈̼̪̟͗͗̀̿̊́̈́̔͘͜ ̵̛̹̳̺̓̔̃̕̕͠ͅМ̴̧̖̘͐о̶̢̡͍̠̼̳͍͇̹̉̓̏̔̈̄̐̂͗͑̏̍̓͜͝͝н̸̥͂̽͊͂͒̈́̐̏̈́̾͝ӣ̶͉̉̆̓̌̓͂͛̾͝͝к̷̹̽͋и̷̺̺̃̔͌̀̉̀͠"
    $ TS.s(ts_hidescreens_fast)
    " {w=0.1}{nw}"

    show minami 1bze at i31
    $ TS.p(0.44)
    show minami 1ba at i31
    $ TS.p(0.5)  
    show minami 1bq at t31
    show hiroto 1a at t33

    $ TS.s(ts_showscreens_fast)
    m "Мы тебя н-не разбудили?"
    show minami 2bzf at f31
    ts_mt "Моника, {nw}"
    show minami 2bb at f31
    extend "будь смелее, ты с мамой всё-таки разговариваешь, а не с чужим человеком, которого впервые видишь!"
    show minami 2bj at t31
    m "Да, мам..."
    show minami 3bn at f31
    ts_mt "На самом деле, я уже готовилась ко сну, а тут вы."
    show minami 3bv
    ts_mt "А в чём дело?"
    show minami 3bu at t31
    m "Папа сказал... сказал, что у тебя для меня... хорошие новости заготовлены..."
    show minami 3bl at f31
    ts_mt "Ах да, совсем забыла! "
    show minami 1br at f31
    extend "С этой работой уже ничего не помню..."
    show minami 1bt at f31
    ts_mt "Так вот. Когда у тебя там фестиваль будет?"
    $ TS.s(ts_hidescreens_fast)
    " {w=0.1}{nw}"
    show minami 1bze at t31
    $ TS.p(0.44)
    show minami 1ba at t31
    $ TS.s(ts_showscreens_fast)
    "Я не хочу уже даже и слышать про этот фестиваль, потому что, кажется, что он уже никогда не наступит."
    em "Не переживай, {i}когда-нибудь{/i} наступит!"
    em "А вот доживёшь ли ты до него – это уже совсем другой вопрос..."
    m "..."
    m "{size=14}Через неделю...{/size}"
    show minami 4bk at f31
    ts_mt "Какое приятное совпадение!"
    show minami 3bn at f31
    ts_mt "Поскольку я закончила раньше положенного срока, запуск новой ракеты будет уже в [gtextsuka]."
    show minami 2bzf at f31
    ts_mt "Я переночую один последний раз, {w=0.05}{nw}"
    show minami 2bd at f31
    extend "и в [gtextsuka1] у меня будет самолёт."
    show minami 3bk at f31
    ts_mt "К вечеру я уже буду дома, когда ты как раз вернёшься со своего фестиваля!"
    show minami 3bj at t31
    "Меня за эти три дня многое пугало, но сейчас я лишь задаюсь одним вопросом."
    "«Почему все говорят про фестиваль через неделю, но никто не говорит конкретные даты и дни недели?»"
    "Нет, я помню, что запуск маминой ракеты будет в субботу, в полночь понедельника у неё будет самолёт, и к вечеру она будет дома."
    "Но просто:"
    window hide
    play sound nfy
    show zatemnenie
    python:
        _preferences.volumes['music'] = 0.0

    $ TS.s(ts_showscreens)
    show screen c10_text_blya
    pause
    hide screen c10_text_blya

    show monika 2bd at f11
    em "Говорю же, это просто сон."
    em 4bd "А во сне, среди прочего, происходит абсолютная путаница с датами. Да и с именами, как ты уже поняла, тоже странности происходят."

    show monika 2bc at t11
    "«Но на прошлой же неделе такого не было!»"
    show monika 2bi at f11
    em "Потому что на прошлой неделе тебе снился другой сон. Более детализированный и менее ужасный."
    em 2bd "А на этой неделе тебе снится уже другой сон. А на следующей неделе – третий сон."
    em 3bd "Забыла уже, что я говорила про циклы?"
    em 3bi "Каждый цикл – это новый сон, который ничего общего с предыдущим не имеет."
    em 3bg "Поэтому я и хотела, чтобы ты вела себя естественно, а не шарахалась от каждого звука и движения."
    em 1br "Но, видимо, этому так и не суждено сбыться..."
    show monika 1bo at t11
    "«Х-х-х... Хорошо, я постараюсь вести себя как обычно. Как будто я тоже живу эту неделю, не зная, что меня ждёт дальше.»"
    show monika 2bl at f11
    em "Вот так-то лучше!"
    em 1bn "Кстати, до тебя там мама всё докричаться не может, ответь ей уже, пожалуйста..."
    hide monika
    "«Что?!»"
    hide zatemnenie with linearblur
    python:
        _preferences.volumes['music'] = .46
    show minami 3bs at f31
    show hiroto 2p at t33
    play sound ssikanul
    play sound2 psy_fast_1
    $ TS.s(vpunch)
    ts_mt "Моника!"
    show minami 2bs at t31
    show hiroto 2p at t33
    m "А? Что? Прости, мам, я что-то... задумалась..."
    show minami 2bn at f31
    show hiroto 1j at t33
    ts_mt "Совсем ты себя не бережёшь..."
    show minami 3bk at f31
    ts_mt "Небось, тот самый фестиваль из тебя все соки выжал?"
    show minami 3bj at t31
    m "Э-э-э, да... Хорошо, что это всё {i}скоро закончится{/i}..."
    em "Да что всё я-то?"
    "«Да как будто ты не знаешь...»"
    show minami 1bzf at f31
    ts_mt "Ладно, Моника, {nw}"
    show minami 1bt at f31
    extend "рада была тебя услышать, но, видимо, ты устала за сегодня даже больше, чем я."
    show minami 2bn at f31
    ts_mt "Передай телефончик папе, я ещё ему хочу кое-что сказать. А ты иди отдыхай."
    show minami 2bm at t31
    $ persistent.ingame_pizda = False
    m "Хорошо, мам. Спокойной ночи."
    python:
        _preferences.volumes['music'] = 0.0
        _preferences.volumes['sfx'] = 1.0
    $ persistent.ingame_pizda = True
    play sound scream_pereponkam_pizda
    show n_cg1b1337
    show minami 3bzf at t31
    ts_mt "Я надеюсь, ты умрёшь самой насильственной смертью в самых страшных муках{w=1.5}{nw}"
    stop sound
    $ persistent.ingame_pizda = False
    hide n_cg1b1337
    python:
        _preferences.volumes['music'] = .45
        _preferences.volumes['sfx'] = .65
        _history_list = []

    show minami 3bk at f31
    ts_mt "Спокойной ночи, солнышко. Люблю тебя.{fast}"
    show minami 3bj at t31
    m "Я... тоже тебя люблю..."

    if _preferences.language == "english":
        $ ts_ft_name = "Dad"
    else:
        $ ts_ft_name = "Папа"

    play sound ts_glitch2
    scene ts_kitchen
    with memglitchbolee
    stop sound
    stop music fadeout 4

    show hiroto 1c at f11
    ts_ft "{size=-6}Можешь идти, я тебе потом телефон занесу.{/size}"
    show hiroto 1e at t11
    "Как будто от него какая-то практическая польза будет..."
    show hiroto 1c at f11
    $ persistent.sprite_time = "day"
    ts_ft "Так вот, [gtextsuka]..."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_darkbed
    with wipeleft_scene

    $ TS.s(ts_showscreens)

    play music ts_ios fadein 2
    $ persistent.sprite_time = "night"
    "Как же я устала..."
    "Вроде время ещё раннее, даже для меня, но этот день выдался настолько насыщенным, что у меня уже просто нет никаких сил, чтобы делать хоть что-то."
    "У меня есть силы разве что на то, чтобы дойти до кровати, раздеться и увалиться намертво."
    show monika 1pd at f11
    em "Что значит «увалиться намертво»? А стих кто писать будет?"
    show monika 1pc at t11
    m "Я его уже написала. А на то, чтобы редактировать или тем более переписывать стих, у меня нет ни сил, ни желания. Да и просто лень мне."
    m "Стих написан? Написан. Ошибок нет? Вроде как нет – я его несколько раз перечитывала, и ни одной ошибки не заметила."
    m "Так что я спать. Завтра будет день, завтра будут новые свершения. Но не сегодня."
    show monika 1pg at f11
    em "..."
    em "Ну а{w=0.5}{nw}"
    show blink
    "Однако я уже провалилась в сон."
    "В прошлый {b}вторник{/b} я проснулась в половине пятого утра..."
    if unluck6 == True:
        "...а затем всё равно опоздала в школу..."
    else:
        "...но даже несмотря на то, что я выспалась, я доспала ещё примерно час..."
    stop music fadeout 5
    scene black
    "Но сегодняшний день был гораздо более тяжёлым и изматывающим."
    "И я в любом случае проснусь не раньше того времени, в котором я просыпаюсь обычно."
    "Однако додумать мысль до конца я уже не успела."
    "Спустя пару секунд, как я закрыла глаза, я уже провалилась в сон."
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"
    $ TS.s(ts_null_transform)
    jump ts_scenario_11