label ts_scenario_2:

    python: # ОБНОВЛЯЕМ RPC
        try:
            rpc.update(state="Акт I | Глава II",details="Поиски. Юри",large_image="aonectwo",start=time.time())
        except AssertionError:
            pass

    $ persistent.rpclabel = "2"

    $ persistent.carter2menu = False
    $ persistent.carter3menu = False
    $ persistent.badendmenuperedglitch = False
    $ persistent.badendmenuskipglitch = False
    $ persistent.badendmenu = False
    $ persistent.goodendmenu = False
    $ persistent.peredbadendmenu = False
    $ persistent.peredgoodendmenu = False

    $ save_name = "Поиски. Юри"

    pause 2
    play sound chp1
    $ Chapter("АКТ ПЕРВЫЙ")
    $ Chapter("АКТ ПЕРВЫЙ")
    $ Chapter("глава вторая")
    $ Chapter("глава вторая")
    $ Chapter("Поиски. Юри")
    stop sound fadeout 7
    $ Chapter("Поиски. Юри")
    play music ts_gramatik
    scene ts_bedroom
    with ed_night_dis

    show layer screens at ts_showscreens

    "Новую неделю я начала с твёрдой решимостью разузнать, кто же эта таинственная девочка, читающая на обеде."
    "Все выходные я только и делала, что просто перебирала разные варианты имён и репетировала первые предложения в зависимости от имени."

    m "Если её зовут Хлоя, то я скажу нечто вроде «О, Хлоя? Как Хлоя Морец?»"
    m "«Талантливая девочка, с самого детства отлично играла»..."
    m "..."
    m "А если её зовут Ханако..."
    m "Нет, всё это тупо, неправильно!"

    "Читать не хотелось."
    "Писать не хотелось."
    "Мне вообще ничего не хотелось."
    "Единственное, чего мне хочется - это узнать её хотя бы чуточку лучше..."
    "Впрочем, а что мне мешает?"
    "С Мирой же получилось! С Каори же получилось!"
    "И с Сайори тоже получилось!.."
    "Но с другой стороны, а что {i}получилось{/i}?"
    "Получилось, что это Мира объявила меня своим другом. И Каори. Да и Сайори, по сути, тоже."
    "Я ничего для этого не делала, просто была послушной девочкой."
    "Как, знаете, есть такая шутка: интроверт не заводит друзей. Интроверт находит экстраверта, а экстраверт, в свою очередь, делает его своим другом."
    "...несмешная шутка, не так ли?"
    "Впрочем, в каждой шутке есть доля шутки, а всё остальное - правда."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene black
    with wipeleft_scene

    show layer screens at ts_showscreens

    "Так и пролетели все выходные."
    "Что в очередной раз доказывает, что время идёт {b}гораздо{/b} быстрее, чем нам кажется."
    "Я только легла в кровать в пятницу, а сейчас уже утро понедельника."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound ts_alarm
    scene ts_bedroom
    show unblink

    show layer screens at ts_showscreens

    "Часы показывают ровно семь утра."
    "До занятий ещё полтора часа, я успеваю умыться, почистить зубы, позавтракать, неспешным шагом дойти до школы, и всё равно у меня будет ещё время."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_bathroom
    with wipeleft_scene

    show layer screens at ts_showscreens

    "Холодная вода и не менее холодное послевкусие зубной пасты подарили мне заряд для бодрости на весь день."
    "Папа всегда говорит, что нужно умываться именно холодной водой - так взбодришься быстрее."
    "Но от этого на душе приятнее не становится."

    m "Бр-р-р..."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_kitchen
    with wipeleft_scene

    show layer screens at ts_showscreens

    "После утреннего моциона я иду завтракать."
    "Честно говоря, я не особо привередлива в плане завтрака, но у меня есть одно обязательное условие:"
    "Там должен быть кофе."
    "Обожаю кофе."
    "Помимо того, что он мне просто нравится, это ещё и дополнительный заряд бодрости, чтобы сразу на целый день."

    show hiroto 1b at ln11

    ts_ft "Доброе утро, Моника!"
    show hiroto 1a at f11
    m "Доброе, пап."
    ts_ft 1b "Ну, что на завтрак?"
    
    show hiroto 1a at t11
    "В последнее время мы готовим завтраки по очереди."
    "Папа говорит, что я уже достаточно взрослая и самостоятельная, чтобы и самой готовить завтраки."
    "Хотя бы простые."
    "«Иначе как же тебя в университет возьмут, если ты такая несамостоятельная?»"
    "И знаете... Хоть и правда, но всё равно немного обидно."

    m "Хлопья с молоком и кофе."
    
    show hiroto 2b at f11
    
    ts_ft "О-о-о, хорошечно."
    show hiroto 2a at t11
    "Папа тоже любит кофе гораздо больше чая."
    "Видимо, это у нас семейное."

    show hiroto 2g at f11

    ts_ft "Ну что, какие планы на день?"
    show hiroto 1e at t11
    m "Да ничего необычного, школа, клуб, затем домой, затем ужин, затем спать."

    "Я не говорю папе то, что сказала мне Сайори."

    stop music fadeout 5

    m "А у тебя?"
    
    show hiroto 1b at f11
    
    ts_ft "Да в целом, не сильно интереснее твоего."    
    ts_ft "Сначала работа, потом ужин с любимой дочерью, и тоже спать лягу."
    
    show hiroto 2g at t11
    
    ts_ft "Скукотища..."

    "Мы оба над этим посмеялись."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_house
    show hiroto 2g at t11
    with wipeleft_scene

    show layer screens at ts_showscreens

    ts_ft "Удачного дня, Моника!"
    show hiroto 2f at f11
    m "И тебе удачного дня, пап!"
    
    show hiroto at cright with move
    hide hiroto

    "Попрощавщись, каждый пошёл своей дорогой: я в школу, он на работу."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play music ts_mdl
    play sound pageflip
    scene ts_street
    with wipeleft_scene

    show layer screens at ts_showscreens

    "Как только я осталась одна, я продолжаю думать."
    "У меня были все выходные, чтобы узнать хоть что-то."
    "Но я так ничего и не узнала."
    "Что же, надеюсь, что либо я, либо Сайори увидим её на обеде ещё раз."
    "На данный момент это наша единственная надежда."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_school_gate_day
    with wipeleft_scene

    play sound pageflip
    scene ts_school_courtyard_day
    with wipeleft_scene

    play sound pageflip
    scene ts_corridor
    with wipeleft_scene

    play sound pageflip
    scene ts_class
    with wipeleft_scene

    show layer screens at ts_showscreens

    "Уроки пролетели гораздо быстрее, чем казалось."
    "Ну-у-у, кроме разве что парочки."
    "В понедельник у нас химия и биология. Два моих самых нелюбимых предмета, и оба в один день."
    "И вот эта парочка тянется настолько ме-е-едленно, что проще убиться, чем дотянуть до конца урока."
    "Хорошо хоть учитель меня ни разу не спросил."
    "Так что оказалось всё не настолько плохо, как изначально ожидалось."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_corridor
    with wipeleft_scene

    show layer screens at ts_showscreens

    "После уроков я как обычно направилась к Литературному клубу."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_club
    with wipeleft_scene

    show layer screens at ts_showscreens

    "Хм. Похоже, что я первая пришла."
    "Впрочем, ничего удивительного. Сайори всегда немного опаздывает."

    play sound door_break
    show sayori 4p at ln11

    "И как будто специально, как только я об этом подумала, Сайори буквально вваливается в кабинет Литературного клуба."

    show layer screens at vpunch

    s "Моника!"
    
    show layer screens at vpunch
    extend " Моника!"
    
    show layer screens at vpunch
    extend " Юри!.."

    "Она меня буквально ошарашила."

    show sayori 4o at d11

    m "Так, давай-ка по-порядку и {cps=15}помедленнее...{/cps}"

    show sayori 4m at h11

    s "Её зовут Юри!"
    m "Что?!"

    show sayori 4n at f11
    m "Что ещё ты узнала?"
    show sayori 1l at t11
    s "Пока это всё..."
    show sayori 2m at f11
    s "А, нет, не всё!"
    show sayori 1x at t11
    s "Ещё я узнала, что она не состоит ни в каком клубе, и я ей сказала, что если она любит читать, то в Литературном клубе ей всегда рады!"

    show sayori 1 at s11

    m "Та-а-ак, а она что?"
    show sayori 3h at t11
    s "Она сказала, что никогда о таком даже и не слышала..."

    show sayori 1m at f11
    show layer master at heartbeat

    m "Да они что, издеваются?!"
    m "Я почти два месяца изо всех сил добивалась того, чтобы в этом клубе было больше народу, а они, видите ли, и знать не знают о таком клубе?!"

    scene ts_club
    show sayori 1m at f11
    pause 0.1
    show sayori 1u at t11

    m "..."
    m "Ладно, всё, хорошо, успокойся..."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"


    show zatemnenie with dspr

    show layer screens at ts_showscreens

    show screen chp_text_23
    pause
    show layer screens at ts_hidescreens
    show screen chp_text_23
    pause 1
    hide screen chp_text_23

    hide zatemnenie with dspr

    show layer screens at ts_showscreens

    m "Сайори..."
    show sayori 2v at f11
    s "Да?"
    m "А ты... ты сказала ей, когда именно ей подходить? А то собрание клуба началось двадцать минут назад, а никто так и не пришёл..."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    show sayori 1u zorder 2 at f11
    pause 0.15
    show sayori 1 zorder 2 at t11
    pause 0.15
    show sayori 2c zorder 2 at s11
    pause 0.15
    show sayori 3m zorder 2 at t11
    pause 0.15
    show sayori 3n zorder 2 at f11
    pause 0.15
    show sayori 1o zorder 2 at t11
    pause 0.15
    show sayori 2l zorder 2 at s11
    pause 0.15
    show sayori 3e zorder 2 at t11
    pause 0.15
    show sayori 5a zorder 2 at f11
    pause 0.15
    show sayori 5b zorder 2 at t11
    pause 0.15

    show sayori 4p at h11

    show layer screens at ts_showscreens

    s "Я забыла!"
    m "..."

    "..."
    "Типичная Сайори..."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_club
    show sayori 1k at t11
    with wipeleft_scene

    show layer screens at ts_showscreens

    "Прошло ещё полчаса."
    "Юри так и не пришла."
    "Может, она, как и все остальные, лишь пообещала, что придёт, а на деле не пришла?"
    "..."
    "На Сайори я уже не злюсь."
    "Да и как я вообще могу на неё злиться?"
    "Она же, по сути, занимается рекрутингом в мой клуб."
    "А я тем временем просто плюю в потолок..."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_club
    show sayori 1k at t11
    with wipeleft_scene

    show layer screens at ts_showscreens

    "Большую часть собрания клуба мы просто молчим."
    "Сайори молчит, потому что, скорее всего, она корит себя за то, что чего-то в разговоре с Юри не сделала."
    "Я же молчу, потому что... корю себя."
    "За то, что накричала на неё."
    "Каждую минуту, каждую секунду, каждое мгновение..."
    "Я чувствую себя виноватой."

    show sayori 1f at s11
    m "Ну что, Сайори, давай-ка сегодня закончим пораньше. Сегодня мы вообще на литературу и разговоры не настроены."
    m "Давай уже завтра."
    s 2h "Да..."

    play sound stuk1
    show sayori 2n at t11

    "Как вдруг, наконец, в дверь постучали. Мягко и элегантно."

    show yuri 1q at ln21
    show sayori 1n at t22
    play music audio.okevryuri

    y "И-извините, а это Литературный клуб?"

    "Робко спросила Юри."
    "То, что я слышала из запыханных рассказов Сайори, я теперь увидела воочию."
    "Девушка. Ростом чуть выше меня. С волосами цвета лаванды примерно до пояса и такого же цвета глазами."
    "И, э-э-э... с «формами» пообъёмнее, чем мои."
    "Нет, конечно, мои «формы» тоже не из самых маленьких, но..."
    "Её формы на порядок больше моих."
    "Я ей даже завидую немного. По-доброму, конечно."
    "У неё спина не болит такие тяжести постоянно таскать?"
    "Я имею в виду, у меня грудь как минимум на пару размеров меньше, чем её, но всё равно, если весь день стоять, то к вечеру спина иногда начинает побаливать."
    "Даже не могу представить, каково ей..."
    "А ещё... То, как она выражается..."
    "Нет, конечно, Сайори в первый раз задала точно такой же вопрос."
    "Но от неё прямо-таки излучался позитив и искренность."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"


    show zatemnenie with dspr

    show layer screens at ts_showscreens

    show screen chp_text_26
    pause
    show layer screens at ts_hidescreens
    show screen chp_text_26
    pause 1
    hide screen chp_text_26

    hide zatemnenie with dspr

    show layer screens at ts_showscreens

    "Юри же, казалось бы, боится совершенно всего на свете."
    "Не удивлюсь, если она всё это время просто стояла у двери и ждала, набираясь смелости открыть её."
    "Но я рада, что она всё-таки это сделала. Как минимум, из-за того, что теперь у нас будет ещё один участник."
    "А там и до минимальных требований в четыре человека недалеко..."
    "Мы с Сайори сразу оживились."

    show yuri 1i at s21
    stop music fadeout 3

    m "А, эм-м-м... да."

    "На второй раз я отвечала уже чуть более уверенно."

    play music audio.t2

    m "Меня зовут Моника, я президент Литературного клуба. Добро пожаловать!"
    y 1q "А м-меня... Юри зовут..."
    s 4s "А я Сайори!"
    y 1j "А тебя я знаю."
    s 3o "Что? Как? Где?"
    y "Мы же буквально сегодня днём пересекались..."
    y 2q "Ты сегодня настолько настойчиво спрашивала, кто я такая, и нет ли у меня планов после школы, что я подумала, что ты хочешь на свидание меня позвать..."
    y 1j "Я даже подумывала сбежать сразу после уроков, думая, что это пранк какой-то."
    y 3f "Но потом я подумала: а что я вообще теряю? Если такая милая девочка приглашает меня в клуб, то, наверное, она там не одна такая милая."

    "Юри впервые с начала нашей встречи посмотрела мне прямо в глаза."

    y 3b "В итоге любопытство взяло вверх, и я отправилась искать этот ваш Литературный клуб."

    show yuri 2o zorder 1 at t21
    y "Правда, т-ты так и не сказала, в каком именно кабинете вы находитесь..."
    s 1l "Э-хе-хе..."
    s "Что вы на меня смотрите?.."
    show yuri 1t at f21
    show sayori 1y at s22
    y "Я уже думала о том, чтобы плюнуть на всё, на этот Литературный клуб, на эту милую девочку, и уйти."
    y 1q "Но что-то мне подсказывало, что в этом Литературном клубе мне будет хорошо..."
    show yuri 1m at t21
    y "Ну и один раз чутьё меня не подвело."

    stop music fadeout 3

    m "А-ха-ха... Эм-м-м... Ну что же, присаживайся. Нас пока в клубе только двое, но мы надеемся, что ты станешь отличным дополнением к клубу."
    y 4b "..."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_club
    with wipeleft_scene

    show layer screens at ts_showscreens
    play music audio.t8

    "Остальная часть клубного собрания прошла быстрее."
    "И хотя после изначального «знакомства» Юри не проронила и слова, всё равно на душе стало как-то... теплее."
    "У меня есть реальные шансы собрать этот клуб, чтобы мы тоже могли готовиться к фестивалю."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    show layer screens at ts_showscreens

    show yuri 1 at t21
    show sayori 1 at t22

    "Довольная собой и всем миром, я объявляю:"

    m "Итак, девочки, собрание окончено! Завтра жду вас обеих в это же время."

    play music ts_rem

    y 3n "О-обеих?"
    m "Ну... да? А что, что-то не так?"
    y 2o "Ну, мы просто... провели время вместе... молча..."
    y "Никаких заданий, никакого обсуждения... вообще ничего..."

    "Я очень боялась этого замечания."
    "И хотя Юри сделала очень справедливое замечание, от этого менее больно не становится."

    m "..."
    s 2l "..."

    "..."

    m "Ну-у-у... Юри, а что ты сейчас читаешь?"
    y 4b "Да нет... Она вам... не понравится..."
    m "Просто скажи нам, что ты сейчас читаешь, а я уже потом решу, что нам с этой информацией делать..."
    y 4a "Что же..."
    y 2f "С-сейчас я перечитываю «Маленького Принца» за авторством..."

    "Дальше я уже не слушаю. Экзюпери. Я её как-то читала в детстве, и мы даже проходили Принца на уроках мировой литературы."
    "У нас она где-то даже есть, но я уже почти всё забыла."
    "Книга не очень большая, не особо сложная, и в какой-то степени даже детская, так что, думаю, для первого нашего обсуждения она вполне сгодится."

    show sayori 1o at s22

    "Сайори же, в свою очередь, об этой книжке никогда даже и не слышала."
    "Поэтому, услышав монолог Юри, она задумалась так, как не задумываются на мировых олимпиадах по математике."

    stop music fadeout 3

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"


    show zatemnenie with dspr

    show layer screens at ts_showscreens

    show screen scenario_2_double_text_suka
    pause
    show layer screens at ts_hidescreens
    show screen scenario_2_double_text_suka
    pause 1
    hide screen scenario_2_double_text_suka

    hide zatemnenie with dspr

    play sound pageflip
    scene ts_club
    show yuri 1 at t21
    show sayori 1 at t22
    with wipeleft_scene

    play music ts_dreams

    show layer screens at ts_showscreens

    m "Тогда решено: каждый из нас идёт домой, прочтёт Маленького Принца, а на завтрашнем собрании клуба мы обсудим, что же хотел сказать автор!"
    s 2x "Отлично!"
    y 1zi "В-вот так-то лучше."
    m "Ну и на такой позитивной ноте я официально объявляю собрание клуба оконченным."

    stop music fadeout 1

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene black with ed_night_dis
    scene ts_club

    play music audio.t3

    show layer screens at ts_showscreens

    "Так прошло несколько дней."
    "Я уже понемногу начинаю привыкать к новому члену клуба."
    "Сайори уже вообще считает Юри своим новым другом."
    "Юри же... кажется, ещё не совсем к нам привыкла."
    "Такое ощущение, что в Юри живут два совершенно разных человека."
    "Такая принципиальная королева книг... и такая тихая и боязливая в плане всего остального."
    "За всё время, что Юри пробыла в клубе, не по теме книг она сказала всего несколько предложений."
    "Кажется, что она за книгами как будто не видит реального мира."
    "Да, действительно, она очень много прочитала книг в своей жизни, на несколько порядков больше меня."
    "Но как только дело доходит до реальных взаимоотношений с реальными людьми, она теряется, заикается, и единственное, чего ей хочется - это быть не здесь."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_club
    with wipeleft_scene

    show layer screens at ts_showscreens

    "Вчера мы закончили обсуждение «Маленького Принца»."
    "Чтобы не перегружать себя и уж тем более не перегружать Сайори, сегодня я решила дать всему клубу выходной, а со следующей недели уже продолжить работать."

    show yuri 1e at t21
    show sayori 1 at t22

    m "Итак, ребята!"

    "В последние несколько дней я постоянно использовала эту фразу."
    "Можно даже сделать её моей своеобразной фишкой."

    stop music fadeout 3

    m "Поскольку сегодня пятница, и мы только вчера закончили обсуждать нашу первую книгу, сегодняшний день я объявляю свободным днём!"

    show sayori 4r at f22

    "Сайори заметно ожила."

    s "Ура-а-а!"

    show yuri 4b at s21

    "Юри же заметно погрустнела."

    play music ts_think fadein 2

    y 4c "..."
    m "Что, что-то не так?.."
    y "Нет, просто..."
    y 4d "И-и-извините, я на минутку!.."
    show yuri at cright with move
    hide yuri
    "Затем она пулей выносится из класса."
    show sayori 1k at t22
    "Мы с Сайори озадаченно обмениваемся взглядами."


    m "..."
    s 1l "Что же..."
    s 2l "Если надо, то надо..."
    m "Сайори, жди здесь - ты за главную. Я пойду пока поищу её."
    s 1h "Х-хорошо..."

    "В следующую секунду я выбегаю из класса вслед за ней."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_corridor
    with wipeleft_scene

    show layer screens at ts_showscreens

    m "Юри!"

    "Ну и где мне теперь её искать?"

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    show zatemnenie with dspr

    show layer screens at ts_null_transform

    menu:
        "Посмотреть в других классах":
            $ unluck = True
            $ unluck_ball += 1
        "Идти вперёд":
            pass

    hide zatemnenie with dspr
    show layer screens at ts_showscreens

    if unluck == True:
        "Я решаю поискать её в других классах."
        "Всё равно этой частью школы в такое время мало кто пользуется."
        "Она как раз и предназначена либо для клубов, либо для тех детей, которых наказали."
        "Что плохого может случиться?"
        "..."
        "Оказалось, что может."
        show layer screens at ts_hidescreens
        " {w=1.0}{nw}"
        play sound pageflip
        scene ts_class
        with wipeleft_scene
        show layer screens at ts_showscreens
        "Вернее, случилось не то, чтобы плохое... просто неловкое."
        show layer screens at ts_hidescreens
        " {w=1.0}{nw}"
        play sound pageflip
        scene ts_corridor
        with wipeleft_scene
        show layer screens at ts_showscreens
        "Чуть ли не в каждом кабинете, в который я заглядывала, были другие люди. Много людей."
        show layer screens at ts_hidescreens
        " {w=1.0}{nw}"
        play sound pageflip
        scene ts_class
        with wipeleft_scene
        show layer screens at ts_showscreens
        "Господи, было так неловко..."
        show layer screens at ts_hidescreens
        " {w=1.0}{nw}"
        play sound pageflip
        scene ts_corridor
        with wipeleft_scene
        show layer screens at ts_showscreens
        "Дойдя до крайнего кабинета на этаже и не увидев там Юри, я наконец решаю пойти в обратную сторону."
        show layer screens at ts_hidescreens
        " {w=1.0}{nw}"
        play sound pageflip
        scene ts_corridor
        with wipeleft_scene
        show layer screens at ts_showscreens
        "После того, как я зря потратила примерно полчаса на то, чтобы тщетно попытаться найти Юри, я всё-таки решила пойти в другую сторону, до туалетов."
    else:
        "Я решаю направиться к туалетам в конце коридора."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_school_bathroom
    with wipeleft_scene


    show layer screens at ts_showscreens

    "Как только я вхожу в уборную, я замечаю, что нахожусь здесь не одна."

    if unluck == True:
        "Нет, я и так знаю, что в школе не только мы втроём находимся, но... как будто здесь есть кто-то ещё."
    else:
        "Здесь есть кто-то ещё."

    ts_unk "Кх-кх-х..."

    "Кто-то... плачет?"
    "Плач вроде женский..."
    "Нет..."
    "Это какой-то... немного другой звук..."
    "Что логично, одна из кабинок заперта."

    if unluck == True:
        "Ну, всё понятно. Какой-то новичок из Дискуссионного клуба не выдержал позора и ушёл плакать."
        "Вернее, {i}ушла{/i}. Плач-то женский."
        "Хотя, может, это просто ещё маленький мальчик, у которого ещё голос не сломался?"

    "..."
    "Переборов себя, я решаю позвать:"

    m "Здесь есть кто-нибудь?"

    "Ответа нет."
    "Я решаю позвать погромче:"

    show layer screens at vpunch

    m "ЕСТЬ КТО-НИБУДЬ?"

    "Ответом мне послужил ещё один то ли всхлип, то ли что-то ещё."

    ts_unk "Кх-кх-х..."

    if unluck == True:
        "Всхлип всё же довольно низкий как для мальчика, у которого ещё не начался пубертатный период."
    else:
        "Всхлип всё же довольно низкий."

    "Я всё же решаю испытать удачу."

    stop music fadeout 5

    m "Ю-Юри?"

    "Юри, узнав меня, только сильнее начала рыдать."
    "И как я могу помочь ей в этой ситуации?"
    "Если вообще могу..."

    m "Юри..."

    "Все слова поддержки и утешения буквально покинули мой разум, поэтому я просто не нахожусь, что сказать."

    m "Юри... Открой кабинку..."
    y "Нет..."
    "Я решаю действовать более настойчиво, но в то же время вежливо."
    m "Юри, пожалуйста... Открой кабинку, и мы поговорим."
    y "..."
    y "Нет..."
    m "Ладно..."
    
    "Не хочешь по хорошему, будет..."
    "А что будет? Не выломаю же я дверь её кабинки."
    "Это, в конце концов, может её поранить."
    "Надо бы придумать способ получше."
    
    "Хм-м-м..."
    "Кабинки не особо-то и высокие."
    "Нет, я тоже не самая высокая, но я в волейбол пару месяцев играла, и у меня довольно хорошо получалось."
    "Если я просто... подпрыгну... то могу увидеть, чем же таким занимается Юри."
    
    "Однако реальность снова оказалась гораздо более жестокой."
    "Кабинка была слишком высокой, чтобы можно было запрыгнуть и посмотреть через неё."
    "Я попыталась допрыгнуть раз двадцать, не меньше, но всё без толку."
    "Хорошо хоть туфли без каблуков надела! Иначе вся эта затея была бы не только сложнее, но ещё я бы просто напугала Юри."
    "И когда я уже хотела было сдаться, я пересилила себя, и попыталась запрыгнуть один последний раз."
    m "Ну же!"
    
    "Наконец-то я ухватилась за верхние края кабинки и подсмотрела за Юри."

    "Но лучше бы я не подсматривала и оставалась в неведении..."

    show layer screens at ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake)

    show yuri 9z at t11
    
    play music ts_dead_theme fadein 1

    "Передо мной предстала Юри..."
    "Но это... была {b}совершенно{/b} не та Юри, которую я уже успела узнать."
    "Это был не бойкий знаток литературы."
    "Это был не тихий и элегантный цветок лаванды."
    "Это был... совершенно другой человек."
    "Психически нездоровый человек."


    show zatemnenie with dspr

    show screen scenario_2_onest_text_suka
    pause
    hide screen scenario_2_onest_text_suka

    hide zatemnenie with dspr


    "Вся в порезах, вся в крови..."

    show yuri 9p at h11

    "Увидев меня, Юри ахает, быстро откатывает рукав обратно и продолжает рыдать."

    show yuri 1zf at f11

    y "Я не могу так больше!"
    y 1x "В классе надо мной постоянно издеваются..."
    y "Издёвки из-за имени, из-за внешности, даже из-за размера груди!"
    y 1zf "Ну неужели люди такие глупые, что не понимают, что {i}это{/i} ты изменить никак не в состоянии?!"

    show yuri 1y at t11

    "Надо же..."
    "А я ещё первоначально немного завидовала ей, потому что она красивее меня..."
    "Интересно, если её одноклассники так сильно издевались над {i}ней{/i}, то что бы они сделали со {b}мной{/b}?"

    y 1x "Сперва мне удавалось затеряться в книгах, чтобы не выслушивать весь этот бессмысленный бред..."
    y 1z "Но з-затем, к-как-то раз..."
    y 4f "Они п-п-п-п-п-п-п..."

    "Юри вся дрожит и заикается. Очевидно, что ей очень неприятно это вспоминать."

    y 2zf "Они п-порвали мою любимую к-к-к-книжку!.."

    show yuri 4f at s11

    "После этих слов Юри снова начинает бесконтрольно рыдать."
    "А я просто стою и смотрю."


    show zatemnenie with dspr

    show screen chp_text_9
    pause
    hide screen chp_text_9

    hide zatemnenie with dspr

    "Как я могу кого-то утешать, когда меня саму никогда не утешали, и я совершенно не знаю, как это делать?!"



    show zatemnenie with dspr


    show screen chp_text_10
    pause
    hide screen chp_text_10

    hide zatemnenie with dspr

    window hide
    scene yurec_pizdec2 with dspr
    "Я присаживаюсь рядом с Юри."
    "Вдоволь нарыдавшись, Юри наконец продолжает."

    window hide
    scene yurec_pizdec1 with dspr

    y 1x "П-после этого случая... мой внутренний голос начал твердить мне, что так мне и нужно."

    window hide
    scene yurec_pizdec3 with dspr

    y "Ч-что я на самом деле какая-то... дефектная..."
    y "Что мне на самом деле нравится быть неполноценной, а всё это время я просто это скрывала..."
    if persistent.cens_mode == True:
        y "Что я просто ебанушка, которая любит ножи..."
    else:
        y "Что я просто ненормальная, которая любит ножи..."
    y "Ч-что у меня так никогда и не будет никаких друзей..."

    stop music fadeout 4

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    pause 2

    show layer screens at ts_showscreens

    m "Уже есть."
    y "Ч-что?"

    window hide
    scene yurec_pizdec4 with dspr

    m "Я говорю, друзья у тебя уже есть."
    y 1zh "Н-не понимаю..."

    play music ts_idby

    "Воодушевлённая тем, что я уместно прервала её монолог, я начинаю говорить."

    window hide
    scene yurec_pizdec5 with dspr

    m "Понимаешь... Мы с тобой на самом деле гораздо ближе, чем может показаться на первый взгляд."
    m "У меня... тоже нет никаких друзей."

    "Я старательно не вспоминаю Каори."

    m "До того, как я создала этот клуб и пришли вы с Сайори, друзей у меня не было."

    "Я буквально хожу по минному полю. Одно неправильное слово, и эта лавандовая девочка снова разрыдается."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"


    show zatemnenie with dspr

    show layer screens at ts_showscreens

    show screen chp_text_11
    pause
    show layer screens at ts_hidescreens
    show screen chp_text_11
    pause 1
    hide screen chp_text_11

    hide zatemnenie with dspr

    show layer screens at ts_showscreens

    "Я отгоняю от себя эти назойливые мысли и продолжаю."

    m "Да, у меня статус местной знаменитости, я ходила во многие клубы, и даже была главной или одной из главных."

    window hide
    scene yurec_pizdec6 with dspr

    m "Но, знаешь..."
    m "Я бы с огромным удовольствием променяла бы это всё на то, чтобы так же, как и ты, просто сидеть и не отсвечивать."

    "После каждого предложения я посматриваю на Юри и думаю, не ошиблась ли я."
    "Но поскольку она ещё не рыдает, а, наоборот, даже утёрла слёзы, я пока справляюсь хорошо."

    m "Я создала этот клуб, поскольку меня уже буквально тошнит от всех этих интрижек других крупных клубов."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"


    show zatemnenie with dspr

    show layer screens at ts_showscreens

    show screen chp_text_12
    pause
    show layer screens at ts_hidescreens
    show screen chp_text_12
    pause 1
    hide screen chp_text_12


    show layer screens at ts_showscreens

    show screen scenario_2_onest_text_suka1
    pause
    show layer screens at ts_hidescreens
    show screen scenario_2_onest_text_suka1
    pause 1
    hide screen scenario_2_onest_text_suka1

    hide zatemnenie with dspr

    show layer screens at ts_showscreens

    "Так вот..."

    window hide
    scene yurec_pizdec8 with dspr

    m "И основное правило моего клуба заключается в том, что здесь не будет слова «неправильно»."
    m "Но... это касается не только стилей литературы... но и самих людей тоже."
    m "Не бывает «неправильных» людей. Есть только «другие» люди, «особенные» люди."

    window hide
    scene yurec_pizdec9 with dspr

    "Впервые с момента нашей встречи Юри мне улыбнулась."
    "Значит, я всё делаю правильно!"

    m "Каждый человек уникален. Да, у каждого есть свои грешки, но хуже от этого мы не становимся."
    m "Да, ты себя режешь. И что, ты от этого плохим человеком стала быть?"
    m "Никакая ты не дефектная!"
    m "Ты же умная, красивая, начитанная!"
    m "И... скажу тебе по секрету..."

    window hide
    scene yurec_pizdec4 with dspr

    m "Когда я впервые тебя увидела, то я даже слегка завидовала тебе... особенно... некоторым... частям тебя."
    m "А если тебя кто-нибудь когда-нибудь оскорбит - приди ко мне."
    m "Вместе мы покажем любому нахалу, чего мы стоим."
    y 2v "Но я же...{nw}"
    m "Тс-с-с..."
    m "Не говори ничего..."

    stop music fadeout 5

    "Однако я осознаю, что мне тоже больше нечего сказать."
    "Поэтому мы вдвоём просто сидим на полу уборной. Юри ещё некоторое время всхлипывает, а я просто время от времени глажу её по волосам."
    "Такие длинные, шёлковые, мягкие..."
    "Нет, мне и своих волос хватает, но была бы моя воля, я бы хотела отрастить такие же волосы, как у неё."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_school_bathroom
    with wipeleft_scene

    show layer screens at ts_showscreens

    "Спустя десять минут Юри наконец заговаривает."

    show yuri 2q at t11

    y "М-может, пойдём обратно уже? С-Сайори наверняка нас уже заждалась."

    "Чёрт. Со всей этой историей я совсем забыла о ней."

    m "Точно! Сайори!"

    show yuri 2n at h11

    play sound door_break
    window hide
    play music t6r
    scene ts_corridor at ts_razebal
    pause 0.3
    scene ts_corridor at ts_beg
    pause 2

    show layer screens at ts_showscreens

    "Я быстро выбегаю из уборной. Юри, не теряя времени, выбегает вслед за мной."

    play sound door_break
    stop music
    
    play music audio.t2
    window hide
    scene ts_club at ts_razebal
    show sayori 4j at t21
    show yuri 2n at t22

    show layer screens at ts_showscreens

    s "Явились, не запылились!"
    s "Где вас только черти носили?!"

    show sayori 3i at f21

    m "А мы, э-э-э..."

    "Внезапно для всех, и в первую очередь, для себя же, голос подала Юри."

    y 2k "Мы с Моникой были в туалете."

    show sayori 3o at t21

    y 3q "Видишь ли, у меня началась... менструация..."
    s 1l "Л-ладно..."
    s 3j "Хотя нет, не ладно! Это вообще ничего не объясняет!"

    show sayori 3o at s21

    y 2o "Очень о-обильная... менструация..."

    show yuri 2k at f22

    "Собравшись с духом, Юри продолжила."

    y 1j "Вот Моника и помогала мне, предложив мне тампон..."
    y 2q "П-правда... Я н-не знала, как им п-пользоваться... У меня в-всё это время п-прокладки были..."

    "Тут поддержала легенду и я."

    m "Д-да!"

    if unluck == True:
        m "Я сначала долго искала Юри, пробежалась по всем классам, и только потом поняла, что она в туалете была."
        m "А уже п-потом я помогала ей разобраться с тампоном."
    else:
        m "А я помогала ей разобраться с тампоном."

    s 3j "Ла-а-адно..."
    show sayori 3i at t21
    "Мы с Юри негласно решили хранить эту её «проблему» в строжайшем секрете."
    "Точно в таком же секрете, как и тему с депрессией Сайори."
    "Хотя, может, это и не депрессия вовсе? Точно не знаю..."
    "Но для своего удобства я буду называть проблемы Сайори именно депрессией."
    "И пока она не предъявила новые обвинения, я быстро решаю соскочить с темы на саму Сайори."

    m "Ну а ты, Сайори, чем занималась, пока нас не было?"
    s 2l "Да я-э-э-э..."
    s 1zc "Впрочем, неважно."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play music ts_dreams fadein 3
    play sound pageflip
    scene ts_club
    show sayori 1a at t21
    show yuri 1a at t22
    with wipeleft_scene

    show layer screens at ts_showscreens

    "Ну что же, так тому и быть."
    "Впрочем, такое количество секретов на таком начальном этапе - это не совсем хорошо..."
    "Я имею в виду, мы же даже ещё не официально зарегистрированный клуб, а уже храним кучу тайн, в том числе и тайн друг друга."
    "{i}Депрессия{/i} Сайори, самовред Юри, моё... всякое..."
    "Что же будет, когда нас будет хотя бы четверо?"
    "А если даже больше?"
    "..."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"
    stop music fadeout 7
    scene black with ed_night_dis

    show layer screens at ts_null_transform

    jump ts_scenario_3