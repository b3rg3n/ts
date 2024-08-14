label ts_scenario_0:

    python: # ОБНОВЛЯЕМ RPC
        try:
            rpc.update(state="Акт I | Пролог",details="Предыстория",large_image="prologue",start=time.time())
        except AssertionError:
            pass

    $ persistent.rpclabel = "0"

    $ persistent.carter2menu = False
    $ persistent.carter3menu = False
    $ persistent.badendmenuperedglitch = False
    $ persistent.badendmenuskipglitch = False
    $ persistent.badendmenu = False
    $ persistent.goodendmenu = False
    $ persistent.peredbadendmenu = False
    $ persistent.peredgoodendmenu = False

    $ save_name = "Предыстория"
    window hide
    pause 1.1
    window hide
    stop music fadeout 4
    scene black
    with ed_night_dis
    pause 1
    play music ts_emmk fadein 4
    scene ts_house
    show zatemnenie
    show dust1
    show dust2
    show dust3
    show dust4
    with ed_night_dis
    $ Chapter("Предыстория")
    pause 0.5
    hide zatemnenie with dspr

    show layer screens at ts_showscreens_nvl

    $ persistent.sprite_time = "cloudly"

    nvlbazar "{font=[prologue_font]}Конечно же, всё начиналось совсем по-другому..."
    nvlbazar "{font=[prologue_font]}Всё начиналось как у остальных людей: родилась, пошла в школу, выучилась... Правда, ещё не до конца, но всё же."
    nvlbazar "{font=[prologue_font]}С самого детства взрослые называли меня «одарённой девочкой»."
    nvlbazar "{font=[prologue_font]}Что во мне такого «одарённого»? В ранние годы я этого не понимала. Но,\nкак говорится, «кто я такая, чтобы спорить со взрослыми?»."
    nvlbazar "{font=[prologue_font]}«Маленькая ещё»... «Не доросла ещё»... «Подрастёшь - поймёшь»... Продолжать можно до бесконечности…"

    nvl clear

    nvlbazar "{font=[prologue_font]}Однако, оглядываясь назад, я поняла: что-то одарённое во мне\nдействительно было."

    nvl clear

    nvlbazar "{font=[prologue_font]}В три года я научилась читать. К пяти годам я уже знала всю базовую таблицу умножения."

    show layer screens at ts_hidescreens_nvl
    nvlbazar " {w=1.0}{nw}"

    nvl clear

    stop ambience
    play sound pageflip
    scene ts_class
    show dust1
    show dust2
    show dust3
    show dust4
    with wipeleft_scene

    show layer screens at ts_showscreens_nvl

    nvlbazar "{font=[prologue_font]}Дальше, уже в школе, пока остальные до сих пор учили буквы, я уже невообразимо быстро читала."
    nvlbazar "{font=[prologue_font]}А пока остальные до сих пор складывали два плюс два, я без калькулятора уже могла перемножать двузначные числа."
    nvlbazar "{font=[prologue_font]}И это мне быстро наскучило: пока остальные на самом деле чему-то учились, я просто витала в облаках."

    nvl clear

    nvlbazar "{font=[prologue_font]}Потому что я уже всё это знала."

    nvl clear

    nvlbazar "{font=[prologue_font]}Но учителя думали, что я витаю в облаках не из-за того, что я знаю гораздо больше, чем обычный первоклассник, а из-за того, что я очень глупая."
    nvlbazar "{font=[prologue_font]}Или, может, это была пресловутая жадность учителей, которым захотелось поднять лёгких денег на «глупой Монике». Этого я уже достоверно не знаю, да и знать не могу."
    nvlbazar "{font=[prologue_font]}В любом случае, после очередного родительского собрания, на котором, по всей видимости, меня в очередной раз гнобили и принижали, папа этого не стерпел."
    nvlbazar "{font=[prologue_font]}И отдал меня в другую, специализированную школу."

    show layer screens at ts_hidescreens_nvl
    nvlbazar " {w=1.0}{nw}"

    nvl clear

    stop ambience
    play sound pageflip
    scene ts_l5old
    show dust1
    show dust2
    show dust3
    show dust4
    with wipeleft_scene

    show hiroto 1b at ln11

    show layer screens at ts_showscreens

    ts_ft "Хочешь в школу к Мире?"

    show hiroto 1a at t11

    show layer screens at vpunch
    m "Конечно!"
    ts_ft 1b "Тогда скажи до свидания этой школе."
    ts_ft "С завтрашнего дня у тебя будет новая жизнь в {i}новой{/i} школе."

    show hiroto 1a at t11

    show layer screens at vpunch
    m "До свидания, школа!"

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    show hiroto 1a at ron11
    pause 0.3
    hide hiroto with dissolve

    show layer screens at ts_showscreens_nvl

    nvlbazar "{font=[prologue_font]}Нет, гением я себя назвать не могу, пусть даже и результат был лучше, чем у большинства детей моего возраста."
    nvlbazar "{font=[prologue_font]}Но помимо чтения, таблицы умножения и прочего, такого важного в начальной школе, и такого бесполезного во всём остальном…"
    nvlbazar "{font=[prologue_font]}Я совершенно не знала, как взаимодействовать с людьми."
    nvlbazar "{font=[prologue_font]}Друзей и подруг можно пересчитать по пальцам одной руки."
    show kuninobu 1ba at t11
    nvlbazar "{font=[prologue_font]}Сначала у меня была одна подружка. Звали её Мира."
    show kuninobu 2bb at t11
    nvlbazar "{font=[prologue_font]}Наши родители и её родители дружили семьями. Как и мы сами, собственно."

    show layer screens at ts_hidescreens_nvl
    nvlbazar " {w=1.0}{nw}"

    nvl clear

    stop ambience
    play sound pageflip
    scene ts_residential
    show dust1
    show dust2
    show dust3
    show dust4
    with wipeleft_scene

    show layer screens at ts_showscreens_nvl
    
    show kuninobu 2bv at t11
    nvlbazar "{font=[prologue_font]}Мы постоянно ходили друг к другу в гости, где постоянно играли друг с другом."
    show kuninobu 2bz at t11
    nvlbazar "{font=[prologue_font]}Мира была немного старше меня, но мы с ней как будто были на одной волне."

    nvl clear

    nvlbazar "{font=[prologue_font]}У неё была ещё старшая сестра, однако сестра эта была от другого брака, да и была она намного старше нас с Мирой."
    nvlbazar "{font=[prologue_font]}Поэтому ни о какой дружбе между мной и ей не могло быть и речи. Уважать друг друга - да. Дружить - уж извольте."

    show layer screens at ts_hidescreens_nvl
    nvlbazar " {w=1.0}{nw}"
    nvl clear

    stop ambience
    play sound pageflip
    scene ts_l5
    show dust1
    show dust2
    show dust3
    show dust4
    with wipeleft_scene

    show layer screens at ts_showscreens_nvl

    show kuninobu 3br at t11
    nvlbazar "{font=[prologue_font]}Однако, когда я пришла в школу к Мире, она как будто отдалилась от меня."
    nvlbazar "{font=[prologue_font]}Оказалось, что у Миры были и свои подруги, с которыми она росла вместе на одной улице, и подруги эти с каким-то презрением смотрели на «какую-то странную девочку»."
    nvlbazar "{font=[prologue_font]}А иногда и вообще смотрели на меня, как на пустое место."
    show kuninobu 2bff at t11
    nvlbazar "{font=[prologue_font]}Нет, вне школы мы продолжали дружить. Мы до сих пор играли вместе, а когда мы стали чуть старше, мы неоднократно ездили в один и тот же лагерь."
    nvlbazar "{font=[prologue_font]}Но и там Мира находила новых друзей и подруг, и они как бы невзначай забывали про меня."
    show kuninobu at thide
    hide kuninobu
    nvlbazar "{font=[prologue_font]}Так что внутри я до сих пор оставалась одинокой."
    nvlbazar "{font=[prologue_font]}Но затем к нам в школу пришла {i}она{/i}."

    nvl clear

    show kaori 22a at ln11

    nvlbazar "{font=[prologue_font]}Её звали Каори. И она была чуть ли не полной противоположностью меня."
    nvlbazar "{font=[prologue_font]}Я была спокойной девочкой."
    show kaori 23c at h11
    nvlbazar "{font=[prologue_font]}Каори была неугомонной."
    show kaori 22a at s11
    nvlbazar "{font=[prologue_font]}Я была неприступной девочкой, для которой нужно сделать что-то стоящее, чтобы со мной подружиться."
    show kaori 23s at h11
    nvlbazar "{font=[prologue_font]}Каори же считала, что каждый, кто провёл с ней больше пяти минут, теперь её друг."
    nvl clear
    
    show kaori 22a at s11
    nvlbazar "{font=[prologue_font]}Я была (да и остаюсь) круглой отличницей."
    show kaori 21v at d11
    nvlbazar "{font=[prologue_font]}Каори была троечницей, с трудом сдавая почти все предметы."
    show kaori 23c at h11
    nvlbazar "{font=[prologue_font]}Каори была очень открытым человеком."
    show kaori 22b at s11
    nvlbazar "{font=[prologue_font]}Я же, наоборот, старалась закрыться ото всех."
    show kaori 22zb at h11
    nvlbazar "{font=[prologue_font]}Однако, как это и бывает во всех этих историях, противоположности притягиваются."
    show kaori 22c at h11
    nvlbazar "{font=[prologue_font]}Мы всё делали вместе, и во всём помогали друг другу."
    nvlbazar "{font=[prologue_font]}Мы ели вместе, мы играли вместе, мы постоянно приходили друг к другу..."
    show kaori 22r at h11
    nvlbazar "{font=[prologue_font]}Прогуливали школу мы тоже вместе. Хотя и было это всего один или два раза."
    nvlbazar "{font=[prologue_font]}Честное слово."
    nvlbazar "{font=[prologue_font]}Мы разве что не спали вместе."

    nvl clear

    show kaori 22a at s11
    nvlbazar "{font=[prologue_font]}Мои родители хорошо относились к Каори, и, в свою очередь, мама Каори хорошо относилась ко мне."
    nvlbazar "{font=[prologue_font]}Вы меня, конечно, спросите, «что, только мама? Папа к тебе не хорошо относился?»"
    show kaori 21u at d11
    nvlbazar "{font=[prologue_font]}Но... Дело в том, что... у Каори нет отца, и воспитывала её одна только мать."
    nvlbazar "{font=[prologue_font]}И мало ей хлопот на свою голову в виде Каори, сама она ко всему прочему была ещё и глухонемой."
    nvl clear


    show kaori 22w at s11
    nvlbazar "{font=[prologue_font]}Нет, полностью глухонемой она не была, какие-то звуки она издавала."
    nvlbazar "{font=[prologue_font]}Как, знаете... как человек, который упал в ледяную воду."
    nvlbazar "{font=[prologue_font]}Я точно не знаю, как это осложнение называется, да и знать я не хочу, но суть примерно такая."
    show kaori 23f at d11
    nvlbazar "{font=[prologue_font]}В любом случае, Каори успешно общалась с мамой на языке жестов. Я же просто писала ей, потому что я языка жестов не знаю, а она, соответственно, писала мне в ответ."
    nvlbazar "{font=[prologue_font]}В общем, один {i}настоящий{/i} друг детства у меня был."
    nvlbazar "{font=[adv_font]}Ура-а-а, достижение, у тебя был хоть кто-то, кто о тебе заботился."
    show kaori at thide
    hide kaori
    nvl clear

    $ persistent.sprite_time = "day"

    nvlbazar "{font=[prologue_font]}Кстати, совсем забыла вас познакомить."
    nvlbazar "{font=[prologue_font]}Хотя, {i}познакомить{/i} кажется не совсем правильным словом..."
    nvlbazar "{font=[prologue_font]}Но с самого детства у меня были очень навязчивые мысли."
    nvl clear
    
    nvlbazar "{font=[prologue_font]}Мысли о том, что я бездарность."
    nvlbazar "{font=[prologue_font]}Мысли о том, что у меня ничего не получится."
    nvlbazar "{font=[prologue_font]}Мысли о том, что если с первого раза я не добилась особых успехов, то оно мне и в принципе не нужно."
    nvl clear
    
    nvlbazar "{font=[prologue_font]}С годами мысли становились всё более навязчивыми, и порой даже вытесняли мой собственный разум."
    nvlbazar "{font=[adv_font]}И порой это даже и к лучшему. Вспомни хотя бы, как ты пересилила себя, и устроилась на подработку спасателем на лето в прошлом году."
    nvlbazar "{font=[adv_font]}Если бы не я, то ты бы даже и не попыталась, и всё лето просидела бы на одном месте."
    nvl clear

    nvlbazar "{font=[prologue_font]}Мы не о подработке говорим, а о жизни. Поэтому {i}пожалуйста{/i}, не мешай."
    show kaori 21o at h11
    nvlbazar "{font=[prologue_font]}Почему у меня «был» друг детства? А потому что после нескольких лет чистой и искренней дружбы Каори перевели в другую школу. А я снова осталась одна."
    nvlbazar "{font=[prologue_font]}«Постаралась» бабушка Каори."
    nvlbazar "{font=[prologue_font]}Как бы ни была против я, как бы ни думали и мои родители, что это совершенно нелогично, против семьи не попрёшь."
    nvlbazar "{font=[prologue_font]}Особенно против такого напористого члена семьи, как бабушка Каори."

    show layer screens at ts_hidescreens_nvl
    nvlbazar " {w=1.0}{nw}"
    nvl clear
    show kaori at ron11
    pause 0.3
    hide kaori with dissolve
    show layer screens at ts_showscreens_nvl

    nvlbazar "{font=[prologue_font]}А я снова осталась один на один с этим жестоким миром."
    nvlbazar "{font=[prologue_font]}Совсем одна. И больше у меня нет никаких друзей, никаких парней, ничего и никого, что могло бы заполнить эту зияющую пустоту."
    nvlbazar "{font=[prologue_font]}И за годы дружбы, которая казалась вечной, я даже не смогла удосужиться найти себе новых настоящих друзей."
    nvlbazar "{font=[prologue_font]}Нет, у меня были какие-то знакомые, и даже хорошие знакомые, но друзьями назвать их у меня язык не повернётся."

    show layer screens at ts_hidescreens_nvl
    nvlbazar " {w=1.0}{nw}"
    nvl clear

    stop ambience
    play sound pageflip
    scene ts_class
    show dust1
    show dust2
    show dust3
    show dust4
    with wipeleft_scene

    show layer screens at ts_showscreens_nvl

    nvlbazar "{font=[prologue_font]}Но это мы уже слишком далеко зашли. Сначала немного откатимся в прошлое."
    nvlbazar "{font=[prologue_font]}Родители всегда требовали от меня становиться лучше. Стараться лучше. {i}Быть{/i} лучше."
    nvlbazar "{font=[prologue_font]}Каждый раз, когда я получала тройку, или даже четвёрку, хотя это и было редко, папа каждый раз раздувал из этого целое событие."
    nvlbazar "{font=[prologue_font]}И хорошо, если он ограничивался тем, что я, его мнению, «чёртова двоечница»."
    nvlbazar "{font=[prologue_font]}Но по большей части родители каждый раз читали мне морали, и растягивается это всё часа на два."
    nvlbazar "{font=[prologue_font]}А если они ещё и пьяные, то, как говорится, пиши пропало."

    nvl clear

    nvlbazar "{font=[prologue_font]}Нет, мои родители не алкоголики, напротив, они выпивают довольно редко, они добрейшей души люди, и очень часто меня поддерживают, если я пробую что-то новое."
    nvlbazar "{font=[prologue_font]}Но когда дело касалось учёбы, и когда я в их глазах была не идеальной девочкой, они устраивали разнос."
    nvlbazar "{font=[prologue_font]}Причём они очень часто повторялись в своих моралях."
    nvlbazar "{font=[prologue_font]}Так что, даже несмотря на то, что читали они мне их нечасто, я уже чуть ли не наизусть знала, кто и что конкретно мне будет говорить."
    nvlbazar "{font=[prologue_font]}Я же, в свою очередь, хотя и была прилежной ученицей, и до сих пор остаюсь отличницей, на самом деле была лентяйкой, каких только поискать надо."


    nvl clear


    nvlbazar "{font=[prologue_font]}Где-то класса с седьмого меня таскали по всяким разным клубам, потому что учителя думали, что такая хорошая и прилежная девочка обязательно станет отличным дополнением к клубу."
    nvlbazar "{font=[prologue_font]}На первых порах, когда я ещё была недостаточно взрослой и самостоятельной, я просто покорно слушалась."
    nvlbazar "{font=[prologue_font]}Да и таскали меня по тем клубам, против которых я хотя бы ничего не имела."
    nvlbazar "{font=[prologue_font]}Сначала это был Книжный клуб."
    nvlbazar "{font=[prologue_font]}Я в детстве довольно много читала, поэтому учителя подумали, что логично было отправить меня именно в Книжный клуб."

    show layer screens at ts_hidescreens_nvl
    nvlbazar " {w=1.0}{nw}"
    nvl clear

    stop ambience
    play sound pageflip
    scene ts_club2re
    show dust1
    show dust2
    show dust3
    show dust4
    with wipeleft_scene

    show layer screens at ts_showscreens_nvl

    nvlbazar "{font=[prologue_font]}Даже несмотря на то, что с годами читала я уже заметно меньше, а последнюю книгу я прочла где-то за год до того, как меня записали в Книжный клуб."
    nvlbazar "{font=[prologue_font]}Когда папа заставил меня прочитать «Графа Монте-Кристо» в одиннадцать лет, у меня просто пропало желание читать хоть что-то."
    nvlbazar "{font=[prologue_font]}Я всё равно довольно успешно справлялась. Я даже была вице-президентом клуба."
    nvlbazar "{font=[prologue_font]}Но мне это просто очень быстро наскучило, поэтому к концу года я вышла из клуба с твёрдым желанием найти себе клуб получше."

    show layer screens at ts_hidescreens_nvl
    nvlbazar " {w=1.0}{nw}"
    nvl clear

    stop ambience
    play sound pageflip
    scene ts_pianoend
    show dust1
    show dust2
    show dust3
    show dust4
    with wipeleft_scene

    show layer screens at ts_showscreens_nvl

    nvlbazar "{font=[prologue_font]}В следующем году меня направили в Музыкальный клуб. И поначалу мне это действительно нравилось."
    nvlbazar "{font=[prologue_font]}У дедушки было пианино, и я, ещё будучи ребёнком, время от времени наобум стучала по клавишам, поэтому, когда мне предложили выбрать инструмент, я без раздумий указала на пианино."
    nvlbazar "{font=[prologue_font]}Да, школьное пианино было далеко не первого качества, и играть я, по сути, не умела..."

    show layer screens at ts_hidescreens_nvl
    nvlbazar " {w=1.0}{nw}"
    nvl clear

    stop ambience
    scene mon_piano_start
    show dust1
    show dust2
    show dust3
    show dust4
    with poplil_pacan

    show layer screens at ts_showscreens_nvl

    nvlbazar "{font=[prologue_font]}Но мне это было и не важно."
    nvlbazar "{font=[prologue_font]}Мне это нравилось."
    nvlbazar "{font=[prologue_font]}Я быстро научилась играть несколько простых песенок."

    show layer screens at ts_hidescreens_nvl
    nvlbazar " {w=1.0}{nw}"
    nvl clear

    stop ambience
    play sound pageflip
    scene ts_pianoend
    show dust1
    show dust2
    show dust3
    show dust4
    with wipeleft_scene

    show layer screens at ts_showscreens_nvl

    nvlbazar "{font=[prologue_font]}Но... Помните, как я говорила, что я невообразимая лентяйка?"
    nvlbazar "{font=[prologue_font]}Так вот: может, это просто лень, а может, расстройство посерьёзнее, но как только дело дошло до композиций посложнее, я разленилась."
    nvlbazar "{font=[prologue_font]}И дело даже не в том, что я не хотела учиться, или не могла – с должным старанием всё должно получиться."
    nvlbazar "{font=[prologue_font]}Мне просто стало лень."

    nvl clear

    nvlbazar "{font=[prologue_font]}В итоге вместо того, чтобы развиваться, я постоянно играла одни и те же пять простых песенок, которые мы разучивали на первых собраниях."
    nvlbazar "{font=[prologue_font]}А когда мне намекнули, что клуб играет уже и более сложные композиции, и что пора бы и мне самой улучшить свои навыки, чтобы я не была слабым звеном, я просто хмыкнула и ушла сама."
    nvlbazar "{font=[prologue_font]}И хотя технически на пианино я играть умею, фактически я умею играть на пианино примерно так же, как если бы не умела вовсе."
    nvlbazar "{font=[prologue_font]}Особенно с учётом того, что это было уже несколько лет назад..."
    nvlbazar "{font=[prologue_font]}А когда ты ещё так молода, тебе кажется, что несколько лет назад были как будто в прошлой жизни."

    show layer screens at ts_hidescreens_nvl
    nvlbazar " {w=1.0}{nw}"
    nvl clear

    stop ambience
    play sound pageflip
    scene ts_gym
    show dust1
    show dust2
    show dust3
    show dust4
    with wipeleft_scene

    show layer screens at ts_showscreens_nvl

    nvlbazar "{font=[prologue_font]}После приключений с Музыкальным клубом меня потянуло в спорт."
    nvlbazar "{font=[prologue_font]}Нет, в хоккей и в прочие преимущественно мужские виды спорта, где в основном нужна грубая сила, а не утончённость, я не играла."
    nvlbazar "{font=[prologue_font]}В конце концов, я же девочка, а не бугай двухметровый..."
    nvlbazar "{font=[prologue_font]}Но наш учитель физкультуры как-то обмолвился, что у нас скоро городские соревнования между школами по волейболу."
    nvlbazar "{font=[prologue_font]}А я как раз неплохо играла в волейбол, поэтому и вызвалась добровольцем."

    nvl clear

    nvlbazar "{font=[prologue_font]}На городских соревнованиях все другие школы просто стёрли нас в пух и прах, но папа всегда говорил, что я играла лучше всех."
    nvlbazar "{font=[prologue_font]}Может, он и предвзят, а может, так всё и самом деле было, это уже было неважно."
    nvlbazar "{font=[prologue_font]}Помимо этого, я уже много лет занималась настольным теннисом, и даже неоднократно ездила на соревнования по городу."
    nvlbazar "{font=[prologue_font]}Опять же, звёзд с неба я не хватала, и я так ни разу ничего и не выиграла, но это был весёлый и интересный опыт."

    nvl clear

    nvlbazar "{font=[prologue_font]}И наконец, папа в детстве научил меня играть в шахматы."
    nvlbazar "{font=[prologue_font]}Однако, как и во всех остальных видах спорта, в шахматах я тоже была не так уж и сильна."

    nvl clear

    nvlbazar "{font=[prologue_font]}Да, с годами я начала обыгрывать папу, всех его друзей, всех моих немногочисленных друзей, просто знакомых и незнакомых людей…"
    nvlbazar "{font=[prologue_font]}Но мне ещё было очень далеко до того, чтобы играть в те же шахматы на деньги и зарабатывать этим на жизнь."
    nvlbazar "{font=[prologue_font]}Может, это пресловутая лень."
    nvlbazar "{font=[prologue_font]}А может... да нет, не может, это всё только потому, что я ленюсь."
    nvlbazar "{font=[prologue_font]}Ведь папа же говорил, что «с должным старанием всё должно получиться»."
    nvlbazar "{font=[prologue_font]}А если не получается, то это лишь значит, что ты недостаточно стараешься."
    nvlbazar "{font=[prologue_font]}И ведь спорить с папой было бессмысленно, ведь папа же взрослый, мудрый..."
    nvlbazar "{font=[prologue_font]}А я что? Всего лишь какая-то маленькая лентяйка, которая, хоть Бог и наделил талантами, все их успешно закопала..."
    
    nvl clear

    nvlbazar "{font=[prologue_font]}Со стороны другим людям казалось, что я умею очень многое."
    nvlbazar "{font=[prologue_font]}Однако внешность бывает очень обманчива. Сама я знаю, что хоть и я умею многое, но я всё умею плохо."
    nvlbazar "{font=[prologue_font]}Что я лентяйка и вообще бездарность."
    nvlbazar "{font=[prologue_font]}Другим казалось, что я мастер на все руки."
    nvlbazar "{font=[prologue_font]}Я же знаю, что так-то оно так, только руки у меня не совсем из правильного места растут..."

    show layer screens at ts_hidescreens_nvl
    nvlbazar " {w=1.0}{nw}"
    nvl clear

    stop ambience
    play sound pageflip
    scene ts_class
    show dust1
    show dust2
    show dust3
    show dust4
    with wipeleft_scene

    show layer screens at ts_showscreens_nvl

    nvlbazar "{font=[prologue_font]}В прошлом году меня перевели в другой класс."
    nvlbazar "{font=[prologue_font]}Все эти люди казались мне совершенно незнакомыми. Впрочем, кроме Каори, со мной и в прошлом классе особо никто не общался."
    nvlbazar "{font=[prologue_font]}Но Каори перевели в другую школу. Так что я как была одна-одинокая, так и после того, как меня перевели в другой класс, ситуация не улучшилась."
    nvlbazar "{font=[prologue_font]}Правда, был один паренёк... Мицуо, кажется?"
    nvlbazar "{font=[prologue_font]}Однако, учитывая мой статус «гордости школы», он, в силу своей стеснительности, боялся со мной даже заговорить."
    nvlbazar "{font=[prologue_font]}Я за весь год от него не услышала ни одного предложения, ни одного вопроса, даже ни единого слова."

    nvl clear

    nvlbazar "{font=[prologue_font]}Впрочем, неважно, помимо него, у меня ещё был целый класс незнакомцев и незнакомок."
    nvlbazar "{font=[prologue_font]}Одним незнакомцем больше, одним незнакомцем меньше... Какая вообще разница?"

    nvl clear

    nvlbazar "{font=[prologue_font]}В этом же году я вступила в Дискуссионный клуб."
    nvlbazar "{font=[prologue_font]}Учитывая мою общую эрудицию, начитанность, и вышеупомянутый статус гордости школы, я быстро поднялась до главенствующих позиций, вплоть до президента клуба."
    nvlbazar "{font=[prologue_font]}Вместе с этим и сам клуб становился больше. Даже больше, чем мне бы самой этого хотелось."
    nvlbazar "{font=[prologue_font]}А сами дискуссии из разносторонних постепенно превращались в однотипные."
    nvlbazar "{font=[prologue_font]}И если мы раньше спорили буквально обо всём на свете, то сейчас мы только и спорим, что о бюджете да о подготовке к тому или иному мероприятию."

    nvl clear

    nvlbazar "{font=[prologue_font]}В итоге вся эта интрижка крупного клуба становилась выше меня, вплоть до того момента, когда я не могла ей ничего противопоставить."
    nvlbazar "{font=[prologue_font]}Так что я просто попросилась, чтобы меня сняли с должности, а сама я ушла в закат, оставив эти интрижки для кого-то другого."
    nvlbazar "{font=[prologue_font]}Пусть другие это расхлёбывают. Не я."

    show layer screens at ts_hidescreens_nvl
    nvlbazar " {w=1.0}{nw}"
    nvl clear

    stop ambience
    play sound pageflip
    scene ts_class
    show dust1
    show dust2
    show dust3
    show dust4
    with wipeleft_scene

    show layer screens at ts_showscreens_nvl

    stop music fadeout 10
    nvlbazar "{font=[prologue_font]}Пришло время выпускного года. И я, побывав уже во многих клубах, примерно понимаю, что я хочу и чего я не хочу видеть в своём клубе."
    nvlbazar "{font=[prologue_font]}Я хочу, чтобы в моём клубе не было слова «неправильно»."
    nvlbazar "{font=[prologue_font]}Я хочу, чтобы в моём клубе каждый мог выражаться, как его душе может быть угодно."
    nvlbazar "{font=[prologue_font]}Я хочу, чтобы в моём клубе мы делились чем-то личным, чем-то сокровенным."
    nvlbazar "{font=[prologue_font]}Решение пришло само собой. Я знаю, какой именно клуб я хочу открыть."
    nvlbazar "{font=[prologue_font]}Литературный клуб."

    stop ambience

    nvl clear

    window hide
    stop music
    play sound br_glitch
    show ts_club2re as bg1 at Glitch(_fps=160, glitch_strength=1)
    $ renpy.pause(1.1, hard=True)
    stop sound
    scene black
    play music ts_new_zastavka_ost_suka fadein 2
    pause 1
    show text "{font=mod_assets/source/fonts/Surfbars.otf}{size=50}Я говорила - ты слушал.\nИ так было всегда.{/size}{/font}":
        xalign 0.5 yalign 0.5
        zoom 0.4 alpha 0
        ease 1.5 zoom 1.0 alpha 1
    pause 3
    show text "{font=mod_assets/source/fonts/Surfbars.otf}{size=50}Я говорила - ты слушал.\nИ так было всегда.{/size}{/font}":
        xalign 0.5 yalign 0.5
        zoom 1.0 alpha 1
        ease 1.5 zoom 0.4 alpha 0
    pause 3
    show text "{font=mod_assets/source/fonts/Surfbars.otf}{size=50}Правда, [user]?{/size}{/font}":
        xalign 0.5 yalign 0.5
        zoom 0.4 alpha 0
        ease 1.5 zoom 1.0 alpha 1
    pause 3
    show text "{font=mod_assets/source/fonts/Surfbars.otf}{size=50}Правда, [user]?{/size}{/font}":
        xalign 0.5 yalign 0.5
        zoom 1.0 alpha 1
        ease 1.5 zoom 0.4 alpha 0
    pause 3
    show text "{font=mod_assets/source/fonts/Surfbars.otf}{size=50}В моменте я перестаю различать:\nгде сон, а где реальность.{/size}{/font}":
        xalign 0.5 yalign 0.5
        zoom 0.4 alpha 0
        ease 1.5 zoom 1.0 alpha 1
    pause 3
    show text "{font=mod_assets/source/fonts/Surfbars.otf}{size=50}В моменте я перестаю различать:\nгде сон, а где реальность.{/size}{/font}":
        xalign 0.5 yalign 0.5
        zoom 1.0 alpha 1
        ease 1.5 zoom 0.4 alpha 0
    pause 3
    show text "{font=mod_assets/source/fonts/Surfbars.otf}{size=50}Просто...\nДослушай до конца...\nЭту историю...{/size}{/font}":
        xalign 0.5 yalign 0.5
        zoom 0.4 alpha 0
        ease 1.5 zoom 1.0 alpha 1
    pause 3
    show text "{font=mod_assets/source/fonts/Surfbars.otf}{size=50}Просто...\nДослушай до конца...\nЭту историю...{/size}{/font}":
        xalign 0.5 yalign 0.5
        zoom 1.0 alpha 1
        ease 1.5 zoom 0.4 alpha 0
    pause 3
    scene ts_intro_move_1
    show zatemnenie

    with ed_night_dis
    $ Chapter("TEAM АНАРХИСТЫ")
    $ Chapter("ПРЕДСТАВЛЯЮТ")
    scene ts_intro_move_2
    show zatemnenie

    with ed_night_dis
    $ Chapter("МОДИФИКАЦИЮ")
    $ Chapter("ДЛЯ DDLC")
    scene ts_intro_move_3
    show zatemnenie

    with ed_night_dis
    $ Chapter("TRUE STORY")
    scene ts_intro_move_4
    show zatemnenie

    with ed_night_dis
    $ Chapter("ПРИЯТНОГО ЧТЕНИЯ")
    stop music
    play sound br_glitch
    show ts_house as bg1 at Glitch(_fps=160, glitch_strength=1)
    $ renpy.pause(1.1, hard=True)
    stop sound


    jump ts_scenario_1