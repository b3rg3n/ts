label ts_scenario_3:

    $ TS.b()

    $ ts_rpc_carter3()

    $ persistent.rpclabel = "3"
    $ persistent.uncolorize = "none"
    $ persistent.sprite_time = "day"

    $ persistent.carter2menu = False
    $ persistent.carter3menu = False
    $ persistent.badendmenuperedglitch = False
    $ persistent.badendmenuskipglitch = False
    $ persistent.badendmenu = False
    $ persistent.goodendmenu = False
    $ persistent.peredbadendmenu = False
    $ persistent.peredgoodendmenu = False

    if _preferences.language == "english":
        $ save_name = "Searching. Natsuki"
    else:
        $ save_name = "Поиски. Нацуки"

    $ TS.p(2)
    play sound chp1
    if _preferences.language == "english":
        $ Chapter("ACT ONE")
        $ Chapter("ACT ONE")
        $ Chapter("chapter three")
        $ Chapter("chapter three")
        $ Chapter("Searching. Natsuki")
        stop sound fadeout 7
        $ Chapter("Searching. Natsuki")
    else:
        $ Chapter("АКТ ПЕРВЫЙ")
        $ Chapter("АКТ ПЕРВЫЙ")
        $ Chapter("глава третья")
        $ Chapter("глава третья")
        $ Chapter("Поиски. Нацуки")
        stop sound fadeout 7
        $ Chapter("Поиски. Нацуки")

    play music ts_gramatik fadein 2

    play sound ts_alarm fadein 2

    $ TS.p(2)

    scene ts_bedroom
    show unblink
    $ TS.m(ts_vstavai_shashlik)
    $ TS.p(3)
    play sound svet_on
    $ TS.p(1.5)

    $ TS.s(ts_showscreens)

    #"Часы показывают ровно семь утра."

    "Новую неделю я начала... с незнания, что мне делать дальше."
    "Неделю назад к нам пришла новая девушка, Юри."
    "Поначалу её немногословность даже пугала."
    "Но в пятницу меня напугала совсем не её немногословность."
    "И даже не фактическое раздвоение личности..."

    window hide
    play sound fb
    scene ts_school_bathroom
    show yuri 9p at t11
    show zatemnenie_light
    show overlay aw_memory_back_1
    $ TS.m(VHS())
    with flash

    $ TS.s(ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake))

    "Меня напугала её мания навредить себе."
    "Юри тогда сказала, что это потому что она чувствует себя ничтожеством и внутренний голос твердил ей перейти от слов к делу."
    "Не знаю, насколько правдивы были её слова в пятницу, но..."
    "Порезы на ней выглядели вполне реальными. Да и сама она... тоже вполне реальной была."
    "Или это всё горяченный бред, и на самом деле никакой Юри и не было?"
    "Что же... Об этом я узн{b}а{/b}ю уже в клубе."

    play sound fb
    window hide
    scene ts_bedroom
    with flash

    $ TS.s(ts_showscreens)

    "А до клуба мне ещё многое нужно сделать."
    "Например, умыться, позавтракать, стерпеть химию и биологию, и дойти до самого клуба."
    "Ну, если начинать прямо сейчас, то, может, и на разговор с папой время останется."

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

    m "Бр-р-р..."
    "Я уже привыкла к холодной воде, и я так умывалась, сколько себя помню."
    "Но всё равно каждый раз как первый."
    "Наспех умывшись и почистив зубы, я спускаюсь на кухню."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_kitchen
    with wipeleft_scene

    $ TS.s(ts_showscreens)

    m "М-м-м..."
    "Поскольку дней всего семь, а нас на данный момент всего двое, то в этот понедельник завтрак готовит папа."
    "Я ещё только спускалась по коридору, а уже чувствовала приятный запах яичницы."
    "Хотя папа – это всё-таки не мама, он всё равно готовит куда лучше меня."
    "Он же папа, он же опытный..."
    show hiroto 1b at ln11
    ts_ft "Доброе утро, солнце!"
    m "Доброе, пап."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    show hiroto 1a at f11
    $ TS.m(ts_osmotr_tipa_center)

    nvl clear

    $ TS.s(ts_showscreens_nvl)

    nvlbazar "{font=[ts_nvl_font2]}Наверное, я должна была познакомить вас с моим папой гораздо раньше."
    nvlbazar "{font=[ts_nvl_font2]}Но так уж получилось, что знакомлю я вас с ним только сейчас."
    nvlbazar "{font=[ts_nvl_font2]}Дела..."
    nvlbazar "{font=[ts_nvl_font2]}Его зовут Ида Хирото, и он, как вы уже догадались, мой папа."
    if _preferences.language == "english":
        $ ts_ft_name = "Hiroto"
    else:
        $ ts_ft_name = "Хирото"
    nvlbazar "{font=[ts_nvl_font2]}Вы меня, конечно, спросите:"
    nvlbazar "{font=[sc_font]}Но как? вы же совсем друг на друга не похожи!"

    nvl clear

    nvlbazar "{font=[ts_nvl_font2]}Понимаете, генетика – это такая штука, в которой для создания человека нужны два других человека, не меньше. Но и не больше."

    show hiroto at thide
    hide hiroto
    show minami 1a at t21
    show monika 1a at t22
    $ TS.m(ts_osmotr_tipa_levocentr)
    nvlbazar "{font=[ts_nvl_font2]}Так вот, я как две капли воды похожа на свою маму."
    nvlbazar "{font=[ts_nvl_font2]}Не зря же существует... не знаю, поверье, поговорка, присказка..."
    nvlbazar "{font=[ts_nvl_font2]}В общем, «если хочешь посмотреть на девушку лет эдак через двадцать, посмотри сначала на её маму»."
    nvlbazar "{font=[ts_nvl_font2]}И в случае меня и моей мамы это {i}поверье{/i} сработало как никогда."
    show minami 1a at thide
    show monika 1a at thide
    hide minami
    hide monika
    $ TS.s(ts_hidescreens_nvl)
    nvlbazar " {w=1.0}{nw}"
    nvl clear

    scene ts_kitchen
    show hiroto 1a at f11

    $ TS.s(ts_showscreens)

    m "Что на завтрак?"
    ts_ft 2b "Яичница с беконом для меня, хлопья с молоком для тебя, и кофе для нас обоих!"

    show hiroto 1a at t11

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    $ TS.s(ts_showscreens_nvl)
    nvlbazar "{font=[ts_nvl_font2]}Я – вегетарианка."
    nvlbazar "{font=[ts_nvl_font2]}Несколько лет назад, ещё в пик моего юношеского максимализма, я как-то просмотрела пару документалок про животноводство."
    nvlbazar "{font=[ts_nvl_font2]}И знаете, то, с какой жестокостью и бездушностью фермеры закалывают беззащитных хрюшек и курочек, просто повергло меня в шок."
    nvlbazar "{font=[ts_nvl_font2]}А если это промышленное производство, то бездушность только многократно усиливается."
    nvlbazar "{font=[ts_nvl_font2]}Поэтому, после одной из таких документалок, я гордо сказала родителям, что с этого момента я наотрез отказываюсь есть мясо."
    nvlbazar "{font=[ts_nvl_font2]}Родители хмыкнули, но спорить со мной не стали."
    nvlbazar "{font=[ts_nvl_font2]}Поэтому, где-то лет с тринадцати и до сегодняшнего дня, я не ем мясо ни в каком виде."

    nvl clear

    nvlbazar "{font=[ts_nvl_font2]}Обычное мясо, ветчина, бекон – на это всё я говорю своё категоричное фи."
    nvlbazar "{font=[ts_nvl_font2]}Нет, на радикальные меры вроде отказа от молочки или яиц, чтобы в итоге есть одни только фрукты да овощи, я ещё не готова."
    nvlbazar "{font=[ts_nvl_font2]}Я же всё-таки ещё растущий организм."
    nvlbazar "{font=[ts_nvl_font2]}Но обещаю, что когда стану взрослой, откажусь и от этого."
    nvlbazar "{font=[ts_nvl_font2]}Но не сейчас."

    $ TS.s(ts_hidescreens_nvl)
    nvlbazar " {w=1.0}{nw}"

    nvl clear

    $ TS.s(ts_showscreens)

    m "Спасибо, пап, ты очень заботливый."
    ts_ft 2g "Всегда пожалуйста, дорогая."
    show hiroto 1f at f11
    ts_ft 1b "Та-а-ак, какие планы на день?"
    show hiroto 1a at t11
    m "Да как обычно, школа, клуб, домой."

    show hiroto 1a at cright with move
    hide hiroto

    "Я подавляю нервозность, когда говорю о клубе."
    "Ну что это такое, ко мне пришло всего два человека, и у обоих такие серьёзные проблемы!"

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"


    show zatemnenie with dspr

    $ TS.s(ts_showscreens)

    show screen chp_text_13
    pause
    $ TS.s(ts_hidescreens)
    show screen chp_text_13
    $ TS.p(1)
    hide screen chp_text_13

    hide zatemnenie with dspr

    $ TS.s(ts_showscreens)

    stop music fadeout 5

    "И это ещё не говоря о том, что я взяла на себя обязанность хранить их секреты ото всех, даже от других членов клуба."
    "Ну то есть, вот же Сайори обрадуется, если я скажу Юри, что у Сайори депрессия, не сказав при этом о том, что у Юри, в свою очередь, мания навредить себе!"
    "Или наоборот..."
    "Но, как говорится, меньше знаешь – крепче спишь. А, соответственно, больше знаешь – спишь меньше.{w} Если вообще спишь."
    "В первую ночь мне даже снились кошмары про Юри."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound fb
    scene ts_club
    show yuri 3y1 at i11
    with flash

    play music audio.t10y
    $ TS.m(heartbeat)
    play ambience audio.hb

    $ TS.s(ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake))

    "Передо мной стоит Юри. Но это... совсем не та Юри, которую я знаю!"
    "Это не похоже ни на одну из уже трёх личностей, это... было совсем другое."
    "Юри как будто обезумела!"

    m "Ю-Юри, а т-ты ч-что здесь делаешь?.."
    y 3y6 "Я хочу, чтобы ты полностью принадлежала мне."
    y "А я – только тебе."
    m "Ч-что?"

    "Но она как будто меня не слышала."

    y "Разве не изумительно это звучит?"
    y 3s "Скажи мне."
    y "Ты принимаешь моё признание?"
    m "Э-э-э..."

    menu:
        "...Да?":
            pass
        "...Нет?":
            pass


    stop music
    stop ambience
    scene ts_club
    show yuri 3d at i11
    y "...А-ха-ха-ха."
    y "А-ха-ха-ха-ха-ха-ха!"
    y 3y5 "А-ха-ха-ха-ха-ха-ха-ха-ха!"
    y 3y3 "{font=[pizdec_font]}А-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА!{nw}"
    window hide


    play sound yurikill
    $ TS.p(1.43)
    show yuri stab_1
    $ TS.p(0.75)
    show yuri stab_2
    show blood:
        pos (610,485)
    $ TS.p(1.25)
    show yuri stab_3
    $ TS.p(0.75)
    show yuri stab_2
    show blood:
        pos (610,485)
    show yuri stab_4 with ImageDissolve("mod_assets/source/images/spr/yuri/stab/4_wipe.webp", 0.25)
    $ TS.p(1.25)
    show yuri stab_5
    $ TS.p(0.7)
    show yuri stab_6:
        2.55
        easeout_cubic 0.5 yoffset 300
    show blood as blood2:
        pos (635,335)
    $ TS.p(2.55)
    hide blood
    hide blood2
    $ TS.p(0.25)
    play sound fall
    $ TS.p(0.25)
    scene black
    $ TS.p(2)

    scene black
    show y_kill
    with dissolve_cg

    $ TS.s(ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake))

    "Дальше, что бы я ни ответила, Юри убивает себя ножом. Дважды в живот, и ещё один раз – в грудь."

    window hide
    play sound ssikanul
    $ TS.p(0.2)
    scene ts_darkbed
    show overlay aw_memory_back_1
    $ TS.m(VHS())
    with vpunch
    $ TS.p(1)

    $ TS.s(ts_showscreens)

    "А затем я просыпаюсь."
    "Что это вообще было?"
    "И почему у Юри были такие безумные глаза?"
    "Она как будто совершенно не видела не то, что меня, она даже себя саму с трудом различить смогла бы, с такими-то глазами берсерка!"
    "Ничего не понимаю..."

    window hide
    play sound fb
    play music audio.t2
    scene ts_kitchen
    show hiroto 1h at t11
    with flash

    $ TS.s(ts_showscreens)

    ts_ft "Моника?"
    ts_ft 1q "Земля вызывает Монику, как слышно?"
    show hiroto 1p at s11
    m "А, да!.. Я просто... задумалась..."
    ts_ft 1h "Ты «задумывалась» все выходные..."
    ts_ft "Ты как будто сама не своя."
    extend " Что-то не так?"
    ts_ft "У тебя в школе какие-то проблемы, или с клубом не ладится?"
    show hiroto 1j at t11
    m "Нет-нет, что ты..."
    m "Просто... навалилось всякое, вот надо и подумать основательно..."
    ts_ft 1h "Ладно..."
    ts_ft 1b "Собирайся, а то в школу опоздаешь!"
    show hiroto 1a at s11
    m "Мой учебный день и твой рабочий день начинаются одновременно, в половину девятого."
    m "Поэтому если я опоздаю в школу, а ты всё ещё будешь сидеть со мной, то и ты на работу опоздаешь."
    ts_ft 2y "Чёрт, точно..."

    stop music fadeout 5

    ts_ft 1b "Тогда я пошёл, но и ты не задерживайся!"
    m "Хорошо, пап..."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_house
    with wipeleft_scene

    $ TS.s(ts_showscreens)

    "Я попрощалась с папой, после чего каждый пошёл своей дорогой."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play music ts_mdl fadein 1
    play sound pageflip
    scene ts_street
    show ts_green_part
    with wipeleft_scene

    $ TS.s(ts_showscreens)

    "Часы показывают 8:10."
    "С учётом того, что мне до школы идти от силы минут десять-пятнадцать, даже неспешным шагом..."

    $ TS.s(vpunch)

    "«Вот же папа!..»"
    "«Разыграл меня, как маленькую девочку...»"
    "Впрочем, я и на взрослую даму не особо-то тяну."
    "Улыбнувшись себе, я продолжаю идти."

    $ TS.s(ts_hidescreens)
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

    $ TS.s(ts_showscreens)

    "Фух, успела."
    "И до уроков ещё осталось минут десять."
    "Что же, начнём этот день!"

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    scene black with dissolve_scene_full
    
    scene ts_class with dissolve_scene_full

    $ TS.s(ts_showscreens)

    "..."
    "Как же я ненавижу биологию!"
    "Если с химией я в относительно нейтрально-прохладных отношениях, то биологию я просто ненавижу."
    "И соответственно, биология ненавидит меня."
    "И почему два моих самых ненавистных предмета должны быть именно в понедельник?!"
    if persistent.cens_mode == True:
        "Просто охуительное начало недели..."
    else:
        "Просто замечательное начало недели..."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound2 zvonok fadein 2
    play sound pageflip
    scene ts_class
    with wipeleft_scene

    $ TS.s(ts_showscreens)

    "Наконец-то, перемена..."
    stop sound2 fadeout 3
    "После второго урока перемена побольше, чтобы все успели перекусить, потому что день предстоит долгий..."
    "А если ещё и кому-то в клубы надо, то покушать просто необходимо."
    "Но сегодня мне что-то не хочется."
    stop music fadeout 3
    "Даже с учётом того, что у меня ещё Литературный клуб, и приду я поздно, папа, по всей видимости, насыпал хлопьев от души, так что я до сих пор не проголодалась."
    "Поэтому вместо того, чтобы обедать, я просто выхожу в коридор и отдыхаю."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_corridor
    with wipeleft_scene

    $ TS.s(ts_showscreens)

    "Как вдруг..."

    play music okevrnat1

    show himari 1a at t31
    show natsuki 1a at t32
    show elena a at t33
    with linearblur

    $ TS.m(ts_ebalo_k_osmotru)

    "Передо мной стоят три девушки. По всей видимости, подружки."
    "Но что-то здесь не так... Совсем не так."

    show natsuki 1f at s32

    pod1 1w "Ну что, Нацуки? Опять будешь доказывать всем, что манга – это литература?"
    n 2e "Да, буду доказывать, и что ты мне сделаешь?!" with vpunch

    show himari 1v at f31
    show natsuki 1f at f32

    "Я присматриваюсь. Девушку с розовыми волосами, по всей видимости, зовут Нацуки."
    "Она гораздо ниже остальных двух девушек."

    pod2 c1 "Нет-нет, ничего, просто..."
    pod1 1i "Нацуки, мы уже, как бы, в предвыпускном классе, и все остальные уже либо перешли на более серьёзные книжки, либо на худой конец просто отказались от манги."
    
    show himari 1k at t31
    show natsuki 1e at t32
    show elena j2 at t33

    $ TS.s(vpunch)

    n "Ну а я буду читать мангу всегда! Это моё хобби!"

    $ TS.s(vpunch)

    n 2h "Ты же не будешь осуждать меня за моё хобби?"

    show himari 1zd at s31
    show natsuki 1i at s32

    pod1 "Нет-нет, что ты..."
    pod1 1w "Просто..."
    pod1 "Тебе не кажется, что это как-то... по-детски?"

    $ TS.s(vpunch)

    n 4e "Нет, не кажется! Манга – это такая же литература, как и обычная художественная!"

    show himari 1v at t31
    show natsuki 4e at s32
    show elena i1 at t33

    pod2 "Нацуки, ну ты же сама сказала, что художественная литература и манга – это, ну, не совсем одно и то же..."
    
    show himari 1x at f31
    show elena b2 at f33
    
    pod1 "Она права, Нацуки. Манга – это такие же комиксы, как и обычные, только читаются справа налево."
    pod1 "И то, и другое можно назвать литературой лишь с {b}очень{/b} большой натяжкой."

    show himari 1zj at t31
    show natsuki 1o at t32
    show elena f1 at t33

    pod1 "Если её так вообще можно назвать..."
    
    show himari 1zj at f31
    show natsuki 1o at s32
    show elena f2 at f33

    "Какие же токсичные у неё друзья..."

    stop music fadeout 5

    n 2w "А {i}я{/i} говорю {i}вам{/i}, что манга – это литература, и только попробуйте убедить меня в обратном!"

    $ TS.s(vpunch)

    n "Но скажу сразу – у вас не получится!"

    show natsuki at cright with move
    hide natsuki

    show himari 1zi at t21
    show elena b2 at t22

    pod1 "Нацуки, подожди!"
    pod2 b "Да уже поздно... Ты видела, как она убежала? На таких-то коротеньких ножках набрать такую скорость – это надо постараться."
    
    show himari 1zzzh at h21
    show elena i at h22

    "Они обе засмеялись."
    "Хотя нет, не засмеялись. Заржали, как самые что ни на есть лошади."

    if _preferences.language == "english":
        $ pod1_name = "Horse"
        $ pod2_name = "Mare"
    else:
        $ pod1_name = "Лошадь"
        $ pod2_name = "Кобыла"

    play music ts_ylm

    "Не стерпев такого хамства, я подбегаю к ним."
    "Нужно {cps=24}{i}аккуратно{/i}{/cps} выяснить, куда же она побежала."
    "Такой шанс представляется один раз в жизни."
    
    m "Куда она побежала?"
    
    show himari 1zzm at f21
    show elena i at f22
    
    pod1 "Ой, здравствуй, Моника, как ваше ниче—{nw}"
    
    show himari 1y at t21
    show elena b2 at t22

    #$ TS.s(ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake))

    $ TS.s(vpunch)

    m "КУДА.{w=0.44} ОНА.{w=0.44} ПОБЕЖАЛА?"
    
    show himari 1v at s21
    show elena f2 at s22

    "Лошади хмыкнули."

    pod2 f2 "Да наверное, в туалетах прячется и рыдает, как обычно..."
    
    show himari at cright with move
    hide himari
    show elena at cright with move
    hide elena

    "Не сказав больше ни слова, я быстро направляюсь к туалетам."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_school_bathroom
    with wipeleft_scene

    $ TS.s(ts_showscreens)

    "..."
    "Нацуки там не оказалось."
    "Да что же у неё за подруги такие, которые даже не знают, куда она уходит, чтобы никому на глаза не попадаться?!"

    play sound door_break

    "Разочарованно захлопнув дверь, я пошла дальше."

    $ TS.s(ts_hidescreens)
    " {w=0.4}{nw}"

    play sound pageflip
    scene ts_corridor
    with wipeleft_scene

    $ TS.s(ts_showscreens)

    "Нет."

    $ TS.s(ts_hidescreens)
    " {w=0.4}{nw}"

    play sound pageflip
    scene ts_class
    with wipeleft_scene

    $ TS.s(ts_showscreens)

    "Нет."

    $ TS.s(ts_hidescreens)
    " {w=0.4}{nw}"

    play sound pageflip
    scene ts_stairs
    with wipeleft_scene

    $ TS.s(ts_showscreens)

    "И тут нет."

    $ TS.s(ts_hidescreens)
    " {w=0.4}{nw}"

    play sound pageflip
    scene ts_l5
    with wipeleft_scene

    $ TS.s(ts_showscreens)

    "Да где же она вообще есть?"
    "Уже и перемена скоро заканчивается..."

    $ TS.s(ts_hidescreens)
    " {w=0.5}{nw}"

    play sound pageflip
    scene ts_school_courtyard_day
    with wipeleft_scene

    $ TS.s(ts_showscreens)

    "Наконец, уже во дворе, мне наконец на глаза попалась Нацуки."
    "Она хоть и маленькая, но у неё волосы настолько яркого цвета, что не заметить её просто невозможно."

    stop music fadeout 3

    show natsuki 1s at t11

    "Кажется, её подруги упоминали, что она постоянно доказывает, что манга – это литература?"
    $ TS.m(ts_osmotr_tipa_center)
    "Да она сама как будто со страниц манги сошла!"
    "Нет, я, конечно, ни одну мангу за всю жизнь так и не прочла, но мне кажется, что примерно так персонажи в манге и выглядят."

    m "Нацуки!"
    n 1o "Ну что ещё?!"
    n 1t "А, ой..."
    n 2w "Я думала, это эти курицы снова меня собираются донимать."

    "Нет, курицами я бы их не назвала."
    "Зато вот кобылами – ещё как."
    "Подождите..."
    "Снова?"
    if persistent.cens_mode == True:
        "Да они что, совсем охуели?"
    else:
        "Да они что, совсем страх потеряли?"
    "Но вслух я говорю совсем другое."

    m "Нет, это... не они. Это я."
    m "Кстати, я Моника. Очень рада знакомству."

    play music ts_ybs

    n 1t "А, Моника... А я тебя знаю."
    n 2l "Ты же у нас вроде гордости школы?"

    show natsuki 1j at s11

    "Ну, может, школа мной и гордится, но я собой точно не горжусь..."

    m "Ну, что-то вроде того."
    m "Я к тебе с предложением."
    n 3c "С предложением? С каким?"

    show natsuki 1g at t11

    m "Ну, ты в разговоре со своими подругами упоминала, что ты постоянно доказываешь всем, что манга – это литература."
    n 2h "Так это и есть литература. Такая же, как и обычная художественная."
    n 1r "Просто эти балбесы великовозрастные никак этого не поймут."
    n 1k "Так что за предложение-то?"

    "Прямолинейность Нацуки поражает. Я даже теряюсь в словах, чтобы довести предложение до ума."

    show natsuki 1a at f11

    m "А-ха-ха... Ну, я, эм-м-м..."
    n 2e "Ну, рожай уже!"

    show natsuki 1g at t11

    "Да я бы с радостью! Мне просто уверенности не хватает, особенно под взором кого-то вроде Нацуки."
    "Собравшись с духом, я на одном дыхании выпалила."

    m "В общем, я недавно открыла Литературный клуб, нас там уже трое, если хочешь, тоже приходи{w=1.7}{nw}"

    "Фух."

    show overlay aw_memory_back_1 with dspr
    $ TS.m(VHS())

    #$ TS.s(ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake))

    "И куда только пропала вся моя уверенность и весь мой пафос?"
    "Куда делось «я хочу, чтобы в моём клубе не было слова 'неправильно'»?"
    "Куда делось «я хочу, чтобы в моём клубе каждый может выражаться, как его душе может быть угодно»?"
    "Наверное, для того, чтобы основать клуб, мало только одного желания, нужна ещё и пробивная сила."

    window hide
    play sound fb
    scene ts_school_courtyard_day
    show natsuki 1i at t11
    with flash

    $ TS.s(ts_showscreens)

    "Нацуки задумалась."

    n 2h "Литературный? Что-то никогда раньше о таком не слышала."

    show natsuki 1i at f11

    "..."
    "...я уже не удивляюсь..."

    m "Да. Литературный клуб."

    "Я не подаю виду, что нам отчаянно нужен четвёртый человек, чтобы клуб просто не расформировали."
    "Не говоря уже о том, что у двоих человек настолько серьёзные проблемы."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"


    show zatemnenie with dspr

    $ TS.s(ts_showscreens)

    show screen chp_text_14
    pause
    $ TS.s(ts_hidescreens)
    show screen chp_text_14
    $ TS.p(1)
    hide screen chp_text_14

    hide zatemnenie with dspr

    $ TS.s(ts_showscreens)

    "Я отгоняю дурные мысли из головы."
    "Ну же, Моника, будь увереннее в себе!"

    m "Да, так во-о-от..."

    show natsuki 1za at t11

    m "Я устала от этих интрижек крупных клубов, и мне хотелось сделать что-нибудь для души."

    "Вот, начало положено!"

    m "И я хочу, чтобы в моём клубе не было слова «неправильно»."
    m "И чтобы в моём клубе каждый мог выражаться, как его душе может быть угодно..."

    "По протоптанной тропинке..."

    m "Вот я, например, читаю классику."

    "По крайней мере, {i}читала раньше{/i}..."

    m "Ещё одной девочке нравятся ужастики."
    n 2x "Бр-р-р... ненавижу ужастики..."
    m "А может, кто-то не любит мангу?"

    show natsuki 3t at f11

    n "Ну-у-у... допустим..."

    show natsuki 1u at t11

    m "Я и говорю, что стили могут быть очень разные, но это всё равно стили."
    m "Стили {b}литературы{/b}."

    show natsuki 1l at h11

    "Услышав заветные слова, Нацуки заметно повеселела."

    n "Значит, ты тоже считаешь, что манга – это литература?"

    show natsuki 1j at f11

    "Нет, {i}такого{/i} я не говорила. Но чтобы Нацуки стало легче на душе, я решаю... приврать немного. Как будто в первый раз."

    m "Э-э-э... да."

    play sound zvonok

    show natsuki 2p at t11

    n "Чёрт, мы опаздываем!"
    n 1l "В общем, скажи остальным, что я там буду!"

    show natsuki at cright with move
    hide natsuki

    m "Подожди!.."
    m "Я же... не сказала тебе, когда и куда подходить..."

    stop music fadeout 5

    "Но эта фраза прозвенела уже вне ушей Нацуки."
    "Что же, половина дела сделана. Четвёртый человек прибыл."
    "Ну-у-у, или по крайней мере, пообещал, что он будет..."
    "Но я как будто нутром чувствую, что эта розоволосая девочка не обманет."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_class
    with wipeleft_scene

    play music ts_mdl

    $ TS.s(ts_showscreens)

    "Учебный день близится к его логическому завершению."
    "После самого тяжкого – химии и биологии – остальная часть дня прошла гораздо быстрее."
    "Я собираю все вещи и направляюсь в клуб."

    stop music fadeout 3

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_corridor
    with wipeleft_scene

    $ TS.s(ts_showscreens)

    "Только я вышла из класса, как меня кто-то позвал."

    play music okevrnat

    n "Моника! Подожди!"

    show natsuki 2v at ln11

    n 2t "Фух, успела..."

    show natsuki 1j at f11

    m "Привет ещё раз, Нацуки."
    n 1k "Ты же мне так и не сказала, когда и куда приходить, поэтому я подождала у кабинета."

    show natsuki 1j at t11

    m "Да, не сказала..."
    m "Я как раз беспокоилась о том, что ты же не знаешь, где находится наш клуб."

    show natsuki 2l at f11

    stop music fadeout 5

    m "Что же, раз уж ты пришла, то просто пойдём со мной."
    m "А на будущее – мы собираемся каждый день вот в {i}этом{/i} кабинете."

    "Я указываю на дверь клуба."

    n "Здорово!"

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound door_open
    $ TS.m(ts_club_vhod)
    $ TS.p(1.2)
    scene ts_club at ts_bg_exodus
    $ TS.p(0.5)

    play music ts_mdl

    $ TS.s(ts_showscreens)

    "Когда мы входим в клуб, я вижу, что мы здесь первые."
    "Странно... Если в случае с Сайори это оправданно, потому что она всегда немного опаздывает, то в случае с Юри..."
    "Она же такая пунктуальная..."

    window hide
    play sound fb
    scene ts_school_bathroom
    show yuri 9p at t11
    show zatemnenie_light
    show overlay aw_memory_back_1
    $ TS.m(VHS())
    with flash

    $ TS.s(ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake))

    "Меня напугала её мания навредить себе."
    "Юри тогда сказала, что это потому что она чувствует себя ничтожеством, и внутренний голос твердил ей перейти от слов к делу."
    "Не знаю, насколько правдивы были её слова в пятницу, но..."
    "Порезы на ней выглядели вполне реальными. Да и сама она... тоже вполне реальной была."
    "Или это всё горяченный бред, и на самом деле никакой Юри и не было?"
    "Что же... Об этом я узн{b}а{/b}ю уже в клубе."

    play music ts_orchid


    play sound fb
    window hide
    scene ts_club
    show natsuki 1n at t11
    with flash

    "О, господи..."
    m "Н-Нацуки, я на минутку!"
    n 1m "Х-хорошо..."

    window hide
    play sound door_break
    scene ts_corridor at ts_razebal
    $ TS.p(0.3)
    scene ts_corridor at ts_beg
    $ TS.p(1)
    play sound door_break
    scene ts_school_bathroom at ts_razebal
    $ TS.p(0.3)

    "С каждым днём знать о всех бедах девочек становится всё труднее."
    "Лишь проверив каждую кабинку, мне стало хоть немного, но легче..."
    "..."
    "Хотя нет, ничерта мне легче не стало! У нас что, один туалет на всю школу?!"


    menu:
        "Искать дальше":
            $ unluck2 = True
            $ unluck_ball += 1
        "Успокоиться и вернуться":
            pass


    if unluck2 == True:

        #$ TS.s(ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake))
    
        $ TS.s(ts_showscreens)

        "Я решаю искать дальше."

        $ TS.s(ts_hidescreens)
        " {w=0.4}{nw}"

        play sound pageflip
        scene ts_corridor
        with wipeleft_scene

        $ TS.s(ts_showscreens)

        "У нас же много туалетов, Юри {b}должна быть{/b} в одном из них!"

        $ TS.s(ts_hidescreens)
        " {w=0.4}{nw}"

        play sound pageflip
        scene ts_school_bathroom1
        with wipeleft_scene

        $ TS.s(ts_showscreens)

        "Юри и в этом туалете нет."
        "Да где же она есть?"

        $ TS.s(ts_hidescreens)
        " {w=0.4}{nw}"

        play sound pageflip
        scene ts_corridor
        with wipeleft_scene

        play sound pageflip
        scene ts_school_bathroom2
        with wipeleft_scene

        $ TS.s(ts_showscreens)

        "Я уже теряю всякую надежду."

        stop music fadeout 3

        $ TS.s(ts_hidescreens)
        " {w=0.4}{nw}"

        play sound pageflip
        scene ts_corridor
        with wipeleft_scene

    
        $ TS.s(ts_showscreens)

        "Обойдя четыре школьных туалета и не найдя Юри ни в одном из них, я всё же решаю идти обратно в клуб."
        "Да я же параноиком становлюсь!"

        $ TS.s(ts_hidescreens)
        " {w=0.4}{nw}"

        play sound pageflip
        scene ts_club
        show yuri 1i at t31
        show natsuki 1i at t32
        show sayori 2b at t33
        with wipeleft_scene

        play music audio.t3

        $ TS.s(ts_showscreens)

        "А когда я вошла в клуб, я вижу, как все остальные девочки просто сидят, как ни в чём ни бывало!"
        "Вот те на..."

        y 2t "Моника, добрый день. А где ты была?"
        m "Где-где... Тебя искала, где же ещё!"
        y 3q "М-меня?.. Так вот же я..."

        show yuri 1o at s31

        m "Да я!.."

        "Нет, рассказывать всему клубу о том, что Юри режется, лучше не стоит."
        show sayori 2u at f33
        "Это, в свою очередь, негативно скажется на депрессии Сайори."
        "И кто знает, какие ещё проблемы есть у Нацуки..."
        "Ну то есть, я видела, как её унижают друзья, но не думаю, что это единственное, о чём мне стоит волноваться."

        show yuri 1q at t31

        m "Ладно, неважно..."
    else:

        stop music fadeout 5

    
        $ TS.s(ts_showscreens)

        "Хотя, а с другой стороны, у нас же далеко не один туалет на всю школу..."
        "Их же много, гораздо больше, чем я смогу посетить одна..."
        "А я просто параноик, который не справляется с обязанностями держать секреты девочек, ну, в секрете."
        m "Хи-хи, ха-ха, я не сумасшедшая, я не сумасшедшая, всё нормально, всё в порядке..."
        "Успокоившись, я выхожу из туалета и направляюсь обратно в клуб."

        $ TS.s(ts_hidescreens)
        " {w=1.0}{nw}"

        play sound pageflip
        scene ts_club
        show yuri 1i at t31
        show natsuki 1l at t32
        show sayori 2x at t33
        with wipeleft_scene

        play music audio.t3
    
        $ TS.s(ts_showscreens)

        "А когда я прихожу обратно в клуб, я вижу, как остальные девочки щебечут, как ни в чём ни бывало."
        "Вернее, щебечут Сайори и Нацуки, Юри же просто внимательно слушает."

        y 2q "М-Моника, добрый день. А где ты была?"
        m "Где-где..."
        "..."
        m "Ладно, неважно..."

    show yuri 1e at t31
    show natsuki 1j at t32
    show sayori 1b at t33

    "Я прочищаю горло, чтобы все обратили на меня внимание."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"


    show zatemnenie with dspr

    $ TS.s(ts_showscreens)

    show screen chp_text_16
    pause
    $ TS.s(ts_hidescreens)
    show screen chp_text_16
    $ TS.p(1)
    hide screen chp_text_16

    hide zatemnenie with dspr

    $ TS.s(ts_showscreens)


    m "Итак, ребята!"
    m "Как вы уже успели понять, сегодня к нам присоединился новый участник."
    m "Её зовут...{nw}"
    s 2x "Нацуки. Мы уже пообщались."

    if unluck2 == True:
        n 3h "Да, пока ты где-то шлялась, мы уже обо всём поговорили."

    s 2m "Ах да, совсем забыла! "
    extend 5c "Моника, так нечестно! Это я должна была привести её в клуб!"

    show yuri 1c at f31
    show natsuki 1j at f32
    show sayori 5c at f33

    m "Ну, не всё же тебе отдуваться за мой клуб, нужно и мне как {b}президенту{/b} как-то посодействовать."

    stop music fadeout 3

    show yuri 1d at t31
    show natsuki 1z at t32
    show sayori 5d at t33

    "Все смеются. Сайори же просто смешно дуется."

    show sayori 2s at f33

    "Однако спустя несколько секунд Сайори присоединяется к общему смеху."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_club
    show yuri 1e at t31
    show natsuki 1j at t32
    show sayori 1b at t33
    with wipeleft_scene

    play music ts_mdl

    $ TS.s(ts_showscreens)

    "Наконец, смех прекращается, а я тем временем продолжаю."

    m "Так вот. Новый участник, зовут её Нацуки, и это означает, что нас наконец-то четверо."
    m "Что, в свою очередь, означает, что теперь мы официально зарегистрируем наш клуб."

    if _preferences.language == "english":
        $ m_name = "Everyone"
    else:
        $ m_name = "Все вместе"

    show yuri 3d at h31
    show natsuki 3z at h32
    show sayori 4r at h33

    m "Ура-а-а!"

    if _preferences.language == "english":
        $ m_name = "Monika"
    else:
        $ m_name = "Моника"

    m "Администратор клубов приходит смотреть на новые клубы каждый понедельник, и, думаю, наличие четырёх человек в клубе ему будет достаточно."
    n 2l "Я по такому случаю даже кексиков перед выходными напеку!"

    show natsuki 3j at f32

    s 3n "Нацуки, ты ещё и готовишь?"
    s 3r "Это же просто замечательно!"

    show sayori 3q at s33

    y 1m "А я, в свою очередь, принесу свой чайный сервиз и любимый чай."
    y 2q "Н-надеюсь, это можно?"
    m "Конечно, можно! Нужно только разрешения спросить."
    y 3zi "Т-тогда замечательно!"

    show yuri 3s at d31

    stop music fadeout 3

    s 2o "Кексики... Чай..."
    s 4r "Да у нас же лучший клуб на свете!"
    m "А-ха-ха, ну... а чего ты ещё ожидала?"

    show yuri 1d at t31
    show natsuki 1z at t32
    show sayori 2s at t33

    "Мы все снова дружно заливаемся смехом."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_club
    show yuri 1c at t31
    show natsuki 1j at t32
    show sayori 2b at t33
    with wipeleft_scene

    play music audio.t2

    $ TS.s(ts_showscreens)

    "Когда пришёл администратор клубов, я с порога гордо заявила, что нас наконец-то четверо, поэтому можно смело регистрировать клуб."
    "Администратор же ответил, что, помимо президента, в клубе должен быть ещё как минимум и вице-президент, на случай, если президент заболел, или что похуже."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    $ TS.s(ts_showscreens)

    "Выбирать особо не было из кого."

    show yuri 3o at f31

    "Я в первую очередь подумывала сделать вице-президентом Юри: она умная, красивая, начитанная, мастер книжного дела..."

    show yuri 4c at t31

    "Но затем..."

    show sayori 2n at f33

    "Затем передумала и всё-таки сделала вице-президентом Сайори."
    "Что тоже не лишено смысла."

    show sayori 2s at t33

    stop music fadeout 4

    "Во-первых, она пришла в клуб первой."
    "Во-вторых, если бы не она, я бы так и не узнала Юри, которую и думала первоначально сделать вице-президентом..."
    "Так что решение пришло само собой."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_club
    show yuri 1a at t31
    show natsuki 1j at t32
    show sayori 1a at t33
    with wipeleft_scene

    play music audio.t3

    $ TS.s(ts_showscreens)

    "Пока я заполняла все бумаги, чтобы официально открыть клуб, собрание уже почти подошло к концу."

    s 2p "Как же это всё долго и нудно!"
    m "А ты что хотела, открыть клуб – это на самом деле очень долгий с точки зрения бюрократии процесс."

    show sayori 2o at f33

    stop music fadeout 3

    m "Так, вот тут подпись поставить... Уже поставила, можно считать клуб открытым для всех желающих!"
    s 2x "Хорошо!"

    show sayori 2q at t33

    play music ts_ftp

    "Когда Сайори тоже подписалась, я чувствую некоторое волнение."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    scene black with ed_night_dis

    $ TS.s(ts_showscreens)

    "Справлюсь ли я со своим собственным клубом?"
    "Теперь уже официально открытым."
    "И как раз вовремя. До фестиваля осталось ровно две недели."
    "Но что, если после фестиваля к нам опять завалятся ученики? Неужели я просто снова уйду, как и все прошлые разы до этого?"
    "Ну уж нет!.."
    "Литература – это моё призвание, моя страсть. И я ни за какие коврижки не променяю литературу и этот клуб на что-либо ещё."
    "..."

    play sound wakeup
    stop music
    $ TS.p(1.5)
    scene ts_club
    show sayori 2q at t33
    with vpunch

    $ TS.s(ts_showscreens)

    s 2l "М-Моника?.. Ты уже несколько минут пялишься в одну точку и даже не двигаешься..."
    m "Ой... Прости..."

    play music audio.t3

    show yuri 1a at t31
    show natsuki 1j at t32
    show sayori 1a at t33

    m "Итак, ребята!"
    m "Пусть Юри даст вам домашнее задание, и на этом можем расходиться."

    show yuri 3n at f31

    y "Я?! О-опять?!"
    y 2o "У-у-у..."
    s 2e "Ну, ты же самая начитанная из всех нас..."
    show sayori 2d at f33
    y "Н-не говори так..."

    show yuri 1k at t31

    "Собравшись с духом, Юри продолжила."

    y 1h "Что же, поскольку у нас сегодня новый участник клуба, лучше почитать что-то нейтральное."
    y "«Душа Императора» всех устроит? Она небольшая, относительно простая, "
    extend 1y6 "и в ней нет никаких ужасов."

    "Последнюю часть про ужасы Юри сказала, косясь на Нацуки."

    if unluck2 == True:
        "По всей видимости, пока, как выразилась Нацуки, я шлялась, она открыто заявила, что ужастики не любит."
    else:
        "По всей видимости, пока меня не было, она открыто заявила, что ужастики не любит."

    show yuri 1l at f31

    "«Душа Императора»... Не думаю, что читала её когда-либо..."

    show natsuki 1n at f32
    show sayori 2o at t33

    "И, судя по лицам остальных девочек, они её тоже вряд ли читали."
    "Но, если Юри говорит, что она небольшая, то она таковой и является."
    "Юри обычно не врёт, особенно если дело касается её любимого занятия – книжек и чтения."

    m "Что же... всем задание ясно?"

    show sayori 1k at f33

    "Все угрюмо закивали."

    m "Тогда, на сегодня собрание клуба официально окончено! Всем спасибо, все свободны!"

    show sayori 1k at cright with move
    hide sayori
    show yuri 1l at cright with move
    hide yuri

    show natsuki 1m at t11
    stop music fadeout 2
    "Сайори и Юри уходят, оставив меня один на один с Нацуки."
    play music ts_conf fadein 1

    n "Моника... Можно тебя попросить об одном одолжении?"
    m "Да, конечно. О каком именно?"
    n 1t "Я видела, в вашем клубе отдельная кладовая есть..."
    n 1m "В общем, можно я ею попользуюсь, чтобы хранить свою мангу?"
    n 2m "Там немного, я займу не больше пары полочек..."
    n 3q "Просто... папа..."

    "Такое ощущение, что после этого предложения она пустится навзрыд."
    "Но оказалось, что Нацуки сильнее этого, поэтому пока держится ровно, хотя в голосе уже слышатся резкие нотки, как будто она заплачет в любую секунду."
    "Я не отвечаю ничего. Нацуки тем временем продолжает бороться с желанием плакать, как маленькая девочка."

    n 12c "Папа считает, что я уже слишком взрослая для чтения манги."
    n "Папа говорит, что манга – это так по-детски и по-глупому."
    n 12i "А я не ребёнок! И уж тем более не глупая!"

    "Наконец, на глазах Нацуки выступили слёзы."

    n "Я взрослый человек, и буду читать, что хочу, и никто мне не указ!"
    n "Хочу – буду читать мангу. Хочу – не буду читать мангу. Я вправе делать что угодно!"
    n 12f "Но... Папа считает, что я, хоть и уже слишком взрослая для чтения манги... ещё недостаточно взрослая и самостоятельная, чтобы самой вправе что-то решать."
    n 12c "И ведь с ним не поспоришь даже! Он же папа, он же взрослый, умный, а я что?"
    n 12f "Всего лишь маленькая девочка..."

    stop music fadeout 5

    "С каждым новым предложением слова Нацуки ранят меня в самое сердце."

    show natsuki 1n at s11

    m "Хватит. Я услышала достаточно."

    show natsuki at cright with move
    hide natsuki

    play music ts_dist 

    play sound fb
    window hide
    scene ts_club
    show overlay aw_memory_back_1
    with flash

    show zatemnenie with dspr

    $ TS.s(ts_showscreens)

    show screen chp_text_1
    pause
    $ TS.s(ts_hidescreens)
    $ TS.p(1)
    hide screen chp_text_1
    $ TS.s(ts_showscreens)
    show screen chp_text_2
    pause
    $ TS.s(ts_hidescreens)
    $ TS.p(1)
    hide screen chp_text_2
    $ TS.s(ts_showscreens)
    show screen chp_text_3
    pause
    $ TS.s(ts_hidescreens)
    $ TS.p(1)
    hide screen chp_text_3
    $ TS.s(ts_showscreens)
    show screen chp_text_4
    pause
    $ TS.s(ts_hidescreens)
    $ TS.p(1)
    hide screen chp_text_4

    hide zatemnenie with dspr

    show sayori 1q at t31:
        alpha 0.5
    with linearblurbolee

    $ TS.s(ts_showscreens)

    "Сайори..."

    show sayori 1w at t31:
        alpha 0.5

    "И её психическое расстройство..."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    show zatemnenie with dspr
    $ TS.s(ts_showscreens)
    show screen chp_text_5
    pause
    $ TS.s(ts_hidescreens)
    $ TS.p(1)
    hide screen chp_text_5
    hide zatemnenie with dspr

    show yuri 1c at t32:
        alpha 0.5
    with linearblurbolee

    $ TS.s(ts_showscreens)

    "Юри..."

    show yuri 9zh at t32:
        alpha 0.5

    "Её самовред и отсутствие друзей..."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    show zatemnenie with dspr
    $ TS.s(ts_showscreens)
    show screen chp_text_5
    pause
    $ TS.s(ts_hidescreens)
    $ TS.p(1)
    hide screen chp_text_5
    hide zatemnenie with dspr

    show natsuki 1z at t33:
        alpha 0.5
    with linearblurbolee

    $ TS.s(ts_showscreens)

    "Нацуки..."

    show natsuki 12f at t33:
        alpha 0.5

    "И её проблемы с друзьями, и особенно с отцом..."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    show zatemnenie with dspr
    $ TS.s(ts_showscreens)
    show screen chp_text_5
    pause
    $ TS.s(ts_hidescreens)
    $ TS.p(1)
    hide screen chp_text_5
    hide zatemnenie with dspr

    stop music fadeout 3

    if persistent.cens_mode == True:
        show zatemnenie with dspr
        $ TS.s(ts_showscreens)
        show screen chp_text_6
        pause
        $ TS.s(ts_hidescreens)
        $ TS.p(1)
        hide screen chp_text_6
        hide zatemnenie with dspr
    else:
        show zatemnenie with dspr
        $ TS.s(ts_showscreens)
        show screen chp_text_7
        pause
        $ TS.s(ts_hidescreens)
        $ TS.p(1)
        hide screen chp_text_7
        hide zatemnenie with dspr

    window hide
    play sound fb
    scene ts_club
    show natsuki 1m at t11
    with flash

    $ TS.s(ts_showscreens)

    n "Моника? Ты отключилась..."
    m "А, что? Д-да..."

    play music okevrnat

    m "Забирай хоть всю кладовку, ею всё равно никто не пользуется..."
    n 2l "Правда? Спасибо тебе огромное, Моника, ты настоящий друг!"

    show natsuki 2j at f11

    m "Да... не за что..."
    m "Слушай, что-то я устала, пойдём домой уже?"
    n 1l "Да-да, конечно!"

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_corridor
    show natsuki 2k at t11
    with wipeleft_scene

    play sound pageflip
    scene ts_stairs
    show natsuki 2k at t11
    with wipeleft_scene

    $ persistent.sprite_time = "day"

    play sound pageflip
    scene ts_l5
    show natsuki 2k at t11
    with wipeleft_scene

    $ persistent.sprite_time = "sunset"

    play sound pageflip
    scene ts_school_gate_evening
    show natsuki 2k at t11
    with wipeleft_scene

    $ TS.s(ts_showscreens)

    n "Ты где живёшь?"
    m "Во-о-он там."

    "Я показываю вправо."

    n "Значит, мне в другую сторону."
    n 2l "До завтра, Моника! И спасибо ещё раз за приглашение!"

    show natsuki 2j at f11

    stop music fadeout 3

    m "Да, всегда пожалуйста..."

    show natsuki 2j at cright with move
    hide natsuki

    "На этом наши пути разошлись."
    $ persistent.sprite_time = "sunset"
    "Как же я устала..."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_house_monika_evening
    with wipeleft_scene

    play music ts_dreams

    $ TS.s(ts_showscreens)

    $ persistent.sprite_time = "day"

    "Я так сильно запуталась в мыслях, что сама не поняла, как дошла до дома."
    "Мышечная память?"
    "И пока я дошла до дома, уже и почти стемнело."
    "Оно и понятно, к концу октября где-то в шесть вечера уже темнеет, если ещё не стемнело полностью."
    "А с учётом того, сколько времени заняло оформление всех бумаг с «разговором по душам» с Нацуки, всё становится на свои места."
    "Свет не горел нигде."
    "Должно быть, папа ещё не вернулся."
    "Папа..."

    window hide
    play sound fb
    scene ts_club
    show natsuki 12f at t11
    show overlay aw_memory_back_1
    $ TS.m(VHS())
    with flash

    $ TS.s(ts_showscreens)

    "Мысли о Нацуки не дают мне покоя."
    "Её отец считает, что она уже слишком взрослая для чтения манги."
    "Я же считаю, что, хотя сама я ни одной манги не прочла, ей все возрасты покорны."
    "Неважно, сколько тебе лет, ты вправе читать всё, что тебе в голову взбрендит..."
    "..."
    "Нет, это неправильно... Звучит так, как будто я и сама не особо одобряю мангу."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"


    show zatemnenie with dspr

    $ TS.s(ts_showscreens)

    show screen scenario_3_onest_text_suka
    pause
    $ TS.s(ts_hidescreens)
    show screen scenario_3_onest_text_suka
    $ TS.p(1)
    hide screen scenario_3_onest_text_suka

    hide zatemnenie with dspr

    $ TS.s(ts_showscreens)

    "Мне по душе классические книги, где есть много слов и мало картинок, а не наоборот."

    stop music fadeout 3

    "Но это я сужу как Моника. А как президент Литературного клуба я сужу совсем иначе."
    "Тяжело..."


    window hide
    play sound fb
    scene ts_house_monika_evening
    with flash

    play sound2 door_open
    scene ts_vhod_nolight
    with pushleft

    $ TS.p(0.5)

    play sound svet_on

    scene ts_vhod_night
    with flash

    scene ts_kitchen
    with wipeleft_scene

    play music audio.t2

    $ TS.s(ts_showscreens)

    "Действительно, папы нет дома."
    "Видимо, снова задерживается на работе."
    "...нет, я не могу так думать."
    "Это просто моя паранойя, хи-хи-хи, ха-ха-ха, на самом деле я совершенно здорова и адекватна..."

    stop music fadeout 3

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"


    show zatemnenie with dspr

    $ TS.s(ts_showscreens)

    show screen chp_text_18
    pause
    $ TS.s(ts_hidescreens)
    show screen chp_text_18
    $ TS.p(1)
    hide screen chp_text_18

    hide zatemnenie with dspr

    $ TS.s(ts_showscreens)

    "Отбросив от себя все негативные мысли, я думаю о том, что папа хотел бы на ужин, но и чтобы я тоже покушала."
    $ TS.m(ts_havchik_search)
    "Та-а-ак, посмотрим..."

    play music audio.t4

    "На выбор есть картошка, рис, яйца и какая-то бакалея."
    "Рис мы только недавно ели, яичницу папа ел на завтрак, бакалея просто не подходит в качестве полноценного ужина."
    "Так что... на ужин у нас картошка."
    "Правда, есть один нюанс, что её нужно почистить, но на один раз на два человека чистить нужно не особо много."
    $ TS.m(ts_havchik_search_end)

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound2 pageflip
    scene ts_kitchen
    with wipeleft_scene

    $ TS.s(ts_showscreens)

    "Спустя несколько минут шесть картофелин почищено и помыто."
    "Теперь вопрос века: пожарить ли мне или просто сварить?"

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"



    $ TS.s(ts_null_transform)

    menu:
        "Пожарить":
            $ unluck3 = True
            $ unluck_ball += 1
        "Сварить":
            pass



    $ TS.s(ts_showscreens)

    if unluck3 == True:
        "Я решаю пожарить картошку. Так будет быстрее."
        "Разрезав эти жалкие шесть картофелин на ломтики и подлив немного масла, я начинаю готовить кушанье."
        "..."
        "А хотя нет... не начинаю..."

        $ TS.s(vpunch)

        if persistent.cens_mode == True:
            m "ДА ГДЕ ЖЕ ЭТА БЛЯДСКАЯ СКОВОРОДКА?"
        else:
            m "ДА ГДЕ ЖЕ ЭТА ЧЁРТОВА СКОВОРОДКА?"

        $ TS.s(ts_hidescreens)
        " {w=1.0}{nw}"

        play sound2 pageflip
        scene ts_kitchen
        with wipeleft_scene

        play sound2 pageflip
        scene ts_gost
        with wipeleft_scene

        play sound2 pageflip
        scene ts_bedroom
        with wipeleft_scene

        play sound2 pageflip
        scene ts_living_room_late
        with wipeleft_scene

        play sound2 pageflip
        scene ts_kitchen
        with wipeleft_scene

        $ TS.s(ts_showscreens)

        "Потратив добрые десять минут на поиски этой сковородки, я в итоге её нашла."
        "Жарка и то займёт меньше, чем поиски."
        "Вот теперь я точно начинаю готовить кушанье."
        $ TS.m(ts_havchik_gotovka)
        play ambience zharim_sashlik fadein 2
        "Я старательно размешиваю импровизированный ужин, а затем сажусь немного отдохнуть."

        stop ambience fadeout 4
        stop music fadeout 4

        $ TS.s(ts_hidescreens)
        " {w=1.0}{nw}"

        play sound2 pageflip
        scene ts_living_room_late
        with wipeleft_scene

        $ TS.s(ts_showscreens)

        m "{b}КА-А-А-АК{/b} ЖЕ Я УСТА-А-А-АЛА!" with hpunch

        $ TS.s(ts_hidescreens)
        " {w=1.0}{nw}"

        play sound2 pageflip
        scene ts_living_room_late
        with wipeleft_scene

        $ TS.s(ts_showscreens)

        "Прошло уже... достаточно много времени, чтобы я заметила что-то странное."

        play music ts_ap

        "Пахнет чем-то... горелым..."

        $ TS.s(vpunch)

        m "ЧЁРТ, КАРТОШКА!"

        $ TS.s(ts_hidescreens)
        " {w=1.0}{nw}"

        play sound2 pageflip
        scene ts_kitchen
        with wipeleft_scene

        $ TS.m(ts_havchik_gotovka)

        $ TS.s(ts_showscreens)

        "Однако вместо картошки от неё остались одни только угольки."
        if unluck2 == True:
            "Господи, какой же неудачный день!"
            if unluck == True:
                "Или это неудачная я?"

                $ TS.s(ts_hidescreens)
                " {w=1.0}{nw}"


                show zatemnenie with dspr

                $ TS.s(ts_showscreens)

                show screen chp_text_19
                pause
                $ TS.s(ts_hidescreens)
                show screen chp_text_19
                $ TS.p(1)
                hide screen chp_text_19

                hide zatemnenie with dspr

                $ TS.s(ts_showscreens)

        stop music fadeout 7

        $ TS.m(ts_havchik_gotovka_end)

        "Так или иначе, от ужина ничего не осталось."
        "Разочарованно вздохнув, я просто стала дожидаться папу, чтобы что-то приготовил уже он."
        "А я ведь с утра ничего не ела..."

        play sound stomach_growl

        "Живот урчит не хуже, чем у кита."

        $ TS.s(ts_hidescreens)
        " {w=1.0}{nw}"

        $ TS.p(2)

    else:
        $ TS.m(ts_havchik_gotovka)
        "Я решаю сварить картошку. Это хоть и чуть дольше, но зато более безопасно."
        play ambience water_pizdec_kakaya_goryachaya fadein 2
        "Разрезав эти жалкие шесть картофелин на кубики, чтобы они быстрее сварились, я начинаю куховарить."
        "Вариться картошка будет всё равно дольше, чем жариться, так что я решаю немного вздремнуть."
        stop ambience fadeout 2
        $ TS.s(ts_hidescreens)
        " {w=1.0}{nw}"

        play sound2 pageflip
        scene ts_living_room_late
        with wipeleft_scene

        $ TS.s(ts_showscreens)

        m "{b}КА-А-А-АК{/b} ЖЕ Я УСТА-А-А-АЛА!" with hpunch

        $ TS.s(ts_hidescreens)
        " {w=1.0}{nw}"

        scene ts_living_room_late_night
        with dissolve2

        $ TS.s(ts_showscreens)

        "Прошло уже... достаточно много времени."

        $ TS.s(vpunch)

        m "ЧЁРТ, КАРТОШКА!"

        $ TS.s(ts_hidescreens)
        " {w=1.0}{nw}"

        play sound2 pageflip
        scene ts_kitchen
        with wipeleft_scene

        play ambience water_pizdec_kakaya_goryachaya fadein 2

        $ TS.m(ts_havchik_gotovka)

        $ TS.s(ts_showscreens)

        stop music fadeout 7

        "Слава Богу, картошка ещё не сварилась."
        "Как раз закипела, как раз приобрела достаточно мягкую консистенцию, чтобы её нельзя было называть сырой."
        "И поскольку гарнир уже, по сути, готов, теперь нужно будет придумать что-то для разнообразия, чтобы это можно было называть полноценным ужином."
        "Лёгкий овощной салатик из огурчиков и помидорчиков вполне для этого подойдёт."

        stop ambience fadeout 3

        $ TS.s(ts_hidescreens)
        " {w=1.0}{nw}"

        play sound2 pageflip
        scene ts_kitchen
        with wipeleft_scene

    play music ts_tor fadein 2

    $ TS.s(ts_showscreens)

    "..."
    "Папы всё нет и нет."
    "Я уже начинаю переживать."

    if unluck3 == True:
        "И больше всего переживает мой желудок."
        "После неудачной затеи с жареной картошкой мой перекус состоял разве что из пары огурцов."
        "Всё ещё лучше, чем ничего, но этого всё равно мало."
    else:
        "Я хоть и поела, но после ужина меня только больше разморило, даже несмотря на то, что я только недавно дремала."

    "Когда он вообще придёт?"
    "От нечего делать, я решаю ещё раз подремать, но уже нормально, в своей постели."
    "Часика должно быть достаточно..."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound2 pageflip
    scene black
    with wipeleft_scene

    $ TS.p(1)

    scene ts_darkbed
    show unblink

    $ TS.m(ts_vstavai_shashlik1)
    $ TS.p(3)

    $ TS.s(ts_showscreens)

    "Ох..."
    "Похоже, плохой идеей было не заводить будильник..."
    "Который сейчас час вообще?"
    "..."
    "Часы показывают, что спала я от силы минут сорок."
    "Видимо, я не только устала, но ещё и настолько на нервах, что даже заснуть нормально не могу."
    "А с учётом такого вечернего сна, да ещё и такого рваного, уснуть в привычное для себя время уже не получится."

    stop music fadeout 4

    "Впрочем, что плохого может случиться с одного раза?"
    "И на этой ноте самовнушения я спускаюсь на кухню."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound2 pageflip
    scene ts_kitchen
    with wipeleft_scene

    $ TS.s(ts_showscreens)

    "И как раз в этот момент домой наконец-то приходит папа."

    play music audio.t2

    show hiroto 2b at ln11

    ts_ft "Я дома!"
    m "Привет, пап!"
    ts_ft 2g "Ну здравствуй, дорогуша."

    show hiroto 1f at s11

    m "Что-то ты сегодня совсем поздно."
    ts_ft 1y "На работе задержался очень сильно."
    ts_ft 1v "Только я закончил рабочий день, только я завёл машину..."
    ts_ft 1q "А она не заводится, ты представляешь?"
    ts_ft 2q "В итоге, пока я позвонил своему знакомому, пока он доехал, пока мы дотянули машину до дома..."
    ts_ft 1h "В общем, всё это время, драгоценное время..."
    ts_ft "В итоге домой я пришёл не ближе к шести, а только сейчас."

    show hiroto 1j at t11

    "Всё оказалось гораздо прозаичнее, чем я ожидала."

    if unluck2 or unluck3 == True:
        "Да и, по крайней мере, не одной мне сегодня не везёт."

    ts_ft 2g "Ладно, не будем о плохом."
    ts_ft 2b "Я проголодался, просто умираю с голоду!"

    if unluck3 == True:
        "Не ты один..."

    ts_ft "Моника, что у нас на ужин?"

    if unluck3 == True:

        show hiroto 1d at f11

        m "Э-э-э... на ужин у нас чай..."
        ts_ft "И с чем?"
        m "С ложкой..."
        ts_ft 2a1 "Ты ничего не приготовила?"
        m "Я пыталась приготовить ужин, я пыталась пожарить картошку..."
        m "А когда я всего на минутку отошла, вся картошка превратилась в угольки..."
        ts_ft 1b1 "Божечки..."
        ts_ft 2h "Так ты же ничего не ела весь день!"

        ts_ft 2h "Так, ну-ка давай, быстренько пожарю нам яичницу. Лучше, чем ничего!"

        show hiroto 1p at t11

        m "Да я огурчиков поела, а потом я что-то вздремнула..."
        ts_ft 2q "И сколько же каллорий в твоих огурцах? Как кот наплакал!"

        "Ну-у-у, я бы не сказала... Но спорить с папой не хотелось, особенно сегодня."
        "У меня ведь на сегодня были припасены хорошие новости. Но если мы продолжим спорить, то хорошие новости просто утонут в негативе спора."
        "Так что я лишь молча киваю и жду яичницу."

        show hiroto 2q at cright with move
        hide hiroto

        play ambience zharim_sashlik fadein 2

        ts_ft "Моника, тебе сколько яиц разбивать?"
        m "Трёх яиц хватит."

        "Папа молча кивает и отсчитывает ровно семь яиц."

        stop ambience fadeout 3

        $ TS.s(ts_hidescreens)
        " {w=1.0}{nw}"

        play sound2 pageflip
        scene ts_kitchen
        with wipeleft_scene

        $ TS.s(ts_showscreens)

        "Пять минут спустя готовая яичница, расставленная на двух тарелках, уже дожидается нас на столе."

        show hiroto 1c at t11

        ts_ft "Ты с чем яичницу будешь?"
        m "Да мне и просто яиц хватило бы. Но раз уж ты настаиваешь, то я буду с овощами."
        ts_ft 1y "Как скажешь. Я, наверное, тоже с салатиком буду. Порежешь?"
        m "Конечно."

        $ TS.s(ts_hidescreens)
        " {w=1.0}{nw}"

        play sound2 pageflip
        scene ts_kitchen
        with wipeleft_scene

        $ TS.s(ts_showscreens)

        "Ужин проходит молча. За всё время мы не сказали друг другу ни слова."

        show hiroto 1e at t11

        "Только когда мы убираем тарелки в посудомойку, папа как бы невзначай спрашивает:"

        ts_ft 1y "Так... Что ты там говорила про чай с ложкой?"

    else:

        show hiroto 1f at t11

        m "На ужин у нас картошка с овощным салатом и чай. Прости, но чай только с ложкой."
        m "Точнее, только у тебя. Я уже поела."

        show hiroto 1a at f11

        m "Правда, пока я тебя дождалась, она уже и остыла. Сейчас разогрею."

        "Папа улыбается."

        ts_ft 2b "Да не надо, сам не инвалид. Уж с разогревом картошки я справлюсь."

        "С этими словами папа направляется к плите."

        $ TS.s(ts_hidescreens)
        " {w=1.0}{nw}"

        play sound2 pageflip
        scene ts_kitchen
        with wipeleft_scene

        $ TS.s(ts_showscreens)

        "Через пять минут картошка снова горячая, она слегка полита маслом и приправлена зеленью."

        m "Тебе салатик положить?"
        ts_ft "Да, пожалуйста."

        $ TS.s(ts_hidescreens)
        " {w=1.0}{nw}"

        play sound2 pageflip
        scene ts_kitchen
        with wipeleft_scene

        $ TS.s(ts_showscreens)

        "Ужин проходит молча. За всё время мы не сказали друг другу ни слова."
        "Хотя хорошую новость сказать очень хочется, я умело держу рот на замке."

        show hiroto 1e at t11

        "Только когда мы убираем тарелки в посудомойку, папа как бы невзначай спрашивает:"

        ts_ft 1y "Так... Что ты там говорила про чай с ложкой?"

    "Я улыбаюсь."

    m "Сейчас поставлю."

    show hiroto at cright with move
    hide hiroto

    $ TS.m(ts_havchik_gotovka)

    "Кофе на ночь он принципиально не пьёт. Хотя с сердцем у него особых проблем нет."
    "Если они вообще есть..."
    "Поэтому на всякий случай мы рядом с кофе всегда храним пачку чёрного чая с бергамотом."
    "Другой чай папа просто не пьёт. Говорит, невкусно, и что с бергамотом лучше."
    "Ну, а я от кофе не откажусь. Всё равно уже режим угробила. Как говорится, помирать, так с музыкой."
    "Я заливаю воды побольше и ставлю чайник кипятиться."

    $ TS.m(ts_havchik_gotovka_end)

    stop music fadeout 5

    play ambience chainik_kipit fadein 2

    "Кстати, кажется, Юри говорила, что она принесёт свой чайный сервиз и свой любимый чай?"
    "Кто знает, может, один из видов чая Юри понравится папе даже больше пресловутого бергамота?"
    "Мысленно усмехнувшись, я жду, пока чайник закипит."

    stop ambience fadeout 3

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound2 pageflip
    scene ts_kitchen
    with wipeleft_scene
    play sound chainik_svistit
    play music audio.t8

    $ TS.s(ts_showscreens)

    "Наконец, чайник закипел, и я завариваю чай со всё тем же бергамотом для папы и растворимый кофе для себя."
    "Ни я, ни папа не пьём чай или кофе с сахаром."
    stop sound fadeout 2
    "Сахар у нас используется в основном для того, чтобы мама что-нибудь испекла."
    "И то, печёт мама у нас довольно редко."
    "А когда она уезжает, то мы и вовсе оставляем почти тот же объём сахара, что и до отъезда."
    "Мы можем разве что разбавить свой утренний кофе либо сливками, либо молоком, чтобы просто кофе был не такой горячий."
    "Ну либо я могу сварить ту же гречку с сахаром, чтобы она просто не была такой сухой..."
    "А так – только чистый чай или чистый кофе."
    "Не понимаю, как другие люди кладут богохульный сахар в эти поистине божественные напитки... Но о вкусах не спорят, верно?"
    "Даже если вкусы одних людей объективно хуже других..."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound2 pageflip
    scene ts_kitchen
    show hiroto 1a at t11
    with wipeleft_scene

    $ TS.s(ts_showscreens)

    m "Твой чай, пап."
    ts_ft 1a1 "Кофе? На ночь?"
    show hiroto 1b1 at f11
    m "Ну, тут либо «с одного раза ничего не будет», либо «помирать, так с музыкой»."
    m "В любом случае, кофе я себе уже сделала. Не выливать же его."
    ts_ft 2c "Ну, если бы я был настроен на спор, то я бы его из принципа вылил и заставил тебя сделать себе чай."

    show hiroto 1e at t11

    m "Пап, ну ты же знаешь, что я не особо люблю чай, даже с бергамотом. Мне больше кофе по душе."
    ts_ft 2c "Это ты сейчас так говоришь. Посмотрим, как ты запоёшь через десяток-другой лет."
    ts_ft 2b "В любом случае, сегодня я спорить не намерен, потому что уже устал, поэтому пей что хочешь."
    m "Вот уж спасибо тебе, пап, большое."

    "Говорю я слегка дразнительным тоном."

    show hiroto 2t at h11

    "Мы оба засмеялись с этого."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound2 pageflip
    scene ts_kitchen
    show hiroto 1d at t11
    with wipeleft_scene

    $ TS.s(ts_showscreens)

    "Настал тот момент, которого я ждала весь вечер."

    m "Па-а-ап..."
    ts_ft 2d "Что?"
    m "А у меня для тебя хорошие новости есть..."
    ts_ft 2c "И какие же?"
    m "Наш клуб наконец-то официально зарегистрировали!"
    ts_ft 2g "Правда?! Моя ты умница! Я всегда в тебя верил!"

    show hiroto 2f at f11

    "И вот так всегда... Пока я почти два месяца тужилась, чтобы найти хоть кого-то для этого клуба, он раз за разом припоминал мне, что лучше бы я осталась в Дискуссионном."
    "Но как только я добилась своего, папа тут же сменил пластинку и сказал, что ни секунды во мне не сомневался."
    "..."
    "Но портить момент не хочется."
    "Поэтому вместо этого я просто говорю:"

    m "Да! Сегодня я нашла ещё одну девочку, и..."
    ts_ft 1c "«Ещё одну девочку»? Это что получается, у вас в клубе четыре человека, и все четверо – девушки?"
    m "Ну-у-у... Да?"
    ts_ft 1h "Моника... Ты же знаешь, как я забочусь о твоём благосостоянии..."
    ts_ft 2g "Но неужели литература – это настолько девчачье занятие?"

    show hiroto 2h at t11

    "Я знаю, к чему он клонит."

    m "Нет, литература – это такая вещь, для которой совершенно неважно, какого ты пола."
    m "Но просто три человека, которых я... нашла... они все по воле случая оказались девочками."

    show hiroto 2f at s11

    m "Но я уверяю, что после фестиваля, на котором мы {b}обязательно{/b} проявим себя с лучшей стороны, к нам придут и другие участники."

    show hiroto 2i at t11

    m "И вот после фестиваля другие участники могут быть и парнями."
    ts_ft 2g "Ладно, убедила."
    ts_ft 1c "Сколько там до вашего фестиваля осталось, кстати?"

    show hiroto 1e at s11

    m "Две недели."

    ts_ft "Хорошо..."

    show hiroto 1e at cright with move
    hide hiroto

    "Он допивает свой чай и уходит."
    "Неужели он на меня обиделся? И из-за чего, из-за того, что в моём клубе {s}пока{/s} нет парней?"

    stop music fadeout 7

    m "Хочешь, в шахматы сыграем?"

    show hiroto 1d at ln11

    ts_ft 1a1 "Моника, что-то я устал за сегодня, может, завтра?"
    ts_ft 1a1 "Я лучше просто немного телевизор посмотрю, да спать лягу."

    "Теперь уже обиделась я."
    "Ну уж нет!"

    show hiroto 1d at h11

    $ persistent.sprite_time = "day"

    m "Тогда я с тобой пойду!"

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"


    play sound pageflip
    scene ts_living_room_telek_sudba_night
    with wipeleft_scene



    play music audio.t9

    $ TS.s(ts_showscreens)

    "Мы сидим молча и просто наблюдаем за приключениями в Ленинграде..."

    "Как вдруг на меня накатывает новая волна воспоминаний о Нацуки."

    play sound fb
    window hide
    scene ts_club
    show natsuki 2k at t11
    show overlay aw_memory_back_1
    $ TS.m(VHS())
    with flash

    $ TS.s(ts_showscreens)

    n 12f "Но... Папа считает, что я, хоть и уже слишком взрослая для чтения манги... ещё недостаточно взрослая и самостоятельная, чтобы самой вправе что-то решать."
    n 12c "И ведь с ним не поспоришь даже! Он же папа, он же взрослый, умный, а я что?"
    $ persistent.sprite_time = "day"
    n 12f "Всего лишь маленькая девочка..."

    play sound fb
    window hide
    scene ts_living_room_telek_sudba_night
    with flash

    $ TS.s(ts_showscreens)

    $ persistent.sprite_time = "cloudly"

    "..."
    "Нет... У меня с моим отцом всё будет иначе!"

    show hiroto 1e at t11

    "Я набираюсь смелости и спрашиваю:"

    m "Пап?"
    ts_ft 1c "Что такое, дорогая?"

    show hiroto 2f at s11

    m "Я тебе, кажется, давно не говорила, как сильно я тебя люблю..."
    m "Как ты меня поддерживаешь во всех начинаниях..."
    m "Как ты утешаешь меня, если у меня что-то не получается..."

    "Если это не касается учёбы, конечно же..."
    "Но это предложение вслух я уже не произношу. Вместо этого я произношу {i}немного{/i} другое..."

    m "Я люблю тебя, пап. Всем сердцем."
    ts_ft 2y "Что это на тебя сегодня нахлынуло?.."

    show hiroto 2x at t11

    "Однако, увидев мой максимально хмурый и суровый взгляд, папа быстро собрался с силами и продолжил."

    ts_ft 2g "Я тоже люблю тебя, доченька. Тоже всем сердцем."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    $ TS.m(ts_obnimashki_center_finalle)
    $ TS.p(1)
    show blink

    $ TS.s(ts_showscreens)

    "А затем мы обнялись. Как будто мне лет эдак шесть-семь, папа берёт ещё очень лёгкую меня на свои сильные руки и обнимает меня."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    show hiroto 1f at t11
    hide blink
    show unblink
    $ TS.m(ts_obnimashki_center_finalle1)

    $ TS.s(ts_showscreens)

    "Я сижу у него на коленях, и он улыбается мне. Так искренне, как он мне уже давно не улыбался."
    "Я улыбаюсь в ответ и говорю:"

    m "Ладно, поздновато уже, мы спать не собираемся?"
    ts_ft 2c "Ну, я-то собираюсь, потому что устал очень. А вот насчёт тебя я не знаю. Ты, во-первых, дремала, во-вторых, кофе на ночь—{nw}"

    show hiroto 1e at s11

    m "Да брось, пап, ты же знаешь, что это всё враки и неправда."
    m "Вот увидишь, я минут через пятнадцать снова вырублюсь."
    m "Тем более, если честно, я тоже невероятно устала, а вечерний сон и кофе на вечер были лишь компенсацией за такое напряжение."

    show hiroto 1g at t11

    stop music fadeout 7

    ts_ft "Ну, как знаешь."
    ts_ft 2b "Тогда, спокойной ночи?"
    show hiroto 2f at f11
    m "Спокойной ночи, пап. Люблю тебя."
    ts_ft 2g "Я тоже тебя люблю, солнышко."
    show hiroto 1e at t11
    "Папа выключает телевизор, и мы расходимся по своим спальням."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound2 pageflip
    scene ts_darkbed
    with wipeleft_scene

    play music ts_rem

    $ TS.m(ts_padenie_na_bed)
    $ TS.p(1)
    play sound ts_bed_squeak

    $ TS.s(ts_showscreens)

    "Я даже не заметила, как дошла до своей комнаты и разделась."
    "Настроение сегодня было лучше некуда."

    if unluck2 or unluck3 == True:
        "Даже если сегодня не всё пошло по плану..."
    elif unluck2 and unluck3 == True:
        "Даже если сегодня всё пошло не по плану..."

    "«Сегодня к нам добавился четвёртый человек, мы наконец официально зарегистрировали наш клуб.»"
    "«Правда, у этого человека тоже всё не совсем гладко...»"
    "«Но, во-первых, я с этой 'неровностью' тоже сталкивалась, так что примерно знаю, как надо действовать.»"
    "«А во-вторых...»"
    show blink
    "Додумать я не успела."
    "Сонный мир победил. Морфей оказался сильней."

    window hide
    stop music
    play sound br_glitch
    show ts_darkbed as bg1 at Glitch(_fps=160, glitch_strength=1)
    $ TS.p(1.1)
    stop sound
    scene black
    $ TS.p(3)

    jump ts_scenario_4