label ts_bad_ending_blya:

    $ TS.b()

    $ ts_rpc_carter12()

    $ persistent.rpclabel = "12"


    $ persistent.carter2menu = False
    $ persistent.carter3menu = False
    $ persistent.badendmenuperedglitch = False
    $ persistent.badendmenuskipglitch = False
    $ persistent.badendmenu = False
    $ persistent.goodendmenu = False
    $ persistent.peredbadendmenu = True
    $ persistent.peredgoodendmenu = False

    if _preferences.language == "english":
        $ save_name = "Into the abyss"
    else:
        $ save_name = "В бездну"

    scene black

    $ TS.p(2)

    play sound chp3
    if _preferences.language == "english":
        $ Chapter("Epilogue")
        $ Chapter("Epilogue")
        $ Chapter("Into the abyss")
        stop sound fadeout 7
        $ Chapter("Into the abyss")
    else:
        $ Chapter("Эпилог")
        $ Chapter("Эпилог")
        $ Chapter("В бездну")
        stop sound fadeout 7
        $ Chapter("В бездну")

    $ TS.p(2)

    $ persistent.uncolorize = "none"

    play music ts_crysis_beta fadein 4
    play sound_loop kardio_normal fadein 4
    scene ts_emergency_room
    show ts_emergency_room_anim
    show ts_prosnulas_ot_ahuya
    $ TS.m(blur_drunk_blya_low)
    with Dissolve(4)
    $ TS.s(ts_showscreens)
    "..."
    "Я жадно глотаю воздух."
    "Ч-ч-что это? Г-г-где я вообще?"
    "Это... н-не комната Сайори..."
    "Судя по мониторам, я в какой-то больнице."
    "Тело ослаблено и всё обмякло."
    $ TS.m(ts_alkonersha)
    "Я рефлекторно пытаюсь встать, но, к моему удивлению, у меня не получается."
    "На шум прибежало несколько людей в разного цвета халатах. Я так понимаю, это медсёстры и санитары."
    if _preferences.language == "english":
        $ misc_name = "Nurse"
    else:
        $ misc_name = "Медсестра"
    misc "Очнулась... Наконец-то!"
    misc "Я сейчас доктора позову, я быстро!"
    m "Л-ладно..."
    "Спустя несколько секунд медсестра возвращается обратно вместе с солидного вида мужчиной."
    if _preferences.language == "english":
        $ doc_name = "Dr. Bergen"
    else:
        $ doc_name = "Д-р Берген"
    doc "О, вы наконец-то очнулись. Это очень хорошо."
    doc "Добрый день. Меня зовут доктор Майкл Берген, я заведующий нейрохирургическим отделением."
    doc "Вы пробыли в коме четыре с небольшим года."
    hide ts_emergency_room_anim
    show ts_emergency_room_anim4
    play sound_loop kardio_fastest
    $ TS.s(vpunch)
    m "Четыре {b}ГОДА?{/b}"
    "А как же папа? Мама? Все мои друзья?.."
    hide ts_emergency_room_anim4
    show ts_emergency_room_anim
    play sound_loop kardio_normal
    doc "Тише-тише... Я знаю, что это сложно, но пожалуйста, не нервничайте. Вам нужны тишина и покой."
    m "Папа? Мама? Друзья?{w=0.8}{nw}"
    doc "Понимаю, у вас накопилось много вопросов за всё это время, но позвольте вопросы сначала буду задавать я."
    doc "Как вас зовут?"
    m "Моника... Ида Моника... А вы разве не знаете?.."
    doc "Я просто проверяю ваши знания и память. Сами понимаете, четыре года – это довольно длительный срок, а с вашей травмой вполне возможны некоторые провалы в памяти."
    m "Травма? Провалы?.."
    doc "Ах да, вы же не знаете..."
    doc "Вы в нетрезвом состоянии разбились о самый край школьной парты. Точнее, двух школьных парт."
    doc "На почве этого вы потеряли сознание и у вас началось обильное кровоизлияние."
    doc "Хорошо хоть вы там были не одни, и ваши подружки вовремя позвонили в скорую."
    doc "Фельдшеры быстро отреагировали на вызов и забрали вас в карете скорой помощи, где позже над вами была проведена операция и был поставлен конкретный диагноз."
    doc "Открытая черепно-мозговая травма с ушибом тяжёлой степени в лобно-теменной области справа."
    doc "Кстати, попробуйте пошевелить конечностями – все нормально функционируют?"
    "Я делаю всё, как сказал врач – вроде всё нормально."
    doc "Очень хорошо."
    doc "Удивительно, вот вроде внешне на вас ни царапины, а над вами и вашей жизнью боролись лучшие врачи."
    doc "Доктор Нельяс, безусловно, сотворил по меньшей мере чудо, буквально вытащив вас с того света..."
    doc "Но даже после этого врачи не были до конца уверены, выживете ли вы, поэтому поместили вас в медикаментозную кому."
    doc "Ну да ладно, не будем о плохом – плохое уже было. Сейчас-то вы как себя чувствуете?"
    "А как я себя чувствую? Со всей этой бурей из бесконечно повторяющегося кошмара в виде одной недели, я говорю всего лишь одно слово:"
    m "...освобождённой..."
    doc "...Ладно, что бы это ни значило..."
    doc "В общем, когда наркоз окончательно отойдёт, и вы сможете сами себя обслуживать – прошу в наше отделение."
    doc "Или вы хотите, чтобы я на носилках вас отнёс?"
    m "Да нет... я сама..."
    doc "Ну вот и славно. Если хотите – можете вздремнуть, если, конечно, вы за четыре года так и не отдохнули."
    m "Да... лучше вздремну..."
    doc "Тогда до встречи."
    m "До свидания..."
    "И как только он ушёл, я вспомнила о том, что этот гад так и не рассказал мне, что произошло со всеми моими родными и близкими!"
    "Хотя, может, он и сам не знает..."
    "Аки, а ты как?.."
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"
    stop music fadeout 4

    $ TS.p(4)
    $ TS.s(ts_showscreens_fast)
    "Аки?"
    stop sound_loop fadeout 2
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"
    scene black with ts_paint
    $ TS.p(1)
    scene ts_hospital_room
    show dust1
    show dust2
    show dust3
    show dust4
    with ts_paint
    play music ts_ita fadein 2
    $ TS.s(ts_showscreens)
    "Я уже две недели в палате отделения нейрохирургии."
    "Соседи по палате, конечно, замечательные, но к им всем хотя бы иногда приходят родные и близкие."
    "Ко мне же за все эти две недели не пришёл вообще никто..."
    "Доктор Берген, как и ожидалось, не знает, что приключилось со всеми моими родными и друзьями."
    "Он знает лишь только, что первые несколько недель все они чуть ли не круглосуточно дежурили, подменяя друг друга, и даже спали они не у себя дома, а у двери реанимации."
    "Правда, не все из них, и далеко не всегда, но такое событие запомнилось ему даже спустя четыре года."
    "Врач говорил про какого-то голубоглазого светловолосого мужчину – по всей видимости, это папа."
    "Однако спустя некоторое время ряды продолжали редеть, пока примерно через три месяца не осталось совершенно никого..."
    "Я сразу же настроилась на худшее, что они либо обо мне просто забыли, либо они все умерли."
    "Естественно, об этом я тоже спрашивала у доктора, но тот лишь отмахнулся, сказав: «Это уже ваши личные дела, я в них не лезу»."
    "И каждый раз, когда приходил кто-то из родных или близких одного из моих соседей по палате, я лишь зарывалась лицом в подушку и тихо скулила..."
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"
    scene black with ts_paint
    $ TS.p(1)
    scene ts_hospital_corridor
    show dust1
    show dust2
    show dust3
    show dust4
    with ts_paint
    $ TS.s(ts_showscreens)
    "Спустя месяц я стала достаточно самостоятельной, чтобы наконец-то выписаться из этого ада."
    "Как странно, я только выбралась из одной «Недели Сурка», чтобы попасть в ещё один."
    "Может, это просто ещё один слой сна? Если я убью себя в этом слое, проснусь ли я в реальности? Или я проснусь в ещё одном слое более высокого уровня?"
    "За всё это время Аки так ни разу и не заговорила со мной."
    "Да, конечно, она постоянно обзывала меня, называла меня тупой бездарностью и всеми производными, но..."
    "В какой-то мере я уже привыкла к ней, потому что это единственный человек, который не забывал всё происходившее за эту неделю."
    "И по иронии судьбы, это единственный человек, которого я считала настоящим, даже несмотря на то, что это просто моё подсознание."
    "Собрав все эпикризы, я направляюсь обратно в приёмное отделение."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_waiting_room
    with wipeleft_scene

    $ TS.s(ts_showscreens)

    m "Девушка, здравствуйте..."
    misc "Добрый день, Моника. На выписку?"
    m "Да, и побыстрее, если можно. Ещё минута в этом аду, и я с собой что-нибудь сделаю..."
    misc "Ну, не будьте столь категорично настроены, я уверена, что вам хоть что-то понравилось!"
    m "Ну... у вас кормят неплохо, тут я с этим согласна."
    m "Но в остальном – это даже хуже, чем в моих снах..."
    "Медсестра не заметила мою язвительную ремарку и продолжила как ни в чём ни бывало."
    misc "Да, питание здесь просто замечательное!"
    misc "В общем, вот, ваш эпикриз. Не болейте больше!"
    stop music fadeout 4
    m "Я уж постараюсь... До свидания."
    misc "Всего доброго!"
    "Да пошла ты..."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"
    scene black with ts_paint
    $ TS.p(1)
    scene ts_house
    show dust1
    show dust2
    show dust3
    show dust4
    with ts_paint
    $ TS.s(ts_showscreens)

    play music ts_aiv fadein 1

    "Дом... милый дом..."
    "Правда, с учётом последних событий, и с учётом того, насколько долго «жила в отеле», он уже не такой-то и милый..."
    "Но это {b}мой{/b} дом."
    "Я нерешительно открываю дверь."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_entrance_day
    with wipeleft_scene

    $ TS.s(ts_showscreens)

    m "Мама? Папа?"
    m "Ау-у-у-у, вы дома?"
    m "Я пришла. Наконец-то..."
    "Тишина в ответ."
    "Странно... Хотя я уже ничему в своей жизни не удивляюсь..."
    window hide

    play sound2 pageflip
    scene ts_kitchen_night
    with pushleft

    $ TS.p(0.5)

    play sound svet_on

    scene ts_kitchen
    with flash

    $ TS.s(ts_showscreens)

    "Я включаю свет и странно оглядываюсь."
    "Какой сегодня вообще день? Какой сейчас вообще {b}год{/b}?"
    "Однако моё внимание привлекли не даты, а записка на столе."
    "Даже как-то странно, что я не заметила её, как только включила свет."
    "Она висела прямо на холодильнике под магнитиком, который мама привезла из одной из командировок. Сама записка, как ни странно, тоже от мамы. По крайней мере, я узнаю её почерк."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    scene ts_kitchen:
        blur 9.0
    with dissolve

    $ TS.s(ts_showscreens)

    play sound pageflip

    if _preferences.language == "english":
        show screen poem(poem_farewell_eng)
    else:
        show screen poem(poem_farewell)

    pause

    play sound pageflip
    $ TS.s(ts_hidescreens)
    $ TS.p(1)
    hide screen poem


    scene ts_kitchen
    with dissolve

    $ TS.s(ts_showscreens)
    
    "С каждым новым предложением я всё больше начинаю слезиться."
    "Папа... Папочка мой дорогой..."
    "Прости меня, это всё я виновата..."
    "Если бы не это чёртово вино Юри и моё неугомонное желание выпить побольше спиртного, этого бы никогда и не произошло..."
    "А мама... Надеюсь, ей там будет лучше... куда бы она там ни отправилась..."
    "Остаток дня я провожу со слезами на глазах, на щеках, по всей кухне. Я продолжаю рыдать, пока наконец не засыпаю."
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"
    scene black with ts_paint
    $ TS.p(1)
    scene ts_school_gate_day
    show dust1
    show dust2
    show dust3
    show dust4
    with ts_paint
    $ TS.s(ts_showscreens)
    "И зачем я вообще пришла в школу?"
    "...ах да, я же технически так её и не закончила."
    "Надеюсь, за четыре года все учителя ещё не забыли, что была вообще такая Ида Моника, местная звезда школы, которая клубы меняла как перчатки..."
    "Вздохнув, я направляюсь внутрь."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_school_courtyard_day
    with wipeleft_scene

    play sound pageflip
    scene ts_l5
    with wipeleft_scene

    play sound pageflip
    scene ts_corridor
    with wipeleft_scene

    $ TS.s(ts_showscreens)

    "Хотя многие учителя за это время и поменялись, директор Раддан остался."
    "Спрошу у него за девочек из клуба, и, если это вообще возможно, слёзно попрошусь доучиться жалкие полгода."
    "А то что это такое, мне уже двадцать три почти, а у меня даже среднего образования нет..."

    stop music fadeout 5

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    scene black with ts_paint
    $ TS.p(1)


    show ts_cor_split_animated
    show ts_of_split_animated
    $ TS.p(0.99)

    $ TS.s(ts_showscreens)
    play sound stuk
    show daisuke 1ba at t44
    m "Извините... можно?"
    show daisuke 2bc at f44
    if _preferences.language == "english":
        $ misc_name = "Raddan"
    else:
        $ misc_name = "Раддан"
    misc "А, мисс Ида! Сколько лет, сколько зим... Проходите, конечно."

    play music ts_hftc1 fadein 3
    play sound door_open
    scene ts_office
    show daisuke 2bf at f11
    with wipeleft
    misc "Слышал о вашем горе... Но сейчас всё хорошо, вы выздоровели?"
    show daisuke 2bh at t11
    "«Если ты слышал о моём горе, почему же ты за четыре года так ни разу ко мне и не пришёл? И даже врач не говорил, что был какой-то мужчина...»"
    "«Хотя нет, врач-то как раз о мужчине и говорил. Но не о том. О моём любимом папочке...»"
    "«А ты, тварь, за четыре года ни разу даже не удосужился подумать, как же там наша местная звезда.»"
    "С этими мыслями я невольно начинаю слезиться, но быстро беру себя в руки, что директор даже не заметил."
    m "Да... выздоровела..."
    show daisuke 1bc at f11
    misc "Ну тогда, может, чайку? Или лучше кофе?"
    show daisuke 1ba at t11
    m "Вообще, я изначально хотела с вами поговорить... О моих друзьях. Из клуба."
    show daisuke 1bh at t11
    m "Но от кофе я тоже не откажусь, спасибо."
    "На словах о девочках из Литературного клуба директор заметно погрустнел."
    show daisuke 2bg at f11
    misc "Из клуба, да..."
    misc 2bf "А вы имена их не помните? А то за эти годы столько новых учеников, всех и не вспомнишь."
    show daisuke 2bh at t11
    m "Да, конечно. Сайори, Юри и Нацуки. А фамилии... э-э-э..."
    "И тут я внезапно вспоминаю, что так ни разу не спросила их про фамилии."
    "Пум-пурум..."
    show daisuke 1be at f11
    misc "Нет, мне и имён достаточно... Они довольно редкие, так что даже в таком потоке учеников я бы их не спутал."
    misc 2bc "Да, действительно были такие. Яторо Нацуки, Аме Сайори и Касанэ Юри." #МУЖИИИИИИИИК КАСАНЬЕ, НАШ МУЖИК
    misc "Они во главе с вами все были в Литературном клубе четыре года назад."
    misc "После вашей... травмы... исполняющим обязанности президента клуба была назначена мисс Аме."
    misc 1bf "Однако, естественно, лишившись президента клуба за неделю до фестиваля, и не набрав даже минимум в четыре человека, клуб попросту расформировали."
    misc "Помимо этого, у мисс Аме была клиническая депрессия, о которой мы..."

    play sound fb
    $ TS.m(VHS())
    show s_kill_bg_zoom_cb zorder 1
    show s_kill_bg2_zoom_cb zorder 1
    show s_kill_zoom_cb zorder 3
    show s_kill2_zoom_cb zorder 3
    show s_kill_cb as s_kill_zoom_trans zorder 3:
        truecenter
        alpha 0.5
        zoom 2.0 xalign 0.5 yalign 0.05
        pause 0.5
        dizzy(1, 1.0)
    with flash
    $ TS.s(ts_showscreens_fast)
    misc "Узнали слишком поздно..."
    misc "Вечером того же дня, сразу после фестиваля, её нашли повешенной у себя же дома. Мы ничего не смогли сделать..."
    $ TS.s(ts_hidescreens_fast)
    " {w=0.1}{nw}"
    scene ts_yrec_trup_end
    $ TS.m(VHS())
    with ts_paint
    $ TS.s(ts_showscreens_fast)
    misc "Что касается мисс Касанэ, то она не выдержала смертей, по сути, двух из трёх людей, которых она считала друзьями."
    misc "И через две недели её нашли в кабинете уже бывшего клуба со вспоротым животом."
    $ TS.s(ts_hidescreens_fast)
    " {w=0.1}{nw}"
    scene ts_nat_trup_end
    $ TS.m(VHS())
    with ts_paint
    $ TS.s(ts_showscreens_fast)
    misc "Что же до мисс Яторо..."
    misc "Помимо того, что она потеряла всех своих друзей за буквально несколько недель, над ней, как оказалось, издевались её друзья и даже её собственный отец..."
    m "И ей настолько надоело то, что её никто не воспринимает всерьёз, что однажды она подумала: «А зачем это всё нужно?», и свернула себе шею. Тоже насмерть."
    "Последние слова я уже договариваю за него. Это ровно то, что рассказывала мне Аки ещё тогда, в тот самый первый цикл много месяцев назад."
    play sound fb
    scene ts_office
    show daisuke 2bh at t11
    with flash
    $ TS.s(ts_showscreens_fast)
    "После этой фразы я падаю навзрыд."
    "Все мои друзья, все мои близкие... Все, кем я когда-либо дорожила, либо мертвы, либо находятся на другом конце земного шара." #плоскоземельщики сосать
    show daisuke 2bf at f11
    misc "Я сожалею о вашей утрате... Но это жизнь, все рано или поздно умирают..."
    show daisuke 2bh at t11
    "Я тем временем просто продолжаю рыдать."
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"
    $ TS.p(5)
    $ TS.s(ts_showscreens)
    "Лишь спустя пятнадцать минут я хоть как-то успокаиваюсь и говорю хотя бы членораздельно."
    m "Ладно... спасибо вам большое, господин Раддан... Теперь-то я точно знаю..."
    show daisuke 2bf at f11
    misc "Знаете что?"
    show daisuke 2bh at t11
    m "Да так, неважно..."
    "Я шмыгаю носом и говорю."
    m "Ну, господин Раддан, до скорых встреч."
    show daisuke 2bg at f11
    misc "Подождите, а кофе?"
    show daisuke 2bh at t11
    "Кофе так и остался нетронутым."
    m "Ах да. Спасибо, что напомнили."
    "Я залпом выпиваю всю чашку и ещё раз пытаюсь попрощаться с ним. На этот раз уже окончательно и навсегда."
    m "Прощайте, господин Раддан."
    stop music fadeout 2
    show daisuke 1be at f11
    misc "Д-до свидания..."
    show daisuke 1bh at t11
    "Надеюсь, крыша не заперта..."
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play music ts_hftc2 fadein 2
    play sound pageflip
    scene ts_roof
    with wipeleft_scene

    $ TS.s(ts_showscreens)

    "Какая же я неудачница..."
    "Из-за одной моей авантюры... Из-за одной моей оплошности..."
    "Все мои друзья... мертвы..."
    "Но ничего... скоро это всё закончится..."
    "Ветерок такой тихий и приятный... даже успокаивающий..."
    "Хотя что я вообще говорю? Ни один ветер не сможет успокоить все мои утраты..."
    show sayori 1a at t51:
        alpha 0.4
    with linearblur
    $ TS.s(ts_showscreens_fast)
    "Сайори..."
    show yuri 1a at t52:
        alpha 0.4
    with linearblur
    $ TS.s(ts_showscreens_fast)
    "Юри..."
    show natsuki 1a at t53:
        alpha 0.4
    with linearblur
    $ TS.s(ts_showscreens_fast)
    "Нацуки..."
    show hiroto 1a at t54:
        alpha 0.4
    with linearblur
    $ TS.s(ts_showscreens_fast)
    "Папа..."
    show minami 1a at t55:
        alpha 0.4
    with linearblur
    $ TS.s(ts_showscreens_fast)
    "Даже мама..."
    hide sayori
    hide yuri
    hide natsuki
    hide hiroto
    hide minami
    with linearblur
    $ TS.s(ts_showscreens)
    "Никого из них больше нет..."
    "А всё это... из-за меня..."
    "Я снова начинаю плакать."
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"
    $ TS.p(5.5)
    $ TS.s(ts_showscreens)
    "Закончив рыдать как маленькая девочка, я решительно встаю."
    "И направляюсь... к краю крыши."
    "Ух, высоко-то как!"
    "Но так даже лучше: так меня точно никто не спасёт..."
    em "Эй-эй, ты что делаешь?!"
    "Здесь этаж пятый, не меньше. Мне этого хватит с головой."
    "Но тут в дело снова вмешался этот проклятый инстинкт самосохранения."
    em "Слушай, а может, лучше не стоит?"
    em "Всё-таки высоко..."
    m "Да я уже десятки раз так делала во сне..."
    em "Ну так в этом-то всё и дело! Это же не сон, это реальность!"
    m "А что вообще есть {i}реальность{/i}? Просто ещё один слой? Сама же говорила, что то, как я спала – это были просто очень детализированные сны."
    m "Что, если реальность на самом деле – это просто ещё один большой сон?"
    em "Да говорю же, не надо, разобьёшься ведь насмерть!"
    m "Знаешь, {b}Аки{/b}... А я говорю, что надо."
    em "Нет, стой, подожди!{w=0.5}{nw}"
    window hide
    play music ts_hftc3
    $ TS.m(ts_roof_beg)
    play sound ts_running
    $ TS.p(2.5)
    stop sound
    play sound2 ts_zabor_crash
    $ TS.p(0.5)
    stop sound2
    scene black
    $ TS.p(0.15)

    play sound ts_introshoot
    scene ts_sky_fon
    show ts_wind_wnim at ts_running_fast
    $ TS.m(ts_padenie_s_krishi_suka)
    $ TS.p(2.5)
    stop sound

    scene ts_mon_padenie_fon
    show ts_mon_padenie_maloletka
    $ TS.m(ts_bad_end_padenie_anim_blya)
    $ TS.p(6)
    scene ts_mon_padenie_fon:
        blur 0
        ease 1.5 blur 5.5
        ease 1.5 blur 3
        ease 1.5 blur 7.5
        ease 1.5 blur 3
        ease 1.5 blur 5.5
        ease 1.5 blur 3
        repeat
    show ts_mon_padenie_maloletka_static:
        xalign 0.5
        yalign 0.5
        zoom 1.0
        parallel:
            linear 1.0 zoom 1.03
        parallel:
            ease 1.0 xalign 0.475
            ease 1.0 xalign 0.525
            repeat
        parallel:
            ease 1.5 rotate 1.15 zoom 1.035
            ease 1.5 rotate -1.3 zoom 1.025
            repeat
    $ TS.m(ts_bad_end_padenie_anim_blya1)
    $ TS.p(2)
    $ TS.s(ts_showscreens)
    "Секунды, что я лечу вниз, кажутся часами. Но мне уже всё равно."
    "Литературный клуб снова соберётся вместе. Мы с папой тоже будем вместе..."
    "Да и с мамой мы рано или поздно встретимся..."
    window hide
    scene ts_sky_fon
    show ts_wind_wnim at ts_running_fast
    $ TS.m(ts_padenie_s_krishi_suka)
    $ TS.p(3.5)
    stop music
    scene black
    play sound sfx_body_bump
    show ts_altbloodanim
    $ TS.p(2)

    scene ts_bad_end_moni_dead_anim_sooqa:
        align(0.05, 0.8) zoom 3.0
        ease 15 align(0.75, 0.8) zoom 3.0
        ease 5 align(0.5, 0.5) zoom 1.0
    with Fade(1.5, 2, 1.2)

    $ TS.s(ts_showscreens)

    "Ведь реальность – это просто ещё один слой."
    "Даром что я в новом слое не возвышаюсь над всем, а падаю. Прямо в бездну."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    scene black
    with Fade(1.5, 2, 1.2)

    $ TS.p(1)

    play sound psy_fast_3
    scene ts_mon_padenie_dead
    $ TS.p(0.05)
    scene ts_mon_padenie_full
    $ TS.p(0.05)
    scene ts_mon_padenie_dead
    $ TS.p(0.05)
    scene ts_mon_padenie_full
    $ TS.p(0.05)
    scene ts_mon_padenie_dead
    $ TS.p(0.05)
    scene ts_mon_padenie_full
    $ TS.p(0.05)
    stop sound
    scene black

    $ TS.s(ts_null_transform)
    window hide

    jump bad_credits_ts_label