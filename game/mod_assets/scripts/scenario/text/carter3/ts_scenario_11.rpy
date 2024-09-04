label ts_scenario_11:

    $ renpy.block_rollback()

    python: # ОБНОВЛЯЕМ RPC
        ts_rpc_carter10()

    $ persistent.rpclabel = "10"

    $ persistent.sprite_time = "day"
    $ persistent.carter2menu = False
    $ persistent.carter3menu = True
    $ persistent.badendmenuperedglitch = False
    $ persistent.badendmenuskipglitch = False
    $ persistent.badendmenu = False
    $ persistent.goodendmenu = False
    $ persistent.peredbadendmenu = False
    $ persistent.peredgoodendmenu = False

    $ persistent.uncolorize = "lite"

    play music ts_roae fadein 2

    play sound ts_alarm fadein 2

    pause 2

    scene ts_bedroom
    show unblink
    show layer master at ts_vstavai_shashlik
    pause 3
    play sound svet_on
    pause 1.5

    show layer screens at ts_showscreens

    "Наступает среда."
    "...по крайней мере, я чувствую, что сегодня среда."
    "Аки же вроде говорила, что во сне происходит путаница с конкретными датами и днями недели."
    "Однако, помимо понедельника, я прожила ещё одну день и ещё одну ночь. Значит, сегодня среда."
    "И пусть кто-то со мной только поспорит."
    "Я главный и единственный герой моей жизни, а остальные в моей жизни лишь наблюдатели."
    "На часах тем временем привычные семь утра."
    "По крайней мере, {b}я{/b} чувствую, что сейчас семь утра. Или около того."
    if unluck6 == True:
        "...ладно, на улице уже достаточно светло, но папа ещё не вломился ко мне с криками, что я снова проспала, значит, я проснулась как раз примерно вовремя."
    else:
        "...ладно, на улице уже достаточно светло, но папа ещё не вломился ко мне с криками, что я проспала, значит, я проснулась как раз примерно вовремя."
    "Кажется, сегодня снова готовлю я? Хотя, не то чтобы это ещё было важно..."
    "Если всё, что говорит Аки, верно, то я могу хоть всю неделю дома не появляться, и к субботе папа обо всём забудет..."
    show monika 1pi at f11
    with linearblur
    em "Я тебе это уже пятый день вдалбливаю, а ты только сейчас это поняла?"
    em 1pr "Я, конечно, всегда знала, что ты не особо отличаешься умом и сообразительностью, но чтобы {i}настолько{/i}..."
    show monika 1pq at t11
    m "Пришла мне настроение с утра пораньше испортить?"
    show monika 3pb at f11
    em "Нет, ты и сама без меня справишься! А я просто констатирую очередной факт."
    em 1pd "Ладно, давай умываться уже."

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

    show monika 1bc at t11
    "Наспех умывшись и почистив зубы, я быстро спускаюсь на кухню."
    show monika 2bd at f11
    em "И что, даже не пожалуешься в очередной раз, как тебе неприятно умываться холодной водой, даже несмотря на то, что умываешься именно холодной водой с самого детства?"
    show monika 2bh at t11
    m "Пожаловалась бы, но у меня нет времени. Надо же ещё завтрак приготовить. Хотя бы простой и быстрый."
    show monika 3bk at f11
    em "А не ты ли жаловалась на тему того, какой папа страшный и ужасный?"
    show monika 3bj at t11
    m "Жаловалась, да. Но я уже как-то привыкла к странностям папы. Что в обычной жизни, что в этих циклах."
    "Да, весь вторник папа время от времени ещё «пугал» меня, однако эффект новизны быстро выветрился, да и я стала вести себя более естественно."
    "Остальные, кстати, делали примерно то же самое: иногда пугали меня, однако в целом первый обмен стихами прошёл так же, как и на прошлой неделе."
    "Конечно, стихи девочек были написаны слово в слово, буква в букву, и даже мысли по поводу моего стиха и стиха каждой из девочек вообще не отличались, но..."
    stop music fadeout 3
    "Наверное, это и к лучшему?"
    "Мысленно усмехнувшись, я всё-таки спускаюсь на кухню."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_kitchen
    with wipeleft_scene

    show layer screens at ts_showscreens

    play music ts_sail fadein 2
    $ persistent.ingame_pizda = False
    "Оглядываясь по сторонам, я вижу, что папа уже тут как тут."
    $ gtextsuka = glitchtext(18)
    $ persistent.ingame_pizda = True
    show layer screens at ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake)
    show ts_hiroto_psyhodelic_pizdoc_eye at ln11
    ts_ft "Привет, [gtextsuka][gtextsuka]{w=0.7}{nw}"
    hide ts_hiroto_psyhodelic_pizdoc_eye
    $ persistent.ingame_pizda = False
    show layer screens
    show hiroto 1b at f11
    ts_ft "Доброе утро, Моника!{fast}"
    show hiroto 1a at t11
    m "Д-доброе, пап..."
    show hiroto 1b at f11
    ts_ft "Что на завтрак?"
    show hiroto 1a at t11
    "Хотела бы я и сама знать..."
    m "Э-э-э... Макароны. Тебе с сосисками, а мне с сахаром. Ну и хлопья с молоком и кофе, как обычно..."
    show hiroto 1t at f11
    ts_ft "А ты макароны варить-то хоть умеешь?"
    show hiroto 1s at t11
    show layer screens at vpunch
    m "Да! И причём получше многих."
    show hiroto 1g at f11
    ts_ft "Ладно, ладно, не злись так, я же просто пошутил."
    show hiroto 1f at t11
    if unluck4_cooking == True or unluck6 == False: #ну короче блять сцены, где Моника сама готовит
        "Внезапно я осознаю, что папа ещё не видел, как я готовлю."
        "Впрочем, он ещё не знает, что я умею готовить крупы или макароны..."
    else:
        "Внезапно я осознаю, что ни с того, ни с сего сорвалась на папу."
        "Впрочем, папа не из обидчивых..."
    m "В общем, минут через пятнадцать-двадцать всё будет готово. Я позову, когда можно будет кушать."
    show hiroto 1t at f11
    ts_ft "Хорошо."
    show hiroto 1s at t11
    m "Вот и замечательно. А теперь освободите, пожалуйста, кухню, кухарке работать над завтраком надо."
    show hiroto 1u at f11
    ts_ft "Ладно, ладно, освобождаю."
    show hiroto 1u at ron11

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_kitchen
    with wipeleft_scene

    show layer screens at ts_showscreens

    if unluck4_cooking == True or unluck6 == False:
        "Как обычно, я набираю примерно треть кастрюли и ставлю её кипятиться."
    else:
        "Я набираю примерно треть кастрюли и ставлю её кипятиться."
    "Хотя и набрала я немного, это всё равно займёт некоторое время."
    "В свободное же время я решаю сделать папе бутербродов на работу."
    $ persistent.ingame_pizda = False
    m "{size=+6}Пап, ты с чем бутерброды будешь?{/size}"

    $ persistent.ingame_pizda = True
    show layer screens at ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake)

    scene ts_kitchen_glitch_pizdets
    ts_ft "{size=+6}Мне без разницы, главное, чтобы там были твои GLAZA.{/size}"
    m "{size=+6}Что, прости?{/size}"
    scene ts_kitchen
    show layer screens
    $ persistent.ingame_pizda = False
    ts_ft "{size=+6}Я говорю, да как обычно, с колбаской и сыром.{/size}"
    m "{size=+6}Хорошо.{/size}"
    "Я отсчитываю три ломтика хлеба и начинаю нарезать папе бутерброды."
    "И конечно же, по закону подлости на хлебе слишком много места, чтобы положить два кусочка колбасы, но слишком мало, чтобы положить три."
    "Впрочем, как говорила Сайори: «Лучше перебдеть, чем недобдеть»."
    "Или она не так говорила?"
    show monika 2bd at f11
    with linearblur
    em "Да, именно так она и говорила. Если не в этом сне, так в другом."
    show monika 2ba at t11
    "«Ладно...»"
    "Сказала я внутренним голосом, сама того не заметив."
    if unluck_ball >= 4:
        "Наверное, чтобы папа не задавал лишних вопросов..."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_kitchen
    with wipeleft_scene

    show layer screens at ts_showscreens

    "Спустя пару минут три бутерброда готовы."
    "В каждый из них я всё-таки положила по три кусочка колбасы. Пусть лучше третий кусочек вывалится, и папа его просто поднимет со стола, чем если бы половина ломтика была абсолютно пустой."
    "Вода тем временем уже начинает закипать."
    "Я предусмотрительно кладу немного соли в почти кипящую воду, которая издаёт приятный пшикающий звук."
    show monika 3bb at f11
    with linearblur
    em "А если бы ты солила не только воду, но и сами макароны, то было бы ещё лучше."
    show monika 1ba at t11
    "Я хочу огрызнуться, но понимаю, что её слова не лишены смысла."
    if unluck6 == False:
        "Тем более, что в прошлый раз я чувствовала, что макароны какие-то недосоленные."
    "«Ладно, сами макароны я тоже посолю ещё немного. Довольна?»"
    show monika 3bb at f11
    em "Довольна."
    em 2bd "Смотри, вода уже так и просит, чтобы в неё добавили макароны."
    show monika 2ba at t11
    stop music fadeout 5
    "Я поворачиваюсь к кастрюле и осознаю, что Аки так-то права."
    "Вода уже вовсю бурлит, и следующим логичным шагом было бы добавить в неё макароны."
    "Что я, собственно, и делаю."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_kitchen
    with wipeleft_scene

    show layer screens at ts_showscreens

    play music ts_alt fadein 2
    "В детстве папа постоянно ломал спагетти, чтобы они сварились быстрее, однако я знаю, что это моветон, и что итальянцы бы это как минимум не одобрили."
    "А как максимум – сожгли бы на костре..."
    "Тем более, что я и так русая, почти что рыжая, так что всё логично."
    "И хотя я никогда не была в Италии, да и вряд ли там побываю, я всё равно кладу целые спагетти, а не поломанные."
    stop music fadeout 2
    "Да, они так варятся чуть дольше, но зато это гораздо более аутентично."
    play music ts_sail fadein 2
    if unluck6 == False:
        "Положив макароны в воду и понадеявшись, что в этот раз я положила достаточно, я наливаю воду в чайник и ставлю чайник тоже кипятиться."
    else:
        "Положив макароны в воду и понадеявшись, что я положила достаточно, я наливаю воду в чайник и ставлю чайник тоже кипятиться."
    "Таким образом, весь завтрак сразу будет подан почти что сразу же."
    "Хлопья с молоком – это самое простое и требующее меньше всего усилий, если для этого вообще какие-то усилия нужно прилагать."
    "Просто насыпать хлопья, залить молоком, и вот тебе готовое блюдо."
    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_kitchen
    with wipeleft_scene

    show layer screens at ts_showscreens
    "Ещё через пару минут завтрак полностью готов."
    m "{size=+6}Пап, иди завтракать!{/size}"
    "Однако папа не отвечает."
    $ persistent.ingame_pizda = False
    "...Нет, по утрам никаких политических передач не показывают, поэтому логичным объяснением будет лишь то, что он не дождался завтрака и уснул..."

    $ persistent.ingame_pizda = True
    show layer screens at ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake)


    show ts_hiroto_zalagal at f11
    ts_ft "[gtextsuka][gtextsuka][gtextsuka][gtextsuka]{w=0.2}{nw}"
    hide ts_hiroto_zalagal
    show layer screens
    $ persistent.ingame_pizda = False
    show hiroto 1b at f11
    ts_ft "{size=+4}Иду-иду!{/size}{fast}"
    show hiroto 1a at t11
    "...ну или он просто не сразу спустился. Что тоже не лишено смысла – дом-то у нас явно не из маленьких."
    m "Приятного аппетита, пап..."
    show hiroto 1b at f11
    ts_ft "Спасибо, Моника. Взаимно."
    show hiroto 1a at t11
    m "{size=-4}Спасибо...{/size}"
    show hiroto 1b at t11
    stop music fadeout 3
    "Сегодня мы по большей части завтракаем молча, и лишь изредка папа задаёт банальные вопросы вроде того, как я проведу день, и что сегодня нового в клубе."
    show hiroto 1a at t11
    "Я точно так же банально отвечаю..."
    play music ts_podmetro
    show layer screens at vpunch
    "Как тут я вспоминаю, что написать стих-то я и забыла!"
    "Я резко ахаю и тут же замолкаю."
    show hiroto 1h at t11
    "Папа же, которому не совсем свойственно подмечать эмоциональные тонкости, такую резкую смену настроения не заметить просто не мог."
    show hiroto 1h at f11
    ts_ft "Моника, с тобой всё хорошо? Ты что-то очень резко замолчала."
    show hiroto 1j at t11
    "«Нет, пап, всё просто ужасно, это всего лишь второй обмен стихами, а президент клуба, который должен подавать пример другим, сам стих не написал, и даже ни разу об этом не задумался!»"
    m "Да, пап, всё нормально, просто... Фестиваль всё ближе, нервы всё более расшатанные, и всё такое..."
    stop music fadeout 2
    "Одно хорошо, что под предлогом предстоящего фестиваля можно оправдать любое несвойственное мне поведение."
    play music ts_sail fadein 2
    show hiroto 1h at f11
    ts_ft "Ну ладненько..."
    show hiroto 1j at t11
    "А хотя нет, ещё хорошо, что папа после упоминания о фестивале как будто напрочь забывает обо всём, о чём он только что говорил."
    "Однако это всё равно не отменяет того, что я так и не написала стих."
    "..."
    "Так, ладно... Дыши ровнее... Я хотя бы примерно помню, о чём тот стих, который я писала в прошлую среду..."
    "Да, пусть и не дословно, но в общих чертах я всё ещё его помню."
    show hiroto 1f at t11
    "После того, как папа увидел, что я успокоилась, он и сам успокоился и улыбнулся."
    show hiroto 1b at t11
    "И в итоге мы оба с этого просто посмеялись."
    stop music fadeout 4
    em "Ха, ха, как смешно, бездарность забыла написать стих, а теперь ещё и смеётся с этого факта."
    "«А ты заткнись вообще, и без тебя тошно.»"
    em "..."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_kitchen
    with wipeleft_scene

    show layer screens at ts_showscreens

    play music ts_gramatik
    show hiroto 1a at t11
    "Позавтракав, я машинально перевожу взгляд на часы..."
    window hide
    python:
        _preferences.volumes['music'] = 0.0
        _preferences.volumes['sfx'] = 1.0
    scene ts_kitchen_glitch_pizdets

    python:
        currentpos = get_pos()
        startpos = currentpos - 0.2
        if startpos < 0: startpos = 0
        track = "<from " + str(startpos) + " to " + str(currentpos) + ">mod_assets/source/audio/ost/ts_glitch_music9.ogg"
        renpy.sound.play(track, loop=True)

    show monika g2 at i11
    pause 1
    stop sound
    python:
        _preferences.volumes['music'] = .45
        _preferences.volumes['sfx'] = .65
    scene ts_kitchen
    show hiroto 1a at t11
    "...Ах да. Время здесь теперь течёт своим чередом, оно мне неподвластно."
    "Ну, если папа ещё не кричит, что мы опаздываем, то сейчас не позже восьми утра."
    "Зная, что ничего снова не получится, я всё равно решаю испытать удачу и тактично спросить папу, который час."
    m "Пап, а мы не опаздываем?"
    show hiroto 1v at f11
    ts_ft "Да рано ещё выходить, ещё достаточно времени."
    show hiroto 1s at t11
    $ persistent.ingame_pizda = False
    m "А достаточно – это сколько конкретно, если не секрет?"
    show hiroto 1t at f11
    ts_ft "Не секрет, да. Ещё {w=0.01}{nw}"
    $ gtextsuka = glitchtext(44)
    $ persistent.ingame_pizda = True
    show layer screens at ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake)
    window hide
    python:
        _preferences.volumes['music'] = 0.0
        _preferences.volumes['sfx'] = 1.0
    scene ts_kitchen_glitch_pizdets

    python:
        currentpos = get_pos()
        startpos = currentpos - 0.2
        if startpos < 0: startpos = 0
        track = "<from " + str(startpos) + " to " + str(currentpos) + ">mod_assets/source/audio/ost/ts_glitch_music10.ogg"
        renpy.sound.play(track, loop=True)

    show monika g1loop at i11
    ts_ft "[gtextsuka][gtextsuka]"
    stop sound
    python:
        _preferences.volumes['music'] = .45
        _preferences.volumes['sfx'] = .65
    show layer screens
    $ persistent.ingame_pizda = False
    scene ts_kitchen
    show hiroto 1s at i11
    "Ну, видимо, не судьба узнать мне точное время."
    "Что же, буду действовать по наитию. Так сказать, на глазок."
    show hiroto 1w at t11
    m "Ну, тебе, может, и рано, ты же машину починил..."
    m "А мне вот в самый раз. Если что, длинной дорогой пойду."
    show hiroto 1z at f11
    ts_ft "Ну-у-у, хорошо..."
    show hiroto 1b1 at t11
    m "Вот и отлично!"
    $ persistent.ingame_pizda = False
    m "Всё, пока, пап, люблю тебя!"
    hide hiroto
    $ persistent.ingame_pizda = True
    python:
        _preferences.volumes['music'] = 0.0
        _preferences.volumes['sfx'] = 1.0
    play sound ts_smeh_pizdec
    show layer screens at ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake)
    show ts_hiroto_zalagal at i11
    ts_ft "Я хочу четвертовать тебя, распотрошить тебя, выколоть тебе глаза и съесть твои конечности{w=0.5}{nw}"
    show layer master
    stop sound
    show layer screens
    $ persistent.ingame_pizda = False
    hide ts_hiroto_zalagal
    python:
        _preferences.volumes['music'] = .45
        _preferences.volumes['sfx'] = .65
        _history_list = []
    show hiroto 2g at f11
    ts_ft "И я тебя люблю."
    show hiroto 1f at t11
    stop music fadeout 3
    "Что он сказал? Уже неважно."
    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"
    show hiroto 1f at ron11
    hide hiroto with dissolve
    show layer screens at ts_showscreens
    "Хмыкнув, я направляюсь к выходу."
    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_house
    with wipeleft_scene


    pause 2

    play sound pageflip
    scene ts_street
    with wipeleft_scene

    show layer screens at ts_showscreens

    play music ts_ios fadein 2
    "Ну, я вышла. И что теперь?"
    show monika 2k at f11
    with linearblur
    em "Ну как что? У тебя ещё вообще-то стих не написан!"
    em 1n "Ай-ай-ай, как же так, весь такой правильный президент, сама дала задание всем остальным, и сама же забыла это задание сделать..."
    show monika 1m at t11
    m "Так, ну-ка!.. Я и сама знаю и помню об этом."
    show monika 3l at f11
    em "Ну так если ты знаешь и помнишь, что у тебя стих не написан, почему ты за целый вечер так и не вспомнила, что его всё-таки нужно написать?"
    em 2n "Каждый раз, когда я думаю, что более бездарной ты быть не можешь, ты раз за разом доказываешь мне обратное."
    show monika 2m at t11
    m "Тихо там на балконе!"
    show monika 2a at t11
    m "Я ещё в общих чертах помню, о чём стих, я писала его буквально на прошлой неделе."
    m "За одну перемену перепишу стих, и всё, и как будто Моника снова идеальная во всём."
    show monika 4b at f11
    em "Слу-у-ушай... А давай я тебе помогу!"
    show monika 5a at t11
    m "И как именно ты мне поможешь?"
    show monika 3b at f11
    em "Ну, я тоже помню твой шедевр литературы, причём даже лучше, чем ты!"
    em 2b "Поэтому, если у тебя возникнут какие-то сложности с подбором слов или знаками препинания, обращайся ко мне!"
    show monika 5a at t11
    m "Я же пожалею об этом потом, так ведь?"
    show monika 2j at t11
    m "Ну ладно, если тебе будет не сложно...{w=0.8}{nw}"
    show monika 3l at f11
    em "Да-да-да, мне сложно не будет."
    em 4b "У тебя будет {nw}"
    hide monika
    play sound slender
    show monika g1loop at i11
    extend "лучшее стихотворение на свете!{nw}"
    window hide
    pause 1.5
    stop sound
    show monika 4a at t11
    show layer screens at ts_showscreens_fast
    m "...что?"
    show monika 2n at f11
    em "Да ничего."
    em 3b "Смотри, а вот уже и школа!"

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"
    hide monika
    with linearblur
    scene ts_street at ts_bg_into
    pause 0.5
    scene ts_school_gate_day at ts_bg_exodus
    pause 0.5

    show layer screens at ts_showscreens

    stop music fadeout 3
    "Действительно, пока я разговаривала с Аки, я и сама не заметила, как очутилась прямо у входа в школу."
    "Следующим логичным шагом во всех смыслах этого слова было бы зайти в эту школу."

    show layer screens at ts_hidescreens
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

    show layer screens at ts_showscreens

    play music ts_sealevel fadein 2
    "Поскольку в коридоре почти никого и никакой учитель не подходит ко мне с вопросом, почему я не на уроке, то это означает, что я пришла пораньше."
    show monika 4b at f11
    with linearblur
    em "Ну, раз пришла пораньше, то самое время писать стих!"
    show monika 3a at t11
    m "Да, стих..."
    show monika 2h at t11
    m "О чём он был, кстати, не напомнишь?"
    show monika 2i at f11
    em "Ты что, издеваешься?"
    show monika 2h at t11
    m "Да шучу я – надо же хоть как-то обстановку разрядить."
    show monika 1r at f11
    em "Инфантилка..."
    show monika 1q at t11
    m "Да всё, всё, теперь серьёзно. Стих, да."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"
    hide monika
    with linearblur
    scene ts_corridor at ts_bg_into
    pause 0.5
    scene ts_notebook at ts_bg_exodus
    pause 0.5

    show layer screens at ts_showscreens

    "Та-а-ак, какая там первая строка?"
    "Про цвета, да."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    scene ts_notebook:
        blur 9.0
    with dissolve

    show layer screens at ts_showscreens

    play sound pageflip

    show screen poem(poem_m22a)

    pause

    play sound pageflip
    show layer screens at ts_hidescreens
    pause 1.0
    hide screen poem


    scene ts_notebook
    with dissolve

    show layer screens at ts_showscreens
   
    "..."
    "Они не... что «не»?"
    "Всего три слова, а я уже забыла, какое там следующее слово."
    "Не останавливаются? Не прекращаются? Не заканчиваются?"
    "Ладно, вспомню потом..."
    "Пишем дальше."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    scene ts_notebook:
        blur 9.0
    with dissolve

    show layer screens at ts_showscreens

    play sound pageflip

    show screen poem(poem_m22b)

    pause

    play sound pageflip
    show layer screens at ts_hidescreens
    pause 1.0
    hide screen poem


    scene ts_notebook
    with dissolve

    show layer screens at ts_showscreens

    
    "Чёрт, ещё и ручка пишет, как на последнем издыхании..."
    "Некоторые буквы и свежей ручкой едва видно, а к моменту, когда мы будем делиться стихами, половины стиха видно не будет."
    "Что у нас там дальше?"


    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    scene ts_notebook:
        blur 9.0
    with dissolve

    show layer screens at ts_showscreens

    play sound pageflip

    show screen poem(poem_m22c)

    pause

    play sound pageflip
    show layer screens at ts_hidescreens
    pause 1.0
    hide screen poem


    scene ts_notebook
    with dissolve

    show layer screens at ts_showscreens

    
    "Да твою мать! Ручка {b}уже{/b} отсыхает, а ведь ещё и пяти минут не прошло!"
    "От злости я пишу следующие слова большими буквами."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    scene ts_notebook:
        blur 9.0
    with dissolve

    show layer screens at ts_showscreens

    play sound pageflip

    show screen poem(poem_m22d)

    pause

    play sound pageflip
    show layer screens at ts_hidescreens
    pause 1.0
    hide screen poem


    scene ts_notebook
    with dissolve

    show layer screens at ts_showscreens


    "..."
    "От того, что я написала «какофония бессмысленного шума» большими буквами, ничего не поменялось."
    "Ну да и ладно. Как говорится, что написано пером, не вырубишь и топором."
    "Только вот вместо пера у меня долбаная{w=0.44}"
    show layer screens at vpunch
    extend " засыхающая{w=0.44}"
    show layer screens at vpunch
    extend " ручка{w=0.44}."
    "Если я допишу этот стих до конца, это уже будет чудом."
    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"
    pause 2
    show layer screens at ts_showscreens
    "Ладно, кажется, я отвлеклась."
    "Кажется, Юри на {i}прошлой неделе{/i} что-то говорила о том, как я пытаюсь перекричать шум?"
    "Ну, единственный способ «перекричать шум» в письменном виде – это писать сами слова побольше, покрупнее."
    "Это я и делаю."


    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    scene ts_notebook:
        blur 9.0
    with dissolve

    show layer screens at ts_showscreens

    play sound pageflip

    show screen poem(poem_m22e)

    pause

    play sound pageflip
    show layer screens at ts_hidescreens
    pause 1.0
    hide screen poem


    scene ts_notebook
    with dissolve

    show layer screens at ts_showscreens

    
    "А как там дальше было? Что-то про волны?"
    "И ещё прилагательные какие-то..."
    "Безумные? Возможно."
    "Штормовые?.."
    "...нет, всё-таки тут другое прилагательное нужно..."
    "Раскатывающиеся? Нет..."
    "...вот же, грохочущие!"
    "Довольная, я пишу следующую строку."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    scene ts_notebook:
        blur 9.0
    with dissolve

    show layer screens at ts_showscreens

    play sound pageflip

    show screen poem(poem_m22f)

    pause

    play sound pageflip
    show layer screens at ts_hidescreens
    pause 1.0
    hide screen poem


    scene ts_notebook
    with dissolve

    show layer screens at ts_showscreens

    stop music fadeout 3

    "Если до собрания клуба выживет хоть одно слово, я этому несказанно обрадуюсь..."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    scene ts_notebook at ts_bg_into
    pause 0.5
    scene ts_corridor at ts_bg_exodus
    pause 0.5

    show layer screens at ts_showscreens

    play music ts_ootw fadein 2
    "Тем временем начинают набегать другие ученики."
    "Естественно, они видят, чем я занимаюсь, но мешать не решаются."
    "В классе я и так заработала своеобразную репутацию нелюдимого человека, поэтому и в этот раз они разве что подумали, что «блаженная опять мемуары какие-то пишет»."
    "А мне всё равно, я слишком сосредоточена на том, чтобы переписать стих как можно скорее."
    play sound zvonok
    "Чёрт, не успела..."
    "Впрочем, я эту тему и без того наизусть знаю, лично для меня там не будет абсолютно ничего нового, поэтому я вместе с остальными иду в класс, чтобы закончить написание стиха уже там."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"
    scene ts_corridor:
        align (0.5, 0.5) zoom 1
        ease 1.2 align (0.3, 0.4) zoom 1.5
    pause 0.7
    play sound door_open
    pause 0.5
    scene ts_class at ts_bg_exodus
    pause 0.5
    show layer screens at ts_showscreens

    teacher "Доброе утро, класс."
    teacher "Записываем тему сегодняшнего урока..."
    "Я делаю вид, что записываю вместе с остальными, и спустя пару минут, когда все уже вошли в ритм урока, я незаметно достаю свою записную книжку и продолжаю писать."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    scene ts_class at ts_bg_into
    pause 0.5
    scene ts_notebook_glitch at ts_bg_exodus
    pause 0.5

    show layer screens at ts_showscreens
    "Однако за то время, пока я делала вид, что являюсь обычным учеником, я напрочь забыла остаток стихотворения."
    "«Аки? Можешь мне помочь?»"
    em "{b}Как именно?{/b} Меня же нет."
    "«Ну, в смысле, мысленно помочь, а я уже буду записывать.»"
    em "Ладно, хорошо..."
    em "На какой строке ты остановилась?"
    "«На волнах, которые безумные и грохочущие.»"
    em "Так, ладно... Чисто логически – у тебя есть подлежащее с соответствующими атрибутами..."
    em "Поэтому за ним должен идти глагол, иначе предложение получается неполным."
    em "Если у тебя есть волны, которые безумные и грохочущие, то какими глаголами они должны продолжаться?"
    "«Хм-м-м... Они... рычат? Визжат?»"
    em "Визжат, да. А волны, которые такие же безумные и грохочущие, но поменьше, какими глаголами должны обладать?"
    "«Хм-м-м... На ум приходит только пронзительный писк... Ну и рёв тоже...»"
    em "Во-о-от. Пищат, визжат, пронзают. Это и будет следующая строка."
    "«Хорошо...»"

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    scene ts_notebook_glitch:
        blur 9.0
    with dissolve

    show layer screens at ts_showscreens

    play sound pageflip

    show screen poem(poem_m22fuck)

    pause

    play sound pageflip
    show layer screens at ts_hidescreens
    pause 1.0
    hide screen poem


    scene ts_notebook_glitch
    with dissolve

    show layer screens at ts_showscreens
    
    "Ладно, что там дальше?"
    em "А дальше всё, я и так тебе уже помогла, дальше сама..."
    show layer screens at vpunch
    "«ЧТО?»"
    "Однако Аки меня абсолютно не слышит. Или, по крайней мере, притворяется, что не слышит..."
    "Ну и ладно, ну и пусть! Ну и пожалуйста, ну и не нужно!"
    "Всё равно остаток стиха я более-менее помню."
    "В следующей строке там было что-то про тригонометрию."
    "Синус? Косинус? Тангенс? Котангенс?"
    "Я решаю, что котангенс здесь как будто лишний, поэтому останавливаюсь на первых трёх словах."
    "Все три слова я пишу большими буквами."
    "Во-первых, потому что я всё ещё зла на Аки, а во-вторых, у меня и без того несколько строк большими буквами написано: одной больше, одной меньше – какая разница?"

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    scene ts_notebook_glitch:
        blur 9.0
    with dissolve

    show layer screens at ts_showscreens

    play sound pageflip

    show screen poem(poem_m22g)

    pause

    play sound pageflip
    show layer screens at ts_hidescreens
    pause 1.0
    hide screen poem


    scene ts_notebook_glitch
    with dissolve

    show layer screens at ts_showscreens
    
    "Остальную часть стиха я пишу на одном дыхании."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    scene ts_notebook_glitch:
        blur 9.0
    with dissolve

    show layer screens at ts_showscreens

    play sound pageflip

    show screen poem(poem_m22h)

    pause

    play sound pageflip
    show layer screens at ts_hidescreens
    pause 1.0
    hide screen poem


    scene ts_notebook_glitch
    with dissolve

    show layer screens at ts_showscreens

    
    if persistent.cens_mode == True:
        "Так и не вспомнив одну строку из стихотворения, я устало подумала «да пошло оно всё к хуям» и написала первое попавшееся предложение, которое мне только пришло в голову."
    else:
        "Так и не вспомнив одну строку из стихотворения, я устало подумала «да пошло оно всё к чертям» и написала первое попавшееся предложение, которое мне только пришло в голову."
    "Всё равно эта строка была слишком бессмысленной, поэтому вспомнить целую строку у меня просто нет сил."
    "Кстати, об этом... я же так и не вспомнила, какое же слово было в первой строке!"
    "Впрочем, неважно. Даже если я всё равно вспомню слово, или просто возьму первое попавшееся слово, нет никаких гарантий, что это слово тоже не отсохнет."
    "Я смотрю на {i}окончательный{/i} вариант."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    scene ts_notebook_glitch:
        blur 9.0
    with dissolve

    show layer screens at ts_showscreens

    play sound pageflip

    show screen poem(poem_m22i)

    pause

    play sound pageflip
    show layer screens at ts_hidescreens
    pause 1.0
    hide screen poem


    scene ts_notebook_glitch
    with dissolve

    show layer screens at ts_showscreens

    
    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    scene ts_notebook_glitch at ts_bg_into
    pause 0.5
    scene ts_class at ts_bg_exodus
    pause 0.5

    show layer screens at ts_showscreens
    "Ещё примерно половина букв из моего предыдущего порыва вдохновения отсохли."
    "И пусть. Даже если бы я просто дала пустой лист со словами «вот мой стих», девочки бы отреагировали точно так же, как и в прошлый раз."
    "Теперь хотя бы со спокойной душой можно готовиться к собранию клуба."
    stop music fadeout 3
    play ambience clock_stena fadein 1
    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"
    show blink
    pause 2
    hide blink
    show unblink
    show layer screens at ts_showscreens
    "Остальные уроки прошли... ещё более обыденно."
    "На первом уроке у меня хотя бы было развлечение «написать стих прямо в школе, потому что я забыла написать его заранее»."
    "А на всех остальных уроках я просто скучала."
    "Но когда учитель замечал, что я как-то излишне скучаю, он задавал мне каверзные вопросы по теме урока, на которые я спокойно отвечала."
    "Сказать, что он удивился – это не сказать ничего."
    if persistent.cens_mode == True:
        "Он просто охуел от неожиданности."
    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"
    stop ambience fadeout 1
    scene ts_class at ts_coridor_glitch
    show black zorder 5 at ts_black_glitch
    show blackout_exh zorder 5
    show anim_exhausted zorder 5
    show m_rectstatic zorder 5
    with dspr
    play music ts_while fadein 1
    nvl clear
    show layer screens at ts_showscreens_nvl
    nvlbazar "Это очень напомнило мне мой первый класс в старой школе."
    nvlbazar "Тогда я тоже постоянно смотрела в окно и думала о своём, учитель замечал, что я не работаю с классом, и задавал то, что должен знать первоклассник."
    nvlbazar "А я каждый раз спокойно отвечала. Даже больше того, что обычно должен знать ребёнок в первом классе."
    nvlbazar "И в шесть лет я в упор не замечала очевидного: ну, учитель спрашивал, я отвечала, что тут такого?"
    nvlbazar "Зато папе приходилось ой как несладко..."
    nvl clear
    nvlbazar "На каждом родительском собрании в отдельный пункт выносилось то, что я, видите ли, девочка-аутистка."
    nvlbazar "Я не работала с классом, я постоянно скучала, смотрела в окно, и дальше по списку."
    nvlbazar "Но сейчас-то я знаю, что аутист в классе явно не я. Более того, их гораздо больше одного."
    nvlbazar "Как-то раз, ещё тогда, на одной перемене я написала максимально крупно:\n{size=+30}4 x 4 = 16{/size}."
    nvlbazar "На что мне ответили, что я, видите ли, плюс неправильно поставила, и вообще я идиотка, потому что будет не 16, а 8."
    nvlbazar "Тогда я даже не понимала, как со мной поступили..."
    nvl clear
    nvlbazar "А с течением лет я уже даже зла на них не держу. Хотя я их так и не простила."
    nvlbazar "Просто снисходительно говорю: «Ладно уж, было и было...»"
    nvlbazar "Ну и я постоянно рассказываю эту историю всем своим немногочисленным друзьям и просто хорошим знакомым."
    stop music fadeout 3
    show layer screens at ts_hidescreens_nvl
    nvlbazar " {w=1.0}{nw}"
    nvl clear
    show blink
    pause 1
    play ambience clock_stena fadein 1
    scene ts_class
    show unblink
    show layer screens at ts_showscreens
    "Говорят, история циклична..."
    "Но я ещё даже в ту пятницу, когда мы пили вино, никогда бы и подумать не могла, что сейчас, спустя столько времени, ситуация повторится чуть ли не один в один."
    "Осталось только, чтобы в какой-то момент папу вызвали школу, чтобы снова сказать, что я девочка-аутистка, потому что не работаю с классом, отвлекаюсь и смотрю в окно."
    "..."
    "Если, конечно, мне удастся выбраться из этой заеденной плёнки под названием «неделя перед фестивалем»."
    "Сколько мне здесь ещё сидеть?.."
    "Неделю? Пять недель? Год? Два? Десять?"
    "А может, я застряла здесь навсегда..."
    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"
    scene ts_club_medlenno_glutch
    pause 6
    scene black with dissolve2
    play sound fb
    scene ts_club
    with flash
    show layer screens at ts_showscreens
    "Как обычно, я прихожу в клуб первой."
    "Хотя, это и не удивительно. Последний урок каждого дня у меня находится в кабинете совсем рядом с кабинетом Литературного клуба."
    "..."
    "Я слегка нервничаю."
    "Да, утром я думала, что девочки не будут замечать никакой разницы между тем, какое стихотворение я написала в прошлую среду, и какое я написала сегодня."
    "Но я всё равно нервничаю."
    "А вдруг всё-таки заметят?.."
    "Ладно, надо отвлечься."
    "Можно было бы написать что-то... Я же президент {b}Литературного{/b} клуба, в конце-то концов."
    "Но новую ручку я так и не купила."
    "Ладно, дома возьму новую."
    "А может, просто почитать?"
    "Да, чтение должно быть в самый раз."
    "Однако как только я достала книгу..."
    play sound stuk1
    "...как тут же в комнату входит..."
    show yuri dragon at ln11
    play music ts_tos fadein 2
    "Юри."
    "Я не подаю виду."
    m "П-привет, Юри..."
    show yuri 1zi at f11
    y "Здравствуй, Моника..."
    y 2t "Что с тобой? Ты вся какая-то бледная..."
    show yuri 2zg at t11
    m "А... Да это ничего, просто всё переживаю о фестивале..."
    show yuri 2v at f11
    y "Совсем себя не бережёшь..."
    show yuri 2w at t11
    "Видимо, упоминание фестиваля – это какое-то стоп-слово, потому что каждый раз, как на вопрос, всё ли со мной нормально, я отвечаю, что это просто всё из-за фестиваля, все волшебным образом от меня отстают."
    "Этот раз, естественно, исключением не стал."
    "Я думала, что Юри продолжит допытывать меня, потому что технически, переживания о фестивале и страх перед тем, что я увидела пару минут назад – это немного разные вещи."
    "Но волшебное слово «фестиваль» в очередной раз делает чудеса."
    show yuri 4b at f11
    y "Так... и что мы будем сегодня делать?"
    show yuri 4b at t11
    m "Ну, сначала дождёмся остальных...{w=1}{nw}"
    show yuri 2d at h11
    y "Отлично! Я пока пойду почитаю..."
    show yuri 2d at lon11
    m "А потом пой...{w=0.5}"
    hide yuri
    extend " А, неважно уже..."
    "Юри уже как и не было."
    "Ну, если читает и она, то наконец-то смогу почитать и я."
    show monika 2k at f11
    em "И сколько процентов от прочитанного ты хотя бы запомнишь? Один? Да?"
    show monika 2j at t11
    m "Отстань."
    "Поскольку Юри уже целиком и полностью погрузилась в чтение, остального мира для неё как будто не существует."
    "Поэтому я могу поговорить с Аки нормально, а не мысленно."
    show monika 2l at f11
    em "А ты не думаешь, что то, что ты разговариваешь со своим подсознанием – это уже как минимум не нормально?"
    em 1n "Хотя, ты в принципе не особо...{w=0.44} нормальная..."
    show monika 1m at t11
    m "Я сказала {size=+10}ОТС{/size}{nw}"
    extend "{size=+10}ТАНЬ!{/size}" with vpunch
    show monika 2l at f11
    em "У-тю-тю, какие мы грозные, по столу ударяем."
    em 2b "По голове себе ещё ударь, может, прояснится что-то."
    show monika 2a at t11
    "Ладно, почитать в клубе мне сегодня уже не удастся..."
    show monika 1y at f11
    em "Да перестань, не такая я уж и надоедливая."
    show monika 1e at t11
    m "Такая. Прямо бесишь меня."
    show monika 3b at f11
    em "Ну, если я, как ты говоришь, «бешу тебя», то{w=0.8}{nw}"
    play sound door_snesli_nahui
    show layer master at ts_razebal
    show monika 3t at h11
    pause 0.3
    show layer screens at ts_showscreens_fast
    "Договорить Аки не успела, потому что в комнату вошли... нет, ввалились Сайори и Нацуки."
    "Причём ввалились они настолько громко, что даже Аки испугалась, а я так тем более."
    "Юри же просто точно так же методично читает."
    "Кажется, что выражение «остального мира для неё как будто не существует» – это ни разу не преувеличение..."
    show monika 1p at f11
    stop music fadeout 2
    em "Л-ладно, потом поговорим..."
    hide monika
    with linearblur
    show sayori glitch at ln21
    show natsuki glitch1 at ln22
    $ gtextsuka = glitchtext(24)
    $ gtextsuka1 = glitchtext(44)
    $ m_name = "[gtextsuka]"
    m "Здарова [gtextsuka1] мы хотим шоб ты умерла самой мучительной смертью{nw}"
    show sayori 2x at f21
    show natsuki 1l at f22
    play music t5_all fadein 2
    $ m_name = "Сай и Нац"
    m "Привет, Моника!"
    show sayori 2a at t21
    show natsuki 1j at t22
    $ m_name = "Моника"
    m "Привет, девочки." 
    "Я спокойно отвечаю им."
    "Сейчас мне даже не страшно ни снаружи, ни изнутри."
    "Наверное, за несколько дней я уже привыкла к подобному, что сейчас это даже не особо пугает меня."
    "Хотя иногда пугает всё равно. Вроде первого появления Юри в клубе за сегодня."
    $ persistent.ingame_pizda = False
    "Я больше боюсь того, чтобы чернила на моей ручке не отсохли окончательно, чем {i}вот этого{/i}."

    show layer screens at ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake)

    $ persistent.ingame_pizda = True
    python:
        _preferences.volumes['music'] = 0.0
        _preferences.volumes['sfx'] = 1.0
    play sound_loop ts_glitch_music12
    play sound2 ts_smeh_pizdec

    scene ts_club_glitch_pizdets
    show ts_yrec_kill_nahui_suicide_blya at left
    show ts_sayori_zalagala_chereshnya:
        align (0.9, 0.15)
    show ts_maloletka_pozvonok_sloman_nahui


    $ y_name = "[gtextsuka]"
    if persistent.cens_mode == True:
        y "Ну здарова, ебантяйки малолетние. Чё, Нацуки, как по житухе вообще, батя тебя сёння не сильно пиздил?"
    else:
        y "Ну здарова, малолетки. Чё, Нацуки, как по житухе вообще, батя тебя сёння не сильно бил?"
    y "Сколько он кстати тебе дал сегодня, копейки три? Остальное, как обычно, будешь собирать под торговым автоматом?"

    $ n_name = "[gtextsuka1]"
    n "И те не хворать, Юрец."
    hide ts_maloletka_pozvonok_sloman_nahui
    show natsuki ghost at i32
    show natsuki mouth at i32
    show n_moving_mouth

    n "Да знаешь, вроде всё нормуль у нас с батей. А ты вот сколько порезалась за эту неделю?"
    n "На руке-то хоть одно здоровое место осталось, или прям всю руку искромсала?"

    stop sound_loop
    stop sound2

    scene ts_club

    show layer screens

    $ persistent.ingame_pizda = False
    python:
        _preferences.volumes['music'] = .45
        _preferences.volumes['sfx'] = .65

    show yuri 1j at f31
    show sayori 2a at t32
    show natsuki 1j at t33
    $ y_name = "Юри"
    y "Привет, девочки."
    show yuri 1i at t31
    show sayori 2a at t32
    show natsuki 1l at f33
    $ n_name = "Нацуки"
    n "Привет, Юри."
    show yuri 1i at t31
    show sayori 2a at t32
    show natsuki 1j at t33
    "А хотя... з-знаете... забудьте, о чём я только что говорила."
    "С другой стороны, это было не столько страшно, сколько... тревожно."
    "Откуда вообще Нацуки и Юри знают о проблемах друг друга?"
    "И знают ли они о депрессии Сайори?"
    "Или это всё только в моей голове, и девочки просто говорят то, что хотела бы сказать я?"
    em "Скорее всего, последнее. Это же сон, помнишь?"
    if unluck_ball >= 5:
        em "Или кома... До конца не понятно."
    "«Без тебя знаю...»"

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_club
    show yuri 1a at t31
    show sayori 1a at t32
    show natsuki 1a at t33
    with wipeleft_scene

    show layer screens at ts_showscreens

    "Ладно, переходим к делам насущным."
    "Пока мы тут прохлаждаемся, возможно, ещё половина оставшихся букв отсыхает."
    "Сама-то я стих помню, и могу по памяти воспроизвести пропущенные буквы, если не все, то хотя бы большинство."
    "А остальные, по идее, видят этот стих впервые, поэтому им трудно будет понять, о чём оно."
    "Им и в прошлый раз было трудно понять, а сейчас так и подавно."
    "В общем, я перехожу сразу к делу."
    show yuri 1e at t31
    show sayori 1b at t32
    show natsuki 1za at t33
    m "Итак, ребята!"
    "Я бы хотела как-то правильно начать, но у меня все слова из головы вылетели."
    "Поэтому всё, что у меня получается выдавить – это:"
    m "П-пришло время поделиться стихами!"
    m "Все же написали стихи на сегодняшнюю встречу?"
    em "Все написали. Кроме тебя, бездарности с памятью золотой рыбки."
    "«Не мешай.»"
    show yuri 2j at t31
    show sayori 3x at t32
    show natsuki 2d at t33
    stop ambience fadeout 3
    play sound nfy
    $ renpy.notify("Настоятельно рекомендуем здесь сохраниться.")
    "Девочки дружно загалдели."
    show yuri 1i at t31
    show sayori 2a at t32
    show natsuki 1a at t33
    m "Н-ну, тогда... начинаем..."

    $ c11poemsreadfirst = False
    $ c11yurecchecknul = False
    $ c11sayourichecknul = False
    $ c11natsukichecknul = False

    $ poemsread = 0

    jump poemresponsesuka_loop

label poemresponsesuka_loop:

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_club
    with wipeleft_scene

    show layer screens at ts_showscreens



    if not c11poemsreadfirst:
        $ menutextsuka = "Кому я покажу стихотворение первой?"
    else:
        $ menutextsuka = "Кому я покажу стихотворение следующей?"


    menu:
        "[menutextsuka]"
            
        "Сайори" if not c11sayourichecknul:
            if not c11poemsreadfirst:
                "Начну-ка я лучше с Сайори."
                $ c11poemsreadfirst = True
            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"

            play sound pageflip
            scene ts_club
            show sayori 1d at t11
            with wipeleft_scene

            show layer screens at ts_showscreens
            m "Привет, Сайори."
            show sayori 1zc at f11
            s "Привет, Моника."
            s 2x "Ну что, готова показать стихотворение?"
            show sayori 2a at t11
            if poemsread > 0:
                show layer master at ts_blur_transform_suka(0, 2, 9)
                "Хотя это предложение кажется совершенно обыденным и безобидным, я чувствую, как она, да и остальные тоже, просто надо мной насмехаются."
                "Ну, то есть... Это же я ко всем подхожу первая с этим вопросом, как будто мне больше всех надо."
                "Хотя... мне ведь на самом деле больше всех надо... От успеха этой авантюры так-то будущее клуба зависит!"
                em "А зависит ли? Ты же уже вроде и сама поняла, что до фестиваля в этом сне ты не доживёшь. И во всех остальных тоже."
                em "Цикл заканчивается в пятницу, за три дня до фестиваля. А затем мы откатываемся обратно на субботу прошлой недели."
            else:
                pause 4
                show layer master at ts_blur_transform_suka(0, 2, 9)
                play sound wakeup
            show layer master
            play sound ssikanul
            show sayori 3j at f11
            s "Моника, ты вообще меня слышишь?!"
            show sayori 1i at t11
            m "А, что? Коне-е-ечно, готова, как никогда ранее!"
            m "А {i}ты{/i} готова?"
            show sayori 3j at f11
            s "За кого ты меня вообще принимаешь?"
            s 2j "Написала, конечно!"
            show sayori 2i at t11
            m "Ладно, ладно, не тушуйся ты так..."
            show sayori 2c at f11
            s "Ну так, я могу прочитать твоё стихотворение?"
            show sayori 2b at t11
            m "Д-да, конечно, только сразу предупрежу, что{w=0.5}{nw}"
            show sayori 3j at f11
            show layer screens at vpunch
            $ persistent.ingame_pizda = False
            s "Дай-ка сюда."
            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"
            show sayori 3b at f11
            stop music fadeout 5
            pause 5
            play music ts_gone fadein 5
            $ persistent.ingame_pizda = True

            show sayori 3o at f11 with dissolve_cg
            scene ts_club_glitch_pizdets
            show sayori 3o at f11
            show ts_glaza
            with Dissolve(4)

            show ts_sayori_zalagala_chereshnya:
                align(0.5, 0.05)
            show layer screens at ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake)


            s "Так я же его помню."
            "ОНА {b}ПОМНИТ{/b}?" with vpunch
            "Она же видит этот стих впервые!"
            "А на этой неделе у меня в этом стихе ещё и половина букв отсохла."
            "Она его даже понимать не должна, не то, что помнить!"
            "Но внешне я остаюсь спокойной."
            m "А-ха-ха... Р-разве?"

            stop music

            scene ts_club
            show layer screens
            $ persistent.ingame_pizda = False

            show sayori 4r at f11
            s "Да! Ты же хотела сделать что-то вроде продолжения стихотворения, как оно там называлось..."
            show sayori 4r at t11
            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"
            pause 0.4
            play music ts_first_day_of_sun fadein 2
            show layer screens at ts_showscreens_fast
            show sayori 2o at t11
            "Вот теперь я узнаю самую обычную Сайори – у неё феноменальная память на бесполезные факты, но как только дело доходит до каких-то реальных знаний, она мешкается."
            "Вот и сейчас, ей требуется несколько секунд на то, чтобы вспомнить название моего предыдущего стиха."
            show sayori 4s at f11
            s "А, так вот же, «Дыра в стене»!"
            show sayori 4q at t11
            "Похвально, что она вспомнила даже точное название, а не просто «что-то там про дырки и стены»..."
            show sayori 4b at f11
            s "А теперь, хочешь прочесть моё?"
            show sayori 3a at t11
            m "К-конечно..."
            show sayori 4r at t11
            s "Отлично! Держи!"


            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"

            scene ts_club:
                blur 9.0
            show sayori 4r at i11:
                blur 9.0
            with dissolve

            show layer screens at ts_showscreens


            play sound pageflip

            show screen poem(poem_act3_s)

            pause

            play sound pageflip
            show layer screens at ts_hidescreens
            pause 1.0
            hide screen poem

            scene ts_club
            show sayori 4q at i11
            with dissolve

            show layer screens at ts_showscreens

            $ c11sayourichecknul = True
            $ poemsread += 1
            "Ха. Это что-то новенькое..."
            "А точнее, совсем новое. Я вообще этого стиха не помню!"
            if poemsread == 1:
                "Может, это одно из последствий пресловутого эффекта бабочки?"
                "Хотя нет, по идее, девочки написали стих ещё вечером прошлого дня..."
                "Так что они бы всё равно написали именно эти стихи, вне зависимости от того, что бы написала я."
            else:
                em "Я помню."
                "«Н-но как?!»"
                em "Скажем так, я просто знаю больше, чем тебе кажется..."
            show sayori 3l at f11
            s "Н-ну как тебе?"
            show sayori 3y at t11
            m "Очень... необычно, Сайори..."
            m "И очень... неожиданно..."
            m "Это правда ты написала?"
            show sayori 4j at f11
            s "Ну а кто же ещё?!"
            s "Я же сказала, что на сегодняшнее собрание я напишу лучшее стихотворение в мире!"
            show sayori 4i at t11
            "По-моему, в прошлый раз она это сказала, когда написала «Бутылочки»..."
            em "Не говорила она такого."
            show sayori 2zd at f11
            s "{size=-6}А ещё... мне в этом стихе очень близка его главная героиня. Как будто она – это и есть я...{/size}"
            show sayori 2t at t11
            m "Я знаю, Сайори..."
            pause 0.6
            show sayori 2f at t11
            "После этих слов Сайори как-то отстраняется от меня."
            show sayori 2h at f11
            s "Серые тучки всё не уходят. Я думала, если я вымещу это на бумаге, то они уйдут хотя бы временно, но..."
            s 4w "Тучки стали только гуще!"
            show sayori 3ze at t11
            m "Тише, тише, не вини себя..."
            "Я обнимаю её."
            "Юри и Нацуки как-то странно на нас смотрят, но мне всё равно."
            "Кошмарный это сон или нет, но мне всё равно жаль эту девочку."
            show sayori 2zd at f11 with dissolve_cg
            s "Ладно, Моника, хватит, а то Нацуки с Юри могут не то подумать."
            show sayori 2t at t11
            m "Ну, если ты этого хочешь, то так тому и быть."
            m "Но знай, что я всегда рядом и поддержу тебя."
            show sayori 2d at t11
            "Сайори смахивает слёзы с ресниц и отвечает."
            show sayori 2zc at f11
            s "Да ладно, сама не котёнок беспомощный. Я справлюсь. Как-нибудь."
            show sayori 2d at t11
            pause 0.7
            show sayori 2i at t11
            "Я бы хотела ещё что-то возразить, но спорить с таким взглядом Сайори я всё же не решилась."
            show sayori 2i at cright with move
            hide sayori
            stop music fadeout 5
            "Ну да и ладно, у меня же не одна только Сайори в клубе."
            "Кстати, о птичках – а как там у Юри и Нацуки дела обстоят?"

            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"

            play sound pageflip
            scene ts_club
            show yuri 1i at t21
            show natsuki 2r at t22
            with wipeleft_scene

            show layer screens at ts_showscreens


            "Юри и Нацуки только что прочли стихи друг друга."
            "На лице Юри самодовольная ухмылка. Нацуки же просто свирепо смотрит на неё."
            show natsuki 2q at f22
            n "{size=-8}Это ещё что за несуразица такая?{/size}"
            show yuri 2f at f21
            show natsuki 2r at t22
            y "А? Ты что-то сказала?"
            show yuri 2e at t21
            show natsuki 1h at f22
            n "Да ничего, ничего..."
            n 2e "Ну, что я могу сказать, стих вышел чересчур изящным и замудрённым, как это обычно у тебя бывает."
            show yuri 1j at f21
            show natsuki 2g at t22
            y "Ну, спасибо большое."
            y "{size=-8}Правда, не могу сказать того же о твоём стихе...{/size}"
            show yuri 1i at t21
            show natsuki 1c at f22
            n "Что, прости?"
            show yuri 1g at t21
            show natsuki 1s at t22
            "Ой-ой, у меня {b}очень{/b} плохое предчувствие..."
            show yuri 1l at t21
            $ persistent.ingame_pizda = False
            "Юри пренебрежительно бросает стих обратно на парту и продолжает."

            $ persistent.ingame_pizda = True
            show layer screens at ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake)


            play music ts_glitch_music11 fadein 2
            show yuri 3r at f21
            show ts_psihuet1 zorder 3:
                alpha 0.5
            show layer master at heartbeat2(1)
            y "Что слышала, швабра мелкая!" with vpunch
            y 2k "Для особо глухих повторяю ещё раз: твой стих – это примитивная херня."
            y 2y4 "Была бы моя воля, я бы скормила этот стих собакам, и их отходы всё равно бы представляли бóльшую ценность, чем это убожество."
            show yuri 2m at t21
            show natsuki 2p at f22
            n "Да что {i}ты{/i} вообще понимаешь в искусстве стихосложения, мисс «Какое бы абсолютно неуместное средневековое словечко мне запихнуть в этот стих»?!"
            show yuri 1d at f21
            show natsuki 2o at t22
            y "О, ты учишься не по дням, а по часам, даже выучила новые словечки вроде «стихосложение» или «средневековое»."
            y 1j "Я-то думала, что тебе будет слишком сложно выучить слово, в котором больше трёх слогов."
            show yuri 1i at t21
            show natsuki 2p at f22
            n "Да как ты вообще смеешь?!"
            n "Сама-то не лучше, написала абсолютно бессвязный высокопарный бред и выдала это за стихотворение!"
            hide ts_psihuet1
            show ts_psihuet2 zorder 3
            show layer master at heartbeat2(2)
            n 1e "Юри, скажи честно, сколько новых шрамов на тебе появилось, пока ты писала эту хрень?"
            show yuri 2y6 at f21
            show natsuki 2f at t22
            y "На личности переходим, значит?"
            y "Ну ладно, не я эту войну первой начала..."
            show yuri 2y4 at t21
            show natsuki 2zb at t22
            y "А скажи-ка мне, Нацуки, сколько раз тебя отец отлупил, пока {i}ты{/i} писала эту несуразицу?"
            show yuri 2y4 at t21
            show natsuki 2zb at t22
            "Я чувствую, что я должна что-то сказать, как-то вмешаться..."
            "Но что-то меня сдерживает..."
            if poemsread < 3:
                show sayori 4z at f31
                show yuri 2y4 at t32
                show natsuki 2zb at t33
                s "Девочки, хватит, я не люблю ссор!"
                show sayori 2f at t31
                show yuri 2y7 at f32
                show natsuki 2p at f33
                if persistent.cens_mode == True:
                    y "А тебя это вообще ебать не должно!"
                else:
                    y "А тебя это вообще не касается!"
                y 3y3 "Мне абсолютно всё равно, что у тебя депрессия или что-то ещё."
                y "Ну, раз у тебя депрессия, то убейся об стенку, или повесься, мне всё равно."
                show sayori 4w at t31
                show yuri 2y3 at t32
                show natsuki 2o at t33
                pause 0.5
                show sayori at lhide
                hide sayori
                show yuri 2y4 at t21
                show natsuki 2zb at t22
                y "А с тобой я ещё не закончила."
                scene black
                show y_glitch_head:
                    align(0.5, 0.5)
                show layer master at ts_walking
                y "Сколько копеек в месяц тебе даёт папа?"
                show layer master at ts_walking1
                y "Сколько раз в неделю он тебя кормит?"
                show layer master at ts_walking2
                y "Когда он в последний раз тебя вообще кормил?"
                show layer master at ts_walking3
                y "Или ты, как обычно, пойдёшь клянчить мелочь или собирать монетки под торговыми автоматами в школе?"
                show layer master at ts_walking4
                "Юри рыскает по карманам и находит несколько монеток."
                show layer master at ts_walking5
                y "Вот. На воду без газа должно хватить."
                show layer master at ts_walking6
                y "Сколько, кстати, синяков под твоим телом, которые мы не должны видеть?"
                show layer master at ts_walking7
                y "С десяток? Или больше?"
                stop music fadeout 2
                scene ts_club
                show yuri 2y4 at t21
                show natsuki 12b at h22
                pause 0.8
                show natsuki 12d at h22
                pause 0.8
                show natsuki 12f at h22
                pause 1
                show natsuki at lhide
                play sound door_break
                hide natsuki
                jump poemend_abrupt
            elif poemsread == 3:
                $ persistent.ingame_pizda = False
                show layer screens
                show layer master
                stop music
                stop sound
                scene ts_club

                show sayori 4p at f31
                show yuri 2y2 at h32
                show natsuki scream at h33
                s "Так, всё, довольно!"
                show sayori 3i at t31
                show yuri 2y2 at t32
                show natsuki scream at t33
                "И тут внезапно прибегает Сайори."
                play music ts_tos fadein 2
                show sayori 3j at f31
                show yuri 2o at t32
                show natsuki 2u at t33
                s "Девочки, я читала оба ваших стихотворения, и мне они одинаково понравились!"
                s "Вы же это хотели услышать?"
                s 2h "Нет такого стиха, который мне бы понравился больше или меньше."
                show sayori 2h at f31
                show yuri 1q at t32
                show natsuki 1t at t33
                s "Стих Юри про королеву на морском дне и стих Нацуки про мальчика, который ненавидит весь мир, конечно, очень разные..."
                s 2zc "Но этим они мне и понравились."
                s "Все мы очень разные, и пишем в очень разных стилях, но это же очень хорошо!"
                s 2l "Гораздо лучше, чем если бы все мы писали о примерно одном и том же в примерно одном и том же стиле..."
                s 2e "Так бы было очень скучно..."
                show sayori 4j at f31
                show yuri 2o at t32
                show natsuki 2u at t33
                s "Но, в любом случае, стиль стилем, а переходить на личности – это очень плохо!"
                s 3h "Я не знаю, правда ли это, что Юри режется, а над Нацуки издевается её папа..."
                s 4j "Но всё равно не нужно выносить сор из избы!"
                s "Так что вы сейчас же друг перед другом извинитесь, и мы не будем больше никогда поднимать эту тему!"
                show sayori 4i at t31
                show yuri 2w at t32
                show natsuki 2zc at t33
                "После пламенной речи Сайори в клубе повисла гробовая тишина."
                "Никто не был в силах произнести ни звука."
                "Юри и Нацуки – это понятно, они наговорили друг другу очень много лишнего, и им не хотелось извиняться первыми..."
                "Но я же была буквально ошарашена тем, как Сайори распутала эту ситуацию."
                em "Может, тогда лучше Сайори сделаем президентом клуба, а ты, как и в прошлый раз, сложишь свои полномочия и уйдёшь в закат?"
                "«Ну, не так кардинально...»"
                "«Но всё же я {b}очень{/b} рада, что такой человек, как Сайори, есть именно у меня в клубе.»"
                em "Да, очень хорошо, что в клубе есть хоть один взрослый и ответственный человек, и что это не просто истерички под руководством бездарности, которая сливается при первой же проблеме!"
                "«...»"
                "Внезапно первой голос подала Нацуки."
                show sayori 4i at t31
                show yuri 2w at t32
                show natsuki 2q at f33
                n "Л-ладно, Юри, прости меня... Не стоило мне вообще поднимать эту тему и переходить на личности..."
                show sayori 4i at t31
                show yuri 2v at f32
                show natsuki 2s at t33
                y "Т-ты меня тоже прости, Нацуки... Я просто не удержалась, и тоже поступила очень низко."
                show sayori 4i at t31
                show yuri 2w at t32
                show natsuki 2t at f33
                n "Тогда, мир?"
                show yuri 2u at t32
                show natsuki 2t at t33
                "Юри просто улыбнулась."
                show sayori 4j at f31
                s "Вот так-то лучше."
                s 2v "Мне просто... очень больно видеть, как мои друзья ссорятся..."
                s 2zc "Но ведь хорошо то, что хорошо заканчивается, так ведь?"
                stop music fadeout 4
                show sayori 2t at t31
                show yuri 2zi at t32
                show natsuki 2y at t33
                "Остальные согласно закивали."
                "Я же просто стояла в полнейшем ступоре."
                em "Очнись, тебе же ещё последнее слово в твоём карманном клубе давать..."
                "Ой, точно..."
                jump poemend_normal

        "Нацуки" if not c11natsukichecknul:
            if not c11poemsreadfirst:
                "Начну-ка я лучше с Нацуки."
                $ c11poemsreadfirst = True

            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"

            play sound pageflip
            scene ts_club
            show natsuki 1a at t11
            with wipeleft_scene

            show layer screens at ts_showscreens

            m "П-привет ещё раз, Нацуки..."
            show natsuki 1c at f11
            n "Да вроде виделись уже."
            n 1d "Так что, стих-то покажешь?"
            show natsuki 1a at t11
            if poemsread > 0:
                "Да они что, сговорились все?"
            m "Нет, ты первая."
            show natsuki 1f at f11
            n "{size=-6}Что это ещё за детский сад?..{/size}"
            n 2e "Вот! Теперь ты показывай."
            "Стихотворение Нацуки написано во всё той же простенькой тетрадке."
            "Я хотела повторить с ней диалог с прошлой недели, но, кажется, Нацуки сейчас слишком раздражена, чтобы ходить вокруг да около."
            em "Да что ты говоришь? Прямо-таки мисс Догадливость!"
            em "Сама же её разозлила, и теперь искренне не понимаешь, почему же так, а не иначе!"
            stop music fadeout 4
            m "Ладно-ладно... вот...{w=1}{nw}"
            show natsuki 1e at f11
            n "Дай сюда."
            show natsuki 1f at t11
            "Нет, серьёзно, что с ней не так?"
            em "А ты сама-то не догадалась ещё?"
            $ persistent.ingame_pizda = False
            em "Или у тебя, как и всегда, память золотой рыбки, и ты уже забыла то, о чём думала, буквально три секунды назад?"
            play music ts_glitch_music12 fadein 6
            scene ts_club_glitch_pizdets with Dissolve(6)
            show layer master at heartbeat2(1)


            $ persistent.ingame_pizda = True
            show layer screens at ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake)

            show natsuki ghost1 at f11
            n "Это что-то новенькое..."
            n ghost2 "Хотя, оно не сильно-то от прошлого твоего стиха отличается, да?"
            m "В с-смысле? О ч-чём ты говоришь?"
            $ persistent.ingame_pizda = False
            stop music
            show layer screens
            show layer master
            scene ts_club
            show natsuki 1k at f11
            n "Ну, ты же на прошлое собрание очень похожий стих писала, тоже про какой-то шум, какофонию и прочее подобное."
            show natsuki 1za at t11
            m "А, ты в этом смысле... Ну-у-у, да..."
            show natsuki 2h at f11
            n "Так, подожди-ка, а ты что имела в виду?"
            show natsuki 2i at t11
            m "Н-ничего! Давай-ка я лучше твой стих прочту!"
            show natsuki 1h at f11
            play music ts_first_day_of_sun fadein 2
            n "Какая-то ты очень подозрительная с начала недели..."
            n "Ничего не хочешь нового рассказать?"
            show natsuki 1g at t11
            m "Да что ты, это ничего, просто фестиваль на носу, вот я вся и мечусь туда-сюда, хочу, чтобы всё по высшему разряду прошло..."
            show natsuki 1h at f11
            n "Хорошо, на этот раз поверю..."
            show natsuki 1i at t11
            "Впервые за эту неделю мне очень хочется сделать так, чтобы новый цикл начался поскорее."
            em "О-хо-хо, даже быстрее, чем ты можешь предположить!"
            show natsuki 1y at f11
            n "Ладно, заговорилась я с тобой. Короче, смотри и учись, как пишут настоящие мастера слога!"
            show natsuki 1y at t11
            "Ну-ну..."

            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"

            scene ts_club:
                blur 9.0
            show natsuki 1y at i11:
                blur 9.0
            with dissolve

            show layer screens at ts_showscreens


            play sound pageflip

            show screen poem(poem_act3_n)

            pause

            play sound pageflip
            show layer screens at ts_hidescreens
            pause 1.0
            hide screen poem

            scene ts_club
            show natsuki 1z at i11
            with dissolve

            show layer screens at ts_showscreens

            $ c11natsukichecknul = True
            $ poemsread += 1

            "Ха. Это тоже что-то новенькое."
            "Хотя нет... совсем новое! Я этого никогда ранее в жизни не читала!"
            em "Я читала."
            "«Да как так-то? Почему ты знаешь то, чего не помню я? Я думала, ты моё подсознание, а не всезнающий бог.»"
            em "Ну, скажем... просто читала."
            em "Может, ты этого просто не помнишь... зато отчётливо помню я."
            em "Правда, давно это уже было, но не суть..."
            "«Как скажешь...»"
            "Но что-то мы отвлеклись..."
            "То есть, да, стихотворение написано в стандартном, если можно так выразиться, стиле Нацуки, и оно в целом похоже на «Эми Любит Пауков», которое она писала в прошлую пятницу, но..."
            "Как будто есть что-то... не свойственное ей..."
            show natsuki 1za at t11
            "Я озвучиваю Нацуки свои мысли, но пока без упоминания абстрактной Эми."
            show natsuki 1k at f11
            n "Ну... Всегда есть такой человек, который вечно всем не доволен, и ему нужно, чтобы всё было только так, как он скажет."
            n 1h "А если же что-то {b}не{/b} будет так, как он скажет, он обидится и уйдёт плакать."
            n 1r "{size=-10}Некоторые из них, кстати, даже в этом самом клубе находятся...{/size}"
            show natsuki 1zb at t11
            m "Что, прости?"
            show natsuki 1zc at f11
            n "..."
            n 12c "Ничего уже... давай дальше..."
            show natsuki 12b at t11
            "Я, конечно, со слов Аки, и не самая догадливая, но даже я понимаю, что она имеет в виду Юри."
            em "Не самая догадливая – это ещё очень мягко говоря!"
            "В любом случае, я решаю не давить на неё."
            show natsuki 12a at t11
            m "...Как скажешь..."
            show natsuki 1c at f11
            n "Вот и поговорили."
            n "А теперь отдай стихотворение."
            if not c11sayourichecknul or c11yurecchecknul:
                n 1k "Мне его ещё другим показывать надо."
            show natsuki 1za at t11
            m "Да, конечно..."
            show natsuki 1s at t11
            show layer master at ts_razebal
            play sound ts_bumaga_sound
            pause 0.8
            show natsuki 1s at cright with move
            hide natsuki
            "В мгновение ока Нацуки забирает у меня тетрадь со стихом и тут же испаряется."
            "Нет, серьёзно, что с ней не так?"
            if poemsread < 3:
                "Впрочем, мне и самой другим свой стих показать надо..."

            jump poemresponsesuka_loop

        "Юри" if not c11yurecchecknul:
            if not c11poemsreadfirst:
                "Думаю, в этот раз начну с Юри."
                $ c11poemsreadfirst = True


            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"

            play sound pageflip
            scene ts_club
            show yuri 1i at t11
            with wipeleft_scene

            show layer screens at ts_showscreens


            m "Здравствуй, Юри."
            show yuri 1f at f11
            y "Привет, Моника."
            y 1b "Ты написала стих?"
            show yuri 1a at t11
            if c11natsukichecknul == True:
                "Я не знаю, сговаривались ли они заранее, чтобы сразу затопить меня, но мне это не нравится..."
            m "Да, написала..."
            m "Ты, как я вижу, тоже стих принесла..."
            "Я замечаю знакомую записную книжку в руках Юри, которая мне запомнилась ещё с прошлого вторника."
            "Только теперь надписи на ней стали ещё более неразборчивыми, чем в прошлый раз."
            "Очередная мелочь кошмара, который я называю повторением этой недели, или же?.."
            "Ладно, неважно."
            stop music fadeout 4
            show yuri 1b at f11
            y "Ты не против, если я сначала твоё стихотворение прочту?"
            show yuri 1a at t11
            m "Не против, конечно..."
            $ persistent.ingame_pizda = False
            "Мне даже интересно будет узнать, что ты вычленишь из той отрывистой писанины, которая ещё не отсохла..."
            play music ts_glitch_music10 fadein 6
            scene ts_club_glitch_pizdets
            show yuri 1a at i11
            show ts_glaza_yrec
            with Dissolve(6)

            show layer master at heartbeat2(1)
            $ persistent.ingame_pizda = True
            show layer screens at ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake)

            y "Хм..."
            y "Я уже видела... нечто очень похожее..."
            if poemsread > 0:
                "Да что же такое со всеми творится сегодня?"
                "Какие-то двусмысленные намёки..."
                "Ты помнишь стих, который я писала на прошлой неделе, или всё-таки нет?!"
            m "Р-разве?"

            $ persistent.ingame_pizda = False

            show layer master
            show layer screens

            stop music
            scene ts_club
            show yuri 1f at f11
            y "Ну да. Ты же и на прошлое собрание писала стихотворение на похожую тематику."
            y 1b "Я даже думала, что ты хотела развить тему про Дыру в стене, и поэтому написала что-то вроде продолжения."
            y 4a "..."
            play music ts_first_day_of_sun fadein 2
            show yuri 3n at h11
            y "Прости, если я поспешила с выводами..."
            show yuri 2o at f11
            y "Я просто подумала, что...{w=1.4}{nw}"
            show yuri 2o at t11
            if poemsread > 0:
                "Видимо, всё-таки не помнишь..."
                "Тогда откуда все эти намёки?"
                "Ничего не понимаю..."
            m "Да нет, Юри... всё ты правильно говоришь..."
            m "Именно это я и имела в виду..."
            show yuri 2q at f11
            y "Н-ну, раз ты так говоришь..."
            show yuri 2q at t11
            m "А теперь, если ты не против, я прочту и твоё..."
            show yuri 1f at f11
            y "Что ты, вовсе нет."
            y 1h "Только хочу предупредить, что написано оно... не совсем в моём стиле..."
            show yuri 1g at t11
            m "Ну... стих есть стих, верно?"
            show yuri 1j at f11
            y "Н-ну, тоже верно, да..."
            show yuri 1i at t11
            "Я беру стихотворение Юри и начинаю читать."

            show layer screens at ts_hidescreens
            " {w=1.0}{nw}"

            scene ts_club:
                blur 9.0
            show yuri 1i at i11:
                blur 9.0
            with dissolve

            show layer screens at ts_showscreens


            play sound pageflip

            show screen poem(poem_act3_y)

            pause

            play sound pageflip
            show layer screens at ts_hidescreens
            pause 1.0
            hide screen poem

            scene ts_club
            show yuri 1i at i11
            with dissolve

            show layer screens at ts_showscreens

            $ c11yurecchecknul = True
            $ poemsread += 1
            if c11natsukichecknul:
                "Где-то я это уже видела..."
                "Не сам стих, разумеется, а в общем, где все девочки, по сути, написали совершенно новые стихи, которые вроде как и в соответствующем стиле написаны, но всё равно им как будто не свойственны."
                "И кстати говоря..."
            else:
                "Ну, про стих, который не совсем в её стиле, Юри вроде как и не соврала..."
                "Но и всю правду тоже не сказала."
                "Метафоры есть, иносказательность есть, какие-то словечки, которые я впервые вижу, тоже есть."
                "Единственное из «не её стиля» – это излишняя рифмованность..."
                "...Господи, да я сама уже как Юри говорю!"
            "У меня всего один вопрос."
            m "Юри, а скажи-ка мне..."
            show yuri 3p at t11
            m "А кто главная героиня этого стихотворения?"
            show yuri 3p at t11
            pause 0.5
            show yuri 2n at t11
            pause 0.5
            show yuri 2o at t11
            pause 1
            show yuri 2q at f11
            y "Н-ну ты же и сама видела, это к-королева на г-глубине дна морского..."
            show yuri 2n at t11
            m "Ладно, сформулирую вопрос иначе: кто олицетворяет собой эту королеву на морской глубине?"
            show yuri 2n at t11
            pause 0.5
            show yuri 2o at t11
            pause 1
            show yuri 1o at f11
            y "{size=-10}Я олицетворяю...{/size}"
            y 4b "Просто... я вся такая незаметная, тихая, что некоторые одноклассники говорят, что пока все сидят на уроке, Юри сидит на дне морском..."
            y 4a "Конечно, они не совсем так сказали, потому что они и словосочетаний-то таких не знают, но суть остаётся той же..."
            y "И я вот подумала: "
            extend 2r "«Да, я на дне морском. Я королева морского царства! А вы все просто кучка бездарей»."
            show yuri 2w at t11
            "Юри переводит дыхание пару раз, прежде чем закончить свою мысль."
            show yuri 2q at f11
            y "И вот так, строка за строкой, и стих буквально на глазах родился..."
            show yuri 2q at t11
            "Очевидно, что воспоминания о её одноклассниках у неё... не из самых приятных."
            m "А это было до или после того, как?..{w=1}{nw}"
            show yuri 2k at f11
            y "После. Намного после."
            play sound psy_fast_1
            show yuri 1l at i11
            with memglitch
            stop sound
            y 1l "И знаешь, спустя некоторое время я таки дала отпор этим хулиганам."
            y 1j "И после этого случая меня они перестали трогать от слова совсем, а за глаза говорят, что я не совсем в своём уме."
            y "Ну да и пусть. То, что обо мне говорят за глаза, меня не касается."
            play sound psy_fast_2
            show yuri 1i at i11
            with memglitch
            stop sound
            "Да-а-а, Юри хоть и тихая девочка, но иногда она может устроить некоторым самым отъявленным хулиганам... весёлую жизнь."
            "Да и в принципе я уже опытным путём выяснила, что в Юри живут как минимум две совершенно разные личности. А то и больше."
            m "Л-ладно, Юри, спасибо, что поделилась со мной этим, но... что-то мы Сайори и Нацуки задерживаем, тебе не кажется?"
            show yuri 1f at f11
            y "Знаешь... мне тоже так кажется. Наверное, будем расходиться уже."
            y 1b "И спасибо за то, что выслушала. Это вроде и мелочь, но всё равно приятно."
            y "Думаю, именно из таких мелочей и складывается дальнейшая дружба на всю жизнь."
            show yuri 1a at t11
            m "Да, я тоже так думаю..."
            show yuri 1d at f11
            y "Тогда, до скорого!"
            show yuri 1c at t11
            m "Да, Юри, ещё увидимся..."
            show yuri 1c at cright with move
            hide yuri
            "На этом наши пути с Юри временно разошлись."
            if poemsread < 3:
                jump poemresponsesuka_loop
            
label poemend_abrupt:
    $ persistent.ingame_pizda = False
    show layer screens
    $ unluck7 = True
    $ unluck_ball += 1
    show yuri 2y6 at t11
    play music ts_dtm fadein 2

    y "..."
    m "Сегодня мы на обмен стихами вообще не настроены..."
    m "Просто... уходи..."
    play sound door_break
    show yuri 2y6 at cright with move
    hide yuri
    "Да, это просто сон. Да, в субботу всё опять заново. Но я всё равно не могу видеть, как Юри разогнала всех остальных."
    em "А что же ты тогда просто смотрела, как Юри всех разгоняет?"
    em "Что же ты не вмешалась? Чего же ты сама не закончила спор?"
    "Я... не знаю..."
    em "Зато я знаю. Ты просто эгоистичная двуличная мразь."
    em "На словах ты президент, а на деле ты же просто сидишь на обочине жизни и не отсвечиваешь, как будто тебя это вообще не касается!"
    em "Сон это или нет, факта это не отменит."
    em "Эгоистичная. Двуличная. Мразь."
    "Не желая больше терпеть упрёков Аки, я просто ухожу домой в слезах."
    em "От меня всё равно не скроешься!"
    python:
        _preferences.volumes['music'] = 1.0
        _preferences.volumes['sfx'] = 1.0
    play sound_loop ts_bzdr_distortion

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound door_break
    scene ts_corridor at ts_razebal
    pause 0.35
    play sound2 ts_running
    scene ts_corridor at ts_running_fast
    pause 0.5
    play sound pageflip
    scene ts_l5 at ts_running_fast
    with wipeleft_scene_fast
    play sound pageflip
    scene ts_school_courtyard_evening at ts_running_fast
    with wipeleft_scene_fast

    play sound pageflip
    scene ts_school_gate_evening at ts_running_fast
    with wipeleft_scene_fast
    play sound2 ts_running
    play sound pageflip
    scene ts_street_late at ts_running_fast
    with wipeleft_scene_fast

    play sound pageflip
    scene ts_house_monika_evening at ts_running_fast
    with wipeleft_scene_fast
    stop sound2
    play sound door_break
    scene ts_vhod_night at ts_razebal
    pause 0.4


    play sound2 ts_othodos_ot_bega fadein 1
    play sound pageflip
    scene ts_bedroom
    show layer master at ts_ustal_suka
    with wipeleft_scene_fast

    show layer screens at ts_showscreens

    show monika 1h at t11
    "Я бегу так быстро, как только могу, только чтобы Аки побыстрее заткнулась."
    "Через пять минут я уже прибежала домой."
    stop sound2 fadeout 1
    show layer master
    scene ts_bedroom
    show monika 2i at f11
    em "Ты действительно думаешь, что если ты прибежишь домой, то скроешься от меня?"
    em "Если да, то я тебя разочарую."
    $ persistent.ingame_pizda = False
    em 2r "*Кхе-кхе*"
    em 5c "{cps=*0.8}{b}БЕЗДАРНОСТЬ БЕЗДАРНОСТЬ БЕЗДАРНОСТЬ БЕЗДАРНОСТЬ БЕЗДАРНОСТЬ БЕЗДАРНОСТЬ БЕЗДАРНОСТЬ БЕЗДАРНОСТЬ БЕЗДАРНОСТЬ{/b}{/cps}{nw}"

    $ persistent.ingame_pizda = True
    show layer screens at ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake)

    stop sound_loop

    python:
        currentpos = get_pos()
        startpos = currentpos - 0.2
        if startpos < 0: startpos = 0
        track = "<from " + str(startpos) + " to " + str(currentpos) + ">mod_assets/source/audio/oski/ts_bzdr_distortion.ogg"
        renpy.music.play(track, loop=True)

    em "{cps=*0.8}{b}БЕЗДАРНОСТЬ БЕЗДАРНОСТЬ БЕЗДАРНОСТЬ{/b}{/cps}{nw}"
    scene ts_kitchen_glitch_pizdets
    show ts_hiroto_zalagal
    show black zorder 5 at ts_black_glitch

    em "{cps=*0.8}{b}БЕЗДАРНОСТЬ БЕЗДАРНОСТЬ БЕЗДАРНОСТЬ{/b}{/cps}{nw}"
    scene ts_sayori_bedroom_glitch_pizdets
    show ts_natsuki_zalagala_blyadina
    show black zorder 5 at ts_black_glitch
    show blackout_exh zorder 5

    em "{cps=*0.8}{b}БЕЗДАРНОСТЬ БЕЗДАРНОСТЬ БЕЗДАРНОСТЬ{/b}{/cps}{nw}"
    scene ts_l5_glitch_pizdets
    show ts_yuri_zalagala_blyadina
    show black zorder 5 at ts_black_glitch
    show blackout_exh zorder 5
    show anim_exhausted zorder 5

    em "{cps=*0.8}{b}БЕЗДАРНОСТЬ БЕЗДАРНОСТЬ БЕЗДАРНОСТЬ{/b}{/cps}{nw}"
    scene ts_closet_glitches_balya
    show black zorder 5 at ts_black_glitch
    show blackout_exh zorder 5
    show anim_exhausted zorder 5
    show m_rectstatic zorder 5
    show ts_hiroto_psyhodelic_pizdoc_eye zorder 6 at ipp11
    em "{cps=*0.8}{b}БЕЗДАРНОСТЬ БЕЗДАРНОСТЬ БЕЗДАРНОСТЬ{/b}{/cps}{nw}"
    scene ts_residental_glitch_pizdets
    show black zorder 5 at ts_black_glitch
    show blackout_exh zorder 5
    show anim_exhausted zorder 5
    show m_rectstatic zorder 5
    show ts_sayori_zalagala_blyadina at Glitch(_fps=1000.)
    show ts_psihuet2 zorder 6
    em "{cps=*0.8}{b}БЕЗДАРНОСТЬ БЕЗДАРНОСТЬ БЕЗДАРНОСТЬ{/b}{/cps}{nw}"
    scene ts_kitchen_psyhodelic_pizdec_glitch
    show black zorder 5 at ts_black_glitch
    show blackout_exh zorder 5
    show anim_exhausted zorder 5
    show m_rectstatic zorder 5
    show ts_hiroto_zalagal at Glitch(_fps=1000.)
    show ts_psihuet3 zorder 6
    em "{cps=*0.8}{b}БЕЗДАРНОСТЬ БЕЗДАРНОСТЬ БЕЗДАРНОСТЬ{/b}{/cps}{nw}"

    play music ts_dtm fadein 5
    scene ts_bedroom
    show monika 5c at t11
    play sound scream_pereponkam_pizda
    m "{font=[shl_font]}А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А{/font}{nw}"
    stop sound fadeout 2
    "Первобытный крик постепенно переходит в бесконтрольное рыдание."
    "Что, что я могла ещё сделать?"
    "Аки права. Я действительно бездарность."
    "Я не могу справиться даже с тремя другими участницами клуба! Я не могу справиться со своими прямыми обязанностями!"
    show monika 5b at f11
    em "А сама говорила, что в Дискуссионном клубе ты была медиатором споров..."
    em "Бездарность, эгоистка и лицемерка – вот ты кто, а не президент клуба!"
    show monika 5c at t11
    "А что, если после фестиваля их будет больше, как я говорила папе?"
    show monika 5b at f11
    em "Ты сначала до этого фестиваля доживи."
    show monika 5c at t11
    "...ну да, и это тоже."
    "Одно хорошо, что пока я истерила, папы не было дома."
    "Иначе у него могли бы появиться несколько неудобных вопросов, на которые я бы тоже не смогла ответить..."
    show monika 1r at f11
    em "Серьёзно? Это то, что тебя больше всего волнует?"
    show monika 1q at t11
    m "Ну, не больше всего... но и это тоже..."
    m "Ладно, давай отдыхать, а то вся эта ситуация уже сильно на мозги давит."
    m "Сон это или нет, но это всё равно уже слишком..."
    show monika 2i at f11
    em "Ага... ещё скажи, что нужно стих к следующей встрече написать."
    show monika 2h at t11
    m "А будет ли вообще следующая встреча после того, как все друг с другом перессорились?"
    m "Но в любом случае, стих написать надо. Хотя бы для своего же спокойствия и умиротворения."
    show monika 2d at f11
    em "Так у тебя же ручка не пишет, а бежала ты из школы быстрее ветра."
    show monika 2j at t11
    m "И кто в этом виноват, скажи мне на милость?"
    show monika 3l at f11
    em "А вот и скажу – ты сама."
    em 4b "Потому что это всё в твоей голове."
    show monika 4a at t11
    m "А если я скажу тебе убираться из моей головы, то ты, разумеется, не уберёшься..."
    show monika 4b at f11
    em "Именно!"
    show monika 2a at t11
    m "Х-х-х..."
    m "Ладно, чего уж там, напишу стих ручкой без чернил. Если надавливать посильнее, то хотя бы след от ручки останется..."
    window hide
    play sound psy_fast_2
    scene ts_notebook_glitch at ts_coridor_glitch
    show black zorder 5 at ts_black_glitch
    show blackout_exh
    show anim_exhausted
    show m_rectstatic zorder 0
    with memglitchstr
    stop sound
    show monika 1c at t11
    "Однако на ум не приходит ни слова, за которое можно зацепиться."
    show monika 2d at f11
    em "Может, напишешь про события сегодняшнего собрания?"
    show monika 2c at t11
    m "А какие там вообще были события? Там были сплошные эмоции... Ну и Юри, которая снова была совершенно не в себе."
    show monika 3b at f11
    em "Ну вот об этом и напиши!"
    show monika 2a at t11
    "Внезапно на меня снисходит озарение."
    "Я вымещаю всю боль, всё разочарование, всю злость, все негативные эмоции в это стихотворение."
    "Конечно, показывать его хоть кому-то крайне нежелательно... особенно Юри."
    "Однако я выговорилась, а это всё, что важно."
    "Я победно перечитываю стихотворение."
    scene black
    show layer master
    show layer screens
    window hide
    $ persistent.ingame_pizda = False
    $ renpy.block_rollback()
    python:
        currentpos = get_pos()
        startpos = currentpos - 0.2
        if startpos < 0: startpos = 0
        track = "<from " + str(startpos) + " to " + str(currentpos) + ">mod_assets/source/audio/ost/ts_dtm.ogg"
        renpy.music.play(track, loop=True)

    show exception_bg zorder 2
    show fake_exception zorder 2:
        xpos 0.1 ypos 0.05
    show fake_exception3 zorder 2:
        xpos 0.1 ypos 0.15
    show layer master at heartbeat2(1)
    $ renpy.block_rollback()
    pause
    hide fake_exception3

    scene ts_nebo_fon_bgshka_suka
    show fake_exception4 zorder 2:
        xpos 0.1 ypos 0.15
    show layer master at heartbeat2(2)
    $ renpy.block_rollback()
    pause
    hide fake_exception4
    scene ts_club_glitch_pizdets
    show fake_exception5 zorder 2:
        xpos 0.1 ypos 0.15
    show layer master at heartbeat2(3)
    $ renpy.block_rollback()
    pause
    hide fake_exception5
    scene ts_kitchen_glitch_pizdets
    show fake_exception6 zorder 2:
        xpos 0.1 ypos 0.15
    show layer master at heartbeat2(4)
    $ renpy.block_rollback()
    pause
    hide fake_exception6
    scene black
    show exception_bg zorder 2
    show fake_exception7 zorder 2:
        xpos 0.1 ypos 0.15
    show layer master at heartbeat2(5)
    $ renpy.block_rollback()
    pause
    stop music
    show layer master
    play sound winerrorsound

    if renpy.android:
        show screen dialog("ru.bergen.truestory.apk\n\nВ файлах скрипта обнаружена критическая ошибка. Необходимо перезапустить игру. Остановимся на ещё работающем скрипте.", ok_action=Return())
    else:
        show screen dialog("truestory.exe\n\nВ файлах скрипта обнаружена критическая ошибка. Необходимо перезапустить игру. Остановимся на ещё работающем скрипте.", ok_action=Return())


    $ renpy.block_rollback()
    pause
    hide screen dialog
    play sound winerrorsound
    if renpy.android:
        show screen dialog("ru.bergen.truestory.apk\n\nПерезапускаем?", ok_action=Return())
    else:
        show screen dialog("truestory.exe\n\nПерезапускаем?", ok_action=Return())
    $ renpy.block_rollback()
    pause
    hide screen dialog
    $ renpy.block_rollback()
    scene black
    pause 0.5

    if hour in [20,21,22,23,24,0,1,2,3,4,5,6]: #НОЧЬ
        play sound br_glitch
        show ts_menu_move_anim as bg1 at Glitch(_fps=160, glitch_strength=1)
        pause 0.6
        stop sound
        hide ts_menu_move_anim as bg1 at Glitch(_fps=160, glitch_strength=1)
    elif True: #ДЕНЬ
        play sound br_glitch
        show ts_menu_move_anim_three as bg1 at Glitch(_fps=160, glitch_strength=1)
        pause 0.6
        stop sound
        hide ts_menu_move_anim_three as bg1 at Glitch(_fps=160, glitch_strength=1)

    jump ts_scenario_12

    #$ renpy.full_restart(transition=None, label="splashscreen")

label poemend_normal:
    play music ts_tar fadein 3
    show yuri 2o at t31
    show sayori 4k at t32
    show natsuki 2u at t33
    m "И-и-и... Итак, ребята!"
    show yuri 2e at t31
    show sayori 3b at t32
    show natsuki 1za at t33
    "Все девочки в один момент повернулись ко мне."
    m "В общем... несмотря на все разногласия и препятствия, которые встали у нас на пути, я считаю, что собрание мы заканчиваем на хорошей ноте."
    show yuri 2q at t31
    show sayori 3l at t32
    show natsuki 2t at t33
    "Девочки смущённо закивали."
    m "Тогда, что я могу ещё сказать... Хорошего вам вечера, и {b}чтобы завтра без всяких вольностей{/b}."
    show yuri 2o at t31
    show sayori 2f at t32
    show natsuki 2u at t33
    m "Я понимаю, что сама сказала о том, что «в моём клубе каждый мог бы выражаться так, как его душе будет угодно», но не стоит опускаться до такого."
    m "А сейчас – собрание окончено. Жду вас всех завтра."
    show yuri 2q at t31
    show sayori 3l at t32
    show natsuki 2t at t33
    "Девочки как-то разрозненно попрощались и ушли каждая своей дорогой."
    "Пойду и я."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_corridor
    with wipeleft_scene

    play sound pageflip
    scene ts_l5
    with wipeleft_scene

    play sound pageflip
    scene ts_school_courtyard_day
    with wipeleft_scene

    play sound pageflip
    scene ts_school_gate_evening
    with wipeleft_scene


    play sound pageflip
    scene ts_street_late
    with wipeleft_scene

    play sound pageflip
    scene ts_house_monika_evening
    with wipeleft_scene

    show layer screens at ts_showscreens


    "Поскольку всё прошло как-то очень быстро, то папа, скорее всего, ещё на работе."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_vhod_night
    with wipeleft_scene

    show layer screens at ts_showscreens


    m "Папа? Я дома!"
    "Однако ответа не было."
    "На часы не было никакого смысла смотреть, однако через несколько секунд папа так и не подошёл."
    "Видимо, всё-таки ещё рано для него."
    "Не обращая внимания на надоедливую Аки, которой не терпится в очередной раз сказать мне, что я бездарность, я направляюсь к себе, чтобы переодеться."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_bedroom
    with wipeleft_scene

    show layer screens at ts_showscreens

    "Так..."
    "Чтобы Аки снова не капала мне на мозги, лучше написать стихотворение сразу же, не откладывая это всё на потом."
    "А то иначе всё может получиться, как в прошлый раз."
    show monika 2bd at f11
    with linearblur
    em "То, что ты не откладываешь стих на потом – это, конечно, похвально."
    em "Но вот у меня вопрос: а ты новую ручку купила?"
    show monika 2bc at t11
    m "А мне и не нужно её покупать."
    "Поскольку папы ещё нет, я перехожу на обычный голос."
    m "У меня и так всё есть."
    play sound ts_yashik_open
    "Я демонстративно открываю выдвижной ящик стола и показываю Аки ещё пять нетронутых ручек."
    show monika 1bn at f11
    em "Ладно, убедила..."
    play sound ts_yashik_close
    show monika 1bm at t11
    "Я с ухмылкой закрываю ящик."
    show monika 2bd at f11
    em "А о чём ты стихотворение писать будешь?"
    show monika 2bc at t11
    m "Этого я ещё не знаю... Но, как говорится, аппетит приходит во время еды – вот и вдохновение ко мне придёт в процессе написания."
    show monika 2bi at f11
    em "Я бы, конечно, с этим поспорила... ну да не суть..."
    show monika 2bc at t11

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"
    hide monika
    with linearblur
    scene ts_bedroom at ts_bg_into
    pause 0.5
    scene ts_notebook at ts_bg_exodus
    pause 0.5

    show layer screens at ts_showscreens

    show monika 2bc at t11
    with linearblur
    "Так... Стих, стих, стих..."
    "Надо стих бы написать..."
    "..."
    "Хотя кого я обманываю? В голове за сегодняшний день такая каша, что вычленить одну конкретную тему для стихотворения очень сложно."
    "Если это вообще возможно..."
    show monika 1br at f11
    em "Не у тебя одной сегодня полная каша в голове..."
    show monika 1bq at t11
    m "Как скажешь..."
    window hide
    play sound psy_fast_2
    scene ts_notebook_glitch at ts_coridor_glitch
    show black zorder 5 at ts_black_glitch
    show blackout_exh
    show anim_exhausted
    show m_rectstatic zorder 0
    with memglitchstr
    stop sound
    "Да что же это такое? Я уже минут двадцать пытаюсь написать хоть одно слово, но по итогу передо мной до сих пор остаётся только чистый лист бумаги!"
    show monika 2bd at f11
    with linearblur
    em "Слу-у-у-у-ушай... А может, тебе как раз про сегодняшние события в клубе написать?"
    show monika 2ba at t11
    m "Да какие это события, это скорее эмоции..."
    m "Но всё же очень хорошо, что Сайори вовремя вмешалась, иначе кто знает, чем бы это всё закончилось..."
    show monika 2br at f11
    em "Я тебе уже говорила сделать Сайори президентом клуба, чтобы ты просто отмалчивалась в сторонке и говорить что-то только тогда, когда тебя спросят?"
    show monika 2bq at t11
    m "..."
    show monika 2bn at f11
    em "Ладно, не об этом сейчас..."
    em 2ba "Но вот об этих эмоциях и о том, как Сайори спасла представление, стих и напиши!"
    show monika 2ba at t11
    "Я думаю."
    m "Знаешь... а неплохая идея."
    m "Главное только не петь дифирамбы Сайори слишком... слишком."
    show monika 2bn at f11
    em "В общем, идею я тебе дала, а как именно ты распишешь – это уже дело твоё."
    show monika 2bm at t11
    "Внезапно на меня снисходит озарение."
    "Я вымещаю в это стихотворение всю боль, всё разочарование, всю злость, все негативные эмоции... и все хвалебные оды Сайори."
    "Надеюсь, что она не слишком переволнуется из-за этого..."
    "В конце концов, каждый мой обмен стихами с Сайори заканчивался слезами на её глазах."
    "Боюсь только представить, какова будет её реакция на стихотворение, напрямую посвящённое ей."
    "Однако я выговорилась, а это всё, что важно."
    "Я победно перечитываю стихотворение."

    scene black
    show layer master
    show layer screens
    window hide
    $ persistent.ingame_pizda = False
    $ renpy.block_rollback()
    python:
        currentpos = get_pos()
        startpos = currentpos - 0.2
        if startpos < 0: startpos = 0
        track = "<from " + str(startpos) + " to " + str(currentpos) + ">mod_assets/source/audio/ost/ts_tar.ogg"
        renpy.music.play(track, loop=True)

    show exception_bg zorder 2
    show fake_exception zorder 2:
        xpos 0.1 ypos 0.05
    show fake_exception3 zorder 2:
        xpos 0.1 ypos 0.15
    $ renpy.block_rollback()
    pause
    hide fake_exception3

    scene ts_kitchen_glitch_pizdets
    show fake_exception6 zorder 2:
        xpos 0.1 ypos 0.15

    $ renpy.block_rollback()
    pause
    hide fake_exception6
    scene black
    show exception_bg zorder 2
    show fake_exception7 zorder 2:
        xpos 0.1 ypos 0.15

    $ renpy.block_rollback()
    pause
    stop music
    show layer master
    play sound winerrorsound
    if renpy.android:
        show screen dialog("ru.bergen.truestory.apk\n\nВ файлах скрипта обнаружена критическая ошибка. Необходимо перезапустить игру. Остановимся на ещё работающем скрипте.", ok_action=Return())
    else:
        show screen dialog("truestory.exe\n\nВ файлах скрипта обнаружена критическая ошибка. Необходимо перезапустить игру. Остановимся на ещё работающем скрипте.", ok_action=Return())

    $ renpy.block_rollback()
    pause
    hide screen dialog
    play sound winerrorsound
    if renpy.android:
        show screen dialog("ru.bergen.truestory.apk\n\nПерезапускаем?", ok_action=Return())
    else:
        show screen dialog("truestory.exe\n\nПерезапускаем?", ok_action=Return())
    $ renpy.block_rollback()
    pause
    hide screen dialog
    $ renpy.block_rollback()
    scene black
    pause 0.5

    if hour in [20,21,22,23,24,0,1,2,3,4,5,6]: #НОЧЬ
        play sound br_glitch
        show ts_menu_move_anim as bg1 at Glitch(_fps=160, glitch_strength=1)
        pause 0.6
        stop sound
        hide ts_menu_move_anim as bg1 at Glitch(_fps=160, glitch_strength=1)
    elif True: #ДЕНЬ
        play sound br_glitch
        show ts_menu_move_anim_three as bg1 at Glitch(_fps=160, glitch_strength=1)
        pause 0.6
        stop sound
        hide ts_menu_move_anim_three as bg1 at Glitch(_fps=160, glitch_strength=1)

    jump ts_scenario_12