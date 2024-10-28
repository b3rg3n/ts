label ts_scenario_6:

    show layer screens at ts_null_transform

    $ renpy.block_rollback()

    python: # ОБНОВЛЯЕМ RPC
        ts_rpc_carter6()

    $ persistent.rpclabel = "6"
    $ persistent.uncolorize = "none"
    $ persistent.sprite_time = "day"
    $ persistent.carter2menu = True
    $ persistent.carter3menu = False
    $ persistent.badendmenuperedglitch = False
    $ persistent.badendmenuskipglitch = False
    $ persistent.badendmenu = False
    $ persistent.goodendmenu = False
    $ persistent.peredbadendmenu = False
    $ persistent.peredgoodendmenu = False

    if _preferences.language == "english":
        $ save_name = "Broadening horizons"
    else:
        $ save_name = "Новые начинания"

    play sound chp2
    if _preferences.language == "english":
        $ Chapter("ACT TWO")
        $ Chapter("ACT TWO")
        $ Chapter("chapter two")
        $ Chapter("chapter two")
        $ Chapter("Broadening horizons")
        stop sound fadeout 7
        $ Chapter("Broadening horizons")
    else:
        $ Chapter("АКТ ВТОРОЙ")
        $ Chapter("АКТ ВТОРОЙ")
        $ Chapter("Глава вторая")
        $ Chapter("Глава вторая")
        $ Chapter("Новые начинания")
        stop sound fadeout 7
        $ Chapter("Новые начинания")


    play sound ts_alarm fadein 2

    pause 2

    scene ts_bedroom
    show unblink
    show layer master at ts_vstavai_shashlik
    pause 3
    play sound svet_on
    pause 1.5

    show layer screens at ts_showscreens

    play music audio.okevrmon fadein 4

    "На часах обычные и привычные семь утра. А на календаре понедельник."
    "Нет, я не проснулась только что, и не спала все оставшиеся выходные."
    "Просто остаток выходных был скучным до невозможности."
    if act2_chess == True:
        "В субботу, после позора в шахматах и крайне двусмысленного стиха, я поспала, поужинала с папой, а затем провела вечер с ним, пялясь в телевизор."
    else:
        "В субботу, после крайне двусмысленного стиха, я поспала, поужинала с папой, а затем провела вечер с ним, пялясь в телевизор."
    "В воскресенье, когда уже всё вернулось к привычному ритму жизни, папа приготовил завтрак, который снова был скорее рассчитан на него одного."
    "Ну неужели с первого раза не понятно, что молочку я не ем?!"
    "Но ничего. Сегодня понедельник. Сегодня готовлю я. И сегодня я приготовлю {i}себе{/i}, что захочу."
    "Ну и папе, может, что-то достанется."
    "Но для начала ещё нужно умыться."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_bathroom
    with wipeleft_scene

    show layer master at ts_clean_eblet
    pause 2
    play sound open_water_sink
    pause 0.5
    stop sound
    play sound_loop water_sink_stream
    pause 1
    play sound water_splash
    pause 1.6
    stop sound_loop
    play sound close_water_sink
    pause 0.5

    show layer screens at ts_showscreens

    m "Бр-р-р..."

    show monika 1bl at ln11

    em "А говорила, что умываешься холодной водой всю жизнь."

    show monika 1bj at s11

    "За эти выходные мы с моим... моей... в общем, чем-то, тоже сдружились."
    "Или, скорее, не то чтобы сдружились, но, по крайней мере, стали ладить лучше."
    "И я даже перестала пугаться каждый раз, когда он... она... оно... в общем, внезапно появляется."

    show monika 1bd at t11

    em "Я тебе уже кучу раз говорил... говорила... говорило... что я – это и есть ты."
    em 2bd "Но если ты всё-таки хочешь использовать всякие модные местоимения, которые в последнее время стали отдельной темой для беседы, используй {i}она/её{/i}."

    show monika 1ba at s11

    m "Ладно..."
    m "А от холодной воды я морщусь, кстати, потому что каждый раз как первый."
    m "Тебе вот будет приятно, если на тебя ведро ледяной воды выльют?"

    show monika 3bk at t11

    em "Да не кипятись ты так..."
    em 2bd "Во-первых, я просто спросила это, чтобы начать разговор."
    em 4bb "А во-вторых, я это и без тебя прекрасно знаю!"

    show monika 3bj at s11

    m "Х-х-х..."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_gost
    with wipeleft_scene

    play sound pageflip
    scene ts_kitchen
    with wipeleft_scene

    show layer screens at ts_showscreens

    "Та-а-ак, посмотрим..."
    "..."
    "Чёрт. Самое сложное в готовке – это выбрать, что именно ты будешь готовить."
    "Может, гречку?.."

    if unluck4_cooking == True:
        "Хотя, я ведь только пару дней назад её ела..."
        em "А потом ты в школу капитально опоздала."
        em "А ещё потом ты так же капитально напилась."
        em "Так что лучше не стоит."
        m "А что тогда?!"
    else:
        "Хотя, нет..."

    stop music fadeout 4

    "Выбирать было особо не из чего. Поэтому выбор снова пал на хлопья с молоком и кофе."

    if unluck3 == True:
        "Позор с жареной картошкой всё не выходит у меня из головы."
        "Слышишь? Убирайся из моей головы!"
        em "Это чуть попозже будет..."
        m "Что?"
        em "Да так, неважно..."
        "О чём я говорила?..{w=1} Хлопья с молоком и кофе, да."

    "В детстве я очень любила молоко. Настоящее, только сдоенное с коровы, и чуть-чуть подержанное в холодильнике."
    "Но тёплое молоко я не любила и не люблю до сих пор. Даже с вышеупомянутым кофе."

    play music audio.t6
    show hiroto 1a at ln11

    "Пока я размышляла о молоке, вместо того, чтобы готовить, в комнату зашёл папа. Уже полностью одетый, который только и ждёт, чтобы его накормили и отправили на работу."

    ts_ft 1b "Доброе утро, солнце!"

    show hiroto 1a at s11

    m "Утречка, пап."
    ts_ft 1b "Что на завтрак?"

    show hiroto 1f at t11

    m "Я, э-э-э... не придумала ещё. Пока просто хлопья с молоком и кофе для нас обоих."
    ts_ft 1c "Знаешь... Хлопья с молоком – это, конечно, вкусно, но это не самая питательная пища."
    ts_ft 1g "Напомни мне на неделе, чтобы я научил тебя варить хотя бы те же крупы или макароны."

    show hiroto 1f at s11

    m "Пап, да я и так это всё умею... Я просто не успела сообразить что-то на сегодняшний завтрак."
    ts_ft 1u "Ну, для тебя же лучше... В университете на одних хлопьях далеко не уедешь!"

    show hiroto 1s at t11

    "Я хотела возразить ему, что, скорее всего, в университете будет что-то вроде столовой, в которой профессионалы своего дела за сдельную плату организуют всё тебе по высшему разряду, но не стала."
    "В конце концов, я же на самом деле умею варить ту же гречку или макароны, а это уже открывает окно для возможностей. Добавить тот же шпинат, и вот тебе приемлемый ужин."

    ts_ft 1c "Ну, в любом случае, я лучше бутербродами перебьюсь. Они {i}питательнее{/i}, в конце концов."


    show hiroto 1e at s11

    stop music fadeout 2

    "Он язвительно сделал акцент на слове «питательнее»."

    show hiroto at cright with move
    hide hiroto

    $ currentpos = get_pos()
    $ audio.t6o =  '<from ' + str(currentpos) + ' loop 10.893>mod_assets/source/audio/ost/orig/6o.ogg'

    play music audio.t6o fadein 2

    "Он идёт к хлебнице над холодильником и отрезает три кусочка хлеба."
    "Затем он берёт из холодильника колбасу и сыр, и аккуратными ломтиками кладёт по паре кусочков на каждый ломтик хлеба."
    "Тем временем я сыплю хлопья и заливаю их молоком, а потом ставлю чайник кипятиться."
    "Я где-то читала, как некоторые сначала заливают молоко, а уже в него насыпают хлопья. Больные ублюдки."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_kitchen
    with wipeleft_scene

    show layer screens at ts_showscreens

    stop music fadeout 3

    "Когда чайник закипел, я разливаю кофе по чашкам, и начинаю есть хлопья."
    "Нет, кофе тоже можно поставить, но он всё равно ещё очень горячий, а в условиях не самого большого стола, есть риск, что мой кофе просто разольётся."

    "Поэтому пусть лучше стоит на большом столе, вдали от моих или папиных рук."

    $ audio.t6 =  '<from ' + str(currentpos) + ' loop 10.893>mod_assets/source/audio/ost/orig/6.ogg'
    play music audio.t6 fadein 2

    show hiroto 1a at rn11

    "Папа тем временем начинает пить кофе с бутербродами."
    "Он также заблаговременно сделал ещё парочку, чтобы съесть их на обеде."
    "В те времена, когда мама дома, на работу его готовит именно она."
    "Однако, когда мама в командировке, он не брезгует подготовиться к очередному рабочему дню и сам."
    "Кстати, об этом..."


    m "Ну что, пап, какие планы на день?"
    ts_ft 2g "Обычно этот вопрос задаю сначала я."
    ts_ft "Но, раз уж спросила... Поскольку я {i}починил{/i} машину, я, во-первых, проведу чуть больше времени с тобой перед отъездом..."

    stop music fadeout 3

    ts_ft 1c "А во-вторых, ну-у-у... поработаю, да. У меня на повестке дня несколько судов, поэтому починил я машину очень вовремя."
    ts_ft "Идти пешком или на общественном транспорте в разные концы города – задача не из самых лёгких."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play music ts_dist fadein 3
    scene ts_kitchen at ts_fon_blur_postepenno
    show hiroto 1a at s11

    show overlay aw_memory_back_1
    show layer master at VHS(0.83, 0.83, 0.77, 1.0)
    with dissolve2

    show layer screens at ts_showscreens

    "Папа у меня – обычный рядовой госслужащий. Знаете, не из тех, чтобы жить в десяти квартирах, записанных на всех его родственников, но на жизнь мы всё равно не жалуемся."
    "Особенно с учётом того, что мама у меня тоже работает на довольно высокооплачиваемой работе."
    "Хотя, если спросить меня в любое время, а кем работают мои родители, я напрочь забываю всё."
    "Нет, я, конечно, знаю, что папа работает где-то в отделе опеки нашего города, а мама что-то там проектирует для каких-то космических кораблей... Но не более того."
    "Отсюда, кстати, и тот факт, что она постоянно в командировках, в том числе и заграничных."

    stop music fadeout 4

    "Но, несмотря на то, что она зарабатывает на порядок больше папы, он на жизнь тоже не жалуется."
    "Он как-то несколько раз, ещё давно, говорил мне нечто вроде: «У меня есть твоя мама, у меня есть ты, у меня есть работа, а сколько на ней платят – это уже дело десятое»."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"
    play sound wakeup
    pause 1.3

    scene ts_kitchen 
    show hiroto 1a at i11
    with vpunch

    show layer screens at vpunch
    ts_ft 2q "..ика!"

    show hiroto 1p at t11

    m "Ой!"

    "От неожиданности я аж поперхнулась кофе. Хорошо хоть не разлила его."

    ts_ft 1h "Ты ещё не проснулась до конца или что?"

    show hiroto 1j at s11

    m "А... Да нет, просто задумалась..."

    play music audio.t2 fadein 2

    ts_ft 1h "Я говорю, а у тебя какие планы?"

    show hiroto 1j at t11

    m "Да... вроде тоже как обычно, школа, клуб, домой."
    m "Правда, до фестиваля всего неделя осталась, а Литературный клуб к нему совершенно не готов, нужно срочно придумывать {i}хоть что-то{/i}."

    "А с учётом того, как мы думали с Сайори по поводу того, как бы нам привлечь новых участников где-то с месяц назад, что-то мне подсказывает, что ничем хорошим это не кончится..."

    show hiroto 1f at s11

    m "Правда, есть у меня одна идейка, как бы нам разнообразить времяпрепровождение в клубе... Но пока это секрет!"
    ts_ft 1g "Ну вот и хорошо, пора бы и проявить свои президентские качества."
    ts_ft 1h "А то всё время делегируешь полномочия другим, и в итоге всю работу за тебя выполняет... напомни, как зовут ту девочку с длинными волосами?"

    show hiroto 1j at t11

    m "Юри."

    show hiroto 1f at f11

    m "И вообще, знаешь... ты прав. Пора бы и мне самой сделать или придумать хоть что-то, а то плохой из меня лидер получается."
    em "Может, именно за это тебя выперли из Дискуссионного клуба?"

    stop music fadeout 2

    "«Да не выперли меня, я сама оттуда ушла.»"

    play music audio.t2g2 fadein 2

    em "Ну ладно, ты {i}сама ушла{/i} из Дискуссионного клуба, потому что ты плохой лидер, и не можешь справиться хотя бы с десятком подчинённых."
    em "Хорошо хоть в Литературном клубе, помимо тебя, только три человека, но я в любом случае не думаю, что после фестиваля люди придут из-за твоих «лидерских качеств»."
    em "Они скорее придут из-за того, что вы все милые девочки, и одна из них к тому же довольно популярная."
    em "Но они не проведут под твоим начальством и недели, как только они узнают, что лидер ты на самом деле совершенно бездарный."
    em "И вообще...{nw}"

    stop music
    play sound stol_udar


    m "Да заткнись ты уже!" with vpunch

    show hiroto 1o at t11

    show layer screens at vpunch
    ts_ft "Прошу прощения?!"

    show hiroto 1p at t11

    m "Извини, пап... я не тебе..."
    em "Видишь? Я же говорила, говорила!"

    show layer screens at vpunch
    em "Ты не только бездарная, но ещё и неуравновешенная!"

    show hiroto 1q at t11

    ts_ft "А кому тогда?"

    show hiroto 1p at t11

    m "..."
    m "...н-никому. Прости, пап..."

    play music audio.t8 fadein 3

    ts_ft 1h "Моника, с тобой всё хорошо?"

    show hiroto 1j at t11

    m "Н-ну... да?"

    "Хвала богам, что папа сегодня не настойчивый, поэтому он просто сказал:"

    ts_ft 1a2 "Ну ладно..."
    ts_ft 1y "Так что там по поводу клуба?"

    show hiroto 1s at t11

    m "Говорю же, се-к-рет!"

    "Сказав это, мы оба заканчиваем свои завтраки и ставим посуду в мойку."
    "Часы тем временем показывают уже восемь."
    "До школы ещё полчаса. Если идти медленным шагом, то минут за пятнадцать управлюсь. Может, даже на лавочке немного отдохну."

    m "Пап, мы часом выходить не собираемся?"
    ts_ft 1c "Ну, если хочешь, то можешь выходить сейчас. Я чуть попозже выйду, минут через десять."

    show hiroto 1a at t11

    m "Ну, тогда... До вечера, пап!"
    ts_ft 1g "До вечера, Моника. Люблю тебя."

    show hiroto 1f at t11

    stop music fadeout 3

    "Видно, что он уже не обижается, и списал недавнюю выходку на рудименты моего переходного периода."

    m "И я тебя люблю, пап."

    "После этих слов я выхожу."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_house
    with wipeleft_scene

    play sound pageflip
    scene ts_street
    show ts_green_part
    with wipeleft_scene

    play music ts_iwtp fadein 3

    show layer screens at ts_showscreens

    show monika 2l at rn11

    m "Ну и что это было?"
    em "Что именно было?"

    show layer screens at vpunch

    m "Да весь твой утренний перформанс! Из-за тебя я опозорилась перед папой!"
    em 1i "Ну-у-у..."
    extend 2l " А что такого-то?"

    show monika 2j at s11

    show layer screens at vpunch

    m "Ты реально не понимаешь?!"
    em 2r "Да всё я понимаю..."
    em "В конце концов, это всё-таки говорю тебе не я, а ты сама себе это говоришь."
    em 4b "Поэтому ты не только бездарная и неуравновешенная, ты ещё и слабая, потому что не можешь даже переспорить собственное подсознание!"
    em 1n "И как тебя только в Дискуссионный клуб взяли?.."
    extend 2b " Не говоря уже про руководящие должности..."

    show monika 2a at t11

    m "..."
    em 2b "Что, нечего мне даже ответить? И впрямь слабая..."

    show monika 1a at s11

    m "Нет. Я просто умышленно не буду с тобой разговаривать, по крайней мере, до первого урока."

    show monika 1c at t11

    m "Убирайся.{w=0.44} Из.{w=0.44} Моей.{w=0.44}"

    show monika at cright with move
    hide monika
    stop music

    extend " {b}ГОЛОВЫ!{/b}" with vpunch

    if unluck_ball >= 3:
        "Пара человек как-то подозрительно на меня посмотрели."
        "Однако сразу после они просто хмыкнули, мол, «ненормальная», и пошли себе дальше."
        em "Тише, тише, не нужно так кричать. Или ты хочешь опозориться перед каждым живым человеком?"
        "«Убирайся из моей головы.»"

    em "Ладно, ладно, убираюсь..."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play music ts_mdl fadein 3

    play sound pageflip
    scene ts_school_gate_day
    with wipeleft_scene

    play sound pageflip
    scene ts_school_courtyard_day
    with wipeleft_scene

    play sound pageflip
    scene ts_l5
    with wipeleft_scene

    play sound pageflip
    scene ts_corridor
    with wipeleft_scene

    play sound pageflip
    scene ts_class
    with wipeleft_scene

    show layer screens at ts_showscreens

    "Наконец-то школа... Наконец-то куча людей... И мне не придётся иметь дело с... этой..."

    show layer screens at vpunch
    em "У меня, вообще-то, имя есть!"
    "«Что, правда? И как же тебя зовут?»"
    em "Просто зови меня Аки. Не сильно сложнее, чем «эта», всего три буквы, два слога, и даже отдалённо похоже на твоё же имя."

    "«А мне всё равно. Я продолжу называть тебя 'эта', просто из вредности.»"
    em "Называй как хочешь, это не отменит того факта, что ты бездарность."
    "«Ах ты!..»"

    stop music

    play sound ssikanul
    teacher "Мисс Ида!" with vpunch

    "Упс... Пока я спорила со своим извращённым подсознанием, я и не заметила, как уже начался и вовсю идёт урок..."
    m "А!.. Да!.. Что?"
    teacher "Вы меня не слушаете!"
    m "Простите..."
    teacher "Ладно, на первый раз прощаю."
    m "{size=-10}Спасибо...{/size}"
    show layer screens at vpunch
    "Да что же это такое?! Из-за этой... 'этой'... у меня одни проблемы!"
    em "Я тебе ещё раз говорю, просто зови меня Аки."
    "«Ладно, {i}Аки{/i}. Теперь довольна?!»"
    em "Вот так-то лучше!"
    em "Всё, не буду тебе мешать – с биологией ты и так не особо ладишь, а я не хочу, чтобы ты ещё больше ненавидела её."

    if persistent.cens_mode == True:
        "«Вот уж спасибо тебе, блять, большое...»"
    else:
        "«Вот уж спасибо тебе большое...»"

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play music audio.t3 fadein 3

    play sound pageflip
    scene ts_class
    with wipeleft_scene

    show layer screens at ts_showscreens

    "В таком неспешном ритме и прошёл весь школьный день."
    "Аки не особо тревожила, что тоже не может не радовать."
    "Что же, вполне логичным продолжением было бы пойти в клуб."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_corridor
    with wipeleft_scene

    play sound pageflip
    scene ts_club
    with wipeleft_scene

    show layer screens at ts_showscreens

    stop music fadeout 3

    "Оглянувшись по сторонам, я понимаю, что снова пришла первая."
    em "Ты хотела сказать, {i}мы{/i} пришли."
    m "Ой, да заткнись ты уже..."

    show natsuki 1k at rn11
    play sound ssikanul
    show layer screens at vpunch
    n "Заткнись? Ты это кому?"

    show natsuki 1za at f11

    m "!.."
    extend " Никому..."
    show layer screens at vpunch
    em "Прогресс налицо! К вечеру ты перед всеми своими {i}друзьяшками{/i} опозоришься!"
    "Она сказала «друзьяшками» каким-то чрезмерно язвительным и насмешливым тоном."
    "Но я не придала этому какого-то особого значения."

    play music audio.okevrnat fadein 3

    m "Кстати, здравствуй, Нацуки."
    n "Ну здравствуй, алкоголичка!"
    "Х-х-х..."
    "Я делаю вид, что в пятницу ничего противоречивого не прошло, и продолжаю."
    m "Да... Я думала, я первая пришла, а оказалось, что ты пришла ещё раньше."
    n 2d "А, да я сама только пару минут назад пришла!"
    n 1c "Я думала какую-то новую мангу почитать, ну, знаешь... "
    extend 2l "Чтобы прям необычное!"
    n 1k "Поэтому я в кладовой и копалась: сложно найти что-то необычное, если ты уже большую часть всей коллекции прочитала."
    n 2d "Но вот! Наконец-то нашла!"
    n 2k "Честно говоря, я эту мангу уже когда-то начинала читать, ещё лет в десять, но тогда она мне показалась слишком скучной."
    n 2l "Но теперь я заметно повзрослела, и, думаю, в этот раз я её осилю!"

    show natsuki 1j at t11

    "В руках она держит первый том пресловутой манги."
    "Я читаю название."
    m "«Ванильные Девочки»?"
    m "Тебе не кажется, что это немного... по-детски?"
    n 2e "Ну начинается..."

    show natsuki 2g at s11

    m "Нет, я не имею в виду мангу в целом... Я про конкретно эту."
    n 1q "Ну-у-у... "
    extend 1c "Как думаешь, почему я не дочитала её, когда ещё маленькой была?"

    show natsuki 1za at t11

    "Вообще, вариантов много..."

    show natsuki 1j at f11

    "Но, к счастью, Нацуки отвечает на заданный вопрос сама."
    n 2c "Потому что для моего ещё слишком молодого мозга вся эта повседневка была слишком тяжёлой для восприятия."

    show natsuki 1za at t11


    "Повседневка... Оглядываясь назад, теперь я её в какой-то мере понимаю."
    "Когда папа заставил меня прочитать «Графа Монте-Кристо» примерно в том же возрасте, я тоже кривилась и противилась."
    "Но, для справки, книгу я всё-таки дочитала."
    "Ну-у-у... или почти дочитала. Я так и не осилила где-то полсотни последних страниц."
    "Однако, учитывая общее настроение, не думаю, что в этих пятидесяти страницах была какая-то сверхнеожиданная развязка, которая в корне меняет сюжет всей книги."
    "А там, на секундочку, этих страниц в общем было далеко за тысячу!"
    "Насколько вообще большой должна быть эта манга, чтобы перевесить {i}это{/i}?"
    "Я озвучиваю тот же вопрос Нацуки, только без последней части."
    n 1c "На данный момент вышло десять томов примерно по триста страниц каждый."

    show natsuki 1j at s11

    "Ну, из того, что я вообще знаю о манге, в одной странице не больше пары предложений текста."
    "То есть, даже и не близко к моей степени мучения."
    n 1k "Зна-а-ачит... "
    extend 1l "Хочешь, вместе почитаем?"

    show natsuki 1j at t11

    "Чего?!"
    "Чтобы я читала мангу? Да это же просто абсурд!"
    "Но вслух я произношу совершенно другое:"
    m "Ну-у-у... Давай попробуем, что ли..."
    n 4z "Ура!"
    n 2l "Тогда садись! Может, теперь-то я пойму её!"

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    scene n_cg1_bg
    show n_cg1_base
    show dust1
    show dust2
    show dust3
    show dust4
    with poplil_pacan

    show layer screens at ts_showscreens

    n "Знаешь..."
    n "Как-то даже непривычно читать мангу... вместе с кем-то ещё."

    scene n_cg1_bg
    show n_cg1_base
    show n_cg1_b1
    show n_cg1_exp2
    show dust1
    show dust2
    show dust3
    show dust4

    n "Все мои друзья насмехаются надо мной из-за одного только названия!"
    n "А манга, вообще-то, может рассказывать истории не хуже классических произведений, которые все обожают!"
    m "Ну, не все из них, но... в целом, я согласна."

    hide n_cg1_exp2
    show n_cg1_exp1

    n "Ну вот видишь! Хоть кто-то со мной согласен!"

    scene n_cg1_bg
    show n_cg1_base
    show dust1
    show dust2
    show dust3
    show dust4

    n "Ну, мы читать будем или нет?"
    m "А, да... Конечно..."
    n "Поскольку я не читала её уже сто лет, и я уже всё забыла, лучше начать сначала."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene n_cg1_bg
    show n_cg1_base
    show dust1
    show dust2
    show dust3
    show dust4
    with wipeleft_scene

    show layer screens at ts_showscreens

    "Мы читаем мангу уже некоторое время."
    "Поверить не могу, я... и читаю мангу! Это же немыслимо!"
    "Хотя, спустя пару десятков страниц, история мне даже начинает нравиться."
    "Хотя в смысл и суть повествования я не особо вникаю, сама рисовка и стиль мне даже... родственны?"
    "Это не скучная классика, где через пару десятков страниц {i}сплошного текста{/i} история даже и не начинает завязываться."
    "В манге всё совсем иначе."
    em "Ну что, выбрасываем все классические книжки, которые у тебя есть, и начинаем коллекционировать мангу, как Нацуки?"
    "«Ну, не до таких крайностей...»"
    "«Может, это вообще единственная манга, которая мне понравится.»"
    em "Как там Юри в пятницу говорила? Если не попробуешь, то никогда и не узнаешь?"
    "«Она не совсем такое говорила...»"

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    scene ts_club
    show natsuki 1j at i11
    with poplil_pacan

    show layer screens at ts_showscreens

    n 1k "Ну, для первого раза достаточно."
    n 1l "Итак, что тебе понравилось? Кто тебе понравился?"

    show natsuki 1j at s11


    m "Ну, э-э-э... Да, в целом, сам стиль повествования... неплох..."
    "Я не хочу признаваться в том, что не вдавалась в подробности от слова совсем."
    n 2c "Так а из персонажей тебе кто больше всех понравился?"

    show natsuki 1g at t11


    "Я лихорадочно начинаю перебирать все варианты и выпаливаю первое, что приходит в голову."
    m "Ну-у-у... Минори... понравилась..."
    n 2l "Правда? Мне тоже больше всех Минори нравится!"
    n "Это потому, что она вся такая неуклюжая, да?"

    show natsuki 1j at f11

    "Нет, это потому, что её имя чаще всего встречалось за всё то время, что мы читали."
    m "Э-э-э... Да! Она вся такая неловкая, неуклюжая и всё такое..."
    show layer screens at vpunch
    em "Прямо как ты сейчас."
    em "Как же ты классику в детстве читала, если у тебя из головы всё выветривается пять минут спустя?"
    show layer screens at vpunch
    stop music fadeout 3
    "«Просто заткнись.»"
    n 2l "Именно! А ещё...{w=1}{nw}"

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"


    play sound stuk
    pause 3
    play sound door_open
    pause 1
    play music audio.t5_all fadein 3
    show yuri 1a at ln31
    show sayori 1a at ln32
    show natsuki 1a at t33

    show layer screens at ts_showscreens

    "Договорить Нацуки не успела – в этот момент в комнату входят Сайори и Юри."

    s 2x "Привет, Моника! Привет, Нацуки!"

    show sayori 2a at f32

    "Поскольку Сайори уже видела меня в субботу, и {i}выпустила пар{/i} ещё тогда, скорее всего, высмеивать меня она больше не будет."
    "По крайней мере, я на это надеюсь."
    y 1b "Всем привет."

    show yuri 1c at f31

    "Юри же вообще сделала вид, что она просто забыла, что произошло в пятницу."
    "Либо же она на самом деле забыла..."
    "Что, впрочем, тоже не совсем лишено смысла."
    n 2h "Что, даже не продолжите смеяться над Моникой? "
    extend 2w "Девочки, я в вас разочарована..."

    show natsuki 2x at f33

    s 3h "Да брось, Нацуки!"
    s 2h "Монике и так стыдно за произошедшее, а тут ещё и ты накручиваешь..."

    show sayori 2f at t32
    show yuri 1c at t31
    show natsuki 2x at t33

    m "Да ладно тебе, Сайори, я и не обижаюсь уже..."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    show yuri at thide
    hide yuri
    show sayori at thide
    hide sayori
    show natsuki at thide
    hide natsuki

    show overlay aw_memory_back_1
    show zatemnenie_light
    show layer master at VHS(0.83, 0.83, 0.77, 1.0)
    with dspr


    show layer screens at ts_showscreens

    "Хотя внутри меня всё ещё гложет чувство вины."
    show layer screens at vpunch
    em "А я бы в отместку накрутила её шею, градусов так на двести..."
    "«Фе, какая мерзость!»"
    em "Ой, да как будто ты через пару циклов будешь лучше."


    stop music
    window hide
    play sound fb
    scene ts_club
    show yuri 2t at i31
    show sayori 2f at i32
    show natsuki 2o at i33
    with flash

    y "Моника? Ты опять отключилась..."

    show yuri 2zg at s31

    m "А... Да это ничего, просто..."
    "Я прочищаю горло."

    play music audio.t3 fadein 3
    show yuri 2e at t31
    show sayori 2b at t32
    show natsuki 2za at t33

    m "Ладно. Итак, ребята!"
    m "Как вы уже знаете, каждый год в ноябре в школе проводится фестиваль клубов."

    show yuri 1g at s31
    show sayori 1k at s32
    show natsuki 1i at s33

    m "И поскольку наш клуб, хоть и новый, но уже официально зарегистрированный, нам нужно тоже подготовить хоть что-то, чтобы не ударить в грязь лицом."
    m "Потому что, хоть это и просто четыре девушки, занимающиеся своими делами, каждая из нас в какой-то мере представляет клуб."
    m "Поэтому... э-э-э..."
    n 1h "Моника, ближе к делу."

    show natsuki 1i at t33

    m "Да-да, ближе уже некуда."
    m "Поэтому нам нужно придумать хоть какие-то клубные активности помимо того, что мы просто обсуждаем книги, которые недавно прочитали."
    y 1j "{size=-10}Ты хотела сказать, книги, которые они в первый раз вообще видят...{/size}"

    show yuri 1i at t31

    m "Что, прости?"
    y 1h "Нет, ничего..."
    m "Так вот..."
    m "Недавно у меня появилось вдохновение, и я написала небольшой стих..."
    show layer screens at vpunch
    em "Спустя... сколько там лет ты не писала вообще ничего?"

    show yuri 2e at t31
    show sayori 2b at t32
    show natsuki 2za at t33

    m "И я тут подумала: а ведь писать стихи гораздо проще, чем кажется!"
    m "Как говорится, просто двигай рукой и плыви по течению."

    show yuri 4c at s31
    show sayori 1e at s32
    show natsuki 1u at s33

    m "Поэтому, вот вам и активность на сегодняшний день: напишите стих, чтобы к завтрашнему собранию мы все смогли обсудить его друг с другом."
    m "В стихе не обязательно должна быть замудрённая рифма – её ведь вообще может не быть!"
    m "В конце концов, главное в стихе – не рифма. Гораздо более важен сам слог и размер."
    m "И чтобы вы не чувствовали, что я вас как-то ущемляю или что-то подобное – я сяду писать стихотворение вместе с вами!"

    show yuri 1v at t31

    y "М-Моника!.."
    y 2q "К-как-то это всё... н-неожиданно..."

    show yuri 2o at t31
    show sayori 2l at t32

    s "Да, Моника, ты не находишь это всё немного... спонтанным и... нелогичным?"

    show sayori 2k at t32
    show natsuki 1n at t33

    "Нацуки же даже не удосужилась возразить."
    m "Да бросьте, девочки! Мы же в конце концов не Книжный клуб, чтобы просто читать книжки и обсуждать их!"
    m "Мы же целый отдельный Литературный клуб!"

    window hide
    stop music
    play sound br_glitch

    show yuri 2o at Glitch(_fps=1000.)
    show sayori 2k at Glitch(_fps=1000., glitch_strength=.3)
    show natsuki 1n at Glitch(_fps=1000., glitch_strength=.3, color_range1="#0a00", color_range2="0f0")

    $ renpy.pause(1.1, hard=True)
    stop sound

    play music audio.t9
    scene ts_club
    show yuri 2o at i31
    show sayori 2k at i32
    show natsuki 1n at i33

    m "А литература – это не просто какие-то книги!.."
    "«И манга», я хотела сказать. Но вовремя осеклась. Потому что кое-кто этого не поймёт."
    "В зависимости от расклада, либо Юри, либо Нацуки."
    "Но поскольку Юри кажется более тихой, то я всё-таки включила мангу как подраздел книг."
    m "...это ещё и любые другие формы письменности."
    m "Стишки, рассказики, дневники всякого рода, другая проза, да даже не совсем литературные виды искусств, как пьеса – перед тем, как актёры её играют, сценарист сначала её пишет."
    m "И вот всё это – это тоже литература."

    show yuri 3v at t31
    show natsuki 2u at t33

    m "Поэтому, чем лениться дальше и просто кушать кексы и пить {i}чай{/i}, постарайтесь написать хотя бы простенький стишок. Хотя бы парочку четверостиший."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    show yuri at thide
    hide yuri
    show sayori at thide
    hide sayori
    show natsuki at thide
    hide natsuki

    show overlay aw_memory_back_1
    show zatemnenie_light
    show layer master at VHS(0.83, 0.83, 0.77, 1.0)
    with dspr


    show layer screens at ts_showscreens

    "Хотя, с другой стороны, а почему им должно быть не всё равно?"
    "Этот клуб нужен в первую очередь мне. С натяжкой можно сказать, что этот клуб нужен и Сайори, потому что она вице-президент моей поделки..."
    "А эти две... Им и не важно, будет у них клуб или не будет."
    "Для них двоих гораздо более важны друзья, которых можно в этом клубе найти."
    stop music fadeout 3
    "Ну и, если всё сложится, я могу помочь им с их проблемами."
    em "Ты сначала себе со своими проблемами помоги, а потом уже в их дела влезай."

    window hide
    play music t3 fadein 3
    play sound fb
    scene ts_club
    show yuri 1g at f31
    with flash


    show layer screens at ts_showscreens

    y "Н-ну... "
    extend 1j "Д-допустим, ты права..."

    show yuri 1i at t31
    show sayori 2l at f32

    s "Н-ну что же... Д-давай... попробуем..."

    show sayori 2l at t32
    show natsuki 1t at f33

    n "Довольно самоиронично про чай..."
    n 2k "Ну давай попробуем написать стишки."

    stop music fadeout 3

    show natsuki 2j at t33

    m "Вот это совсем другой разговор."
    m "Тогда пишем!"

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play music audio.t4 fadein 2
    scene ts_notebook
    with pushleft

    show layer screens at ts_showscreens

    "Мы все начали писать стихотворения."
    "Точно так же, как в Дискуссионном клубе я на равных дискутировала с остальными, в Литературном я на равных с остальными пишу стихи."
    "..."
    "Однако после творческого порыва в субботу сегодня мне на ум не приходит ни строчки, ни даже хорошего слова, чтобы я могла от чего-то оттолкнуться."
    "Я мельком смотрю на остальных девочек."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    scene ts_club
    with pushright

    show yuri 1g at ln11
    pause 0.75

    pause 0.5

    show yuri 1g at ron11
    pause 0.75
    hide yuri

    show sayori 2o at ln11
    pause 0.75

    pause 0.5

    show sayori 2o at ron11
    pause 0.75
    hide sayori

    show natsuki 1s at ln11
    pause 0.75

    pause 0.5

    show natsuki 1s at ron11
    pause 0.75
    hide natsuki

    show layer screens at ts_showscreens

    "Девочки тоже натужно пытаются выжать из себя хоть что-то."
    "Но их ручки хотя бы двигаются. Значит, что-то да получается."


    $ renpy.music.set_volume(0.0)

    window hide
    play sound fb
    play sound2 ts_bad_credits1 fadein 2
    scene ts_notebook_glitch at ts_coridor_glitch
    show black zorder 5 at ts_black_glitch
    show blackout_exh
    show anim_exhausted
    show m_rectstatic zorder 0
    with flash

    show layer screens at ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake)

    "Я же, в свою очередь..."
    "Не получается у меня ничего!"
    em "С должным старанием всё должно получиться."
    "«Тебя только в этот момент не хватало...»"
    em "А что такого? Может, всё-таки признаешь, что ты бездарность?"
    "«И что от этого поменяется?»"
    em "Ничего! Просто я в очередной раз в этом убежусь."
    "«Заткнись. Ты не существуешь. Тебя нет. Это всё только в моей голове.»"
    em "Конечно, в твоей, а в чьей же ещё?"
    "«Да тихо ты!»"
    "Внезапно меня осеняет."
    em "Вот это другое дело, хоть одна ясная мысль в твоей пустой голове материализовалась."
    em "Но это не отменяет того, что ты бездарность."
    "«Просто... не мешай...»"

    window hide
    stop sound2
    $ renpy.music.set_volume(0.6)
    play sound fb
    scene ts_notebook
    with flash

    show layer screens at ts_showscreens

    "Спустя несколько минут стихотворение готово."
    "Я победно перечитываю его."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    scene ts_notebook with dissolve:
        blur 9.0

    show layer screens at ts_showscreens

    if not persistent.first_poem:
        $ persistent.first_poem = True
        show expression "mod_assets/source/images/gui/poem_dismiss.webp" as poem_dismiss:
            xpos 1050 ypos 590

    play sound pageflip

    if _preferences.language == "english":
        show screen poem(poem_m1_eng)
    else:
        show screen poem(poem_m1)

    pause

    play sound pageflip
    show layer screens at ts_hidescreens
    pause 1.0
    hide screen poem
    hide poem_dismiss

    scene ts_club
    with pushright

    show layer screens at ts_showscreens

    "Да, девочки могут не понять его смысл. Да что там, даже я сама с трудом могу его понять!"
    "Однако у меня есть что-то вроде традиции: писать стихи за один присест, а затем не редактировать их вообще."
    "Кажется, это и будет моим окончательным вариантом."

    stop music fadeout 3

    "Я ещё раз смотрю на остальных."

    show yuri 2l at t31
    show sayori 4s at t32
    show natsuki 1y at t33

    "Кажется, Сайори и Нацуки уже тоже закончили. Юри же до сих пор пишет, не отвлекаясь ни на что и ни на кого."
    "Я мельком смотрю на часы. Что-то уже и поздновато."

    play music audio.t8
    show sayori 2b at t32
    show natsuki 1a at t33

    m "Итак, ребята!"
    "Юри даже после моего окрика и не шелохнулась."
    n 1l "Вероятно, слишком ушла в себя, чтобы взаимодействовать с людьми."

    show sayori 4s at h32
    show natsuki 1y at h33

    "Сайори засмеялась следом за Нацуки."
    "Да и я тоже, чтобы не выбиваться из компании, вымученно хихикнула."
    "Юри казалась совершенно непоколебимой."

    show sayori 4n at t32

    "И пока Сайори не начала тыкать Юри пальцем и бог знает чем ещё, я продолжаю."
    m "А-ха-ха... Да, так вот..."
    m "Все же закончили стихотворение?"

    show sayori 2a at d32
    show natsuki 1a at d33

    "Нацуки и Сайори согласно закивали."
    m "Ну, тогда пусть Юри закончит писать, и на этом можем расходиться."

    show yuri 2f at f31

    y "Я тоже закончила."

    show yuri 2e at t31

    m "Вот и отлично."
    m "Что же, сегодня мы поделиться уже точно не успеем..."
    m "Но завтра мы все обязательно поделимся этими стихами друг с другом!"
    m "А сейчас – собрание окончено. Всем спасибо, все свободны!"

    show yuri 3d at h31
    show sayori 4s at h32
    show natsuki 1y at h33

    if _preferences.language == "english":
        $ m_name = "Everyone"
    else:
        $ m_name = "Все вместе"

    show layer screens at vpunch
    m "Пока, Моника!"

    if _preferences.language == "english":
        $ m_name = "Monika"
    else:
        $ m_name = "Моника"

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    stop music fadeout 3

    play sound door_open

    show yuri 3d at lon31
    show sayori 4s at lon32
    show natsuki 1y at lon33

    pause 0.5

    hide yuri
    hide sayori
    hide natsuki

    show layer screens at ts_showscreens

    "Распрощавшись, девочки уходят. А я остаюсь думать."


    show monika 4k at ln11

    em "Ты хотела сказать, {i}мы{/i} остаёмся."

    show monika 3j at t11

    "...хотя, знаете? Что-то поздно уже, пойду-ка я лучше домой."

    show monika 2d at f11

    em "Эй, подожди! Всё равно от меня не спрячешься!"

    show monika at cright with move
    hide monika

    "Я выключаю свет и быстрым шагом иду домой."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound door_open
    pause 1
    play sound2 pageflip
    scene ts_light_off_corridor
    with wipeleft_scene

    show layer screens at ts_showscreens

    em "Погоди!.."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_l5
    with wipeleft_scene

    show layer screens at ts_showscreens

    em "Постой..."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_school_gate_evening
    with wipeleft_scene

    show layer screens at ts_showscreens

    $ persistent.sprite_time = "day"

    em "Моника..."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play music ts_iwtp fadein 3

    $ persistent.sprite_time = "sunset"

    play sound pageflip
    scene ts_street_late
    show ts_yel_part
    with wipeleft_scene

    show monika 5c at rn11

    show layer screens at ts_showscreens

    em "Да остановись ты уже!"

    show monika 5c at t11

    m "Что такое?! Передумала насчёт того, что я бездарность?"

    show monika 4k at f11

    em "Нет, это вселенская постоянная!"

    show monika 2i at f11

    em "Я по другому поводу."

    show monika 3n at f11

    em "Неужели... Неужели ты снова написала стих про меня?.."

    show monika 1m at t11

    "На этот раз мне даже оправдываться лень."
    m "Да. Про тебя. И про то, как сильно ты мне мешаешь сосредоточиться."

    show monika 3n at f11

    em "Ну, во-первых, я польщена..."

    show monika 4k at f11

    em "А во-вторых, не так-то и сильно я {i}мешала тебе{/i}."
    em 4b "Стих-то ты всё-таки написала!"

    show monika 2a at t11

    show layer screens at hpunch
    m "Господи, да когда же это всё закончится..."

    show monika 2i at f11

    em "А ты проверь."

    show monika 3l at f11

    em "Ущипни себя, например. Ну, просто чтобы убедиться, что ты не спишь!"

    show monika 3j at t11

    m "Нет, на такую дешёвую провокацию я не куплюсь."

    if unluck_ball >= 4:
        show monika 2i at f11

        em "Ну, кто знает..."
        show layer screens at hpunch
        em "Может, ты вообще в коме находишься, а ущипнуть себя – это своего рода проверка на то, спишь ты или нет."

        show monika 2h at t11

        m "Нет. Сайори же сказала, что сон – это сон, а реальность – это реальность, и ей я доверяю."
        m "И за исключением того, что я вслух разговариваю со своим подсознанием, всё вполне реально."
        m "По крайней мере, краски не чрезмерно яркие, и хожу я с нормальной скоростью, а не как под водой."
        "Я как-то читала в одном журнале признаки того, что ты спишь."
        "И даже несмотря на то, насколько реально всё происходящее, есть некоторые черты, которые возможны только во сне."
        "Как, например, ходьба как будто под водой."

        show monika 2i at f11

        em "Доверять девочке, которую знаешь всего несколько недель?"
        em 1r "Мда-а-а, и куда только подевалась настоящая неприступная Моника, для которой, чтобы подружиться с ней, должны пройти месяцы, если не годы?.."

        show monika 1q at t11

        m "Ну, людям свойственно меняться..."

        show monika 2k at f11
        show layer screens at hpunch
        em "Даже таким бездарностям, как ты?"

        show monika 2j at t11

        m "Да."

        show monika 2o at s11

        "На спор со своим подсознанием я не в настроении."

    show monika 2p at f11
    stop music fadeout 5

    em "Жаль..."

    show monika 2n at f11

    em "Я бы с удовольствием посмотрела на это..."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_house_monika_evening
    with wipeleft_scene


    show layer screens at ts_showscreens

    "Пока я {i}разговаривала{/i}, я и сама не заметила, как дошла до дома."
    "Свет не горел нигде. Видимо, папа ещё не пришёл."
    "Впрочем, он утром сказал, что у него весь день всякие суды."
    "Я даже не знаю, где эти суды находятся, но, думаю, как минимум один из них довольно далеко от нашего дома..."
    "Внушив себе эту мысль, я вхожу в дом."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_vhod_nolight
    with wipeleft_scene

    play sound2 svet_on
    scene ts_vhod_night
    with flash

    play music ts_sis fadein 3

    play sound pageflip
    scene ts_living_room_late
    with wipeleft_scene

    show layer screens at ts_showscreens

    "Действительно, папы дома ещё нет."

    play sound door_open

    "И как только я об этом подумала, следом за мной входит папа."

    ts_ft "Моника, я пришёл!"
    m "Привет, пап! Я в гостиной."
    ts_ft "Сейчас приду."

    show hiroto 2b at rn11

    ts_ft "Здравствуй, Моника."

    show hiroto 2b at t11

    "Однако улыбка с его лица так и не сходит."
    m "Пап... а ты чего такой довольный?"

    show hiroto 2g at f11

    ts_ft "Я сегодня позвонил маме..."

    show hiroto 2b at f11

    ts_ft "Впрочем, можешь и сама ей позвонить!"

    show hiroto 1a at t11

    m "Слушай, а не поздно уже?"
    "Я настолько не слежу за жизнями своих родителей, что даже ни разу не удосужилась спросить, в какой конкретно стране у неё эта самая «заграничная командировка»."
    em "Двойка тебе за внимательность и учтивость. Да и за всё остальное тоже."

    show hiroto 2c at f11

    ts_ft "Да там разница в часовых поясах пара часов максимум. В худшем случае, мы позвоним ей перед сном."
    ts_ft 2b "Так что не будет такого, что мы разбудим её посреди ночи."
    ts_ft 1c "Но сначала всё-таки надо поужинать. Или ты уже?"

    show hiroto 1e at t11

    m "Нет, я сама только пару минут назад пришла, решила немного отдохнуть."

    show hiroto 1g at f11

    ts_ft "Ты хоть в школе ела?"

    show hiroto 1j at t11

    m "Ну-у-у... да?"
    "Я снова нагло вру. Кроме утренних хлопьев и кофе, я не ела вообще ничего. Я буквально умираю с голоду."

    show hiroto 2g at f11

    ts_ft "Ну славненько тогда."

    show hiroto 1v at f11

    stop music fadeout 4

    ts_ft "Та-а-ак... "
    extend 1b "Моника, ты картошку жареную будешь?"

    show hiroto 1a at t11

    m "Конечно."

    if unluck3 == True:
        em "Заодно папа покажет тебе, как нужно жарить картошку, чтобы она в итоге не превратилась в угольки."
        "«Вот только тебя мне не хватало...»"

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play music ts_mdl fadein 3

    play sound pageflip
    scene ts_kitchen
    with wipeleft_scene

    show layer screens at ts_showscreens

    "Десять минут спустя картошка уже начищена, порезана и уже жарится на сковороде."

    if unluck3 == True:
        em "Только, в отличие от нашей сони, папа за картошкой действительно бдит."

    "Не знаю, как у него так быстро и хорошо получается."
    "Папа как-то рассказывал, что в армии он частенько дежурил в столовой, и хвастался, что ведро картошки он чистит минут за тридцать, если не ещё меньше."
    "Чего ему стоит почистить всего парочку?"

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_kitchen
    with wipeleft_scene

    show layer screens at ts_showscreens

    "Ещё спустя минут пять дымящаяся картошка уже рассыпана по двум тарелкам."

    show hiroto 1b at ln11

    ts_ft "Приятного аппетита, Моника."

    show hiroto 1a at t11

    m "Спасибо, пап. Взаимно."

    show hiroto 1g at f11

    ts_ft "Спасибо."

    show hiroto 1e at t11

    "Вау. Очень вкусно."
    "После того, как мы съели пару кусков, папа наконец спрашивает."

    show hiroto 1b at f11

    ts_ft "Так что там за секрет такой в вашем клубе, о котором ты мне всё никак не хотела рассказывать?"

    show hiroto 1a at t11

    m "Ну-у-у..."
    m "У нас с девочками появилась новая активность. Мы теперь не только обсуждаем книги, но и стихи пишем. А завтра мы будем ими обмениваться."
    m "Я думаю сделать это постоянной клубной активностью."

    show hiroto 1c at f11

    ts_ft "И что, прямо-таки все справились?"

    show hiroto 1e at t11

    m "А почему мы должны были не справиться? Это же мой клуб, в конце концов."
    em "Я бы поспорила на тему...{nw}"
    show layer screens at vpunch
    "«Заткнись и не перебивай.»"

    show hiroto 1g at f11

    ts_ft "Моя умница."
    ts_ft 1c "Но я скорее говорил на тему того, что писать что-то своё – это творческий процесс."
    ts_ft "А творческий процесс – это в первую очередь вдохновение. А оно может как прийти, так и нет."
    ts_ft "Ты не можешь ожидать того, что все девочки будут писать шедевры литературы ежедневно."

    show hiroto 1e at t11

    m "Но сегодня же все справились..."

    show hiroto 1d at f11

    ts_ft "А завтра могут справиться не все."

    show hiroto 1e at t11

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    show zatemnenie_light
    show overlay aw_memory_back_1
    show layer master at VHS(0.83, 0.83, 0.77, 1.0)
    with dissolve2

    show layer screens at ts_showscreens

    "Папа у меня тоже своего рода человек творческий, и по молодости тоже писал стихи."
    "Но это были не обычные любовные стишки, которые в своё время пишет чуть ли не каждый подросток, у которого гормоны разыгрались."
    "Папа писал серьёзные и довольно тяжёлые для восприятия тексты. По крайней мере, он так говорил."
    "Но с другой стороны, вполне логично, что темы были довольно сложными – всё в соответствии с его высшим образованием, которое тоже не из самых лёгких."
    "Нет, я не говорю о том, что кому-то учиться легче, а кому-то сложнее. В конце концов, все профессии нужны, все профессии важны."
    "Но успехов в учёбе добивались лишь единицы. К счастью, папа был одной из тех «единиц»."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"


    scene ts_kitchen
    show hiroto 1e at i11
    with dissolve2

    show layer screens at ts_showscreens

    m "Ну, сегодня справились все. А завтра будет завтра. Тем более, завтра у них ещё весь вечер будет, чтобы написать стихотворение."
    m "Да и к тому же, даже если стих, который они написали в клубе, кому-то не понравится, у них будет ещё весь вечер, чтобы отредактировать или даже полностью переписать его."

    show hiroto 1g at f11

    ts_ft "Ладно, убедила."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_living_room_late
    show hiroto 1a at i11
    with wipeleft_scene

    show layer screens at ts_showscreens

    "С этими словами мы заканчиваем есть. Но развлекательная программа на вечер ещё не окончена."
    m "Ладно, так мы будем маме звонить или нет?"

    show hiroto 1g at f11

    ts_ft "Ну, набирай."

    show hiroto 1f at t11

    "Я в предвкушении набираю маму."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    show hiroto 1b at f11

    play sound mobila_gudok

    pause 8


    show layer screens at ts_showscreens

    ts_ft "Поставь на громкую связь. Я тоже скажу ей кое-что."

    stop music fadeout 3
    stop sound fadeout 3

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    scene black with ed_night_dis_faster

    pause 1

    play music ts_wod fadein 3

    show ts_gost_split_animated
    show ts_hotel_split_animated

    pause 0.99

    show minami 1bd at rn33
    show hiroto 1a at ln31

    if _preferences.language == "english":
        $ ts_mt_name = "Minami"
    else:
        $ ts_mt_name = "Минами"

    show layer screens at ts_showscreens

    ts_mt "Алло?"

    show minami 1bc at t33

    m "Привет, мам!"

    show minami 2bk at f33

    ts_mt "Моника! Я так рада тебя слышать!"

    show hiroto 1b at f31

    ts_ft "Привет ещё раз, дорогая."

    show minami 1bb at f33
    show hiroto 1a at t31

    ts_mt "Привет, Хирото."

    show minami 1ba at t33
    show hiroto 1f at t31

    m "Мы тебя не разбудили?"

    show minami 3bn at f33

    ts_mt "Ну, ещё нет, хотя я уже готовилась ко сну, а тут вы."

    show minami 3bb at f33

    ts_mt "А в чём, собственно, дело?"

    show minami 3bn at t33

    m "Это ты мне скажи. Папа сказал, что у тебя для меня какие-то новости заготовлены."

    show minami 3bl at f33

    ts_mt "Ах да, совсем забыла! "
    extend 1br "С этой работой уже ничего не помню..."
    ts_mt 1bt "Так вот. Когда у тебя там фестиваль будет?"

    show minami 1be at t33

    m "Ровно через неделю."

    show minami 4bk at f33

    ts_mt "Какое приятное совпадение!"

    show minami 3bn at f33

    ts_mt "Поскольку я закончила раньше положенного срока, запуск новой ракеты будет уже в эту субботу."
    ts_mt 2bd "Я переночую один последний раз, и в воскресенье в десять вечера по местному у меня будет самолёт."

    show minami 3bk at f33

    ts_mt "К вечеру я уже буду дома, когда ты как раз вернёшься со своего фестиваля!"

    show minami 3bj at t33

    "Моей радости нет предела. Мы наконец-то торжественно встретим вечер всей семьёй, тем более, в такой важный для меня день."
    "Даже если мамы не будет на самом фестивале, она хотя бы будет после него, когда я вернусь домой."
    m "Ура!"

    show minami 2bk at f33

    ts_mt "И не говори."

    show minami 2bn at f33

    ts_mt "Что вы готовите на фестиваль, кстати?"

    show minami 2bn at t33

    "Я слегка нервничаю на этом вопросе."
    m "Э-э-э-это секрет!"

    show hiroto 1b at f31

    ts_ft "{size=-8}Даже я его не знаю...{/size}"

    show minami 1bl at f33
    show hiroto 1b at f31

    if _preferences.language == "english":
        $ m_name = "Everyone"
    else:
        $ m_name = "Все вместе"
    m "А-ха-ха!"
    if _preferences.language == "english":
        $ m_name = "Monika"
    else:
        $ m_name = "Моника"

    "К счастью, папа подыграл мне."

    show minami 3bb at f33
    show hiroto 1a at t31

    ts_mt "Ну, я надеюсь, что чем бы ни было ваше представление, ты не подведёшь маму с папой!"

    stop music fadeout 4

    show minami 3be at t33

    m "Да, мам..."

    show minami 3bk at f33

    ts_mt "Ну вот и славненько!"

    show minami 2bd at f33

    ts_mt "Дай трубку папе, я ещё ему хочу кое-что сказать."

    show minami 3bc at t33

    m "Хорошо."

    show hiroto 1v at f31

    ts_ft "Минами, я как раз тоже хотел кое-что сказать тебе..."

    show hiroto 1c at f31

    ts_ft "{size=14}Можешь идти, я тебе потом телефон занесу.{/size}"

    show hiroto 1e at t31

    m "Хорошо."
    $ persistent.sprite_time = "sunset"
    "Папа остался разговаривать с мамой. Я же после этих слов направилась к себе."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_gost_sunset
    with wipeleft_scene

    $ persistent.sprite_time = "night"

    play music ts_faceless fadein 3

    play sound pageflip
    scene ts_darkbed
    with wipeleft_scene

    show layer screens at ts_showscreens

    "Я так устала... Но я так рада..."
    "Не раздеваясь, я просто плюхнулась в кровать."

    show monika 1pi at ln11

    em "Стареешь, Моника. Ты уже в который раз беспричинно устаёшь."

    show monika 1ph at s11

    m "А мне всё равно. Я настолько устала, что даже на разговор с тобой сил не найдётся."

    show monika 1pf at t11

    show blink

    m "Скоро фестиваль... Скоро приедет мама... И всё у нас будет хорошо..."
    "После этих слов быстро провалилась в сон."
    stop music fadeout 4
    "Извращённое подсознание, конечно, ещё пыталось сказать мне что-то вроде «не надейся», но я его уже не слушала."
    "Я уже сплю. И ничто не может потревожить мой сон."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    scene black

    show layer screens at ts_null_transform

    jump ts_scenario_7