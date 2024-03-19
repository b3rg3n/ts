label ts_scenario_5:
    $ save_name = "С возвращением,\nМоника!"

    python: # ОБНОВЛЯЕМ RPC
        try:
            rpc.update(state="Акт II | Глава I",details="С возвращением, Моника!",large_image="atwocone",start=time.time())
        except AssertionError:
            pass

    $ persistent.rpclabel = "5"
    $ persistent.carter2menu = True
    $ persistent.carter3menu = False

    play sound chp2
    $ Chapter("АКТ ВТОРОЙ")
    $ Chapter("АКТ ВТОРОЙ")
    $ Chapter("Глава первая")
    $ Chapter("Глава первая")
    $ Chapter("С возвращением, Моника!")
    stop sound fadeout 7
    $ Chapter("С возвращением, Моника!")

    scene black
    pause 1

    $ TS.Screens(ts_showscreens)

    s "{size=-6}..ика!{/size}"
    s "{size=-4}Моника!{/size}"
    s "Моника, просыпайся уже!" with hpunch
    m "Пап, ну ещё пять минуточек..."
    s "Вставай давай, пьянь малолетняя!"

    window hide
    play sound fb
    scene ts_sayori_bedroom:
        blur 10
    show sayori 4pi at t11:
        blur 10
    with flash

    $ TS.Screens(ts_showscreens)

    "Передо мной предстала Сайори в пижаме..."

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    show ts_blinking

    pause 0.7

    hide ts_blinking
    show ts_blinking

    $ TS.Screens(ts_showscreens)

    "Я протираю глаза и промаргиваюсь, чтобы чётче рассмотреть."

    scene ts_sayori_bedroom
    show sayori 4pi at i11
    with dspr

    $ TS.Screens(ts_showscreens)

    "Всё та же Сайори. Во всё той же пижаме. Во всё той же комнате..."

    play music audio.m1
    window hide
    play sound fb
    show s_kill_bg_zoom zorder 1
    show s_kill_bg2_zoom zorder 1
    show s_kill_zoom zorder 3
    show s_kill2_zoom zorder 3
    show s_kill as s_kill_zoom_trans zorder 3:
        truecenter
        alpha 0.5
        zoom 2.0 xalign 0.5 yalign 0.05
        pause 0.5
        dizzy(1, 1.0)
    show overlay aw_memory_back_1 zorder 4
    with flash

    $ pps = 2

    $ TS.Screens(ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake))

    "Та же Сайори..."
    "В той же пижаме..."
    "В той же комнате..."
    "Нет..."

    window hide
    play sound fb
    scene ts_sayori_bedroom
    show sayori 4pi at t11
    with flash

    m "..."

    show sayori 2pg at s11

    "Видя моё лицо первобытного ужаса, Сайори и сама не на шутку перепугалась."

    s 2ph "Что такое?"

    show sayori 2pe at h11
    pause 0.4
    show sayori 3pf at h11
    pause 0.4
    show sayori 4pz at h11

    m "{font=[pizdec_font]}{size=+20}{b}А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А{/b}{/size}{nw}"

    "Крик постепенно переходит в бесконтрольное рыдание."

    m "{font=[pizdec_font]}{size=+20}{b}ПРОСТИПРОСТИПРОСТИПРОСТИПРОСТИ{/b}{/size}{nw}"

    m "{font=[pizdec_font]}{size=+20}{b}ЭТО ВСЁ Я ВИНОВАТА, Я ВИНОВАТА, ВИНОВАТАВИНОВАТАВИНОВАТАВИНОВАТА{/b}{/size}{nw}"

    show sayori 2po at s11

    "Сайори всё это время непонимающе смотрит на меня."

    s 2ph "В чём именно ты виновата, Моника?"

    show sayori 2pg at t11

    m "{font=[pizdec_font]}{size=+20}{b}ВО ВСЁМ!{/b}{/size}"
    m "{font=[pizdec_font]}{size=+20}{b}САЙОРИ, ПРОСТИ МЕНЯ, ПОЖАЛУЙСТА, ЕСЛИ МОЖЕШЬ!{/b}{/size}"
    s 2pl "В чём мне тебя прощать? Ты же мой друг..."

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    $ TS.Screens(ts_null_transform)

    show sayori 2pk at s11

    $ pps = 4

    $ TS.Screens(ts_showscreens)

    "Вдоволь нарыдавшись и накричавшись, я наконец-то говорю более-менее нормально."

    m "Я видела сны... очень страшные сны... И одним из этих снов было т-т-т-т-то, к-к-к-как т-т-ты..."

    show sayori 2po at t11

    m "П-п-п-п-п-п-п-п-п-п-п-п-п-п-п..."
    m "...п-п-п-по-по-по-в-в-в-в..."

    "Я всё никак не могу выговорить ключевое слово."
    "Сайори, в свою очередь, всё никак не может понять, что это за слово такое, поэтому и спрашивает."

    s 2ph "Что я сделала?"

    "На одном дыхании я выпалила."

    show sayori 2pm at h11

    $ pps = 2

    $ TS.Screens(ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake))

    m "{font=[pizdec_font]}{size=+20}КАК ТЫ ПОВЕСИЛАСЬ В ТОЙ ЖЕ ПИЖАМЕ ЧТО НА ТЕБЕ НАДЕТА СЕЙЧАС!{/size}"

    "После этих слов я начинаю рыдать пуще прежнего."

    s "{b}ЧТО?{/b}"

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    window hide
    show sayori 2pz at h11
    pause 0.25
    show sayori 2pf at h11
    pause 0.25
    show sayori 2pu at h11
    pause 0.25
    show sayori 2pw at h11

    $ TS.Screens(ts_showscreens)

    "Теперь начинает плакать и Сайори."

    $ TS.Screens(ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake))

    window hide
    show zatemnenie
    show screen akt2_chp1_text
    pause
    hide screen akt2_chp1_text
    show screen akt2_chp1_text1
    pause
    hide screen akt2_chp1_text1
    show screen akt2_chp1_text2
    pause
    hide screen akt2_chp1_text2
    show screen akt2_chp1_text3
    pause
    hide screen akt2_chp1_text3
    show screen akt2_chp1_text4
    pause
    hide screen akt2_chp1_text4
    show screen akt2_chp1_text5
    pause
    hide screen akt2_chp1_text5
    show screen akt2_chp1_text6
    pause
    hide screen akt2_chp1_text6
    hide zatemnenie
    with dissolve

    stop music fadeout 4

    $ pps = 4

    $ TS.Screens(ts_showscreens)

    "Но голос молчал."

    "Ну и ладно! Да и к тому же, чем пытаться переспорить свою шизофрению, у меня есть вполне реальная плачущая Сайори."

    play music audio.t9

    m "Сайори, ну... не плачь..."

    "Я пытаюсь говорить с Сайори точно так же, как и с Юри."

    show sayori at cright with move
    hide sayori

    "Однако, логично, что Юри и Сайори - два {i}совершенно{/i} разных человека."
    "К тому же, одну я просто выслушивала, а второй сказала, что она повесится."
    "Пусть даже это только и сон..."

    show sayori 1pd at t11

    "Сайори, кажется, тоже уловила мою последнюю мысль, вытирает слёзы и говорит."

    s 2pzd "Моника, да всё в порядке..."
    s "Ведь сон - он на то и сон, что в реальности этого не случится."

    show sayori 2pd at s11

    "Я только попыталась парировать тем, что сон - это скорее неосознанные воспоминания, следовательно, это уже было..."

    show sayori 3pi at t11

    "Однако, уловив хмурый взгляд Сайори, заговорить я не решилась."
    "Тем временем Сайори продолжает."

    show sayori 4po at s11

    s "Так вот, на чём я остановилась..."

    show sayori 2pzd at t11

    s "Сон - это просто сон. А реальность - это просто реальность."
    s "Иди обниму..."

    show blink

    s "...и не нужно винить себя за то, что ты не сделала или даже не хотела сделать."

    "Всхлипывать я не перестала, но зато хотя бы немного легче на душе стало."

    stop music fadeout 5

    m "Значит, ты меня прощаешь?.."
    s "А как я могу простить тебя за то, чего ты даже не делала?"
    s "Это я должна извиняться..."

    "После этих слов Сайори тоже начала плакать."
    "Ситуация один в один как в школе примерно месяц назад. Только вместо коридора у нас теперь спальня Сайори..."
    "Спальня..."

    play sound fb
    scene ts_sayori_bedroom
    show sayori 1pd at t11
    with flash

    $ TS.Screens(ts_showscreens)

    m "С-Сайори..."

    show sayori 2pe at f11
    play music ts_gc

    m "А ч-что я... вообще делаю у тебя в спальне?"

    show sayori 2pn at t11

    "Сайори на секунду замешкалась, но затем собралась и гневно отвечает."

    s 4pj "Так ты вчера настолько сильно напилась, что мы с Юри едва твою бессознательную тушку дотащили!"
    s 3ph "Хорошо хоть я живу недалеко от школы, да и тащить мне тебя пришлось не одной!"
    s 4ph "И {b}очень{/b} хорошо, что моих родителей ещё не было дома, а ты хотя бы не устраивала разнос по всему моему дому!.."

    show sayori 2pf at f11

    "А, да... Понемногу и я начинаю вспоминать..."

    window hide
    play sound fb
    scene ts_club:
        blur 10
    show yuri 2r at t31:
        blur 10
    show sayori 2h at t32:
        blur 10
    show natsuki 1n at t33:
        blur 10
    show overlay aw_memory_back_1
    with flash

    $ TS.Screens(ts_showscreens)

    y "Я сказала сидеть на месте!"
    y "Сайори доведёт тебя домой."

    play sound fb
    scene ts_sayori_bedroom
    show sayori 2pf at i11
    with flash

    $ TS.Screens(ts_showscreens)

    s 2ph "Поэтому я просто уложила тебя спать, и ты так проспала до утра."
    s 2pl "Правда, ты кричала во сне, и довольно часто... Но, кажется, теперь я понимаю, из-за чего..."

    show sayori 2pk at f11

    m "Ну... прости, Сайори... Я не намеревалась напиваться до {i}такой{/i} степени..."

    "Если бы в нашем клубе было больше людей, я бы уже к понедельнику сложила свои полномочия и обязанности президента клуба."
    "Хорошо хоть все уже давно перезнакомились друг с другом, и терпеть насмешки я буду разве что от Юри и Нацуки."
    "Представляю, как если бы я настолько напилась на каком-то классном или, того хуже, всешкольном мероприятии."
    "Я бы на следующий же день ушла из этой школы, не стерпев позора..."

    show sayori 4pj at t11

    s "Да? А кто тогда подначивал Юри купить вторую бутылку вина?"

    show sayori 3pi at s11

    stop music fadeout 5

    m "Я это уже смутно помню..."
    m "Ну, прости, Сайори. За {i}это{/i} уж точно прости."
    s 2pl "Да, ладно, всё бывает в первый раз. И похмелье тоже."
    s 2pzc "Прощаю."

    $ pps = 1

    show sayori 1px at t11
    play music audio.okevrsay

    s "Ладно, пойду переоденусь."
    extend 1pl " Раз уж моя пижама так тебя смущает, переоденусь во что-то более нейтральное."
    s 1py "Только, это, можешь выйти на пару секунд? Знаю, мы обе девочки, но я всё равно... стесняюсь..."
    m "А разве я просто не могу отвернуться и закрыть глаза?"
    s 2pl "Ну-у-у, или так, да... Как я только сама об этом не подумала?"

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound2 pageflip
    scene ts_sayori_bedroom
    show sayori 1ba at i11
    with wipeleft_scene

    $ TS.Screens(ts_showscreens)

    "Спустя пару минут Сайори, уже полностью переодетая, весело говорит."

    s 2bx "Я ещё в магазин по пути пойду. Ты со мной?"

    show sayori 2ba at f11

    m "Конечно."
    s 2br "Ну и здорово!"
    s 2bc "Только тс-с-с, родители спят ещё."

    stop music fadeout 3

    show sayori 2bb at t11

    m "Как скажешь..."

    "Мы быстро и тихо выходим из дома."

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound2 pageflip
    scene ts_residential
    with wipeleft_scene

    play music ts_dist

    m "Ой, а я этот район знаю! Это же..."

    window hide
    play sound fb
    scene ts_residential
    show overlay aw_memory_back_1
    with flash

    $ TS.Screens(ts_showscreens)

    "Это же район, в котором живёт Мира, хотела я сказать, но осеклась."
    "В основном потому, что больше здесь Мира не живёт. Она умерла пару лет назад."
    "Я точно не знаю, ни от чего она умерла, ни даже когда конкретно она умерла."
    "Знаю лишь, что от остановки сердца где-то пару лет назад в конце весны или в начале лета."
    "Что очень странно, учитывая, что она ещё с раннего возраста была мастером спорта по плаванию..."
    "В общем, ещё один вопрос, на который нет ответа. И не будет."

    stop music fadeout 4

    "После её смерти родители не выдержали горя и переехали в совершенно другой город на другом конце страны."
    "Ну а сестра уже достаточно взрослая и самостоятельная, у неё уже своя жизнь."
    "А дом, в котором {i}когда-то{/i} жила Мира, теперь пустует..."

    window hide
    play sound fb
    scene ts_residential
    show sayori 1bb at i11
    with flash

    play music audio.okevrsay

    "Однако Сайори, кажется, не заметила ни моей ремарки, ни последующей моей задумчивости."

    s 2bc "Ты где живёшь?"

    show sayori 2bb at f11

    m "Где-то, э-э-э... на другом конце города."

    "Я примерно показываю направление."

    s 2bx "Ну и здорово! Мы пройдём через магазин, а затем разойдёмся по домам."

    show sayori 2ba at t11

    m "Пойдём."

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound2 pageflip
    scene ts_city_day
    show sayori 1bf at i11
    with wipeleft_scene

    $ TS.Screens(ts_showscreens)

    "Всю дорогу до магазина мы шли молча."
    "Мне разговаривать не хотелось, потому что до сих пор было стыдно за вчерашнее."
    "Сайори же не особо-то и настаивала на том, чтобы поговорить со мной."
    "Лишь остановившись у самого магазинчика, Сайори говорит."

    stop music fadeout 5

    s 1bc "Ну, на этом наши пути расходятся."
    s 2bx "До понедельника!"

    show sayori 2ba at s11

    m "Да, до понедельника..."

    show sayori 2ba at cright with move
    hide sayori

    "После этих слов Сайори направилась в магазин, а я пошла дальше до дома."

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound2 pageflip
    scene ts_street
    with wipeleft_scene

    play music ts_mdl

    $ TS.Screens(ts_showscreens)

    "Весь оставшийся путь я думала и пыталась вспомнить произошедшее."

    show monika 5ba at t11

    $ pps = 3

    em "Даже и не пытайся, всё равно не вспомнишь."
    m "А! Ты вообще откуда взялась?"
    em 2bd "Когда поблизости никого, мы можем спокойно говорить."
    em 3bl "Только не забывай, что другие меня не видят, и если кто-то даже издали сможет разглядеть тебя, для других ты покажешься как минимум странной."
    em 1bn "А как максимум - выпишут направление в жёлтый дом."

    show monika 1bm at f11

    m "А я вот всё хотела спросить... А ты вообще кто?"
    em 2bk "А ты забыла уже? Я же подсознание твоё."

    show monika 1bj at t11

    m "Нет, это я помню.{w=0.44}{size=-4}Даже лучше, чем мне хотелось бы...{/size}"
    m "Я имела в виду, почему ты просто зеркальная копия меня?"
    em 4bb "Ну, во-первых, я же буквально часть тебя, поэтому логично, что я как минимум буду похожа на тебя саму."
    em "А во-вторых..."

    show monika 3bh at f11

    "На секунду мне показалось, что моё «альтер-эго» посмотрело не {i}на{/i} меня, а {i}сквозь{/i} меня."

    em 3bn "А впрочем, неважно уже..."

    show monika 3bm at t11

    m "Как скажешь..."

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound2 pageflip
    scene ts_street
    show monika 1ba at i11
    with wipeleft_scene

    $ TS.Screens(ts_showscreens)

    m "Кстати, э-э-э..."
    em 4bb "Просто называй меня Моника. Ну или если официально, то [em_name]."
    em 2bn "Хотя, у тебя, скорее всего, просто язык сломается так меня называть..."
    em 2bb "Поэтому лучше Моника. Да и проще."

    show monika 1ba at f11

    m "Да, {i}Моника{/i}, так вот... Что ты имела в виду под «циклами»?"
    em 1bi "Ну..."
    em 5ba "Впрочем, сама скоро поймёшь. На следующей неделе."

    show monika 1ba at thide
    hide monika

    $ TS.Screens(vpunch)

    m "ЧТО ИМЕННО Я ДОЛЖНА ПОНЯТЬ?"

    "Но моё «подсознание» так же резко испарилось, как и появилось."

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    $ pps = 1

    play sound2 pageflip
    scene ts_house
    with wipeleft_scene

    $ TS.Screens(ts_showscreens)

    "Впрочем, как раз вовремя."
    "Пока я {i}разговаривала{/i} с ней, я и сама не заметила, как дошла до дома."
    "Уже почти полдень, папа уже {i}должен{/i} проснуться и давно бодрствовать."

    stop music fadeout 3

    "Я медленно открываю входную дверь..."

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound2 pageflip
    scene ts_gost
    with wipeleft_scene

    play sound2 pageflip
    scene ts_kitchen
    with wipeleft_scene

    $ TS.Screens(ts_showscreens)

    m "Пап, я дома!"

    "Однако папы на кухне не оказалось."
    "Впрочем, у нас же не одна кухня в доме. Дом довольно большой, может, он сразу и не услышит."
    "Я повторяю громче."

    m "Папа! Я дома!"

    "Однако и это не помогло."
    "И только сейчас я вспоминаю, что у папы же сломалась машина, и он, скорее всего, в гараже."
    "Хорошо хоть голосовые связки не порвала, прежде чем меня осенило!"

    show hiroto 1e at ln11

    "И как раз в этот момент папа возвращается из гаража. Даже подозрительно чистый как для того, у кого сломалась машина."

    show hiroto 1p at f11

    "Увидев меня, он быстро подошёл ко мне. Вот же разнос будет..."
    "Но вместо этого он просто весело сказал."

    play music ts_gp

    ts_ft 2b "Ну привет, гулёна!"

    show hiroto 1a at t11

    "От сказанного я аж потеряла дар речи. Всё, что из меня получилось выдавить - это запинающимся голосом сказать:"

    m "П... п... привет?"

    "Вот уж на самом деле учёба - это {b}единственное{/b}, что его волнует!"

    ts_ft 2z "Ну как там {i}чаепитие{/i}?"

    show hiroto 2r at f11

    "Он так сказал «чаепитие», как будто он уже достоверно знает, что произошло, и просто дразнит меня."
    "И что прикажете делать?"
    "Я могу сразу сказать ему всю правду, а могу поиграть в его игру."
    "Не знаю, что из этого будет больнее, но... будь что будет."

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    show zatemnenie with dspr

    $ TS.Screens(ts_showscreens)

    menu:
        "Сказать правду":
            hide zatemnenie with dspr
            stop music fadeout 2
            pause 2
            $ TS.Screens(ts_showscreens)
            play music audio.t9
            m "Это... не совсем чаепитие было..."
            show hiroto 1j at t11
            m "Скорее, попойка. Для одного человека."
            m "Вчера Юри...{w=0.44} Ну, это та девочка с фиолетовыми волосами...{w=0.44} вместо чая принесла бутылку красного вина."
            m "Сама Юри выпила немного, остальные только губами коснулись и обплевались от крепкого вкуса, ну а я..."
            m "...всё остальное вылакала..."
            m "А после третьей чашки я вообще не помню, что происходило вчера. Очнулась я только с утра в доме у Сайори, это наш новоиспечённый вице-президент."
            show hiroto 1b1 at f11
            "Я не говорю ему о том, что мне снилось."
            em "И правильно делаешь. Нечего старику такие ужасы показывать."
            "«Подсознание» внезапно подключилось к нашему разговору."
            "Я перехожу на мысленный разговор."
            m "«Старик? Ему всего сорок пять!»"
            em "Ну-ну..."
            "Я не обращаю на него... неё... внимания, и продолжаю."
            m "Да, так вот... Очнулась я дома у Сайори, она меня подняла и рассказала некоторые дополнительные подробности прошлого вечера."
            show hiroto 1i at t11
            m "Например, как Юри и Сайори тащили меня...{w=0.44} а точнее, мою «тушку», как она выразилась...{w=0.44} со школы аж до самого её дома, а я тем временем пыталась извернуться и пойти своей дорогой."
            m "Хорошо хоть её дом недалеко от школы находится, иначе я бы даже не знаю, как бы две девочки дотащили полумёртвую пятидесятикилограммовую меня..."
            "...или сколько я там сейчас вешу?.."
            show hiroto 1f at s11
            m "Гораздо проще было бы, если бы {b}ты{/b} дотащил меня сразу до нашего дома..."
            m "Прости за это безобразие..."
            ts_ft 2g "Моника, тебе не за что извиняться."
            ts_ft "Я понимаю, молодость, гормоны играют, и всё такое."
            ts_ft 1y "Как будто сам по молодости таким не был..."
            ts_ft 1c "Но ты должна пообещать, что больше не будешь пить настолько безответственно."
            show hiroto 1f at t11
            m "Уж об этом не беспокойся, я после этого случая вообще пить не буду."
        "Соврать":
            $ unluck5 = True
            hide zatemnenie with dspr
            $ TS.Screens(ts_showscreens)
            "Я решаю соврать. Как будто в первый раз."
            show hiroto 1e at t11
            m "Чаепитие?.. Да вроде как обычно..."
            m "Мы попили чайку, покушали кексиков, а потом..."
            m "Потом, э-э, мы все вчетвером пошли домой к Сайори, и было у нас, ..., что-то вроде вечера для девочек."
            m "Потом... потом Юри и Нацуки к вечеру ушли, а я осталась с Сайори на ночёвку."
            show hiroto 1r at s11
            m "Наутро мы проснулись, и я, ну, просто домой пошла."
            m "Ничего необычного."
            "Фух."
            "Хотя говорила я достаточно ровно и чётко, внутри я как будто вся тряслась."
            "Однако папа, по всей видимости, не поверил в мои сказки Венского леса."
            ts_ft 1z "Что, правда? А я вот располагаю совсем другой информацией."
            show hiroto 1r at t11
            "Ой-ой-ой..."
            ts_ft 2q "Как тебя, полумёртвую, тащили остальные девочки, пока ты на всю улицу кричала всякие непристойности..."
            show hiroto 2p at f11
            m "К-как т-ты..."
            ts_ft 2q "Если я иду пешком, то прохожу как раз мимо твоей школы. А тут как раз ты... Точнее, то, что от тебя осталось..."
            show hiroto 1p at t11
            m "А п-почему т-ты м-меня с собой не забрал?.."
            ts_ft 2z "Знаешь, я изначально хотел..."
            ts_ft 2z1 "Но затем я подумал, что лучше учиться на своих собственных ошибках, поэтому и просто прошёл мимо."
            show hiroto 2r at f11
            m "Ну, знаешь ли!.."
            m "Это довольно подло..."
            ts_ft 2q "А нагло врать прямо мне в лицо - это не подло?"
            show hiroto 1p at t11
            m "Но это же ты первый начал!.."
            ts_ft 1z1 "А ты вторая."
            ts_ft 1h "Моника, ты же уже не малое дитя, а взрослый человек, и за пьянство я тебя осуждать не стану."
            ts_ft 1y "Тем более, как будто сам по молодости таким не был..."
            ts_ft 1h "Да и за враньё я тебя винить не буду, тебе же всё-таки не восемь лет..."
            ts_ft "Но всё равно, врать, тем более, так нагло - это плохо."
            show hiroto 1j at f11
            m "Прости, пап..."
            ts_ft 1g "Ладно, на первый раз прощаю."
            ts_ft 1c "Но всё равно, не пей настолько безответственно."
            show hiroto 1f at t11
            m "Не переживай, пап, я больше вообще никогда пить не буду. Не моё это."

    stop music fadeout 4

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound nfy

    show zatemnenie with dspr

    $ TS.Screens(ts_showscreens)

    show screen chp_5_text1
    pause
    $ TS.Screens(ts_hidescreens)
    show screen chp_5_text1
    pause 1
    hide screen chp_5_text1

    hide zatemnenie with dspr

    $ TS.Screens(ts_showscreens)

    show hiroto 1b at f11

    ts_ft "Ну, вот и поговорили."

    "Мы оба с этого просто рассмеялись."

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound2 pageflip
    scene ts_kitchen
    with wipeleft_scene

    $ TS.Screens(ts_showscreens)

    play music ts_mdl

    show hiroto 1e at t11

    "Пока он ещё не обвинил меня в чём-либо, я решаю перехватить инициативу сама."

    m "А ты, пап, чем занимался всё это время?"
    ts_ft 1c "Ну, во-первых, переживал о тебе."
    ts_ft "Нет, конечно, во все больницы и морги я не названивал, я же всё-таки знаю, что ты не одна домой пошла, а с девочками..."
    ts_ft 2h "Но всё равно переживал."
    ts_ft 1c "К утру я уже немного успокоился и стал мыслить более рационально."
    ts_ft 1g "У меня же всё-таки машина сломанная в гараже стоит."
    ts_ft 1c "Поэтому я как только позавтракал и умылся, начал возиться с ней."
    ts_ft "Я изначально думал обо всём на свете, вплоть до того, что двигатель встал намертво, и больше мы на этой машине ездить не будем никогда."
    ts_ft 1h "А новая машина - это такие траты..."
    ts_ft 2b "Но всё оказалось гораздо проще - там просто несколько контактов отошло."
    ts_ft "Как только я понял, в чём именно причина, я быстренько вставил все контакты там, где им и положено быть, и вот, машина как новенькая!"
    ts_ft 1g "Так что, получается, зря только всю неделю пешком до работы ходил, там делов минут на десять, если не меньше."
    ts_ft "Я даже не испачкался, хотя думал, что к вечеру весь чумазый буду..."
    ts_ft 1b "Так что с понедельника снова буду ездить на машине, и с утра проводить больше времени с любимой дочерью."

    show hiroto 1f at s11

    "Ну и ну..."
    "Я в машинах вообще ничего не смыслю, даже не знаю, какая у нас коробка передач стоит... Но раз папа сказал, что всё так просто, то, наверное, так всё и было."

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    nvl clear

    $ TS.Screens(ts_showscreens)

    nvlbazar "{font=[ts_nvl_font2]}Водить я, соответственно, тоже не умею от слова совсем."
    nvlbazar "{font=[ts_nvl_font2]}Нет, конечно, папа давал мне порулить пару раз в детстве, когда я ещё совсем маленькая была..."
    nvlbazar "{font=[ts_nvl_font2]}Но чтобы водить самой - это уж извольте."
    nvlbazar "{font=[ts_nvl_font2]}Родители неоднократно спрашивали меня на тему того, чтобы водить машину, но я им отвечала, что мол «Буду важной, буду богатой - у меня будет свой водитель, который будет водить вместо меня. А мне самой это не нужно.»"

    nvl clear

    nvlbazar "{font=[ts_nvl_font2]}Дело же даже не в том, что я не знаю правил. Наоборот, если бы я сдавала экзамен по вождению, я бы сдала его с первого раза. Ну максимум, со второго."
    nvlbazar "{font=[ts_nvl_font2]}Но просто... как только я сажусь в машину, я паникую и совершенно не знаю, что мне делать."
    nvlbazar "{font=[ts_nvl_font2]}Поэтому я и наотрез отказываюсь водить и даже учиться водить. Пусть другие это расхлёбывают. Не я."

    $ TS.Screens(ts_hidescreens)
    nvlbazar " {w=1.0}{nw}"

    nvl clear

    $ TS.Screens(ts_showscreens)

    ts_ft 1c "Ладно... Так, это, ты к себе пойдёшь, или?.."

    show hiroto 1e at t11

    "А я и сама даже не знаю. К себе пойду, или же {i}что-то ещё?{/i}"
    "С одной стороны, голова всё ещё немного кружится, а в своей постели спать всё равно на порядок удобнее, чем на полу."
    "С другой стороны... Что-то мы в шахматы с папой давненько не играли..."

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    show zatemnenie with dspr

    $ TS.Screens(ts_showscreens)

    menu:
        "Играть в шахматы":
            $ act2_chess = True

            hide zatemnenie with dspr

            $ TS.Screens(ts_showscreens)

            m "Или. Пап, давай в шахматы сыграем?"
            ts_ft 2h "В шахматы?.."

            show hiroto 1j at s11

            m "Ну же, пап, мы уже сто лет в шахматы не играли! Давай поиграем!"
            ts_ft 1g "Ладно уж..."

            show hiroto 1f at t11

            m "Вот так-то лучше."
            ts_ft 1b "Только ты доску сначала принеси."

            show hiroto 1a at f11

            m "А-э-э-э... Сейчас..."

            $ TS.Screens(ts_hidescreens)
            " {w=1.0}{nw}"

            play sound2 pageflip
            scene ts_living_room
            with wipeleft_scene

            $ TS.Screens(ts_showscreens)

            "В шахматы мы действительно уже очень давно не играли. В последний раз мы играли, когда мне было лет... тринадцать, кажется? Или четырнадцать? В любом случае, очень давно."
            "Я даже не помню, где вообще лежит доска!"
            "Так, посмотрим... После нашего {i}крайнего{/i} раза папа положил доску где-то в гостиную."

            stop music fadeout 4

            "Моё счастье, что с прошлого раза её местоположение никак не изменилось!"
            "А то знаете, вот вроде лежит себе вещь, никого не трогает, а как только она тебе понадобится, так её нет."
            "В любом случае, пару минут спустя я с доской в руках иду обратно к папе."

            $ TS.Screens(ts_hidescreens)
            " {w=1.0}{nw}"

            play sound2 pageflip
            scene ts_kitchen
            show hiroto 1c at i11
            with wipeleft_scene

            play music ts_sgtbc

            $ TS.Screens(ts_showscreens)

            ts_ft "Нашла?"

            show hiroto 1e at f11

            m "Да. Правда, не знаю, все ли фигуры на месте..."
            ts_ft 2b "А это и не важно уже. Если что, заменим подручными средствами."

            show hiroto 2a at t11

            m "Подручными средствами?"
            ts_ft 2b "Ну, знаешь, у нас же много мелочёвки, которую можно поставить на место фигуры."
            ts_ft 1c "Главное, чтобы одинаковая мелочёвка не отвечала за разные фигуры, а то запутаемся..."

            show hiroto 1f at f11

            "Однако это и не было нужно. Все тридцать две фигуры были в целости, сохранности, и на месте."

            ts_ft 1c "Та-а-ак..."
            ts_ft 1b "Ну, в какой руке?"

            show hiroto 1a at t11

            "Поскольку у нас это скорее семейная забава, чем какое-то соревнование, цвет определяется исключительно волей случая."
            "Папа просто протягивает две руки, а я выбираю, каким цветом играть."

            m "М-м-м... В левой."

            "Папа открыл левую руку, в которой была белая пешка."

            ts_ft 1b "Повезло, повезло..."

            "Хотя нам обоим не особо принципиально, каким цветом играть, белый цвет придаёт какую-то дополнительную уверенность."

            ts_ft "Ну, ходи."

            window hide
            play sound fb
            stop music
            scene black
            show monika 1n at i11
            with flash

            $ TS.Screens(ts_showscreens)

            cm "Кхе-кхе..."
            cm "В общем..."

            $ TS.Screens(ts_hidescreens)
            " {w=1.0}{nw}"

            $ TS.Screens(ts_showscreens)

            show zatemnenie with dspr

            menu:
                "А ты вообще кто такая?":
                    pass

            hide zatemnenie with dspr

            $ TS.Screens(ts_showscreens)

            cm 3l "О, ты не волнуйся."
            cm "Хотя спрайт похожий, я не Моника, и даже не шизофрения Моники."

            $ cm_name = "Магнолия"

            cm 4b "Меня зовут Магнолия Карлсен. Можно просто Магнолия. Обращаюсь я к тебе, [user]."
            cm 2d "Скажи мне... Ты умеешь играть в шахматы?"

            $ TS.Screens(ts_hidescreens)
            " {w=1.0}{nw}"

            show zatemnenie with dspr

            $ TS.Screens(ts_showscreens)

            menu:
                "Да":
                    hide zatemnenie with dspr
                    $ TS.Screens(ts_showscreens)
                    cm 2b "Вот и здорово!"
                    cm 2i "Мне же меньше работы..."
                "Нет":
                    hide zatemnenie with dspr
                    $ TS.Screens(ts_showscreens)
                    cm 1n "Ну... не беда..."
                    cm 4k "Всегда ведь можно научиться!"
                    cm 2d "Ты ведь {i}хочешь{/i} научиться играть в шахматы?"
                    cm 2i "Только учти, я буду объяснять самые основы основ, например, как ходят фигуры."
                    cm "Так что если ты надеешься, что после мода на Доки-Доки ты будешь играть сильнее мастеров этой игры - просто... перестань."
                    cm 1d "Итак, я повторяю свой вопрос: ты хочешь обучиться игре в шахматы?"

                    $ TS.Screens(ts_hidescreens)
                    " {w=1.0}{nw}"

                    show zatemnenie with dspr

                    $ TS.Screens(ts_showscreens)

                    menu:
                        "Да":
                            hide zatemnenie with dspr
                            $ TS.Screens(ts_showscreens)
                            $ chess_tutor = True
                            cm 4k "Тогда отлично!"
                            cm 2b "В процессе игры я буду объяснять, как ходят фигуры, и попутно объясню самые базовые принципы игры."
                        "Нет":
                            hide zatemnenie with dspr
                            $ TS.Screens(ts_showscreens)
                            cm 1p "Ну, как знаешь... "
                            extend 1r "{size=-10}Невежда...{/size}"
            window hide
            play sound fb
            play music ts_sgtbc
            scene ts_kitchen
            show hiroto 1a at i41
            with flash

            show chess1 at ts_chess_move_up
            pause 1

            $ TS.Screens(ts_showscreens)
            "Я начинаю игру ходом пешки."

            $ TS.Screens(ts_hidescreens)
            " {w=1.0}{nw}"

            show chess1 at ts_chess_move_down
            pause 0.5
            hide chess1 with dissolve

            show chess2 at ts_chess_move_up
            pause 1
            $ TS.Screens(ts_showscreens)

            if chess_tutor == True:
                show monika 2b at rn44
                cm "Пешки ходят только вперёд и только на одну клетку."
                cm "Однако, первым ходом она может пойти и на две. Но учти, если первым ходом ты сдвинул пешку на одну клетку, это право всё равно теряется."
                $ TS.Screens(ts_hidescreens)
                " {w=1.0}{nw}"
                show monika at ron44
                pause 0.5
                hide monika with dissolve
                $ TS.Screens(ts_showscreens)
            "Папа ухмыляется и отвечает тем же ходом пешки, правда, только на одну клетку."
            $ TS.Screens(ts_hidescreens)
            " {w=1.0}{nw}"

            show chess2 at ts_chess_move_down
            pause 0.5
            hide chess2 with dissolve

            show chess3 at ts_chess_move_up
            pause 1
            $ TS.Screens(ts_showscreens)
            "В детстве я сразу выпускала ферзя на прогулку, прямо как папа."
            "Но с течением лет, начитавшись всяких шахматных книжек и посмотрев несколько видеоуроков по шахматам, я знаю, что, чем рано выпускать ферзя, лучше поставить вторую пешку в центр."

            $ TS.Screens(ts_hidescreens)
            " {w=1.0}{nw}"

            show chess3 at ts_chess_move_down
            pause 0.5
            hide chess3 with dissolve

            show chess4 at ts_chess_move_up
            pause 1
            $ TS.Screens(ts_showscreens)

            show hiroto 1s at f41
            "Папа же, по всей видимости, до сих пор не знает этого простого правила, поэтому тут же выпускает ферзя."

            $ TS.Screens(ts_hidescreens)
            " {w=1.0}{nw}"

            show chess4 at ts_chess_move_down
            pause 0.5
            hide chess4 with dissolve

            show chess5 at ts_chess_move_up
            pause 1
            $ TS.Screens(ts_showscreens)

            if chess_tutor == True:
                show monika 2b at rn44
                cm "Ферзь - это очень сильная фигура. Она может ходить и по горизонтали, и по вертикали, и по диагонали."
                cm 3i "Однако, ферзя нужно очень сильно оберегать, потому что он только один. И выводить его рано лучше не стоит. По крайней мере, пока не развились кони и слоны."
                $ TS.Screens(ts_hidescreens)
                " {w=1.0}{nw}"
                show monika at ron44
                pause 0.5
                hide monika with dissolve
                $ TS.Screens(ts_showscreens)
            ts_ft 2z1 "Ну что, сдаёшься?"
            show hiroto 2r at t41
            m "Ха! И не мечтай!"
            "После этого я уверенно задвигаю пешку ещё на одну клетку, попутно атакуя ферзя."

            $ TS.Screens(ts_hidescreens)
            " {w=1.0}{nw}"

            show chess5 at ts_chess_move_down
            pause 0.5
            hide chess5 with dissolve

            show chess6 at ts_chess_move_up
            pause 1
            $ TS.Screens(ts_showscreens)

            "Однако шахматы - это пошаговая игра, здесь нет такого, чтобы сделать два хода одним цветом подряд."
            show hiroto 1s at s41
            "Поэтому он с лёгкостью отводит ферзя в безопасность."

            $ TS.Screens(ts_hidescreens)
            " {w=1.0}{nw}"

            show chess6 at ts_chess_move_down
            pause 0.5
            hide chess6 with dissolve

            show chess7 at ts_chess_move_up
            pause 1
            $ TS.Screens(ts_showscreens)

            "У меня козыри в рукаве закончились, поэтому я возвращаюсь к изначальному плану развития и просто вывожу коня."

            $ TS.Screens(ts_hidescreens)
            " {w=1.0}{nw}"

            show chess7 at ts_chess_move_down
            pause 0.5
            hide chess7 with dissolve

            show chess8 at ts_chess_move_up
            pause 1
            $ TS.Screens(ts_showscreens)

            if chess_tutor == True:
                show monika 4b at rn44
                cm "Кстати, о конях. Конь - это самая сложная непредсказуемая фигура в шахматах."
                cm "Это единственная из всех фигур, которая может перепрыгивать через другие фигуры."
                cm "Так что даже мастера игры, которые играют всю жизнь, и на эту самую жизнь шахматами и зарабатывают, если у них мало времени на часах, иногда забывают о том, что конь так может."
                cm "А ходит он так, что, по сути, это напоминает букву Г: две клетки в одном из любых четырёх направлений по прямой, а затем ещё одна клетка в направлении, перпендикулярном изначальному."
                cm 2k "Например, на этом ходу Моника походила конём с клетки g1 на клетку f3: по сути, она сходила на две клетки по вертикали g, перепрыгивая пешку, а затем допрыгнула на соседнюю вертикаль f."
                $ TS.Screens(ts_hidescreens)
                " {w=1.0}{nw}"
                show monika at ron44
                pause 0.5
                hide monika with dissolve
                $ TS.Screens(ts_showscreens)
            show hiroto 1a at t41
            "У папы, по всей видимости, козыри тоже закончились (если они у него вообще есть), поэтому он просто выдвинул слона на одну клетку."

            $ TS.Screens(ts_hidescreens)
            " {w=1.0}{nw}"

            show chess8 at ts_chess_move_down
            pause 0.5
            hide chess8 with dissolve

            show chess9 at ts_chess_move_up
            pause 1
            $ TS.Screens(ts_showscreens)

            if chess_tutor == True:
                show monika 2b at rn44
                cm "Слоны двигаются только по диагонали."
                cm 2d "А учитывая, что на старте у тебя есть два слона на разных цветах (c1/f1 и с8/f8 соответственно), и что клетки по диагонали одного и того же цвета..."
                cm 3l "Различают белопольного и чернопольного слона."
                cm 1d "Слоны, наряду с конями - это лёгкие фигуры. Ферзь и ладьи, напротив, считаются тяжёлыми фигурами."
                cm 3i "Номинально слон и конь стоят одинаково, по три очка. Однако, считается, что слон немного, но лучше коня, потому что он дальнобойный."
                cm 3l "Впрочем, играть со слонами или с конями - это сугубо дело вкуса каждого. Иной раз какой-то мастер может легко победить среднего игрока."
                cm "Даже несмотря на то, что у мастера два коня, а у среднего игрока - два слона, и номинально у среднячка фигуры лучше, чем у мастера."
                $ TS.Screens(ts_hidescreens)
                " {w=1.0}{nw}"
                show monika at ron44
                pause 0.5
                hide monika with dissolve
                $ TS.Screens(ts_showscreens)
            "Я продолжаю выстраивать своё развитие, и играю ещё одним конём."

            $ TS.Screens(ts_hidescreens)
            " {w=1.0}{nw}"

            show chess9 at ts_chess_move_down
            pause 0.5
            hide chess9 with dissolve

            show chess10 at ts_chess_move_up
            pause 1
            $ TS.Screens(ts_showscreens)

            "Папа же начинает атаковать исподтишка, и выводит пешку на одну клетку, чтобы я её побила."

            $ TS.Screens(ts_hidescreens)
            " {w=1.0}{nw}"

            show chess10 at ts_chess_move_down
            pause 0.5
            hide chess10 with dissolve

            show chess11 at ts_chess_move_up
            pause 1
            $ TS.Screens(ts_showscreens)

            if chess_tutor == True:
                show monika 2b at rn44
                cm "Шахматы - это не шашки. «Съедать» фигуры здесь вовсе необязательно, если видишь ход получше."
                cm 4b "Иногда пешки могут держать в напряжении друг друга даже не один десяток ходов."
                $ TS.Screens(ts_hidescreens)
                " {w=1.0}{nw}"
                show monika at ron44
                pause 0.5
                hide monika with dissolve
                $ TS.Screens(ts_showscreens)
            "Однако я не ведусь на этот дешёвый фокус, и вместо этого вывожу слона, объявляя шах."

            $ TS.Screens(ts_hidescreens)
            " {w=1.0}{nw}"

            show chess11 at ts_chess_move_down
            pause 0.5
            hide chess11 with dissolve

            show chess12 at ts_chess_move_up
            pause 1
            $ TS.Screens(ts_showscreens)

            if chess_tutor == True:
                show monika 2b at rn44
                cm "Цель игры - объявить шах и мат королю. Мат - это когда у короля нет ни одной свободной клетки, куда он мог бы наступить, чтобы его впоследствии не «съели»."
                cm "Шах же, в свою очередь, скорее означает, что короля нужно срочно куда-то ретировать."
                cm 4b "Есть несколько вариантов защититься от шаха: либо походить самим королём, либо перекрыть клетку, по которой его «простреливают», либо просто съесть саму фигуру, которая объявила шах."
                cm 2i "Но учти, что шах в большинстве случаев никоим образом не приближает тебя к победе. Раздражают ли постоянные шахи? Да. Приближают ли они тебя к мату? Нет."
                cm "Поэтому, делать шах можно, только если он безопасен для всех твоих фигур, и при шахе ты не подставляешь ни одну из них. В противном случае шах давать всё же не стоит."
                $ TS.Screens(ts_hidescreens)
                " {w=1.0}{nw}"
                show monika at ron44
                pause 0.5
                hide monika with dissolve
                $ TS.Screens(ts_showscreens)
            show hiroto 1s at f41
            "Папа просто спокойно подводит пешку, тем самым атакуя моего слона."

            $ TS.Screens(ts_hidescreens)
            " {w=1.0}{nw}"

            show chess12 at ts_chess_move_down
            pause 0.5
            hide chess12 with dissolve

            show chess13 at ts_chess_move_up
            pause 1
            $ TS.Screens(ts_showscreens)

            ts_ft 1t "Что, победить хочешь?"
            extend 1z1 " Ну, в другой раз."

            $ TS.Screens(ts_hidescreens)
            " {w=1.0}{nw}"

            play sound2 pageflip
            scene ts_kitchen
            show hiroto 1s at i41
            with wipeleft_scene

            show chess14 at ts_chess_move_up
            pause 1
            $ TS.Screens(ts_showscreens)

            "Так продолжалось уже некоторое время."
            "Поскольку мы не на корову играем, а просто забавы ради, шахматного таймера у нас тоже нет."
            "Впрочем, он не особо и не нужен - папа ходит достаточно быстро, ну а я с детства привыкла уже долго не засиживаться на одном месте."
            "Может, привычка?.."
            em "А может, болезнь, о которой ты так и не говоришь родителям..."
            "«Просто дай мне спокойно поиграть! Мы с папой и так очень давно не играли, а тут ещё ты мешаешь!»"
            em "Всё, молчу, молчу..."
            "..."
            "Уже вовсю идёт миттельшпиль. А у меня тем временем всё меньше вариантов, как же походить, чтобы при этом глупо не подставиться."
            "Хотя сейчас ходит папа, я уже заранее думаю, как же я ему отвечу."
            "Папа, недолго думая, просто съедает моего коня в ответ."

            $ TS.Screens(ts_hidescreens)
            " {w=1.0}{nw}"

            show chess14 at ts_chess_move_down
            pause 0.5
            hide chess14 with dissolve

            show chess15 at ts_chess_move_up
            pause 1

            if chess_tutor == True:
                $ TS.Screens(ts_showscreens)
                show monika 2b at rn44
                cm "Хотя ходят пешки по прямой, съедают они другие фигуры и пешки на одну клетку по диагонали вверх (или вниз, если играть чёрными)."
                $ TS.Screens(ts_hidescreens)
                " {w=1.0}{nw}"
                show monika at ron44
                pause 0.5
                hide monika with dissolve
            play sound2 pageflip
            scene ts_kitchen
            show hiroto 1b1 at i41
            with wipeleft_scene

            show chess16 at ts_chess_move_up
            pause 1
            $ TS.Screens(ts_showscreens)

            m "Что, уже не настолько уверен в себе?"
            "У меня две лишние пешки, да ещё и одна из моих пешек в шаге от того, чтобы стать вторым ферзём!"
            if chess_tutor == True:
                show monika 2b at rn44
                cm "Помимо прочих свойств, у пешек есть ещё одно: когда она достигает другого конца доски, она может превратиться в любую из фигур. Кроме короля, конечно же."
                cm 4b "Многие игроки зачастую выбирают ферзя, потому что это самая сильная фигура, и с двумя ферзями проигрыш почти что невозможен."
                cm 2d "Однако, есть большое количество этюдов и задачек, которые как раз построены на том, чтобы превратить пешку в фигуру, но не в ферзя, а, например, в коня или ладью."
                $ TS.Screens(ts_hidescreens)
                " {w=1.0}{nw}"
                show monika at ron44
                pause 0.5
                hide monika with dissolve
                $ TS.Screens(ts_showscreens)
            ts_ft 2y "Да ты погоди, ещё не вечер же..."

            $ TS.Screens(ts_hidescreens)
            " {w=1.0}{nw}"

            play sound2 pageflip
            scene ts_kitchen
            show hiroto 1b1 at i41
            with wipeleft_scene

            show chess17 at ts_chess_move_up
            pause 1
            $ TS.Screens(ts_showscreens)

            ts_ft 1z1 "Что, уже не настолько уверена в себе?"
            show hiroto 1r at f41
            "Как же всё перевернулось с ног на голову..."
            "За несколько ходов я потеряла коня, ладью и пару пешек."
            "Папа же, напротив, собрался, не потерял вообще ничего, да и вообще позиция, как мне кажется, теперь глубоко в его пользу..."
            "Я в отчаянии пытаюсь съесть хоть одну пешку."

            $ TS.Screens(ts_hidescreens)
            " {w=1.0}{nw}"

            show chess17 at ts_chess_move_down
            pause 0.5
            hide chess17 with dissolve

            show chess18 at ts_chess_move_up
            pause 1
            $ TS.Screens(ts_showscreens)

            if chess_tutor == True:
                show monika 2b at rn44
                cm "Наконец, поговорим о ладьях."
                cm "Ладьи - это такие тугие бронебойные фигуры, которые ходят только по вертикали или по горизонтали на любое количество клеток."
                cm 3l "Если, конечно, у них на пути не стоят другие фигуры..."
                cm 4b "Ладьи невероятно полезны в эндшпилях, однако, доживают они до него не всегда, а когда на доске ещё много фигур, они ещё и очень неповоротливы."
                $ TS.Screens(ts_hidescreens)
                " {w=1.0}{nw}"
                show monika at ron44
                pause 0.5
                hide monika with dissolve
                $ TS.Screens(ts_showscreens)
            "Папа, недолго думая, провёл слона, делая вилку на моего короля и мою ладью."
            stop music fadeout 3

            $ TS.Screens(ts_hidescreens)
            " {w=1.0}{nw}"

            show chess18 at ts_chess_move_down
            pause 0.5
            hide chess18 with dissolve

            show chess19 at ts_chess_move_up
            pause 1
            $ TS.Screens(ts_showscreens)

            if chess_tutor == True:
                show monika 2b at rn44
                cm "Вилка - это ситуация в шахматах, где одна твоя фигура атакует сразу несколько фигур соперника."
                cm 2l "Лучше всего в вилках показывают себя кони. Это, кстати, возвращаясь к моему монологу об условной игре между мастером с двумя конями и средняком с двумя слонами."
                cm 2b "Но все фигуры могут сделать вилку! Даже пешка и даже король - то, что они ходят только на одну клетку, не означает, что вилку этими фигурами сделать нельзя."
                $ TS.Screens(ts_hidescreens)
                " {w=1.0}{nw}"
                show monika at ron44
                pause 0.5
                hide monika with dissolve
                $ TS.Screens(ts_showscreens)
            "После этого хода я сразу сдаюсь."

            $ TS.Screens(ts_hidescreens)
            " {w=1.0}{nw}"

            show chess19 at ts_chess_move_down
            pause 0.5
            hide chess19 with dissolve

            show hiroto 1r at t11

            $ TS.Screens(ts_showscreens)

            m "Всё, сдаюсь. Доволен?"
            "Я говорю это слегка дерзким, но в целом весёлым тоном, чтобы он не думал, что я это серьёзно."

            $ TS.Screens(ts_hidescreens)
            " {w=1.0}{nw}"

            play music ts_afterword

            $ TS.Screens(ts_showscreens)

            nvl clear
            nvlbazar "{font=[ts_nvl_font2]}В конце концов, это же всего лишь игра."
            nvlbazar "{font=[ts_nvl_font2]}Да и я уже давно не ребёнок, чтобы после проигранной игры швыряться всеми фигурами, «объявляя ничью»."
            nvlbazar "{font=[ts_nvl_font2]}И хоть проигрывать я до сих пор не люблю, повзрослев, я осознала, что постоянно выигрывать не получится, и что надо бы иногда и проигрывать."
            nvlbazar "{font=[ts_nvl_font2]}Причём проигрыши эти зачастую будут выше твоих сил."
            nvlbazar "{font=[ts_nvl_font2]}А иногда, как бы ты ни старалась, победить соперника ну никак не получается."
            nvlbazar "{font=[ts_nvl_font2]}Поэтому я могу лишь с достоинством принять поражение, принять это, и жить дальше."

            $ TS.Screens(ts_hidescreens)
            nvlbazar " {w=1.0}{nw}"

            nvl clear

            $ TS.Screens(ts_showscreens)

            ts_ft 1z1 "Да. Доволен."
            ts_ft 1c "Ты к себе пойдёшь?"
            show hiroto 1e at f11
            m "Да... От шахмат просто мозги вскипели..."
            ts_ft 1b "Не у тебя одной."
            ts_ft 1g "Давненько мы уже с тобой не играли, а кроме тебя, мне даже и играть не с кем..."
            "Мы оба с этого посмеялись."
            show hiroto 1f at t11
            m "Да... к тому же, я же вчера не в мягкой постели спала, а на полу."
            m "Что-то... устала я. Пойду полежу. Может, подремаю часик."
            ts_ft 1g "Давай тогда, до вечера. Люблю тебя, солнце."
            show hiroto 1f at t11

            stop music fadeout 3

            m "И я люблю тебя, пап."
            show hiroto at cright with move
            hide hiroto
            "После этого я отправилась к себе, а папа ушёл смотреть телевизор. Там крутят какую-то очередную политическую передачу. Или новости. Честно, я их не различаю..."
        "Сразу пойти к себе":
            stop music fadeout 3
            hide zatemnenie with dspr
            $ TS.Screens(ts_showscreens)
            m "Что-то мне нездоровится, пап. Пойду всё-таки к себе."
            ts_ft 1h "Как знаешь..."

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"
    play sound2 pageflip
    scene ts_bedroom
    with wipeleft_scene
    play music ts_dreams
    $ TS.Screens(ts_showscreens)

    "Как же я устала..."
    "Вроде и середина дня, я должна быть в самом разгаре бодрствования..."
    "А меня рубит капитально."
    "Может, это всё последствия того самого похмелья?"

    show monika 2bn at ln11

    $ pps = 3
    $ TS.Screens(hpunch)

    em "И не говори... Я сама хоть и не пила вчера, но чувствую себя немногим лучше..."

    show monika 2bm at f11

    m "Господи, ты так и будешь так внезапно появляться? Меня же в один момент инфаркт хватит!"
    em 2bl "А ты так и будешь забывать о том, что я тебе говорила пятнадцать минут назад?"
    em 1bb "Говорю же, без посторонних мы можем совершенно свободно разговаривать."
    em 1bl "Главное, чтобы папа в случайный момент не зашёл посреди того, как ты на меня орёшь. Вот умора будет..."

    show monika 2bj at t11

    $ pps = 1

    m "..."
    m "Ну, с другой стороны, хоть с умным человеком поговорю..."

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"
    play sound2 pageflip
    scene ts_darkbed
    show monika 2bb at i11
    with wipeleft_scene

    $ TS.Screens(ts_showscreens)

    em "Зна-а-ачит... Что делать собираешься?"

    show monika 2ba at f11

    m "Не знаю..."
    m "Вариант один: вырубиться, потому что на полу спать, мягко говоря, было неудобно."

    show monika 1be at t11

    m "Сайори, конечно, подложила матрас, подушку, и укрыла меня одеялом потеплее, но всё равно я чувствую, будто не выспалась."

    show monika 3bh at f11

    m "И желательно уснуть, проснуться, а тебя здесь больше не будет."
    em 3bi "Ты такие вещи не говори."
    em "Сама же сказала, хоть с умным человеком поговоришь."
    em 2br "Возможно, даже с человеком умнее тебя..."

    stop music fadeout 3

    show monika 2bq at t11

    m "...ладно..."
    em 2bn "Вот так-то гораздо лучше."
    em 2bi "Кстати..."

    play music audio.t4

    extend 4bk " Что-то ты не писала ничего уже давненько, ты так не думаешь?"

    show monika 2bj at s11

    "Я пытаюсь огрызнуться в ответ, но затем внезапно понимаю, что моя шизофрения так-то права."
    "Что же я за президент {i}Литературного{/i} клуба, который уже сто лет как ничего ни писал, ни читал?"

    if unluck4_reading == True:
        "Нет, справедливости ради, читала-то я как раз недавно... Из-за этого я вчера даже в школу конкретно опоздала..."
        "Но это не отменяет того факта, что я уже давно ничего своего не писала."

    "Причём писать-то я умею, и пишу довольно хорошо."
    "Правда, все мои стихотворения были на английском, но ничего же не мешает попробовать переступить через себя и написать на родном?"
    "Даже если я этого уже давно не делала..."

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    show monika at cright with move
    hide monika

    scene ts_notebook with pushleft

    $ TS.Screens(ts_showscreens)

    "Та-а-ак... Ну, приступим..."

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    pause 2.5

    $ TS.Screens(ts_showscreens)

    "Спустя где-то минут десять кропотливой работы я рождаю следующее."

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    $ TS.Screens(ts_null_transform)
    call showpoem (poem_test, img="monika 2bn") from _call_showpoem

    $ TS.Screens(ts_showscreens)

    em "Ого, ты написала целый стих про меня..."
    em "Спасибо, конечно, я очень тронута, но... не стоило..."

    show monika 1bm at s11

    m "Да заткнись уже!.. Это... Совсем не о тебе..."
    em 2bl "Правда? А о ком тогда?"

    show monika 2bj at t11

    m "Не о ком, а о чём. Девочка символизирует внутренний мир, который другим недоступен."
    m "Солнце с другой стороны символизирует секреты, которые доступны только тебе самой."
    m "А раскопки - ну, знаешь фразу «копаться в себе»?"
    em 2bd "Знаю."
    em 2bk "Это же, по сути, то, чем ты и занимаешься на протяжении... Сколько там тебе лет?"
    em 3bb "В общем, занимаешься ты этим всю жизнь с тех самых пор, как себя осознала."

    show monika 2bj at h11

    $ TS.Screens(vpunch)

    m "Знаешь, что!.."

    "В пылу я пытаюсь ударить её, но затем резко охлаждаюсь."
    "С другой стороны, а {i}что{/i} она должна знать? Она же не чужой человек. Она, по сути, и есть часть меня."
    "Да и тем более, если посмотреть на меня со стороны, то через полчаса у моего дома уже будут санитары психиатрической лечебницы..."

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"
    play sound2 pageflip
    scene ts_darkbed
    show monika 2bo at i11
    with wipeleft_scene

    $ TS.Screens(ts_showscreens)

    "Ладно. Что-то я на самом деле устала..."
    em 2bn "Да и я что-то тоже..."

    show monika 2bm at s11

    m "Ты что, и мои мысли читать будешь?"
    em 3bi "Я же твоё подсознание, забыла уже опять?"
    em "Я, по сути, и есть твои мысли."
    em 2bm "Может, немного извращённые... "
    extend 1bi "Но это {i}твои{/i} мысли."

    show monika 1bh at t11

    m "Х-х-х..."
    m "А можно мне от тебя избавиться, чтобы ты снова была максимум голосом в моей голове, который я не слушаю?"
    em 2bk "Нельзя! Терпи дальше."

    show monika 1bj at s11

    m "..."
    m "Ладно. Пойду всё-таки спать. Надеюсь, что ты всё-таки настолько же внезапно исчезнешь, как и появилась."
    em 1bi "Не надейся."
    em 4bb "Ну а насчёт того, чтобы поспать - это идея здравая."
    em 1bn "Приятных сновидений, что ли..."

    show monika 1bm at t11

    m "Вот уж спасибо..."
    m "Никогда бы не подумала, что желать спокойных снов мне будет моё раздвоение личности."
    em 2bd "Эй-эй, забыла? У тебя не раздвоение, и не шизофрения. Я всего лишь твоё подсознание."

    show monika 1ba at s11

    m "Да-да..."

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    show monika at cright with move
    hide monika

    $ TS.Screens(ts_showscreens)

    "С этими словами я подготавливаюсь ко сну."
    "Действительно, сон на своей кровати куда лучше сна на полу."
    "Сайори, конечно, молодец, и постаралась, чтобы молодой алкоголичке вроде меня было комфортно, но свою кровать я ни на что не поменяю."
    "Как говорится, в гостях хорошо, а дома лучше."

    show blink

    "«Интересно, как же я буду спать в университете? В общежитиях кровати не сильно-то лучше пола...»"
    "«Хотя, может, родители снимут мне квартиру на время обучения...»"
    "Додумать мысль о спальном месте я не успела. Я провалилась в сон."

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    return