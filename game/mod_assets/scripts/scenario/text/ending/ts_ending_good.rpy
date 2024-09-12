label ts_good_ending_blya:

    $ renpy.block_rollback()

    python: # ОБНОВЛЯЕМ RPC
        ts_rpc_carter13()

    $ persistent.rpclabel = "13"

    $ persistent.carter2menu = False
    $ persistent.carter3menu = False
    $ persistent.badendmenuperedglitch = False
    $ persistent.badendmenuskipglitch = False
    $ persistent.badendmenu = False
    $ persistent.goodendmenu = False
    $ persistent.peredbadendmenu = False
    $ persistent.peredgoodendmenu = True

    if _preferences.language == "english":
        $ save_name = "Just a dream..."
    else:
        $ save_name = "Всего лишь сон..."

    scene black

    pause 2

    play sound chp3
    if _preferences.language == "english":
        $ Chapter("Epilogue")
        $ Chapter("Epilogue")
        $ Chapter("Just a dream...")
        stop sound fadeout 7
        $ Chapter("Just a dream...")
    else:
        $ Chapter("Эпилог")
        $ Chapter("Эпилог")
        $ Chapter("Всего лишь сон...")
        stop sound fadeout 7
        $ Chapter("Всего лишь сон...")

    pause 2

    $ persistent.uncolorize = "none"

    play ambience vibration_rintone fadein 5
    scene ts_bedroom
    with Dissolve(4)
    show layer screens at ts_showscreens

    $ persistent.sprite_time = "day"
    "На этот раз я просыпаюсь... не в спальне Сайори, а у себя."
    "Это что получается, я... выбралась?"
    "Я выбралась... Я выбралась! У меня получилось!"
    "Получилось получилось получилось!"
    "Это всё был только сон!"
    "Только вот чёртов телефон не перестаёт звонить..."
    stop ambience
    play sound ts_pda
    "Я отвечаю на звонок."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    scene black with ts_paint
    pause 1

    show ts_bed_split_animated
    show ts_club_split_animated
    pause 0.99

    show layer screens at ts_showscreens

    show sayori 3i at ln41
    show monika 1pn at f44
    m "А... Алло, да?"
    show sayori 4p at f41
    show monika 1po at t44
    play music ts_ar
    s "Моника, где ты шляешься?! Фестиваль начнётся через полчаса, а тебя до сих пор нет!" with hpunch #причина тряски кстати?
    s 4j "Мы уже всё приготовили, Нацуки кексов напекла, Юри уже наполнила клубную комнату атмосферой, я тоже всё сделала. Одну только тебя ждём!"
    show sayori 4i at t41
    show monika 1pe at t44
    "Даже несмотря на то, что Сайори негодует, я всё равно ничего не могу с собой поделать."
    show monika 1pzd at t44
    "Слёзы счастья выступают на глазах сами собой."
    "Они все живы... фестиваль начнётся через полчаса... всё обязательно будет хорошо..."
    show monika 3pze at f44
    m "Да-да, Сайори... просто... пробки."
    show sayori 3n at f41
    show monika 1pe at t44
    s "Какие ещё пробки? Мы в маленьком городе живём, здесь тысяч пятьдесят жителей, не больше..."
    show sayori 3o at t41
    show monika 1pn at f44
    m "Неважно уже..."
    show monika 3py at f44
    m "В общем, скоро буду. И не начинайте там без меня!"
    show sayori 2l at f41
    show monika 1pe at t44
    stop music fadeout 3
    s "Да мы и так без тебя не начнём..."
    show sayori 2y at t41
    show monika 3pb at f44
    m "Ну и отлично. Всё, давай, до встречи."
    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    scene ts_bedroom with ts_paint

    show layer screens at ts_showscreens
    play music okevrmon
    "Значит, полчаса до фестиваля..."
    "А как же тогда они всю неделю без меня были?.."
    "Хотя, знаете, это значения не имеет."
    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_bathroom
    with wipeleft_scene

    show layer screens at ts_showscreens

    "Быстрыми темпами я умываюсь и чищу зубы."
    "Я так сильно жду этого фестиваля, который, казалось, не наступит уже никогда, что я даже не обращаю внимания на ледяную воду и не менее ледяной привкус зубной пасты."
    "Наскоро умывшись, я спускаюсь на кухню."
    "Это было уже так давно, что уже и не помню, кто там сегодня готовит. Кажется, папа?"
    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_kitchen
    show hiroto 1a at t11
    with wipeleft_scene

    show layer screens at ts_showscreens

    "И да, действительно, когда я спускаюсь, меня уже встречает приятный запах гречки, яичницы с беконом и хлопьев."
    show hiroto 1b at f11
    ts_ft "Привет, Мо—{w=1}{nw}"
    show hiroto 2h at h11
    "Без раздумий я бросаюсь ему в объятия."
    m "Папа, папочка мой любимый... Я так сильно по тебе скучала..."
    m "Я видела такие странные сны... и страшные сны тоже..."
    m "И они все были такими реальными..."
    show hiroto 1y at f11
    ts_ft "Я, к-конечно, тоже очень рад тебя видеть..."
    ts_ft 1z "Но мы с тобой всего одну ночь не виделись, с чего вдруг такие нежности?"
    show hiroto 1b1 at t11
    "Ой..."
    m "Ладно, неважно..."
    show hiroto 1f at t11
    m "Ты мне лучше вот что скажи: когда мама приедет?"
    show hiroto 1g at f11
    ts_ft "Так сегодня же и приедет. Сразу после твоего фестиваля."
    ts_ft 1b "Я, кстати, тоже на этом фестивале буду."
    show hiroto 1a at t11
    "Моему счастью просто нет предела."
    "Меня даже не волнуют мелочи вроде: «А сколько же вообще длился этот сон, если все ведут себя, как будто ничего из ряда вон выходящего не произошло?»."
    "Я просто... счастлива..."
    m "Ладно. Так, что у нас там на завтрак?"
    show hiroto 1b at f11
    ts_ft "Гречка для тебя, яичница с беконом, хлопья по желанию, ну и кофе, само собой."
    ts_ft 1g "Я, конечно, гречку не варил очень давно, но поскольку у тебя такой важный день..."
    show hiroto 1f at t11
    m "Спасибо, папочка, люблю тебя!"
    "Я быстро уплетаю гречку, даже особо не жуя, такими же быстрыми темпами ем хлопья, а затем залпом выпиваю кофе."
    "На весь завтрак у меня уходит не больше пяти минут."
    "Даже на разговоры времени нет, фестиваль важнее. Особенно столь многострадальный..."
    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_kitchen
    show hiroto 1f at t11
    with wipeleft_scene

    show layer screens at ts_showscreens
    "Переодевшись, я говорю папе:"
    m "Ладно, пап, до скорого, а то девочки уже, наверное, меня все заждались..."
    show hiroto 1g at f11
    stop music fadeout 3
    ts_ft "Хорошо, Моника, увидимся в школе!"
    show hiroto 1f at t11
    m "Х-хорошо, пап. Люблю тебя..."
    show hiroto 1g at f11
    ts_ft "И я тебя люблю, солнце."

    play music ts_fresh_air fadein 3
    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_house
    with wipeleft_scene

    play sound pageflip
    scene ts_street
    with wipeleft_scene

    show layer screens at ts_showscreens
    "Мне до сих пор не верится, что это всё на самом деле происходит..."
    "Все девочки в клубе, папа тоже придёт в школу, фестиваль уже начнётся через считанные минуты!.."
    "...правда, есть один человек, по которому я скучаю."
    "Ну, как, «человек»... Аки."
    "С самого утра она не сказала мне ни единого слова."
    "Да, конечно, она постоянно обзывала меня, называла меня тупой бездарностью и всеми производными, но..."
    "В какой-то мере я уже привыкла к ней, потому что это единственный человек, который не забывал всё происходившее за эту неделю."
    "И по иронии судьбы, это единственный человек, которого я считала настоящим, даже несмотря на то, что это фактически просто моё подсознание..."
    "Пока я размышляла об этом, я и сама не заметила, как дошла до школы."

    play ambience vibration_rintone fadein 3

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    scene ts_school_gate_day
    with ts_paint

    show layer screens at ts_showscreens

    "Опять Сайори..."
    "Я перехожу на бег, при этом не снимая трубку."
    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound2 ts_running

    scene ts_school_gate_day at ts_running_fast

    pause 2
    stop sound2 fadeout 1
    play sound pageflip
    play sound3 ts_othodos_ot_bega fadein 2
    scene ts_corridor at ts_ustal_suka
    with wipeleft_scene

    show layer screens at ts_showscreens

    "Спустя где-то секунд сорок я уже у двери клуба."
    "Хорошо, что я в своё время занималась хоть каким-то спортом! Бег хотя бы на такие короткие дистанции не оставил после себя никаких неизгладимых последствий..."
    "Я вваливаюсь в дверь."
    window hide
    stop ambience
    stop sound2
    stop sound3
    play sound door_break
    scene ts_club
    show yuri 2r at t31
    show sayori 3i at t32
    show natsuki 1h at f33
    show layer master at ts_razebal
    show layer screens at ts_showscreens_fast
    n "Явилась не запылилась!"
    show yuri 2r at t31
    show sayori 4j at f32
    show natsuki 1i at t33
    s "Где тебя вообще черти носили?!"
    show yuri 2r at t31
    show sayori 3i at t32
    show natsuki 1i at t33
    m "Во-первых, начальство не опаздывает, начальство задерживается."
    m "А во-вторых..."
    show yuri 2s at t31
    show sayori 3f at t32
    show natsuki 1n at t33
    m "Девочки, простите меня..."
    show yuri 2zi at f31
    show sayori 3f at t32
    show natsuki 1n at t33
    y "За что нам тебя прощать, Моника? Ты же не сделала ничего плохого..."
    show yuri 2s at t31
    show sayori 3f at t32
    show natsuki 1i at t33
    m "Просто, понимаете, мне приснилось кое-что страшное..."
    show yuri 2i at t31
    show sayori 2d at t32
    show natsuki 1t at t33
    m "А хотя, знаете... Неважно. Ведь сон – это просто сон..."
    "Я смотрю на часы, которые снова идут нормально, и понимаю, что до начала фестиваля осталось не больше десяти минут."
    show yuri 1e at t31
    show sayori 2b at t32
    show natsuki 1za at t33
    m "Э-э-э... Ладно. Итак, ребята! Пора превратить эту комнату во что-то стоящее!"
    m "Нацуки, доставай кексы. Юри, доставай баннер и занавески. Сайори, всё готово к сегодняшнему выступлению?"
    show yuri 4b at s31
    show sayori 5a at f32
    show natsuki 12b at s33
    s "А-ха-ха, насчёт этого..."
    s 5b "Мы как-то... особо не заморачивались по поводу этого всего..."
    s 3h "Нет, конечно, кексы готовы, и Юри сделала парочку простеньких декораций, но... не более того..."
    s "Если к нам кто-то придёт, то это уже будет большим достижением, но, видимо, не придёт никто. Разве что возьмут кекс и пойдут дальше..."
    show yuri 4b at s31
    show sayori 3f at s32
    show natsuki 12b at s33
    "Я хотела сказать, зачем они меня вообще сюда гнали, но быстро собралась с силами и вместо этого лишь уверенно отвечаю:"
    show yuri 4a at t31
    show sayori 2e at t32
    show natsuki 12a at t33
    m "О, насчёт этого не переживайте – один человек {b}точно{/b} придёт. Это мой папа."
    m "А даже если никто больше не придёт – мы всё равно проделали работу. А главное – не результат, а сам процесс и веселье, которое вы от этого получаете."
    m "Вам же было весело?"
    show yuri 2q at t31
    show sayori 3l at t32
    show natsuki 2t at t33
    "Девочки стеснительно закивали головой."
    m "Ну вот. Это и есть самое главное. А всё остальное уже не важно."
    m "А теперь давайте уже побыстрее, до начала примерно пять минут осталось."
    show yuri 2d at f31
    show sayori 3r at f32
    show natsuki 2z at f33
    "Похоже, что я их переубедила, потому что после моей речи девочки весело зашуршали своими приготовлениями."
    show yuri 2d at t31
    show sayori 3r at t32
    show natsuki 2z at t33
    m "Кстати, а вы стихи-то написали? Потренировались хорошенько дома?"
    if _preferences.language == "english":
        $ m_name = "Everyone"
    else:
        $ m_name = "Все вместе"
    show yuri 2d at f31
    show sayori 3r at f32
    show natsuki 2z at f33
    m "Ну конечно!"
    stop music fadeout 3
    show yuri 2c at t31
    show sayori 3q at t32
    show natsuki 2z at t33
    if _preferences.language == "english":
        $ m_name = "Monika"
    else:
        $ m_name = "Моника"
    m "Отлично..."
    "Со всеми этими циклами и повторениями я уже и забыла, какие стихи каждая из них написала..."
    "Главное, хотя бы свой собственный не забыть..."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_club
    show yuri 2o at t31
    show sayori 3k at t32
    show natsuki 2u at t33
    with wipeleft_scene

    show layer screens at ts_showscreens

    "С момента начала фестиваля прошло по меньшей мере пятнадцать минут."
    "Девочки в который раз перечитывали свои стихи, и с каждым разом надежда на то, что их услышит хоть кто-нибудь, становилась всё менее и менее яркой."
    "Даже папа не пришёл... А ведь он обещал..."
    m "Л-ладно, девочки..."
    "Все угрюмо закивали."
    play sound stuk
    show yuri 3n at h31
    show sayori 3m at h32
    show natsuki 2p at h33
    show layer screens at vpunch
    "Как тут в дверь резко постучали. От такого дёрнулись все, даже я."
    if _preferences.language == "english":
        $ misc_name = "Student"
    else:
        $ misc_name = "Ученик"
    misc "И-извините, {b}это{/b} комната с кексами?"
    misc "У вас просто в объявлении указан не тот этаж..."
    show yuri 2f at t31
    show sayori 3l at f32
    show natsuki 2s at t33
    s "Что вы все на меня так смотрите?"
    show yuri 2f at t31
    show sayori 3l at t32
    show natsuki 2s at t33
    "Первой взяла себя в руки я."
    play music audio.t3 fadein 2
    m "Э-э-э... да, добро пожаловать в Литературный клуб, меня зовут Ида Моника, а это Касанэ Юри, Аме Сайори и Яторо Нацуки." #НАШ МУЖИК КАСАНЬЕ, НАША СЛОНИХА ЕС ЧО
    show yuri 1u at t31
    show sayori 3y at t32
    show natsuki 2t at t33
    "Остальные девочки робко поприветствовали новоприбывшего ученика."
    misc "Сейчас, я быстренько сообщу всем."
    misc "{size=+10}ЭЙ, ВСЕ СЮДА! КОМНАТА С КЕКСАМИ ЗДЕСЬ!{/size}"
    stop music fadeout 3
    "На крик этого ученика пришли ещё где-то с десяток учеников."
    "Однако папы до сих пор не было видно..."

    play music audio.t8 fadein 3

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_club
    show yuri 1u at t31
    show sayori 3y at t32
    show natsuki 2t at t33
    with wipeleft_scene

    show layer screens at ts_showscreens

    "Как и ожидалось, несколько учеников просто взяли кекс и ушли искать другие клубы, но большинство всё же остались здесь."
    show yuri 1j at t31
    show sayori 3c at t32
    show natsuki 1k at t33
    "Девочки приветствовали новичков, рассказывали им о жизни клуба и прочих мелочах."
    "Я же просто... мечтательно закрыла глаза."
    show blink
    stop music fadeout 4
    "«Ну что, Аки, ты проиграла. Фестиваль случился, никто не умер – всё же хорошо...»"
    "Но мне ожидаемо никто не ответил..."
    "А жаль..."
    hide blink
    show unblink
    play music t5_all fadein 2
    show hiroto 1b at t41
    show yuri 2zi at t42
    show sayori 3zc at t43
    show natsuki 2c at t44
    "А когда я вновь открыла глаза, я наконец-то увидела, как папа уже заигрывает с остальными девочками."
    show hiroto 1a at t41
    show yuri 2s at t42
    show sayori 3d at t43
    show natsuki 2a at t44
    m "Папа!"
    show hiroto 1g at t41
    show yuri 2s at t42
    show sayori 3d at t43
    show natsuki 2a at t44
    ts_ft "Иди сюда, дорогая..."
    show hiroto 1f at t41
    show yuri 2s at t42
    show sayori 3d at t43
    show natsuki 2a at t44
    show layer master at ts_obnimashki_good_finalle
    "Я снова обнимаю его."
    show hiroto 1g at f41
    show yuri 2s at t42
    show sayori 3d at t43
    show natsuki 2a at t44
    show layer master at ts_obnimashki_good_finalle1
    ts_ft "Еле вас нашёл... Если бы не крики одного ученика, то я бы в принципе не смог вас найти..."
    show hiroto 1f at t41
    show yuri 2zi at f42
    show sayori 3d at t43
    show natsuki 2a at t44
    y "Моника, это, я так полагаю, твой отец?"
    show hiroto 1f at t41
    show yuri 2s at t42
    show sayori 3d at t43
    show natsuki 2a at t44
    stop music fadeout 3
    m "Да. Мистер Ида Хирото. Добрейшей души человек."
    stop music
    show hiroto 1j at t41
    show yuri 2t at f42
    show sayori 3e at t43
    show natsuki 2a at t44
    y "Почему вы тогда так не похожи друг на друга?.."
    show hiroto 1j at t41
    show yuri 2t at t42
    show sayori 3e at t43
    show natsuki 2a at t44
    "..."
    play music t5_all fadein 2
    m "Я просто вся в маму пошла..."
    show hiroto 1f at t41
    show yuri 2zi at f42
    show sayori 3d at t43
    show natsuki 2a at t44
    y "Понятно тогда..."
    show hiroto 1d at t41
    show yuri 2s at t42
    show sayori 3d at t43
    show natsuki 2a at t44
    m "Кстати, а где мама?"
    show hiroto 1c at f41
    show yuri 2s at t42
    show sayori 3d at t43
    show natsuki 2a at t44
    stop music fadeout 3
    ts_ft "Я десять минут назад ей звонил – она говорит, что не успела на утренний рейс, поэтому на самом фестивале её не будет."
    ts_ft "Но она говорит, что будет в школе как только, так сразу."
    show hiroto 1a at t41
    show yuri 2s at t42
    show sayori 3d at t43
    show natsuki 2a at t44
    m "Ох, ну здорово."
    "К чёрту уже этот фестиваль – поскорее бы уже с мамой увидеться..."
    play music audio.t8 fadein 2

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_club
    show yuri 2d at t31
    show sayori 3r at t32
    show natsuki 2z at t33
    with wipeleft_scene

    show layer screens at ts_showscreens


    "Ну, могло быть и хуже; но могло быть и лучше."
    "После того, как мы все прочитали стихи, по большей части мы все просто веселились."
    "В клуб к нам так никто и не записался. Жалко, конечно, но это и не удивительно."
    "Да и мы уже такой компанией привыкли всё делать, и на новичков как минимум некоторые из нас будут смотреть с некоторым пренебрежением."
    "Так что, наверное, это и к лучшему."
    "Конечно, папа слегка расстроился, что к нам так и не вступил никто из новичков, но лично я уже привыкла к трём девочкам, и не особо уже хочу добирать ещё кого-то."
    "А это всё, что важно..."
    "После того, как ушёл последний посетитель, я обращаюсь к девочкам."
    m "Итак, девчата!"
    stop music fadeout 3
    show yuri 1e at t31
    show sayori 2b at t32
    show natsuki 1za at t33
    "Девочки как-то странно на меня посмотрели."
    show yuri 1f at f31
    show sayori 2b at t32
    show natsuki 1za at t33
    y "Мне показалось, или ты изменила свою фирменную фразу при обращении к клубу?"
    show yuri 1e at t31
    show sayori 2b at t32
    show natsuki 1za at t33
    m "Ф-фирменную фразу?"
    show yuri 1e at t31
    show sayori 2c at f32
    show natsuki 1za at t33
    m "Да, ты всегда говоришь «Итак, ребята», а сейчас сказала «Итак, девчата»."
    show yuri 1e at t31
    show sayori 2b at t32
    show natsuki 1za at t33
    play music ts_conf
    m "Ну-у-у... Я же выстраивала клуб на перспективу, надеясь, что после фестиваля появятся и парни, и девушки."
    m "Однако фестиваль уже прошёл, а у нас так никто и не прибавился..."
    show yuri 1u at t31
    show sayori 3y at t32
    show natsuki 2t at t33
    m "И я подумала: а оно мне вообще надо? Сейчас мне и нашей небольшой женской компании хватает."
    m "И поскольку это выпускной класс для всех нас, кроме Нацуки, я, пожалуй, изменю свою {i}фирменную фразу{/i}."
    m "Какая вообще разница, ребята мы, девчата, или кто-то ещё? Главное, что мы вместе сейчас, и будем вместе и дальше."
    show yuri 2j at t31
    show sayori 3l at t32
    show natsuki 2t at t33
    "Все девочки смущённо засмеялись."
    stop music fadeout 3
    m "В общем, ладно! Ребята мы или девчата – надо бы после фестиваля всё убрать, чтобы к следующему собранию было всё как обычно, без фантиков и прочего мусора."
    show yuri 2h at f31
    show sayori 3h at f32
    show natsuki 2q at f33
    if _preferences.language == "english":
        $ m_name = "Gals"
    else:
        $ m_name = "Девчата"
    m "Да, Моника..."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_club
    show yuri 2j at t31
    show sayori 3l at t32
    show natsuki 2t at t33
    with wipeleft_scene

    show layer screens at ts_showscreens

    play music ts_afterword fadein 2

    "Спустя примерно двадцать минут от мусора не осталось и следа."
    if _preferences.language == "english":
        $ m_name = "Monika"
    else:
        $ m_name = "Моника"
    m "Ну, собственно... Пора на этом и заканчивать наше мероприятие..."
    m "Жду вас всех завтра!"
    if _preferences.language == "english":
        $ m_name = "Gals"
    else:
        $ m_name = "Девчата"
    show yuri 2b at f31
    show sayori 3x at f32
    show natsuki 2l at f33
    m "Пока, Моника!"
    if _preferences.language == "english":
        $ m_name = "Monika"
    else:
        $ m_name = "Моника"
    show yuri 2a at t31
    show sayori 3a at t32
    show natsuki 2j at t33
    m "До завтра, девочки."
    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"
    play sound door_open
    show yuri 2a at cright with move
    hide yuri
    show sayori 3a at cright with move
    hide sayori
    show natsuki 2j at cright with move
    hide natsuki
    show layer screens at ts_showscreens
    "Все уходят."
    "Ну, наверное, пойду и я..."
    play sound stuk
    "Однако как только я встаю, чтобы направиться к выходу, как тут раздаётся ещё один стук в дверь."
    "И кого там только принесло?! Спектакль уже давно окончен!"
    "Дверь открывается и тот, кого «принесло», повергает меня в очень приятный шок."
    stop music fadeout 3
    show minami 2n at f11
    ts_mt "Извините, а это Литературный клуб?"
    show minami 2j at t11
    m "Мама!"
    show minami 1k at f11
    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"
    scene ts_mon_maman_3 with ts_paint
    show layer screens at ts_showscreens
    play music ts_never fadein 2
    m "Мамочка, я так по тебе скучала!"
    scene ts_mon_maman_2
    ts_mt "Я тоже по тебе очень скучала..."
    scene ts_mon_maman_8
    m "Как добралась вообще, нормально?"
    scene ts_mon_maman_5
    ts_mt "Ну я же ещё в школе тебя увидела, а не дома, поэтому, как ты можешь понять, нормально."
    ts_mt "Как только я вышла из аэропорта, ко мне сразу же кинулись несколько таксистов с предложением подвезти до дома."
    scene ts_mon_maman_4
    ts_mt "Я выбрала одного понравившегося и сказала, что везти меня нужно не до дома, а до школы."
    ts_mt "Он очень странно на меня посмотрел, но желание исполнил. И вот, сорок минут в пути, и я уже здесь."
    scene ts_mon_maman_6
    m "Так а как ты вообще узнала, в какой именно кабинет тебе подходить?"
    scene ts_mon_maman_5
    ts_mt "Так мне папа номер кабинета сбросил сообщением. Потом сказал, мол, «я блуждал долго, но с горем пополам добрался до пункта назначения – не повторяй моих ошибок»."
    stop music fadeout 3
    scene ts_mon_maman_6
    m "Понятно..."
    scene ts_mon_maman_8
    m "Ну, я очень рада, что ты вовремя приехала."
    scene ts_mon_maman_3
    m "Пойдём, мне ещё столько всего рассказать тебе надо!.."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    scene black with ts_paint
    pause 1
    scene ts_kitchen with ts_paint

    show layer screens at ts_showscreens

    play music ts_anxiety fadein 2
    show minami 2ba at t11
    "Всю дорогу от школы до дома и ещё примерно час после этого я всё рассказывала и рассказывала маме все детали и подробности последних полутора месяцев."
    "Как я нашла Сайори."
    "Как я нашла Юри."
    "А затем и Нацуки."
    show minami 3bj at t11
    "Как Нацуки оставила всю коллекцию своей манги, а Юри оставила свой чайный сервиз у нас в клубе."
    "Про проблемы всех девочек, естественно, я тактично умалчиваю."
    show minami 2bl at t11
    "И даже про... {i}чаепитие{/i}."
    "О снах после того самого {i}чаепития{/i}, естественно, я тоже рассказывать не особо горю желанием..."
    "Да, кстати, об этом... По идее, целая неделя ведь прошла – почему за неделю никто так и не удосужился спросить, где же я?"
    "...ладно, сейчас не об этом..."
    show minami 3bk at f11
    ts_mt "А-ха-ха! Ну и как, хоть одну бутылку на четверых вы выпили?"
    show minami 3bj at t11
    m "Ну-у-у... да. Я хотела за второй бутылкой сходить, но девочки решили, что мне уже и так достаточно."
    show minami 3bl at f11
    ts_mt "А-ха-ха... Потомственное семейство алкоголиков, ничего не скажешь..."
    show minami 3bl at t11
    m "Это комплимент был или упрёк?"
    show minami 2bt at f11
    ts_mt "И то, и другое."
    show minami 3bk at t11
    "Мы обе над этим посмеялись."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_kitchen
    show minami 1ba at t11
    with wipeleft_scene

    show layer screens at ts_showscreens
    play sound door_open

    "Время идёт, а мы всё так же весело и непринуждённо разговариваем, как тут на кухню входит и папа."
    show minami 1ba at t21
    show hiroto 2b at ln22
    ts_ft "Тук-тук-тук, я дома!"
    show minami 2bk at f21
    show hiroto 2a at t22
    ts_mt "Здравствуй, любимый."
    show minami 2bj at t21
    show hiroto 2g at f22
    ts_ft "Привет, дорогая."
    show minami 2bj at t21
    show hiroto 2f at t42
    show layer screens at ts_hidescreens_fast
    " {w=0.1}{nw}"
    pause 0.08
    show layer screens at ts_showscreens_fast
    show minami 2bj at t21
    show hiroto 2f at t22
    m "Привет, пап."
    show minami 2bj at t21
    show hiroto 2g at f22
    ts_ft "И тебе привет, солнышко."
    show minami 2bj at t21
    show hiroto 2z at f22
    ts_ft "А вы что, ничего не приготовили?"
    show minami 2bn at f21
    show hiroto 2f at t22
    ts_mt "Да мы что-то заболтались, и совсем счёт времени потеряли..."
    ts_mt 3bv "Кстати, а который час вообще?"
    show minami 3bu at t21
    show hiroto 1c at f22
    stop music fadeout 3
    ts_ft "Ну, если я уже с работы пришёл, то где-то не раньше шести вечера."
    show minami 3bw at h21
    show hiroto 1e at t22
    ts_mt "Ой!"
    show minami 2bt at f44
    ts_mt "Н-не переживайте, сейчас что-нибудь на скорую руку приготовлю!"
    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    scene black with ts_paint
    pause 1
    scene ts_kitchen with ts_paint

    show layer screens at ts_showscreens

    play music ts_train_station fadein 2
    show minami 2bm at t21
    show hiroto 1a at t22
    "Всё-таки мама – это прирождённая кухарка."
    "Она за пятнадцать минут по-быстрому приготовила жареную картошку и какой-то простенький салатик."
    show minami 2bn at f21
    show hiroto 1a at t22
    ts_mt "Приятного аппетита вам."
    show minami 2bm at t21
    show hiroto 1a at t22
    "Я замечаю, что на столе только две тарелки."
    m "А ты не будешь?"
    show minami 2bn at f21
    show hiroto 1j at t22
    ts_mt "Я что-то с дороги устала, не хочу есть, пойду лучше спать лягу..."
    ts_mt "Тарелки я уже с утра помою."
    show minami 2bm at t21
    show hiroto 2f at t22
    m "Понятно..."
    m "Ну, ты иди отдыхай тогда, а мы поужинаем, и тоже уже начнём ко сну готовиться..."
    show minami 2bl at f21
    show hiroto 2f at t22
    ts_mt "Ну и замечательно..."
    show minami 2bk at f21
    show hiroto 2f at t22
    ts_mt "Спокойной ночи, ребят!"
    if _preferences.language == "english":
        $ m_name = "Dad & Moni"
    else:
        $ m_name = "Папа и Мони"
    show minami 2bj at t21
    show hiroto 2g at f22
    m "Спокойной ночи!"
    show minami at lhide
    hide minami
    show hiroto 1f at t11
    if _preferences.language == "english":
        $ m_name = "Monika"
    else:
        $ m_name = "Моника"
    "После этих слов мама пошла к себе в спальню, оставляя нас с папой наедине."
    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_kitchen
    with wipeleft_scene

    show layer screens at ts_showscreens
    "Остаток вечера мы проводим молча. Все слишком истощены, особенно я."
    "Доев картошку, я как бы невзначай говорю папе, что я тоже устала, и что я тоже пойду отдыхать."
    show hiroto 1g at f11
    ts_ft "Хорошо, Моника, спокойной ночи."
    ts_ft "Я ещё немного телевизор посмотрю, и тоже к вам присоединюсь."
    show hiroto 1f at t11
    stop music fadeout 4
    m "Спокойной ночи, пап. Люблю тебя."
    show hiroto 1g at f11
    ts_ft "Я тоже тебя люблю, золотце."
    show hiroto at lhide
    hide hiroto
    "А затем каждый отправился по своим делам: папа – смотреть телевизор, а я – отдыхать."
    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_bedroom
    with wipeleft_scene

    show layer screens at ts_showscreens
    play music ts_afterlife fadein 1
    "Эх, какой всё-таки хороший день!"
    "Фестиваль состоялся, все девочки живы-здоровы, мама приехала... не день, а сплошное счастье."
    "И пусть после фестиваля в наш клуб так никто и не записался..."
    "Всё равно было здорово..."
    "Однако как только я собираюсь выключать свет и раздеваться, я замечаю записку, которую с утра не заметила."
    "При более детальном обзоре я понимаю, что записка эта написана... моим почерком."
    "Что-то я не помню того, как я эту записку писала..."
    "Заинтересованная, я начинаю её читать."

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    scene ts_bedroom:
        blur 9.0
    with dissolve

    show layer screens at ts_showscreens

    play sound pageflip

    if _preferences.language == "english":
        show screen poem(poem_farewell_aki_eng)
    else:
        show screen poem(poem_farewell_aki)

    pause

    play sound pageflip
    show layer screens at ts_hidescreens
    pause 1.0
    hide screen poem


    scene ts_bedroom
    with dissolve

    show layer screens at ts_showscreens

    "Ах ты... козявка..."
    "Это что, она всё подстраивала?"
    "Или всё-таки нет?"
    "И что это за такой намёк, что «тебе был дан второй шанс»?"
    "Слишком сложно для понимания..."
    "Ладно, я слишком уставшая и слишком счастливая, чтобы рассуждать на эту тему..."

    play sound svet_on
    scene ts_darkbed

    "Я выключаю свет, раздеваюсь и ложусь в кровать."
    "Сегодня был такой замечательный день. А дальше будет только лучше..."
    "А кошмарный сон – это ведь всего лишь сон..."
    "Так ведь?"

    show layer screens at ts_hidescreens
    " {w=1.0}{nw}"

    show layer screens
    window hide

    jump good_credits_ts_label