label ts_scenario_0:

    python: # ОБНОВЛЯЕМ RPC
        rpc.update(state="Акт I | Пролог",details="Предыстория",large_image="logogovna",start=time.time())

    $ persistent.rpclabel = "0"

    $ save_name = "Предыстория"
    window hide
    pause 1.1
    window hide
    stop music fadeout 4
    scene black
    with ed_night_dis
    pause 1
    play music ts_mutter fadein 4
    scene ts_house
    show zatemnenie
    show dust1
    show dust2
    show dust3
    show dust4
    with ed_night_dis
    $ Chapter("Предыстория")
    pause 0.5
    hide zatemnenie
    nvlbazar "{font=[ts_nvl_font2]}Конечно же, всё начиналось совсем по-другому…"
    nvlbazar "{font=[ts_nvl_font2]}Всё начиналось, как у остальных людей: родилась, пошла в школу, выучилась… Правда, не до конца, но всё же."
    nvlbazar "{font=[ts_nvl_font2]}С самого детства взрослые называли меня «одарённой девочкой»."
    nvlbazar "{font=[ts_nvl_font2]}Что во мне такого «одарённого»? В ранние годы я не понимала. Но, как говорится, «кто я такая, чтобы спорить со взрослыми?»."
    nvlbazar "{font=[ts_nvl_font2]}«Маленькая ещё»… «Не доросла ещё»… И прочее-прочее-прочее…"

    nvl clear

    nvlbazar "{font=[ts_nvl_font2]}Но, оглядываясь назад, я понимаю: что-то одарённое во мне и правда было."

    nvl clear

    nvlbazar "{font=[ts_nvl_font2]}В три года я научилась читать. К пяти годам я уже знала всю базовую таблицу умножения…"

    nvl clear

    play sound pageflip
    scene ts_class
    show zatemnenie
    show dust1
    show dust2
    show dust3
    show dust4
    with wipeleft_scene

    nvlbazar "{font=[ts_nvl_font2]}Дальше, уже в школе, пока остальные до сих пор учили буквы, я уже невообразимо быстро читала."
    nvlbazar "{font=[ts_nvl_font2]}А пока остальные до сих пор складывали два плюс два, я без калькулятора уже могла перемножать двузначные числа."
    nvlbazar "{font=[ts_nvl_font2]}И это мне быстро наскучило. И пока остальные на самом деле чему-то учились, я просто витала в облаках."

    nvl clear

    nvlbazar "{font=[ts_nvl_font2]}Потому что я всё это уже знала."

    nvl clear

    nvlbazar "{font=[ts_nvl_font2]}Но учителя думали, что я витаю в облаках не потому, что я знаю гораздо больше, чем обычный первоклассник, а потому, что я очень глупая."
    nvlbazar "{font=[ts_nvl_font2]}Поэтому меня и перевели в другую, специализированную школу."

    nvl clear

    play sound pageflip
    scene ts_l5old
    show zatemnenie
    show dust1
    show dust2
    show dust3
    show dust4
    with wipeleft_scene

    ts_ft "Хочешь в школу к Мире?"
    m "Конечно!" with vpunch
    ts_ft "Ну тогда, скажи до свидания этой школе."
    ts_ft "С завтрашнего дня у тебя будет новая жизнь в {i}новой{/i} школе."
    m "До свидания, школа!" with vpunch

    window hide
    pause 1
    hide zatemnenie
    nvlbazar "{font=[ts_nvl_font2]}Нет, гением я себя назвать не могу, но это всё равно было гораздо более впечатлительно, чем могут большинство детей моего возраста."
    nvlbazar "{font=[ts_nvl_font2]}Я скорее была савантом."
    nvlbazar "{font=[ts_nvl_font2]}Нет, совсем глупой я тоже не была, но помимо чтения, таблицы умножения и прочего, такого важного в начальной школе и такого бесполезного во всём остальном…"
    nvlbazar "{font=[ts_nvl_font2]}Я совершенно не знала, как взаимодействовать с людьми. Вот вообще."
    nvlbazar "{font=[ts_nvl_font2]}Друзей и подруг у меня не было, у меня были скорее «деловые партнёры», которым я за деньги давала списывать всякие контрольные и просто домашки по математике и прочему."
    nvlbazar "{font=[ts_nvl_font2]}Была у меня одна подруга, Мира."
    nvlbazar "{font=[ts_nvl_font2]}Наши родители и её родители дружили семьями, и, соответственно, мы тоже дружили."

    nvl clear

    play sound pageflip
    scene ts_residential
    show zatemnenie
    show dust1
    show dust2
    show dust3
    show dust4
    with wipeleft_scene

    hide zatemnenie
    nvlbazar "{font=[ts_nvl_font2]}Мы постоянно ходили друг к другу в гости, где постоянно играли друг с другом."
    nvlbazar "{font=[ts_nvl_font2]}Мира была немного старше меня, но мы с ней как будто были на одной волне."

    nvl clear

    scene ts_residential
    show zatemnenie
    show dust1
    show dust2
    show dust3
    show dust4

    hide zatemnenie
    nvlbazar "{font=[ts_nvl_font2]}У неё была ещё старшая сестра, однако сестра эта была от другого брака, поэтому они были так непохожи друг на друга."

    nvl clear

    play sound pageflip
    scene ts_l5
    show zatemnenie
    show dust1
    show dust2
    show dust3
    show dust4
    with wipeleft_scene

    hide zatemnenie
    nvlbazar "{font=[ts_nvl_font2]}Однако, когда я пришла в эту школу, Мира как будто отдалилась от меня."
    nvlbazar "{font=[ts_nvl_font2]}Оказалось, что у Миры были и свои подруги, а на меня они смотрели, как на пятое колесо."
    nvlbazar "{font=[ts_nvl_font2]}Вроде и нужно, но не сейчас, и вряд ли оно когда-нибудь понадобится."
    nvlbazar "{font=[ts_nvl_font2]}И, несмотря на то, что вне школы мы продолжали дружить, эта дружба резко пикировала."
    nvlbazar "{font=[ts_nvl_font2]}И внутри я до сих пор оставалась одинокой."
    nvlbazar "{font=[ts_nvl_font2]}Но затем в третьем классе к нам в школу пришла {i}она{/i}."

    nvl clear

    show kaori 22a at t11
    nvlbazar "{font=[ts_nvl_font2]}Её звали Каори. И она была чуть ли не полной противоположностью меня."
    nvlbazar "{font=[ts_nvl_font2]}Я была спокойной девочкой."
    show kaori 23c at t11
    nvlbazar "{font=[ts_nvl_font2]}Каори была неугомонной."
    show kaori 22a at t11
    nvlbazar "{font=[ts_nvl_font2]}Я была закрытой девочкой, для которой нужно сделать что-то стоящее, чтобы со мной подружиться."
    nvlbazar "{font=[ts_nvl_font2]}И это не обязательно были какие-то материальные вещи, но вот просто подружиться со мной было нелегко."
    show kaori 23s at t11
    nvlbazar "{font=[ts_nvl_font2]}Каори же считала, что каждый, кто провёл с ней больше пяти минут, теперь её друг."
    nvl clear
    
    show kaori 22a at t11
    nvlbazar "{font=[ts_nvl_font2]}Я была (да и остаюсь) круглой отличницей."
    show kaori 21v at t11
    nvlbazar "{font=[ts_nvl_font2]}Каори была троечницей, с трудом сдавая почти все предметы."
    show kaori 23c at t11
    nvlbazar "{font=[ts_nvl_font2]}Каори была очень открытым человеком."
    show kaori 22b at t11
    nvlbazar "{font=[ts_nvl_font2]}Я же, наоборот, старалась закрыться ото всех."
    show kaori 22zb at t11
    nvlbazar "{font=[ts_nvl_font2]}Но, как это и бывает во всех этих историях, неважно, основаны ли они на реальных событиях, или же они вымышленные, противоположности притягиваются."
    show kaori 22c at t11
    nvlbazar "{font=[ts_nvl_font2]}Мы всё делали вместе, и во всём помогали друг другу."
    nvlbazar "{font=[ts_nvl_font2]}Мы ели вместе, мы играли вместе, мы постоянно приходили друг к другу…"
    show kaori 22r at t11
    nvlbazar "{font=[ts_nvl_font2]}Прогуливали школу мы тоже вместе. Хотя и было это всего один или два раза."
    nvlbazar "{font=[ts_nvl_font2]}Честное слово."
    nvlbazar "{font=[ts_nvl_font2]}Мы разве что не спали вместе."

    nvl clear

    show kaori 22a at t11
    nvlbazar "{font=[ts_nvl_font2]}Мои родители хорошо относились к Каори, и, в свою очередь, мама Каори хорошо относилась ко мне."
    nvlbazar "{font=[ts_nvl_font2]}Вы меня, конечно, спросите, «что, только мама? Папа к тебе не хорошо относился?»"
    show kaori 21u at t11
    nvlbazar "{font=[ts_nvl_font2]}Но… Дело в том, что… У Каори нет отца, и воспитывала её одна только мать."
    nvlbazar "{font=[ts_nvl_font2]}И мало ей хлопот на свою голову в виде Каори, сама она ко всему прочему была ещё и глухонемой."
    nvl clear


    show kaori 22w at t11
    nvlbazar "{font=[ts_nvl_font2]}Нет, полностью глухонемой она не была, какие-то звуки она издавала."
    nvlbazar "{font=[ts_nvl_font2]}Как, знаете… как человек, который упал в ледяную воду."
    nvlbazar "{font=[ts_nvl_font2]}Я точно не знаю, как это осложнение называется, да и знать я не хочу, но суть примерно такая."
    show kaori 23f at t11
    nvlbazar "{font=[ts_nvl_font2]}В любом случае, Каори успешно общалась с мамой на языке жестов, ну а я, как человек, который его не знает, просто писал ей, а она писала мне."
    nvlbazar "{font=[ts_nvl_font2]}В общем, один настоящий друг детства у меня был."
    nvlbazar "{font=[adv_font]}«Ура-а-а, достижение, у тебя был хоть кто-то, кто о тебе заботился.»"
    nvl clear


    show kaori 21o at t11
    nvlbazar "{font=[ts_nvl_font2]}Почему «был»? Потому что после нескольких лет чистой и искренней дружбы Каори перевели в другую школу. А я снова осталась одна."
    nvlbazar "{font=[ts_nvl_font2]}«Постаралась» бабушка Каори."
    nvlbazar "{font=[ts_nvl_font2]}Как бы ни была против я, как бы ни думали и мои родители, что это совершенно нелогично, против семьи не попрёшь."
    nvlbazar "{font=[ts_nvl_font2]}Особенно против такого напористого члена семьи, как бабушка Каори."
    show kaori at thide
    hide kaori
    nvlbazar "{font=[ts_nvl_font2]}А я снова осталась один на один с этим жестоким миром."
    nvlbazar "{font=[ts_nvl_font2]}Совсем одна. И больше у меня нет никаких друзей, никаких парней, ничего и никого, что могло бы заполнить эту зияющую пустоту."
    nvlbazar "{font=[ts_nvl_font2]}И за годы дружбы, которая казалась вечной, я даже не смогла удосужиться найти себе новых настоящих друзей."
    nvlbazar "{font=[ts_nvl_font2]}Именно {b}настоящих{/b}, а не тех, про которых говорят, что они с тобой только в ясный день."

    nvl clear

    play sound pageflip
    scene ts_class
    show zatemnenie
    show dust1
    show dust2
    show dust3
    show dust4
    with wipeleft_scene

    hide zatemnenie
    nvlbazar "{font=[ts_nvl_font2]}Но это мы уже слишком далеко зашли. Сначала снова вернёмся на пару лет назад."
    nvlbazar "{font=[ts_nvl_font2]}Родители всегда требовали от меня становиться лучше. Стараться лучше. {i}Быть{/i} лучше."
    nvlbazar "{font=[ts_nvl_font2]}Каждый раз, когда я получала тройку, или даже четвёрку, хотя это и было редко, папа каждый раз раздувал из этого целое событие."
    nvlbazar "{font=[ts_nvl_font2]}И хорошо, если он ограничивался тем, что я, его мнению, «чёртова двоечница»."
    nvlbazar "{font=[ts_nvl_font2]}Но по большей части родители каждый раз читали мне морали, и растягивается это всё часа на два."
    nvlbazar "{font=[ts_nvl_font2]}А если они ещё и пьяные, то, как говорится, пиши пропало."

    nvl clear

    nvlbazar "{font=[ts_nvl_font2]}Нет, мои родители не алкоголики, напротив, они выпивают довольно редко, они добрейшей души люди, и очень часто меня поддерживают, если я пробую что-то новое."
    nvlbazar "{font=[ts_nvl_font2]}Но когда дело касалось учёбы, и когда я в их глазах была не идеальной девочкой, они устраивали разнос."
    nvlbazar "{font=[ts_nvl_font2]}Причём они очень часто повторялись в своих моралях."
    nvlbazar "{font=[ts_nvl_font2]}Так что, даже несмотря на то, что читали они мне их нечасто, я уже чуть ли не наизусть знала, кто и что конкретно мне будет говорить."
    nvlbazar "{font=[ts_nvl_font2]}Я же, в свою очередь, хотя и была прилежной ученицей, и, как было упомянуто ранее, до сих пор остаюсь отличницей, внутри была лентяйкой, каких только поискать надо."


    nvl clear


    nvlbazar "{font=[ts_nvl_font2]}Где-то класса с седьмого меня таскали по всяким разным клубам, потому что «ну негоже такой хорошей девочке не участвовать в жизни клуба»."
    nvlbazar "{font=[ts_nvl_font2]}На первых порах, когда я ещё была недостаточно взрослой и самостоятельной, я просто покорно слушалась."
    nvlbazar "{font=[ts_nvl_font2]}Да и таскали меня по тем клубам, которые мне хотя бы были интересны."
    nvlbazar "{font=[ts_nvl_font2]}Сначала это был Книжный клуб."
    nvlbazar "{font=[ts_nvl_font2]}Я в детстве довольно много читала, поэтому учителя подумали, что довольно логично отправить меня именно в Книжный клуб."

    nvl clear

    play sound pageflip
    scene ts_club2re
    show zatemnenie
    show dust1
    show dust2
    show dust3
    show dust4
    with wipeleft_scene

    hide zatemnenie
    nvlbazar "{font=[ts_nvl_font2]}Даже несмотря на то, что к подростковому возрасту читала я уже заметно меньше, а последнюю книгу я прочла пару лет назад."
    nvlbazar "{font=[ts_nvl_font2]}Когда папа заставил меня прочитать «Графа Монте-Кристо» в одиннадцать лет, у меня просто пропало желание читать хоть что-то."
    nvlbazar "{font=[ts_nvl_font2]}Я всё равно довольно успешно справлялась. Я даже была вице-президентом клуба."
    nvlbazar "{font=[ts_nvl_font2]}Но мне это просто очень быстро наскучило, поэтому к концу года я вышла из клуба с твёрдым желанием найти себе клуб получше."

    nvl clear

    play sound pageflip
    scene ts_pianoend
    show zatemnenie
    show dust1
    show dust2
    show dust3
    show dust4
    with wipeleft_scene

    hide zatemnenie
    nvlbazar "{font=[ts_nvl_font2]}В следующем году меня направили в Музыкальный клуб. И поначалу мне это действительно нравилось."
    nvlbazar "{font=[ts_nvl_font2]}У дедушки было пианино, и я, ещё будучи ребёнком, время от времени наобум стучала по клавишам, поэтому, когда мне предложили выбрать инструмент, я без раздумий указала на пианино."
    nvlbazar "{font=[ts_nvl_font2]}Да, школьное пианино было далеко не первого качества, половина клавиш не стро{b}и{/b}ла, да и играть я, по сути, не умела…"

    nvl clear

    scene mon_piano_start
    show zatemnenie
    show dust1
    show dust2
    show dust3
    show dust4
    with poplil_pacan

    hide zatemnenie
    nvlbazar "{font=[ts_nvl_font2]}Но мне это было и не важно."
    nvlbazar "{font=[ts_nvl_font2]}Мне это нравилось."
    nvlbazar "{font=[ts_nvl_font2]}Я быстро научилась играть несколько простых песенок."

    nvl clear

    play sound pageflip
    scene ts_pianoend
    show zatemnenie
    show dust1
    show dust2
    show dust3
    show dust4
    with wipeleft_scene

    hide zatemnenie
    nvlbazar "{font=[ts_nvl_font2]}Но… Помните, как я говорила, что я невообразимая лентяйка?"
    nvlbazar "{font=[ts_nvl_font2]}Так вот: может, это просто лень, а может, расстройство посерьёзнее, но как только дело дошло до композиций посложнее, я разленилась."
    nvlbazar "{font=[ts_nvl_font2]}И дело даже не в том, что я не хотела учиться, или не могла – с должным старанием всё должно получиться."
    nvlbazar "{font=[ts_nvl_font2]}Мне просто стало лень."

    nvl clear

    nvlbazar "{font=[ts_nvl_font2]}В итоге вместо того, чтобы развиваться, я постоянно играла одни и те же пять песенок, которые мы разучивали на первых уроках."
    nvlbazar "{font=[ts_nvl_font2]}А когда меня поставили перед фактом, что я вообще не развиваюсь, и пригрозили тем, что я вылечу из клуба, я просто хмыкнула и ушла сама."
    nvlbazar "{font=[ts_nvl_font2]}И хотя технически на пианино я до сих пор играть умею, фактически я умею играть на пианино примерно так же, как если бы не умела вовсе."
    nvlbazar "{font=[ts_nvl_font2]}Особенно с учётом того, что это было уже несколько лет назад…"
    nvlbazar "{font=[ts_nvl_font2]}А когда ты ещё так молода, тебе кажется, что несколько лет назад были как будто в прошлой жизни."

    nvl clear

    play sound pageflip
    scene ts_gym
    show zatemnenie
    show dust1
    show dust2
    show dust3
    show dust4
    with wipeleft_scene

    hide zatemnenie
    nvlbazar "{font=[ts_nvl_font2]}После приключений с Музыкальным клубом меня потянуло в спорт."
    nvlbazar "{font=[ts_nvl_font2]}Нет, в баскетбол и в прочие преимущественно мужские виды спорта я не играла…"
    nvlbazar "{font=[ts_nvl_font2]}Но наш учитель физкультуры как-то обмолвился, что у нас скоро городские соревнования между школами по волейболу."
    nvlbazar "{font=[ts_nvl_font2]}А я как раз неплохо играла в волейбол, поэтому и вызвалась добровольцем."

    nvl clear

    nvlbazar "{font=[ts_nvl_font2]}На городских соревнованиях все другие школы просто стёрли нас в пух и прах, но папа всегда говорил, что я играла лучше всех."
    nvlbazar "{font=[ts_nvl_font2]}Может, он и предвзят, а может, так всё и самом деле было, это уже было неважно."
    nvlbazar "{font=[ts_nvl_font2]}Помимо этого, я уже много лет занималась настольным теннисом, и даже ездила на соревнования по городу и даже по всей префектуре."
    nvlbazar "{font=[ts_nvl_font2]}Опять же, звёзд с неба я не хватала, и я так ни разу и не выигрывала, но это был весёлый и интересный опыт."

    nvl clear

    nvlbazar "{font=[ts_nvl_font2]}И наконец, папа в детстве научил меня играть в шахматы."
    nvlbazar "{font=[ts_nvl_font2]}И уж шахматы-то я никогда не забуду."
    nvlbazar "{font=[ts_nvl_font2]}Но, как и во всех остальных видах спорта, в шахматах я тоже была не так уж и сильна."

    nvl clear

    nvlbazar "{font=[ts_nvl_font2]}Да, с годами я начала обыгрывать папу, всех его друзей, всех моих немногочисленных друзей, просто знакомых и незнакомых людей…"
    nvlbazar "{font=[ts_nvl_font2]}Но мне ещё было очень далеко до того, чтобы играть в те же шахматы на деньги и зарабатывать этим на жизнь."
    nvlbazar "{font=[ts_nvl_font2]}Может, это пресловутая лень."
    nvlbazar "{font=[ts_nvl_font2]}А может… да нет, не может, это всё только потому, что я ленюсь."
    nvlbazar "{font=[ts_nvl_font2]}Ведь папа же говорил, что «с должным старанием всё должно получиться»."
    nvlbazar "{font=[ts_nvl_font2]}А если не получается, то это лишь значит, что ты недостаточно стараешься."
    nvlbazar "{font=[ts_nvl_font2]}И ведь спорить с папой было бессмысленно, ведь папа же взрослый, мудрый…"
    nvlbazar "{font=[ts_nvl_font2]}А я что? Всего лишь какая-то маленькая лентяйка, которая, хоть Бог и наделил талантами, все их успешно закопала…"
    
    
    nvl clear


    nvlbazar "{font=[ts_nvl_font2]}Со стороны другим людям казалось, что «ой, Моника у вас вообще такая талантливая, разносторонняя…»"
    nvlbazar "{font=[ts_nvl_font2]}«Прямо-таки умница-спортсменка-красавица-комсомолка»."
    nvlbazar "{font=[ts_nvl_font2]}Я же знаю, что я просто лентяйка и вообще бездарность."
    nvlbazar "{font=[ts_nvl_font2]}Другим казалось, что я прям мастер на все руки."
    nvlbazar "{font=[ts_nvl_font2]}Я же знаю, что так-то оно так, только руки у меня не совсем из правильного места растут…"

    nvl clear

    play sound pageflip
    scene ts_class
    show zatemnenie
    show dust1
    show dust2
    show dust3
    show dust4
    with wipeleft_scene

    hide zatemnenie
    nvlbazar "{font=[ts_nvl_font2]}В прошлом году меня перевели в другой класс."
    nvlbazar "{font=[ts_nvl_font2]}Все эти люди казались мне совершенно незнакомыми. Впрочем, кроме Каори, со мной и в прошлом классе особо никто не общался."
    nvlbazar "{font=[ts_nvl_font2]}Но Каори перевели в другую школу. Так что я как была одна-одинокая, так и после того, как меня перевели в другой класс, ситуация не улучшилась."
    nvlbazar "{font=[ts_nvl_font2]}Правда, был один паренёк… Мицуо, кажется?"
    nvlbazar "{font=[ts_nvl_font2]}Однако, учитывая мой статус местной знаменитости, он, в силу своей стеснительности, просто боялся со мной даже заговорить."
    nvlbazar "{font=[ts_nvl_font2]}Вообще."
    nvlbazar "{font=[ts_nvl_font2]}Я за весь год от него не услышала ни одного предложения, ни одного вопроса."

    nvl clear

    nvlbazar "{font=[ts_nvl_font2]}Впрочем, неважно, помимо него, у меня ещё был целый класс незнакомцев и незнакомок."
    nvlbazar "{font=[ts_nvl_font2]}Одним незнакомцем больше, одним незнакомцем меньше… Какая вообще разница?"

    nvl clear

    nvlbazar "{font=[ts_nvl_font2]}В этом же году я вступила в Дискуссионный клуб."
    nvlbazar "{font=[ts_nvl_font2]}Учитывая мою общую эрудицию, начитанность, и вышеупомянутый статус местной звезды, я быстро поднялась до главенствующих позиций, вплоть до президента клуба."
    nvlbazar "{font=[ts_nvl_font2]}Вместе с этим и сам клуб становился больше. Даже больше, чем мне бы самой этого хотелось."
    nvlbazar "{font=[ts_nvl_font2]}А сами дискуссии из разносторонних постепенно превращались в однотипные."
    nvlbazar "{font=[ts_nvl_font2]}И если мы раньше спорили буквально обо всём на свете, то сейчас мы только и спорим, что о бюджете да о подготовке к тому или иному мероприятию."

    nvl clear

    nvlbazar "{font=[ts_nvl_font2]}И в конце концов, вся эта интрижка крупного клуба становилась выше меня, вплоть до того момента, когда я не могла ей ничего противопоставить."
    nvlbazar "{font=[ts_nvl_font2]}В итоге я попросилась, чтобы меня сняли с должности, а сама я ушла в закат, оставив эти интрижки для кого-то другого."
    nvlbazar "{font=[ts_nvl_font2]}Пусть другие это расхлёбывают. Не я."

    nvl clear

    play sound pageflip
    scene ts_class
    show zatemnenie
    show dust1
    show dust2
    show dust3
    show dust4
    with wipeleft_scene

    hide zatemnenie
    stop music fadeout 10
    nvlbazar "{font=[ts_nvl_font2]}Пришло время выпускного года. И я, побывав уже во многих клубах, примерно понимаю, что я хочу и чего я не хочу видеть в своём клубе."
    nvlbazar "{font=[ts_nvl_font2]}Я хочу, чтобы в моём клубе не было слова «неправильно»."
    nvlbazar "{font=[ts_nvl_font2]}Я хочу, чтобы в моём клубе каждый мог выражаться, как его душе может быть угодно."
    nvlbazar "{font=[ts_nvl_font2]}Я хочу, чтобы в моём клубе мы делились чем-то личным, чем-то сокровенным."
    nvlbazar "{font=[ts_nvl_font2]}Решение пришло само собой. Я знаю, какой именно клуб я хочу открыть."
    nvlbazar "{font=[ts_nvl_font2]}Литературный клуб."

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