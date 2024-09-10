# ТУТ ЛЕЖАТ ЭКРАНЫ С ТЕКСТОМ ПО ЦЕНТРУ
# Я ЗНАЮ, ЧТО ЭТО ЕБУЧИЙ КОЛХОЗ
# НО ПО-ДРУГОМУ НЕ СДЕЛАТЬ
# С ПЕРЕМЕННЫМИ ЗАТЫК - ЕСЛИ МЕНЯТЬ ШРИФТ - ИГРА КРАШИТСЯ
# С КРИКОМ - "Я БЛЯ ТАКИХ ФАЙЛОВ НЕ ЗНАЮ"
# А БЕЗ ПЕРЕМЕННЫХ РАБОТАЕТ
# КАРОЧЕ - ХУЙ ПРОССЫШЬ, ЧЁ ТАМ НЕ ТАК НАХУЙ

screen alko_text1:
    if _preferences.language == "english":
        text "{size=+15}{font=[sc_font]}What...{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[sc_font]}Это...{/font}{/size}" yalign 0.5 xalign 0.5

screen c10_text_blya:
    if _preferences.language == "english":
        text "{size=+15}{font=[sc_font]}Why?{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[sc_font]}Почему?{/font}{/size}" yalign 0.5 xalign 0.5

screen alko_text2:
    if _preferences.language == "english":
        text "{size=+15}{font=[ink_font]}...is...{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[ink_font]}...что...{/font}{/size}" yalign 0.5 xalign 0.5

screen alko_text3:
    if _preferences.language == "english":
        text "{size=+15}{font=[ts_nvl_font2]}...this?..{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[ts_nvl_font2]}...такое?..{/font}{/size}" yalign 0.5 xalign 0.5

screen alko_text4:
    if _preferences.language == "english":
        text "{size=+25}{font=[shl_font]}Well, what do you think this is? A wine.{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+25}{font=[shl_font]}Как это что? Вино, что же ещё.{/font}{/size}" yalign 0.5 xalign 0.5

screen alko_text5:
    if _preferences.language == "english":
        text "{size=+15}{font=[ts_nvl_font2]}It reminisces me of something... Can't find the word for it however...{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[ts_nvl_font2]}Что-то мне это напоминает... Правда, слова не совсем правильно подобрать могу...{/font}{/size}" yalign 0.5 xalign 0.5

screen alko_text6:
    if _preferences.language == "english":
        text "{size=+15}{font=[ts_nvl_font2]}Maybe it's because I'm not quite sober already...{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[ts_nvl_font2]}Может, это потому, что я уже не совсем трезвая...{/font}{/size}" yalign 0.5 xalign 0.5

screen pizda_text1:
    if _preferences.language == "english":
        text "{size=+15}{font=[ts_nvl_font2]}But that was a fatal mistake. When I tried to get up once again, I miscalculated.{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[ts_nvl_font2]}Но это стало роковой ошибкой. Когда я ещё раз попыталась встать, я просчиталась.{/font}{/size}" yalign 0.5 xalign 0.5

screen pizda_text2:
    if _preferences.language == "english":
        text "{size=+15}{font=[ts_nvl_font2]}And my miscalculation was basically just that I fell down.{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[ts_nvl_font2]}И просчёт мой заключался в том, что я упала.{/font}{/size}" yalign 0.5 xalign 0.5

screen pizda_text3:
    if _preferences.language == "english":
        text "{size=+15}{font=[ts_nvl_font2]}And as if me falling down wasn't enough... I also hit the edge of the table. Twice.{/font}{/size}" yalign 0.5 xalign 0.5
    else:    
        text "{size=+15}{font=[ts_nvl_font2]}И ладно бы просто упала... Я ещё зацепилась за край стола. Дважды.{/font}{/size}" yalign 0.5 xalign 0.5

screen pizda_text4:
    if _preferences.language == "english":
        text "{size=+15}{font=[ts_nvl_font2]}I don't know how unlucky I can be\nto get hit by two different tables with the same height, but\nit turned out as it turned out.{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[ts_nvl_font2]}Не знаю, как можно быть настолько невезучей,\nчтобы упасть о два одинаковых стола с одинаковой высотой,\nно получилось как получилось.{/font}{/size}" yalign 0.5 xalign 0.5

screen pizda_text41:
    if _preferences.language == "english":
        text "{size=+15}{font=[ts_nvl_font2]}And then...{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[ts_nvl_font2]}А потом...{/font}{/size}" yalign 0.5 xalign 0.5


screen pizda_text5:
    if _preferences.language == "english":
        text "{size=+15}{font=[adv_font]}I regret to inform you, but it was you all the way...{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[adv_font]}Мне жаль это признавать, но сделала это всё именно ты...{/font}{/size}" yalign 0.5 xalign 0.5

screen pizda_text6:
    if _preferences.language == "english":
        text "{size=+15}{font=[adv_font]}Or, well, not exactly, they all did a killing blow themselves. But it was you and no one else who brought them to such a state.{/font}{/size}" yalign 0.5 xalign 0.5
    else:    
        text "{size=+15}{font=[adv_font]}Ну, или не совсем. Они все убили себя сами. Но довела их до такого состояния не кто иная, как ты.{/font}{/size}" yalign 0.5 xalign 0.5

screen pizda_text7:
    if _preferences.language == "english":
        text "{size=+15}{font=[adv_font]}Sayori actually had depression. And you oppressed her up until the moment that one morning she tied herself a noose and pulled herself out of chair.{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[adv_font]}У Сайори действительно была депрессия. И именно ты угнетала её вплоть до того, что как-то раз утром она связала себе петлю и сдёрнула себя со стула.{/font}{/size}" yalign 0.5 xalign 0.5

screen pizda_text8:
    if _preferences.language == "english":
        text "{size=+15}{font=[adv_font]}Yuri had self-harm problems. Her inner voice convinced her that she was doing everything right.{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[adv_font]}У Юри были проблемы с нанесением вреда себе. Её внутренний голос убеждал её в том, что она делает всё правильно.{/font}{/size}" yalign 0.5 xalign 0.5

screen pizda_text9:
    if _preferences.language == "english":
        text "{size=+15}{font=[adv_font]}And instead of dissuading her or convincing her to go to the therapist, you encouraged her to do so.{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[adv_font]}А ты, вместо того, чтобы отговаривать её от этого или убеждать сходить к психиатру, только подначивала её.{/font}{/size}" yalign 0.5 xalign 0.5

screen pizda_text10:
    if _preferences.language == "english":
        text "{size=+15}{font=[adv_font]}That went on up until the point where she completely lost her mind and it seemed to her that simply cutting veins is not enough.{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[adv_font]}И это продолжалось до того момента, пока у неё совсем не поехала крыша, и ей не показалось, что простого резания вен мало.{/font}{/size}" yalign 0.5 xalign 0.5

screen pizda_text11:
    if _preferences.language == "english":
        text "{size=+15}{font=[adv_font]}So she went to the extremes by stabbing herself to death. Obviosly, no one saved her.{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[adv_font]}И она пошла на крайние меры путём нанесения себе смертельных ножевых ранений. Спасти её, соответственно, не удалось.{/font}{/size}" yalign 0.5 xalign 0.5

screen pizda_text12:
    if _preferences.language == "english":
        text "{size=+15}{font=[adv_font]}As for Natsuki... She was so full of that no one takes her words seriously, so that one day she thought:{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[adv_font]}Что касается Нацуки... Ей настолько надоело то, что её никто не воспринимает всерьёз, что однажды она подумала:{/font}{/size}" yalign 0.5 xalign 0.5

screen pizda_text13:
    if _preferences.language == "english":
        text "{size=+15}{font=[ink_font]}Why bother anyway?{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[ink_font]}А зачем это всё нужно?{/font}{/size}" yalign 0.5 xalign 0.5

screen pizda_text14:
    if _preferences.language == "english":
        text "{size=+15}{font=[adv_font]}And broke her neck. No one saved her, either.{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[adv_font]}И свернула себе шею. Тоже насмерть.{/font}{/size}" yalign 0.5 xalign 0.5

screen pizda_text15:
    if _preferences.language == "english":
        text "{size=+15}{font=[adv_font]}Surely, there was no direct fault in {i}that{/i} case... But there was an indirect one. Because it was you who encouraged all her friends to mock her.{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[adv_font]}Конечно, в {i}этом{/i} твоей прямой вины нет... Но есть вина косвенная. Ведь именно ты подначивала всех её подруг насмехаться над ней.{/font}{/size}" yalign 0.5 xalign 0.5

screen pizda_text16:
    if _preferences.language == "english":
        text "{size=+15}{font=[adv_font]}What, you're saying there isn't? Because there surtely is.{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[adv_font]}Ну как же нет, если да?{/font}{/size}" yalign 0.5 xalign 0.5


screen scenario_2_double_text_suka:
    if _preferences.language == "english":
        text "{size=+15}{font=[adv_font]}Let's see how she'll 'get happy' by next Yuri's tasks.{/font}{/size}" yalign 0.475 xalign 0.5
        text "{size=+15}{font=[adv_font]}This is {b}far{/b} from the most complex book in the world after all.{/font}{/size}" yalign 0.525 xalign 0.5
    else:
        text "{size=+15}{font=[adv_font]}Посмотрим, как она «обрадуется» следующим заданиям от Юри.{/font}{/size}" yalign 0.475 xalign 0.5
        text "{size=+15}{font=[adv_font]}Это ведь {b}далеко{/b} не самая сложная книга в мире.{/font}{/size}" yalign 0.525 xalign 0.5

screen scenario_2_onest_text_suka:
    if _preferences.language == "english":
        text "{size=+15}{font=[ts_nvl_font2]}On the other hand, have {i}I{/i} ever been mentally sane?{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[ts_nvl_font2]}Впрочем, а {i}я{/i} когда-нибудь была психически здоровой?{/font}{/size}" yalign 0.5 xalign 0.5

screen scenario_2_onest_text_suka1:
    if _preferences.language == "english":
        text "{size=+15}{font=[ts_nvl_font2]}Oh buzz off, can't you see\nthe girl has just stopped crying,\nand you're pumping it all over again.{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[ts_nvl_font2]}Отстань уже, не видишь,\nдевочка только плакать перестала,\nа ты опять нагнетаешь.{/font}{/size}" yalign 0.5 xalign 0.5

screen scenario_3_onest_text_suka:
    if _preferences.language == "english":
        text "{size=+15}{font=[ts_nvl_font2]}But actually, I don't really condone it anyway...{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[ts_nvl_font2]}Впрочем, я же и так её не особо одобряю...{/font}{/size}" yalign 0.5 xalign 0.5

screen scenario_4_onest_text_suka:
    if _preferences.language == "english":
        text "{size=+15}{font=[adv_font]}Oh, that's easy: not only you are lazybones as hell, you're a hypocrite as well.{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[adv_font]}Всё очень просто: ты мало того, что лентяйка, каких поискать надо, так ещё и лицемерка.{/font}{/size}" yalign 0.5 xalign 0.5

screen scenario_4_onest_text_suka1:
    if _preferences.language == "english":
        text "{size=+15}{font=[adv_font]}You meant to say, {i}forever{/i}.{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[adv_font]}Ты хотела сказать, {i}навсегда{/i}.{/font}{/size}" yalign 0.5 xalign 0.5


screen chp_text_1:
    if _preferences.language == "english":
        text "{size=+15}{font=[ts_nvl_font2]}No... that's not possible...{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[ts_nvl_font2]}Нет... это невозможно...{/font}{/size}" yalign 0.5 xalign 0.5

screen chp_text_2:
    if _preferences.language == "english":
        text "{size=+15}{font=[ts_nvl_font2]}Three different girls, three so different problems...{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[ts_nvl_font2]}Три такие разные девочки, три такие разные проблемы...{/font}{/size}" yalign 0.5 xalign 0.5

screen chp_text_3:
    if _preferences.language == "english":
        text "{size=+15}{font=[ts_nvl_font2]}But all those girls, all those problems...{/font}{/size}" yalign 0.5 xalign 0.5
    else:    
        text "{size=+15}{font=[ts_nvl_font2]}И у всех этих девочек, у всех этих проблем...{/font}{/size}" yalign 0.5 xalign 0.5

screen chp_text_4:
    if _preferences.language == "english":
        text "{size=+15}{font=[ts_nvl_font2]}...have a common thing with me.{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[ts_nvl_font2]}...есть схожесть со мной.{/font}{/size}" yalign 0.5 xalign 0.5

screen chp_text_5:
    if _preferences.language == "english":
        text "{size=+15}{font=[ts_nvl_font2]}I have something like that as well.{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[ts_nvl_font2]}Похожее есть у меня.{/font}{/size}" yalign 0.5 xalign 0.5

screen chp_text_6:
    if _preferences.language == "english":
        text "{size=+15}{font=[ts_nvl_font2]}What a great fucking club I opened...{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[ts_nvl_font2]}Какой же охуенный клуб мы открыли...{/font}{/size}" yalign 0.5 xalign 0.5

screen chp_text_7:
    if _preferences.language == "english":
        text "{size=+15}{font=[ts_nvl_font2]}What a great club I opened...{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[ts_nvl_font2]}Какой же классный клуб мы открыли...{/font}{/size}" yalign 0.5 xalign 0.5

screen chp_text_8:
    if _preferences.language == "english":
        text "{size=+15}{font=[adv_font]}Or, well... A bit more...{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[adv_font]}Ну-у-у... или чуть больше...{/font}{/size}" yalign 0.5 xalign 0.5

screen chp_text_9:
    if _preferences.language == "english":
        text "{size=+15}{font=[adv_font]}Wake the hell up, you've got a girl that literally chokes on tears,\nwhile you just sit there and do nothing!{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[adv_font]}Очнись, у тебя девочка слезами захлёбывается,\nа ты просто стоишь и ничерта не делаешь!{/font}{/size}" yalign 0.5 xalign 0.5

screen chp_text_10:
    if _preferences.language == "english":
        text "{size=+15}{font=[adv_font]}Such an egoistic person you are...{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[adv_font]}Какая же ты всё-таки эгоистичная...{/font}{/size}" yalign 0.5 xalign 0.5

screen chp_text_11:
    if _preferences.language == "english":
        text "{size=+15}{font=[adv_font]}Except now it's gonna be your fault, and no one else's.{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[adv_font]}Только теперь уже будет твоя прямая вина, и ничья другая.{/font}{/size}" yalign 0.5 xalign 0.5

screen chp_text_12:
    if _preferences.language == "english":
        text "{size=+15}{font=[adv_font]}You said 'others' as if your club is a major one as well.{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[adv_font]}Ты так сказала «других», как будто ваш клуб тоже крупный.{/font}{/size}" yalign 0.5 xalign 0.5

screen chp_text_13:
    if _preferences.language == "english":
        text "{size=+15}{font=[adv_font]}Like you're so different from those two.{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[adv_font]}Как будто ты от них обеих отличаешься.{/font}{/size}" yalign 0.5 xalign 0.5

screen chp_text_14:
    if _preferences.language == "english":
        text "{size=+15}{font=[adv_font]}You meant to say, three.{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[adv_font]}Ты хотела сказать, троих.{/font}{/size}" yalign 0.5 xalign 0.5

screen chp_text_15:
    if _preferences.language == "english":
        text "{size=+15}{font=[adv_font]}That would never happen.{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[adv_font]}Который никогда не наступит.{/font}{/size}" yalign 0.5 xalign 0.5

screen chp_text_16:
    if _preferences.language == "english":
        text "{size=+15}{font=[adv_font]}As if you don't have enough attention already.{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[adv_font]}Как будто тебе и без того внимания недостаточно.{/font}{/size}" yalign 0.5 xalign 0.5

screen chp_text_17:
    if _preferences.language == "english":
        text "{size=+15}{font=[adv_font]}Like, stuck in an eternal Groundhog Week...{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[adv_font]}Например, застрял в вечной Неделе Сурка...{/font}{/size}" yalign 0.5 xalign 0.5

screen chp_text_18:
    if _preferences.language == "english":
        text "{size=+15}{font=[adv_font]}Only you think like that.{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[adv_font]}Так считаешь только ты.{/font}{/size}" yalign 0.5 xalign 0.5

screen chp_text_19:
    if _preferences.language == "english":
        text "{size=+15}{font=[adv_font]}That's more like it...{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[adv_font]}Вот это больше на правду походит...{/font}{/size}" yalign 0.5 xalign 0.5

screen chp_text_20:
    if _preferences.language == "english":
        text "{size=+15}{font=[ts_nvl_font2]}Or I'm confusing something..?{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[ts_nvl_font2]}Или я что-то путаю?..{/font}{/size}" yalign 0.5 xalign 0.5

screen chp_text_21:
    if _preferences.language == "english":
        text "{size=+15}{font=[ts_nvl_font2]}Looking back...\nMaybe I did\nhave to think for a bit...\nNot at that moment though.{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[ts_nvl_font2]}Оглядываясь назад...\nНаверное, подумать\nвсё-таки стоило...\nНо не в тот момент.{/font}{/size}" yalign 0.5 xalign 0.5

screen chp_text_22:
    if _preferences.language == "english":
        text "{size=+15}{font=[ts_nvl_font2]}But we were little girls back in the day, weren't we..?{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[ts_nvl_font2]}Впрочем, мы же раньше и были маленькими девочками?..{/font}{/size}" yalign 0.5 xalign 0.5

screen chp_text_23:
    if _preferences.language == "english":
        text "{size=+15}{font=[ts_nvl_font2]}But where there's a high point, there has to be a low one as well...{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[ts_nvl_font2]}Но там, где есть белая полоса, обязательно будет и чёрная...{/font}{/size}" yalign 0.5 xalign 0.5

screen chp_text_24:
    if _preferences.language == "english":
        text "{size=+15}{font=[adv_font]}If only you knew that festival you craved for so much will never happen...{/font}{/size}" yalign 0.5 xalign 0.5
    else:    
        text "{size=+15}{font=[adv_font]}Если бы ты только знала, что этого самого фестиваля так никогда и не будет...{/font}{/size}" yalign 0.5 xalign 0.5

screen chp_text_25:
    if _preferences.language == "english":
        text "{size=+15}{font=[ts_nvl_font2]}And, well, problems: every girl has a problem similar to mine.{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[ts_nvl_font2]}Ну и проблемы: у каждой из девочек есть общие со мной проблемы.{/font}{/size}" yalign 0.5 xalign 0.5

screen chp_text_26:
    if _preferences.language == "english":
        text "{size=+15}{font=[ts_nvl_font2]}Even though, as it turned out, that sincerity\nwas not so sincere...{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[ts_nvl_font2]}Пусть, как оказалось, эта искренность\nне была столь уж и искренней...{/font}{/size}" yalign 0.5 xalign 0.5


screen akt2_chp1_text:
    if _preferences.language == "english":
        text "{size=+15}{font=[ts_nvl_font2]}What the hell is that? I'm literally trouble magnet!{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[ts_nvl_font2]}Да что же это такое? Я же буквально источник всех проблем!{/font}{/size}" yalign 0.5 xalign 0.5

screen akt2_chp1_text1:
    if _preferences.language == "english":
        text "{size=+15}{font=[ts_nvl_font2]}What the hell is that? I'm literally trouble magnet!{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[ts_nvl_font2]}Да что же это такое? Я же буквально источник всех проблем!{/font}{/size}" yalign 0.5 xalign 0.5

screen akt2_chp1_text2:
    if _preferences.language == "english":
        text "{size=+15}{font=[ts_nvl_font2]}Not only I was so passed out yesterday, I also drove both me and my friend crazynuts!{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[ts_nvl_font2]}Мало того, что напилась в стельку вчера, так ещё и с утра довела и себя, и свою подругу, до истерики!{/font}{/size}" yalign 0.5 xalign 0.5

screen akt2_chp1_text3:
    if _preferences.language == "english":
        text "{size=+15}{font=[adv_font]}Let's see how you'll talk in a couple of cycles...{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[adv_font]}Посмотрим, как ты запоёшь через пару циклов...{/font}{/size}" yalign 0.5 xalign 0.5

screen akt2_chp1_text4:
    if _preferences.language == "english":
        text "{size=+15}{font=[ts_nvl_font2]}Cycles?..{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[ts_nvl_font2]}Циклов?..{/font}{/size}" yalign 0.5 xalign 0.5

screen akt2_chp1_text5:
    if _preferences.language == "english":
        text "{size=+15}{font=[adv_font]}Oh... scratch that... you'll understand later...{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[adv_font]}Да так... неважно... потом поймёшь...{/font}{/size}" yalign 0.5 xalign 0.5

screen akt2_chp1_text6:
    if _preferences.language == "english":
        text "{size=+15}{font=[ts_nvl_font2]}WHAT DO YOU KNOW? ANSWER ME!{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[ts_nvl_font2]}ЧТО ТЫ ЗНАЕШЬ? ОТВЕЧАЙ!{/font}{/size}" yalign 0.5 xalign 0.5


screen chp_5_text1:
    if _preferences.language == "english":
        text "{size=+15}{font=[adv_font]}You talk like that for now.{/font}{/size}" yalign 0.5 xalign 0.5
    else:
        text "{size=+15}{font=[adv_font]}Это ты сейчас так говоришь.{/font}{/size}" yalign 0.5 xalign 0.5
