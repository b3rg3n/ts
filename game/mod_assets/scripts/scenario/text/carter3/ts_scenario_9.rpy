label ts_scenario_9:

    $ TS.b()

    python: # ОБНОВЛЯЕМ RPC
        ts_rpc_carter9()

    $ persistent.rpclabel = "9"
    $ persistent.sprite_time = "day"
    $ persistent.carter2menu = False
    $ persistent.carter3menu = True
    $ persistent.badendmenuperedglitch = False
    $ persistent.badendmenuskipglitch = False
    $ persistent.badendmenu = False
    $ persistent.goodendmenu = False
    $ persistent.peredbadendmenu = False
    $ persistent.peredgoodendmenu = False

    if _preferences.language == "english":
        $ save_name = "Welcome back... again?"
    else:
        $ save_name = "С возвращением... Снова?"

    play sound winerrorsound
    if renpy.android:
        if _preferences.language == "english":
            show screen dialog("ru.bergen.truestory.apk\n\nIf you suffer from epilepsy, it is highly recommended to turn off the mod right now.", ok_action=Return())
        else:
            show screen dialog("ru.bergen.truestory.apk\n\nЕсли вы страдаете от эпилепсии, настоятельно рекомендуется завершить прохождение мода.", ok_action=Return())
    else:
        if _preferences.language == "english":
            show screen dialog("truestory.exe\n\nIf you suffer from epilepsy, it is highly recommended to turn off the mod right now.", ok_action=Return())
        else:
            show screen dialog("truestory.exe\n\nЕсли вы страдаете от эпилепсии, настоятельно рекомендуется завершить прохождение мода.", ok_action=Return())
    $ TS.b()
    pause
    hide screen dialog
    play sound winerrorsound

    if renpy.android:
        if _preferences.language == "english":
            show screen dialog("ru.bergen.truestory.apk\n\nI won't say it again.", ok_action=Return())
        else:
            show screen dialog("ru.bergen.truestory.apk\n\nДважды я не предупреждаю.", ok_action=Return())
    else:
        if _preferences.language == "english":
            show screen dialog("truestory.exe\n\nI won't say it again.", ok_action=Return())
        else:
            show screen dialog("truestory.exe\n\nДважды я не предупреждаю.", ok_action=Return())
    pause
    hide screen dialog

    $ TS.b()

    play sound chp
    if _preferences.language == "english":
        $ Chapter("ACT THREE")
        $ Chapter("ACT THREE")
        $ Chapter("chapter one")
        $ Chapter("chapter one")
        $ Chapter("Welcome back... again?")
        stop sound fadeout 7
        $ Chapter("Welcome back... again?")
    else:
        $ Chapter("АКТ ТРЕТИЙ")
        $ Chapter("АКТ ТРЕТИЙ")
        $ Chapter("Глава первая")
        $ Chapter("Глава первая")
        $ Chapter("С возвращением... Снова?")
        stop sound fadeout 7
        $ Chapter("С возвращением... Снова?")

    $ TS.p(2)

    $ TS.s(ts_showscreens)

    $ persistent.uncolorize = "lite"

    s "{size=-6}..ика!{/size}"
    s "{size=-4}Моника!{/size}"
    s "Моника, просыпайся уже!" with hpunch
    m "Пап, ну ещё рано..."
    play sound s_kill_glitch1
    s "Вставай давай, пьянь малолетняя!"
    m "Ну хорошо, хорошо!.."
    window hide
    play sound ts_glitch2
    scene ts_sayori_bedroom
    with memglitchbolee
    stop sound
    $ TS.s(ts_showscreens)
    "Передо мной предстала..."
    play music ts_sd fadein 2
    play sound ts_glitch5
    show sayori 4pi at t11
    with memglitchbolee
    stop sound
    "Та же Сайори."
    "В абсолютно той же пижаме.{w} В абсолютно той же комнате."
    "Странно..."
    "Я, конечно, говорила, что сначала буду помогать Сайори... Но не настолько рано..."
    m "С-Сайори..."
    show sayori 4pj at f11
    s "Что такое?"
    show sayori 4pi at t11
    m "А ты... не знаешь, какой сегодня день?"
    show sayori 2ph at f11
    s "А тебе что, настолько память отшибло, что даже не помнишь, какой сегодня день?"
    s 4pj "Сегодня же суббота!"
    show sayori 3pi at t11
    m "Нет, день недели я помню. Я имею в виду дату..."
    show sayori 3pl at f11
    s "Видимо, совсем тебе плохо вчера было..."
    $ persistent.ingame_pizda = False
    s 2px "Забыла уже? Сегодня{w=0.4}{nw}"

    python:
        _preferences.volumes['music'] = .0

    $ gtextsuka = glitchtext(35)

    $ TS.s(ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake))

    play sound slender
    $ persistent.ingame_pizda = True
    show ts_sayori_bedroom_glitch_pizdets zorder 4 at ts_coridor_glitch
    show black zorder 5 at ts_black_glitch
    show blackout_exh zorder 5
    show anim_exhausted zorder 5
    show m_rectstatic zorder 5
    show ts_sayori_zalagala_blyadina zorder 6 at Glitch(_fps=1000.)

    s "[gtextsuka]{nw}"

    window hide
    stop sound

    scene ts_sayori_bedroom

    $ persistent.ingame_pizda = False

    $ TS.s(ts_null_transform)

    python:
        _preferences.volumes['music'] = .65

    show sayori 2pa at t11
    m "Ч-ч-что?"
    show sayori 2pc at f11
    s "Говорю же, сегодня{w=0.4}{nw}"

    $ TS.s(ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake))

    python:
        _preferences.volumes['music'] = .0

    play sound slender
    $ persistent.ingame_pizda = True
    show ts_sayori_bedroom_glitch_pizdets zorder 4 at ts_coridor_glitch
    show black zorder 5 at ts_black_glitch
    show blackout_exh zorder 5
    show anim_exhausted zorder 5
    show m_rectstatic zorder 5
    show ts_sayori_zalagala_blyadina zorder 6 at Glitch(_fps=1000.)

    s "[gtextsuka]{nw}"

    window hide
    stop sound

    scene ts_sayori_bedroom

    $ persistent.ingame_pizda = False

    $ TS.s(ts_null_transform)

    python:
        _preferences.volumes['music'] = .65

    show sayori 2pa at t11
    m "Н-не понимаю..."
    show sayori 4pj at f11
    s "А что тут непонятного?"
    show sayori 4pi at t11
    m "Да всё здесь непонятно!"
    m "Л-ладно, ты мне лучше скажи... сколько осталось до фестиваля?"
    show sayori 3pzc at f11
    s "Тебе всё фестиваль да фестиваль..."
    s 2px "Не переживай, до фестиваля ещё целая неделя, подготовиться успеем."
    show sayori 2pf at t11
    m "{b}{size=+10}ЕЩЁ НЕДЕЛЯ???{/size}{/b}" with hpunch
    "Нет..."
    "Я в это не верю..."
    "Это просто продолжение кошмара, это всё не по-настоящему..."
    m "С-Сайори... А когда мы... пили вино?.."
    show sayori 4pj at f11
    $ persistent.ingame_pizda = False
    s "Что ты всё глупые вопросы задаёшь? Вино мы пили вчера, после чего мы тебя полумёртвую домой тащили!"
#
    python:
        _preferences.volumes['sfx'] = 1.0
        _preferences.volumes['music'] = .0

    play sound2 ts_glitch_music9

    $ TS.s(ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake))

    $ persistent.ingame_pizda = True
    play sound crack
    scene ts_club_glitch_pizdets
    show ts_yuri_zalagala_blyadina:
        align(0.15, 0.35)
    show ts_sayori_zalagala_blyadina at t32
    show ts_natsuki_zalagala_blyadina at t33
    $ TS.m(VHS())

    $ gtextsuka = glitchtext(8)
    $ gtextsuka1 = glitchtext(15)
    y "Я сказала [gtextsuka] сидеть на [gtextsuka1]!"
    y "[gtextsuka] доведёт тебя до [gtextsuka1]."

    $ TS.s(ts_null_transform)

    stop sound2
    python:
        _preferences.volumes['music'] = .65

    $ persistent.ingame_pizda = False
    scene ts_sayori_bedroom
    show sayori 4pi at t11

    m "А-а-а... Д-да... П-п-п-понятно... В-в-вчера, д-да..."
    "Я нервно хихикаю."
    show sayori 2pb at t11
    m "Н-ну, раз уж я проснулась и в {i}добром здравии,{/i} то, может, ты меня уже домой проводишь?"
    "Я не хочу находиться с ней в одной комнате. Мне страшно."
    show sayori 3pc at f11
    s "О, конечно."
    s 3px "Мне, кстати, в магазин также надо, так что нам даже по пути будет!"
    show sayori 3pa at t11
    m "Д-да, к-конечно..."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_residential
    show sayori 1ba at t11
    with wipeleft_scene

    $ TS.s(ts_showscreens)

    "В попытке хоть как-то отвлечься и завязать непринуждённую беседу, я снова начинаю с той же фразы."
    m "О, а я этот район знаю! Это же{w=1.5}{nw}"

    $ TS.s(ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake))

    python:
        _preferences.volumes['sfx'] = 1.0
        _preferences.volumes['music'] = .0

    play sound crack
    play sound2 pizdec_sound
    $ persistent.ingame_pizda = True
    show ts_residental_glitch_pizdets zorder 4 at ts_coridor_glitch
    show black zorder 5 at ts_black_glitch
    show blackout_exh zorder 5
    show anim_exhausted zorder 5
    show m_rectstatic zorder 5
    show ts_sayori_zalagala_blyadina zorder 6 at Glitch(_fps=1000.)

    s "Это же район, в котором когда-то жила Мира."
    m "От-ткуда т-ты...{w=1}{nw}"
    s "Наш дом находится в двух домах от их дома."
    s "Она умерла. Я видела её похороны."
    s "И мы все тоже умрём."
    s "И это всё будет твоя вина."
    m "Ч-что?"

    stop sound2

    $ TS.s(ts_null_transform)

    $ persistent.ingame_pizda = False

    python:
        _preferences.volumes['music'] = .65

    scene ts_residential
    show sayori 2bc at f11

    s "Я говорю, ты где живёшь?"
    show sayori 2bb at t11
    m "Г-г-г-где-то в-в-вон... там..."
    show sayori 2bx at f11
    s "Ну и здорово! Мы пройдём через магазин, а затем разойдёмся по домам."
    show sayori 2ba at t11
    m "Д-д-да... пойдём..."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_city_day
    show sayori 1bb at t11
    with wipeleft_scene

    $ TS.s(ts_showscreens)
    "Всю дорогу до магазина мы шли молча."
    "И всю дорогу до магазина мне попадались одни и те же люди, двигающиеся в одном и том же направлении..."
    "...Нет, но это же всё уже было!"
    "Я что, сплю? Потому что если да, то этот сон мне очень не нравится."
    show sayori 1bf at t11
    "Видя моё нездоровое и беспокойное выражение лица, Сайори смущается."
    show sayori 2bh at f11
    s "Ну... на этом наши пути расходятся..."
    show sayori 2bf at t11
    m "Да, Сайори, давай, до понедельника!"
    show sayori 3bh at f11
    s "Постой!.."
    show sayori at thide
    hide sayori
    "Однако я её уже не слушаю. Я вообще никого не слушаю."
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound2 ts_running

    scene ts_city_day at ts_running_fast

    $ TS.p(2)
    stop sound2 fadeout 1
    play sound pageflip
    play sound3 ts_othodos_ot_bega fadein 2
    scene ts_street at ts_ustal_suka
    with wipeleft_scene

    $ TS.s(ts_showscreens)

    "Может, Сайори просто меня разыгрывает..."
    "Но нет, Сайори не из тех людей, которые качественно шутят..."
    "Да и что такое со всеми остальными людьми, которые тоже делают вид, что этой недели никогда и не было?"
    "Вряд ли Сайори заплатила каждому из них, чтобы поддерживать шутку..."
    "Нужно просто побыстрее добраться домой..."
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_house
    with wipeleft_scene

    $ TS.p(1)

    play sound pageflip
    scene ts_entrance_day
    with wipeleft_scene

    $ TS.p(1)

    play sound pageflip
    scene ts_kitchen
    with wipeleft_scene

    $ TS.s(ts_showscreens)
    m "Папа?"
    "Ответа нет."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    play sound pageflip
    scene ts_living_room
    with wipeleft_scene

    $ TS.s(ts_showscreens)

    m "Папа!"
    "Странно... очень странно..."
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"
    play sound pageflip
    scene ts_gost
    with wipeleft_scene
    $ TS.s(ts_showscreens)
    "Я поднимаюсь наверх."
    $ TS.s(vpunch)
    m "ПАПА!"
    "Второй этаж у нас относительно маленький, да и стены достаточно тонкие, поэтому, если папа в одной из комнат, то он обязательно должен был меня услышать."
    "Однако ответа я так и не дождалась."
    "Папа тоже решил меня разыграть?"
    "Я вспоминаю слова, которые он неоднократно говорил."
    ts_ft "Не пей, Моника, иначе плохо тебе будет."
    "Внушив себе мысль, что это просто затянувшийся и неудачный с момента пробуждения розыгрыш, я спускаюсь на кухню."
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"
    play sound pageflip
    scene ts_kitchen
    with wipeleft_scene

    $ TS.s(ts_showscreens)
    "Как раз вовремя. В этот момент вернулся папа."
    play sound ts_glitch3
    show hiroto 1a at t11
    with memglitchbolee
    stop sound

    m "Папа! Почему все ведут себя...{w=0.44}{nw}"
    "Однако прежде чем я успеваю рассказать хоть что-либо, он просто весело сказал."

    python:
        _preferences.volumes['music'] = .0

    $ gtextsuka = glitchtext(15)

    $ TS.s(ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake))

    play sound slender
    $ persistent.ingame_pizda = True
    show ts_kitchen_glitch_pizdets zorder 4 at ts_coridor_glitch
    show black zorder 5 at ts_black_glitch
    show blackout_exh zorder 5
    show anim_exhausted zorder 5
    show m_rectstatic zorder 5
    show ts_hiroto_zalagal zorder 6 at Glitch(_fps=1000.)

    ts_ft "Ну привет, [gtextsuka]!{w=2}{nw}"

    window hide
    stop sound

    scene ts_kitchen

    $ persistent.ingame_pizda = False

    $ TS.s(ts_null_transform)

    python:
        _preferences.volumes['music'] = .65

    show hiroto 1a at t11
    ts_ft "Ну привет, гулёна!"

    "От услышанного я снова теряю дар речи."
    "Однако если в прошлый раз я потеряла дар речи от того, как легко и непринуждённо он вёл себя несмотря на то, что его дочь вообще-то пропала..."
    "То на этот раз я просто застываю на месте, не в силах произнести не то что хотя бы слово – даже и звука произнести не могу!"
    "Нет, это всё неправильно... Я просто {i}слишком{/i} перепила..."
    "Но с другой стороны, а когда я пила? Да неделю назад я уже пила!"
    "А все ведут себя так, как будто это было вчера!"
    show hiroto 1b1 at t11
    "Папа, увидев застывшее от страха лицо, тоже слегка разволновался."
    show hiroto 1z at f11
    ts_ft "Моника, с тобой всё хорошо?"
    ts_ft 1y "Если что, то я ругать тебя не буду, просто будь осторожнее в следую{w=0.3}{nw}"
    show hiroto 1j at t11
    $ TS.p(2)

    $ TS.m(heartbeat)
    $ TS.s(ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake))

    show hiroto 2k at t11
    m "{b}{font=[shl_font]}ПАПА, ПОЧЕМУ ВСЕ ВЕДУТ СЕБЯ ТАК, КАК БУДТО ПРОШЛОЙ НЕДЕЛИ НИКОГДА НЕ СУЩЕСТВОВАЛО?{/font}{/b}"
    show hiroto 2h at f11
    ts_ft "Ч-что значит «прошлой недели никогда не существовало»?"
    ts_ft 1y "Я что-то не припомню никаких таких провалов..."
    show hiroto 2k at h11
    m "Папа, мне сейчас вот вообще не до шуток!"
    show hiroto 1j at t11
    "Я уже потерпела неудачу в попытках разузнать у Сайори, какой сегодня день, но папа же взрослый человек, серьёзный..."
    "Хотя и со своеобразным чувством юмора..."
    m "Хорошо..."
    m "Пап, вот ты мне скажи... Какое сегодня число?"
    show hiroto 1y at f11
    ts_ft "Моника, ты, наверное, очень сильно перепила, раз уж не помн{w=0.15}{nw}"
    show hiroto 1b1 at h11
    m "Папа!"
    m "Просто.{w=0.44} Скажи.{w=0.44} Число.{w=1.44} Пожалуйста."
    show hiroto 1z at f11
    ts_ft "Ну хорошо, хорошо. Сегодня{w=0.1}{nw}"

    python:
        _preferences.volumes['music'] = .0

    $ gtextsuka = glitchtext(35)

    $ TS.s(ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake))

    play sound slender
    $ persistent.ingame_pizda = True
    show ts_kitchen_glitch_pizdets zorder 4 at ts_coridor_glitch
    show black zorder 5 at ts_black_glitch
    show blackout_exh zorder 5
    show anim_exhausted zorder 5
    show m_rectstatic zorder 5
    show ts_hiroto_zalagal zorder 6 at Glitch(_fps=1000.)

    ts_ft "[gtextsuka]{nw}"

    window hide
    stop sound

    scene ts_kitchen

    $ persistent.ingame_pizda = False

    $ TS.s(ts_null_transform)

    python:
        _preferences.volumes['music'] = .65

    scene ts_kitchen
    show hiroto 1s at t11
    "..."
    "Ну что же, это было довольно предсказуемо."
    "У меня остался ещё один вариант."
    m "А ч-что ты с-сегодня с утра д-делал?"
    show hiroto 1c at f11
    ts_ft "Ну, во-первых, переживал о тебе{w=0.8}{nw}"
    show hiroto 2k at h11
    play sound ts_scream
    m "{font=[shl_font]}А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А{/font}{nw}" #УРОДСКИМ ШРИФТОМ
    show hiroto 2h at f11
    ts_ft "Моника, ты куда?"
    show hiroto at thide
    hide hiroto
    "Я его уже не слушаю, и вместо этого я просто выбегаю из кухни со слезами на глазах."

    stop music fadeout 5

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"
    play sound pageflip
    scene ts_bedroom
    with wipeleft_scene

    $ TS.s(ts_showscreens)

    m "{b}НУ ПОЧЕМУ? ПОЧЕМУ? ПОЧЕМУ?{/b}"
    m "{b}ПОЧЕМУ НИКТО НЕ ПОМНИТ НИЧЕГО ИЗ ТОГО, ЧТО ПРОИЗОШЛО ЗА ЭТУ НЕДЕЛЮ?{/b}"
    m "{b}ПОЧЕМУ АБСОЛЮТНО ВСЕ ДЕЛАЮТ ВИД, ЧТО ЭТОЙ НЕДЕЛИ КАК БУДТО БЫ И НЕ БЫЛО?{/b}"
    play music ts_roae

    play sound ts_glitch6
    scene ts_bedroom

    $ persistent.ingame_pizda = True

    if not renpy.android:
        $ TS.m(AnimatedAberate(25.0))
    $ TS.s(ts_shake2(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake))

    show monika 2bi at f11
    with memglitchstr
    stop sound
    em "Потому что её на самом деле никогда и не было."
    em 4bd "Помнишь, как я сказала вчера, что сон заканчивается?"
    em 3bi "Так вот. Сон закончился."
    em "Начинается [gtextsuka] кошмар."
    show monika 1bh at t11
    $ gtextsuka = glitchtext(144)
    $ m_name = "[gtextsuka]"
    m "[gtextsuka]"

    $ persistent.ingame_pizda = False

    if not renpy.android:
        $ TS.m(StillAberate(25.0))
        $ TS.s(StillAberate(25.0))

    python:
        currentpos = get_pos()
        startpos = currentpos - 0.2
        if startpos < 0: startpos = 0
        track = "<from " + str(startpos) + " to " + str(currentpos) + ">mod_assets/source/audio/ost/ts_roae.ogg"
        renpy.music.play(track, loop=True)

    show monika 2bi at f11
    em "[gtextsuka]{nw}"
    em 4bi "[gtextsuka]{nw}"
    em 3bd "[gtextsuka]{nw}"
    em 1bi "[gtextsuka]{nw}"
    hide monika
    $ TS.p(5)

    $ persistent.ingame_pizda = False

    $ TS.m(ts_null_transform)
    $ TS.s(ts_null_transform)

    stop music
    "Кажется, меня сейчас стошнит..."

    window hide
    play sound2 ts_running
    $ TS.m(ts_bg_into1)
    $ TS.p(0.3)
    play sound door_break
    $ TS.p(0.2)
    scene ts_bathroom
    $ TS.m(ts_bg_exodus1)
    $ TS.p(0.5)
    stop sound2 fadeout 1
    $ TS.m(ts_blevota_anim)
    $ TS.p(1)

    if _preferences.language == "english":
        $ m_name = "Monika"
    else:
        $ m_name = "Моника"
    $ TS.s(hpunch)
    play sound3 ts_blevanula
    $ TS.p(6)
    $ TS.m(ts_blevota_exit_anim)
    "Что это вообще такое было?"
    play music ts_icra fadein 1
    show monika 2bg at f11
    with linearblurbolee
    $ TS.s(ts_showscreens)
    em "Полегчало?"
    show monika 2bf at t11
    m "Ты..."
    $ TS.s(vpunch)
    m "ЭТО ВСЁ ТЫ ВИНОВАТА!"
    show monika 1bp at f11
    em "А почему ты считаешь, что если случается что-то плохое, то это сразу обязательно я?"
    show monika 1bo at t11
    m "Потому что ты магнит всех проблем!"
    show monika 3bl at f11
    em "А ты разве на прошлой неделе не о себе так думала?"
    em 2bd "Ну да и пусть. Раз уж ты так искренне считаешь, что во всём виновата я, надо бы тебе объяснить кое-что ещё."
    em 2bi "Всей предыдущей недели никогда и не существовало. Это всё просто часть сна."
    em "Вторая часть сна началась сегодня. Третья часть сна начнётся в следующую субботу, и так далее."
    em 3bd "Своего рода циклы. И с началом каждого нового цикла никто, кроме тебя и меня, ничего не помнит из того, что происходило за предыдущую неделю."
    em "Поэтому все так искренне удивляются тому, что ты бредишь. Для них всех сумасшедшая именно ты, а не они."
    em 2bl "Во-первых, их больше, и всех их тебе просто не переубедить. А во-вторых..."
    show monika 1bq at t11
    "Аки так и не закончила свою мысль. Впрочем, я и без второго пункта её поняла."
    m "Значит, мне тоже нужно просто делать вид, что этой недели никогда и не происходило?"
    m "Но это же бред, это бессмыслица!"
    show monika 2bn at f11
    em "Ну, ты знаешь, что это бред. И я знаю, что это бред."
    em 3bi "Но для всех остальных это самая обычная неделя, и никто не знает, что ждёт их впереди."
    em 2bd "Девочки заново будут писать стихи, ты заново раздашь им всем задания, и всё такое."
    em 1bn "А теперь давай лучше чисть зубы, и не забудь написать стих, который ты в прошлую субботу написала."
    em "Ты же на этом основании будешь уговаривать девочек написать и свои стихи."
    show monika 1bm at t11
    m "Хм-м-м... «Никто не знает, что ждёт их впереди...»"
    m "Кроме меня..."
    show monika 4bl at f11
    em "Напомнить тебе, как ты всё утро шарахалась от того, что ты, по идее, и так знаешь?"
    show monika 3bj at t11
    m "Эй! Меня просто застали врасплох, вот и всё!"
    show monika 3bk at f11
    em "Ладно бы это было одномоментно... но ты же уже на протяжении нескольких часов точно так же не знаешь, что тебя ждёт!"
    show monika 3bj at t11
    m "Х-х-х... ладно..."
    show monika 2bd at f11
    em "Впрочем, не об этом. Ты стих-то напишешь?"
    show monika 1bc at t11
    m "Напишу... куда я теперь денусь..."
    m "Только я уже не помню, о чём он вообще."
    show monika 2bg at f11
    stop music fadeout 5
    em "Ну как же, как же?"
    em 2bb "Там было что-то про Солнце с другой стороны, которое символизирует мир, который скрыт ото всех, кроме нас самих, и, это, как это называется..."
    em 1by "В общем, идею я тебе дала, ты теперь только вспомни точные слова."
    show monika 1be at t11
    m "Ладно, ладно, напишу уж! Теперь бы вспомнить, что конкретно я написала неделю назад..."
    show monika 4bb at f11
    em "Вот это другое дело."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"
    play sound pageflip
    scene ts_bedroom
    with wipeleft_scene

    $ TS.s(ts_showscreens)
    play music ts_afterlife
    "Хм-м-м..."
    "Ну давай вспоминать."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    scene ts_bedroom at ts_bg_into
    $ TS.p(0.5)
    scene ts_notebook at ts_bg_exodus
    $ TS.p(0.5)

    $ TS.s(ts_showscreens)

    "Слишком уж много произошло за эту неделю, которой, как оказалось, никогда на самом деле и не существовало."
    "Но стих я переписываю относительно уверенно, не забывая ни слова."

    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"

    scene ts_notebook with dissolve:
        blur 9.0

    $ TS.s(ts_showscreens)

    if not persistent.first_poem:
        $ persistent.first_poem = True
        show expression "mod_assets/source/images/gui/poem_dismiss.webp" as poem_dismiss:
            xpos 1050 ypos 590

    play sound pageflip

    if _preferences.language == "english":
        show screen poem(poem_peacedets_eng)
    else:
        show screen poem(poem_peacedets)

    pause

    play sound pageflip
    $ TS.s(ts_hidescreens)
    $ TS.p(1)
    hide screen poem
    hide poem_dismiss

    scene ts_notebook with linearblurbolee

    $ TS.s(ts_showscreens)
    
    "Написано вроде как слово в слово, даже мелочи вроде предлогов на месте, да и порядок слов тот же."
    show monika 2bk at f11
    with linearblurbolee
    $ TS.s(ts_showscreens)
    em "Надо же, как моя маленькая бездарность выросла! Идеально вспомнила стих, и мне даже напоминать ей не пришлось."
    show monika 2bj at t11
    m "Просто... заткнись."
    m "Давай лучше спать уже, за это утро произошло слишком много всего... {i}необычного.{/i}"
    m "Нужно освежить голову. А ещё, я надеюсь, все перестанут придуриваться и вспомнят, что у нас послезавтра фестиваль, вообще-то."
    show monika 3bl at f11
    em "Ну, надейся дальше."
    em 2bd "Но насчёт поспать – с этим я согласна."
    show monika 2bf at t11
    m "Как будто у тебя вообще право голоса есть..."
    m "Ладно. Спать так спать."
    play sound svet_on
    scene ts_darkbed

    "Что вообще происходит? И со всеми моими друзьями, и со всем остальным?"
    "Почему эта неделя повторяется точь в точь?"
    stop music fadeout 3
    "Слишком много всего... Как же я устала..."
    $ TS.s(ts_hidescreens)
    " {w=1.0}{nw}"
    scene black with ed_night_dis
    $ TS.p(1)
    $ TS.s(ts_null_transform)
    jump ts_scenario_10