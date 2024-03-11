label ts_scenario_0:

    python: # ОБНОВЛЯЕМ RPC
        try:
            rpc.update(state="Акт I | Пролог",details="Предыстория",large_image="prologue",start=time.time())
        except AssertionError:
            pass

    $ persistent.rpclabel = "0"

    $ persistent.carter2menu = False
    $ persistent.carter3menu = False

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

    $ TS.Screens(ts_showscreens)

    play ambience pechatka
    nvlbazar "{font=[prologue_font]}Конечно же, всё начиналось совсем по-другому…"
    nvlbazar "{font=[prologue_font]}Всё начиналось, как у остальных людей: родилась, пошла в школу, выучилась… Правда, не до конца... Но всё же."
    nvlbazar "{font=[prologue_font]}С самого детства взрослые называли меня «одарённой девочкой»."
    nvlbazar "{font=[prologue_font]}Что во мне такого «одарённого»? В ранние годы я этого не понимала. Но, как говорится: «кто я такая, чтобы спорить со взрослыми?»."
    nvlbazar "{font=[prologue_font]}«Маленькая ещё»… «Не доросла ещё»… И прочее-прочее-прочее…"

    nvl clear

    nvlbazar "{font=[prologue_font]}Но - оглядываясь назад, я понимаю: что-то одарённое во мне действительно было."

    nvl clear

    nvlbazar "{font=[prologue_font]}В три года я научилась читать. К пяти годам я уже знала всю базовую таблицу умножения…"

    $ TS.Screens(ts_hidescreens)
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

    $ TS.Screens(ts_showscreens)
    play ambience pechatka

    nvlbazar "{font=[prologue_font]}Дальше, уже в школе, пока остальные до сих пор учили буквы - я уже невообразимо быстро читала."
    nvlbazar "{font=[prologue_font]}А пока остальные до сих пор складывали два плюс два - я без калькулятора уже могла перемножать двузначные числа."
    nvlbazar "{font=[prologue_font]}И это мне быстро наскучило: пока остальные на самом деле чему-то учились, я просто витала в облаках."

    nvl clear

    nvlbazar "{font=[prologue_font]}Я всё это знала заранее."

    nvl clear

    nvlbazar "{font=[prologue_font]}Но учителя думали, что я витаю в облаках не потому, что я знаю гораздо больше, чем обычный первоклассник, а потому, что я очень глупая."
    nvlbazar "{font=[prologue_font]}Поэтому меня и перевели в другую, специализированную школу."

    $ TS.Screens(ts_hidescreens)
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

    $ TS.Screens(ts_showscreens)

    ts_ft "Хочешь в школу к Мире?"

    show hiroto 1a at t11

    $ TS.Screens(vpunch)
    m "Конечно!"
    ts_ft 1b "Ну тогда, скажи до свидания этой школе."
    ts_ft "С завтрашнего дня у тебя будет новая жизнь в {i}новой{/i} школе."

    show hiroto 1a at t11

    $ TS.Screens(vpunch)
    m "До свидания, школа!"

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    show hiroto 1a at ron11
    pause 0.3
    hide hiroto with dissolve

    $ TS.Screens(ts_showscreens)

    play ambience pechatka
    nvlbazar "{font=[prologue_font]}Нет, гением я себя назвать не могу, хоть и результат был лучше, чем у большинства детей моего возраста."
    nvlbazar "{font=[prologue_font]}Я была скорее савантом."
    nvlbazar "{font=[prologue_font]}Нет, совсем глупой я тоже не была. Однако, помимо чтения, таблицы умножения и прочего, такого важного в начальной школе и такого бесполезного во всём остальном…"
    nvlbazar "{font=[prologue_font]}Я совершенно не знала, как взаимодействовать с людьми. Вот вообще."
    nvlbazar "{font=[prologue_font]}Друзей и подруг у меня не было: это были скорее «деловые партнёры», которым я за деньги давала списывать всякие контрольные и просто домашки по математике и всему остальному."
    nvlbazar "{font=[prologue_font]}Была у меня одна подруга - Мира."
    nvlbazar "{font=[prologue_font]}Наши родители и её родители дружили семьями. Как и мы, собственно."

    $ TS.Screens(ts_hidescreens)
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

    $ TS.Screens(ts_showscreens)

    play ambience pechatka
    nvlbazar "{font=[prologue_font]}Мы постоянно ходили друг к другу в гости, где постоянно играли друг с другом."
    nvlbazar "{font=[prologue_font]}Мира была немного старше меня, но мы с ней как будто были на одной волне."

    nvl clear

    nvlbazar "{font=[prologue_font]}У неё была ещё старшая сестра, однако сестра эта была от другого брака, поэтому они были так непохожи друг на друга."

    $ TS.Screens(ts_hidescreens)
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

    $ TS.Screens(ts_showscreens)

    play ambience pechatka
    nvlbazar "{font=[prologue_font]}Однако, когда я пришла в эту школу, Мира как будто отдалилась от меня."
    nvlbazar "{font=[prologue_font]}Оказалось, что у Миры были и свои подруги, а на меня они смотрели, как на пятое колесо."
    nvlbazar "{font=[prologue_font]}Вроде и нужно, но не сейчас, и вряд ли оно когда-нибудь понадобится."
    nvlbazar "{font=[prologue_font]}И, несмотря на то, что вне школы мы продолжали дружить, эта дружба резко пикировала."
    nvlbazar "{font=[prologue_font]}И внутри я до сих пор оставалась одинокой."
    nvlbazar "{font=[prologue_font]}Но затем в третьем классе к нам в школу пришла {i}она{/i}."

    nvl clear

    show kaori 22a at ln11
    nvlbazar "{font=[prologue_font]}Её звали Каори. И она была чуть ли не полной противоположностью меня."
    nvlbazar "{font=[prologue_font]}Я была спокойной девочкой."
    show kaori 23c at h11
    nvlbazar "{font=[prologue_font]}Каори была неугомонной."
    show kaori 22a at s11
    nvlbazar "{font=[prologue_font]}Я была закрытой девочкой, для которой нужно сделать что-то стоящее, чтобы со мной подружиться."
    nvlbazar "{font=[prologue_font]}И это не обязательно были какие-то материальные вещи, но вот просто подружиться со мной было нелегко."
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
    nvlbazar "{font=[prologue_font]}Но, как это и бывает во всех этих историях, неважно, основаны ли они на реальных событиях, или же они вымышленные, противоположности притягиваются."
    show kaori 22c at h11
    nvlbazar "{font=[prologue_font]}Мы всё делали вместе, и во всём помогали друг другу."
    nvlbazar "{font=[prologue_font]}Мы ели вместе, мы играли вместе, мы постоянно приходили друг к другу…"
    show kaori 22r at h11
    nvlbazar "{font=[prologue_font]}Прогуливали школу мы тоже вместе. Хотя и было это всего один или два раза."
    nvlbazar "{font=[prologue_font]}Честное слово."
    nvlbazar "{font=[prologue_font]}Мы разве что не спали вместе."

    nvl clear

    show kaori 22a at s11
    nvlbazar "{font=[prologue_font]}Мои родители хорошо относились к Каори, и, в свою очередь, мама Каори хорошо относилась ко мне."
    nvlbazar "{font=[prologue_font]}Вы меня, конечно, спросите, «что, только мама? Папа к тебе не хорошо относился?»"
    show kaori 21u at d11
    nvlbazar "{font=[prologue_font]}Но… Дело в том, что… У Каори нет отца, и воспитывала её одна только мать."
    nvlbazar "{font=[prologue_font]}И мало ей хлопот на свою голову в виде Каори, сама она ко всему прочему была ещё и глухонемой."
    nvl clear


    show kaori 22w at s11
    nvlbazar "{font=[prologue_font]}Нет, полностью глухонемой она не была, какие-то звуки она издавала."
    nvlbazar "{font=[prologue_font]}Как, знаете… как человек, который упал в ледяную воду."
    nvlbazar "{font=[prologue_font]}Я точно не знаю, как это осложнение называется, да и знать я не хочу, но суть примерно такая."
    show kaori 23f at d11
    nvlbazar "{font=[prologue_font]}В любом случае, Каори успешно общалась с мамой на языке жестов, ну а я, как человек, который его не знает, просто писал ей, а она писала мне."
    nvlbazar "{font=[prologue_font]}В общем, один настоящий друг детства у меня был."
    nvlbazar "{font=[adv_font]}«Ура-а-а, достижение, у тебя был хоть кто-то, кто о тебе заботился.»"
    nvl clear


    show kaori 21o at h11
    nvlbazar "{font=[prologue_font]}Почему «был»? Потому что после нескольких лет чистой и искренней дружбы Каори перевели в другую школу. А я снова осталась одна."
    nvlbazar "{font=[prologue_font]}«Постаралась» бабушка Каори."
    nvlbazar "{font=[prologue_font]}Как бы ни была против я, как бы ни думали и мои родители, что это совершенно нелогично, против семьи не попрёшь."
    nvlbazar "{font=[prologue_font]}Особенно против такого напористого члена семьи, как бабушка Каори."

    $ TS.Screens(ts_hidescreens)
    nvlbazar " {w=1.0}{nw}"
    nvl clear
    show kaori at ron11
    pause 0.3
    hide kaori with dissolve
    $ TS.Screens(ts_showscreens)

    nvlbazar "{font=[prologue_font]}А я снова осталась один на один с этим жестоким миром."
    nvlbazar "{font=[prologue_font]}Совсем одна. И больше у меня нет никаких друзей, никаких парней, ничего и никого, что могло бы заполнить эту зияющую пустоту."
    nvlbazar "{font=[prologue_font]}И за годы дружбы, которая казалась вечной, я даже не смогла удосужиться найти себе новых настоящих друзей."
    nvlbazar "{font=[prologue_font]}Именно {b}настоящих{/b}, а не тех, про которых говорят, что они с тобой только в ясный день."

    $ TS.Screens(ts_hidescreens)
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

    $ TS.Screens(ts_showscreens)

    play ambience pechatka
    nvlbazar "{font=[prologue_font]}Но это мы уже слишком далеко зашли. Сначала снова вернёмся на пару лет назад."
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
    nvlbazar "{font=[prologue_font]}Я же, в свою очередь, хотя и была прилежной ученицей, и, как было упомянуто ранее, до сих пор остаюсь отличницей, внутри была лентяйкой, каких только поискать надо."


    nvl clear


    nvlbazar "{font=[prologue_font]}Где-то класса с седьмого меня таскали по всяким разным клубам, потому что «ну негоже такой хорошей девочке не участвовать в жизни клуба»."
    nvlbazar "{font=[prologue_font]}На первых порах, когда я ещё была недостаточно взрослой и самостоятельной, я просто покорно слушалась."
    nvlbazar "{font=[prologue_font]}Да и таскали меня по тем клубам, которые мне хотя бы были интересны."
    nvlbazar "{font=[prologue_font]}Сначала это был Книжный клуб."
    nvlbazar "{font=[prologue_font]}Я в детстве довольно много читала, поэтому учителя подумали, что довольно логично отправить меня именно в Книжный клуб."

    $ TS.Screens(ts_hidescreens)
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

    $ TS.Screens(ts_showscreens)

    play ambience pechatka
    nvlbazar "{font=[prologue_font]}Даже несмотря на то, что к подростковому возрасту читала я уже заметно меньше, а последнюю книгу я прочла пару лет назад."
    nvlbazar "{font=[prologue_font]}Когда папа заставил меня прочитать «Графа Монте-Кристо» в одиннадцать лет, у меня просто пропало желание читать хоть что-то."
    nvlbazar "{font=[prologue_font]}Я всё равно довольно успешно справлялась. Я даже была вице-президентом клуба."
    nvlbazar "{font=[prologue_font]}Но мне это просто очень быстро наскучило, поэтому к концу года я вышла из клуба с твёрдым желанием найти себе клуб получше."

    $ TS.Screens(ts_hidescreens)
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

    $ TS.Screens(ts_showscreens)

    play ambience pechatka
    nvlbazar "{font=[prologue_font]}В следующем году меня направили в Музыкальный клуб. И поначалу мне это действительно нравилось."
    nvlbazar "{font=[prologue_font]}У дедушки было пианино, и я, ещё будучи ребёнком, время от времени наобум стучала по клавишам, поэтому, когда мне предложили выбрать инструмент, я без раздумий указала на пианино."
    nvlbazar "{font=[prologue_font]}Да, школьное пианино было далеко не первого качества, половина клавиш не стро{b}и{/b}ла, да и играть я, по сути, не умела…"

    $ TS.Screens(ts_hidescreens)
    nvlbazar " {w=1.0}{nw}"
    nvl clear

    stop ambience
    scene mon_piano_start
    show dust1
    show dust2
    show dust3
    show dust4
    with poplil_pacan

    $ TS.Screens(ts_showscreens)

    play ambience pechatka
    nvlbazar "{font=[prologue_font]}Но мне это было и не важно."
    nvlbazar "{font=[prologue_font]}Мне это нравилось."
    nvlbazar "{font=[prologue_font]}Я быстро научилась играть несколько простых песенок."

    $ TS.Screens(ts_hidescreens)
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

    $ TS.Screens(ts_showscreens)

    play ambience pechatka
    nvlbazar "{font=[prologue_font]}Но… Помните, как я говорила, что я невообразимая лентяйка?"
    nvlbazar "{font=[prologue_font]}Так вот: может, это просто лень, а может, расстройство посерьёзнее, но как только дело дошло до композиций посложнее, я разленилась."
    nvlbazar "{font=[prologue_font]}И дело даже не в том, что я не хотела учиться, или не могла – с должным старанием всё должно получиться."
    nvlbazar "{font=[prologue_font]}Мне просто стало лень."

    nvl clear

    nvlbazar "{font=[prologue_font]}В итоге вместо того, чтобы развиваться, я постоянно играла одни и те же пять песенок, которые мы разучивали на первых уроках."
    nvlbazar "{font=[prologue_font]}А когда меня поставили перед фактом, что я вообще не развиваюсь, и пригрозили тем, что я вылечу из клуба, я просто хмыкнула и ушла сама."
    nvlbazar "{font=[prologue_font]}И хотя технически на пианино я до сих пор играть умею, фактически я умею играть на пианино примерно так же, как если бы не умела вовсе."
    nvlbazar "{font=[prologue_font]}Особенно с учётом того, что это было уже несколько лет назад…"
    nvlbazar "{font=[prologue_font]}А когда ты ещё так молода, тебе кажется, что несколько лет назад были как будто в прошлой жизни."

    $ TS.Screens(ts_hidescreens)
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

    $ TS.Screens(ts_showscreens)

    play ambience pechatka
    nvlbazar "{font=[prologue_font]}После приключений с Музыкальным клубом меня потянуло в спорт."
    nvlbazar "{font=[prologue_font]}Нет, в баскетбол и в прочие преимущественно мужские виды спорта я не играла…"
    nvlbazar "{font=[prologue_font]}Но наш учитель физкультуры как-то обмолвился, что у нас скоро городские соревнования между школами по волейболу."
    nvlbazar "{font=[prologue_font]}А я как раз неплохо играла в волейбол, поэтому и вызвалась добровольцем."

    nvl clear

    nvlbazar "{font=[prologue_font]}На городских соревнованиях все другие школы просто стёрли нас в пух и прах, но папа всегда говорил, что я играла лучше всех."
    nvlbazar "{font=[prologue_font]}Может, он и предвзят, а может, так всё и самом деле было, это уже было неважно."
    nvlbazar "{font=[prologue_font]}Помимо этого, я уже много лет занималась настольным теннисом, и даже ездила на соревнования по городу и даже по всей префектуре."
    nvlbazar "{font=[prologue_font]}Опять же, звёзд с неба я не хватала, и я так ни разу и не выигрывала, но это был весёлый и интересный опыт."

    nvl clear

    nvlbazar "{font=[prologue_font]}И наконец, папа в детстве научил меня играть в шахматы."
    nvlbazar "{font=[prologue_font]}И уж шахматы-то я никогда не забуду."
    nvlbazar "{font=[prologue_font]}Но, как и во всех остальных видах спорта, в шахматах я тоже была не так уж и сильна."

    nvl clear

    nvlbazar "{font=[prologue_font]}Да, с годами я начала обыгрывать папу, всех его друзей, всех моих немногочисленных друзей, просто знакомых и незнакомых людей…"
    nvlbazar "{font=[prologue_font]}Но мне ещё было очень далеко до того, чтобы играть в те же шахматы на деньги и зарабатывать этим на жизнь."
    nvlbazar "{font=[prologue_font]}Может, это пресловутая лень."
    nvlbazar "{font=[prologue_font]}А может… да нет, не может, это всё только потому, что я ленюсь."
    nvlbazar "{font=[prologue_font]}Ведь папа же говорил, что «с должным старанием всё должно получиться»."
    nvlbazar "{font=[prologue_font]}А если не получается, то это лишь значит, что ты недостаточно стараешься."
    nvlbazar "{font=[prologue_font]}И ведь спорить с папой было бессмысленно, ведь папа же взрослый, мудрый…"
    nvlbazar "{font=[prologue_font]}А я что? Всего лишь какая-то маленькая лентяйка, которая, хоть Бог и наделил талантами, все их успешно закопала…"
    
    nvl clear

    nvlbazar "{font=[prologue_font]}Со стороны другим людям казалось, что «ой, Моника у вас вообще такая талантливая, разносторонняя…»"
    nvlbazar "{font=[prologue_font]}«Прямо-таки умница-спортсменка-красавица-комсомолка»."
    nvlbazar "{font=[prologue_font]}Я же знаю, что я просто лентяйка и вообще бездарность."
    nvlbazar "{font=[prologue_font]}Другим казалось, что я прям мастер на все руки."
    nvlbazar "{font=[prologue_font]}Я же знаю, что так-то оно так, только руки у меня не совсем из правильного места растут…"

    $ TS.Screens(ts_hidescreens)
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

    $ TS.Screens(ts_showscreens)

    play ambience pechatka
    nvlbazar "{font=[prologue_font]}В прошлом году меня перевели в другой класс."
    nvlbazar "{font=[prologue_font]}Все эти люди казались мне совершенно незнакомыми. Впрочем, кроме Каори, со мной и в прошлом классе особо никто не общался."
    nvlbazar "{font=[prologue_font]}Но Каори перевели в другую школу. Так что я как была одна-одинокая, так и после того, как меня перевели в другой класс, ситуация не улучшилась."
    nvlbazar "{font=[prologue_font]}Правда, был один паренёк… Мицуо, кажется?"
    nvlbazar "{font=[prologue_font]}Однако, учитывая мой статус местной знаменитости, он, в силу своей стеснительности, просто боялся со мной даже заговорить."
    nvlbazar "{font=[prologue_font]}Вообще."
    nvlbazar "{font=[prologue_font]}Я за весь год от него не услышала ни одного предложения, ни одного вопроса."

    nvl clear

    nvlbazar "{font=[prologue_font]}Впрочем, неважно, помимо него, у меня ещё был целый класс незнакомцев и незнакомок."
    nvlbazar "{font=[prologue_font]}Одним незнакомцем больше, одним незнакомцем меньше… Какая вообще разница?"

    nvl clear

    nvlbazar "{font=[prologue_font]}В этом же году я вступила в Дискуссионный клуб."
    nvlbazar "{font=[prologue_font]}Учитывая мою общую эрудицию, начитанность, и вышеупомянутый статус местной звезды, я быстро поднялась до главенствующих позиций, вплоть до президента клуба."
    nvlbazar "{font=[prologue_font]}Вместе с этим и сам клуб становился больше. Даже больше, чем мне бы самой этого хотелось."
    nvlbazar "{font=[prologue_font]}А сами дискуссии из разносторонних постепенно превращались в однотипные."
    nvlbazar "{font=[prologue_font]}И если мы раньше спорили буквально обо всём на свете, то сейчас мы только и спорим, что о бюджете да о подготовке к тому или иному мероприятию."

    nvl clear

    nvlbazar "{font=[prologue_font]}И в конце концов, вся эта интрижка крупного клуба становилась выше меня, вплоть до того момента, когда я не могла ей ничего противопоставить."
    nvlbazar "{font=[prologue_font]}В итоге я попросилась, чтобы меня сняли с должности, а сама я ушла в закат, оставив эти интрижки для кого-то другого."
    nvlbazar "{font=[prologue_font]}Пусть другие это расхлёбывают. Не я."

    $ TS.Screens(ts_hidescreens)
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

    $ TS.Screens(ts_showscreens)

    play ambience pechatka
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
    show ts_club2re as bg1 at br_glitches(_fps=160, glitch_strength=1)
    $ renpy.pause(1.1, hard=True)
    stop sound
    scene black
    play music ts_soft fadein 4
    pause 2
    scene ts_intro_move_1
    show zatemnenie
    #show layer master at heartbeat
    with ed_night_dis
    $ Chapter("TEAM АНАРХИСТЫ")
    $ Chapter("ПРЕДСТАВЛЯЮТ")
    scene ts_intro_move_2
    show zatemnenie
    #show layer master at heartbeat
    with ed_night_dis
    $ Chapter("МОДИФИКАЦИЮ")
    $ Chapter("ДЛЯ DDLC")
    scene ts_intro_move_3
    show zatemnenie
    #show layer master at heartbeat
    with ed_night_dis
    $ Chapter("TRUE STORY")
    scene ts_intro_move_4
    show zatemnenie
    #show layer master at heartbeat
    with ed_night_dis
    $ Chapter("ПРИЯТНОГО ЧТЕНИЯ")
    stop music
    play sound br_glitch
    show ts_house as bg1 at br_glitches(_fps=160, glitch_strength=1)
    $ renpy.pause(1.1, hard=True)
    stop sound


    jump ts_scenario_1