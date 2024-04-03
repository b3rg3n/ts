# TRUE STORY SCREEN CREDITS
# by @b3rg3n
# Since 2024

init:

    $ style.credits = Style(style.default)
    $ style.credits.font  = "mod_assets/source/fonts/captureit.ttf"
    $ style.credits.color = "#fff"
    $ style.credits.drop_shadow = [ (1, 1), (1, 1), (1, 1), (1, 1) ]
    $ style.credits.drop_shadow_color = "#000"
    $ style.credits.italic = False
    $ style.credits.bold = False
    $ style.credits.text_align = 0.5
    $ style.credits.xmaximum = 0.8

    image credits = ParameterizedText(style = "credits", size = 50)

    define ts_credits = "Спасибо, что прошли полную версию мода!\n\nНадеемся, что мод оставил вам лишь приятные впечатления!\n\n\n\nВ моде использовались следующие BG:\nbedroom, class, club (club_skill), corridor,\nstreet, house, kitchen, residential - Team Salvato\nmusic_club - Team Salvato/Serenity Forge\nschool_gate (day/evening), school_courtyard - Kimagure After\ngost (day), vhod (day/night/nolight),\nliving_room (day/late/night) - Nuxill#7870\ngym_n, lockers_n - Vanishing Point\ndarkbed - Alex#9077\nstairs - Kimagure After; edited by Nuxill#7870\nbathroom - Uncle Mugen\nclub2re - Wheatley#3103; edited by MalukahMaker#2907, TheMelodyofGaming#7515\n\nAll BG's polished by BERGEN\n\nСпрайты:\nExtended OC sprites - originally from Absolution Chapter One by BaryonGod\nКаори - Hime Sprites by Daikaju Fanboy/BlackRabbitArtworks\nПодруги Нацуки - Himari Sprites by Prox#9492; Elena Sprites by ItzTuna/Elenathebullimom\nХирото (папа Моники) - StormBlazed76\nМама Моники - originally Dr. Bug from Dimensions by chiffmonkey\n\nКомпозиторы:\nDan Salvato\nSergey Eybog\nBetween August and December\n\nВ моде также использовалась следующая музыка:\nHallucinator - Mosh\nPixies - Where is My Mind (piano cover)\nJurrivh - Suicide Note\nMoe Era OST - Final Scene Soft\n\nЗвуки:\nDDLC SFX\nEverlasting Summer SFX\nSeven Summer Days SFX\nfreesound.org\n\nЕсли ваша работа была использована\nв моде, но ваше авторство\nне было указано -\nсвяжитесь с разработчиками.\nМы исправим это досадное недоразумение.\n\nКонец демо версии.\n\nЗа новостями\nпо дальнейшей разработке\nследите в нашем\n{a=https://discord.com/invite/8B3eKkU37q}Discord канале{/a}\nи\n{a=https://vk.com/teamanarkhisty}группе в вк{/a}.\n\nПродолжение следует...\n\n\n\n\n\n\n"

label good_credits_ts_label:

    python: # ОБНОВЛЯЕМ RPC
        try:
            rpc.update(state="Финал",details="Титры",large_image="credits",start=time.time())
        except AssertionError:
            pass

    $ persistent.rpclabel = "999"

    stop music fadeout 3
    scene black with ed_night_dis

    play music ts_good_credits fadein 2
    pause 2

    $ Chapter("True Story", time=3.25)
    $ Chapter("True Story", time=3.25)

    $ Chapter("  Моя история\nподошла к концу", time=3.25)
    $ Chapter("  Моя история\nподошла к концу", time=3.25)

    $ Chapter("   Признавайся -\nтебе же понравилось", time=3.25)
    $ Chapter("   Признавайся -\nтебе же понравилось", time=3.25)

    $ Chapter("Правда?", time=3.25)

    scene ts_intro_move_1
    show zatemnenie_light
    with ed_night_dis_faster

    $ TS.Screens(ts_showscreens)

    show ts_credits_bergen_1 at ts_show_credits_videosos
    
    show screen ts_good_credits_scr_1
    show screen ts_good_credits_scr_11

    pause 5

    $ TS.Screens(ts_hidescreens)

    show ts_credits_bergen_1 at ts_hide_credits_videosos

    show screen ts_good_credits_scr_1
    show screen ts_good_credits_scr_11

    pause 1.0

    scene ts_intro_move_2
    show zatemnenie_light
    with ed_night_dis_faster

    hide screen ts_good_credits_scr_1
    hide screen ts_good_credits_scr_11

    $ TS.Screens(ts_showscreens)

    show ts_credits_mad_1 at ts_show_credits_videosos
    
    show screen ts_good_credits_scr_2
    show screen ts_good_credits_scr_22

    pause 5

    $ TS.Screens(ts_hidescreens)

    show ts_credits_mad_1 at ts_hide_credits_videosos
    
    show screen ts_good_credits_scr_2
    show screen ts_good_credits_scr_22

    pause 1.0

    scene ts_intro_move_3
    show zatemnenie_light
    with ed_night_dis_faster

    hide screen ts_good_credits_scr_2
    hide screen ts_good_credits_scr_22

    $ TS.Screens(ts_showscreens)

    show ts_credits_bergen_1 at ts_show_credits_videosos
    
    show screen ts_good_credits_scr_3
    show screen ts_good_credits_scr_33

    pause 5

    $ TS.Screens(ts_hidescreens)

    show ts_credits_bergen_1 at ts_hide_credits_videosos
    
    show screen ts_good_credits_scr_3
    show screen ts_good_credits_scr_33

    pause 1.0

    scene ts_sakura
    show zatemnenie_light
    show lepestki_krutyatsa
    with ed_night_dis_faster

    show credits ts_credits:
        xalign 0.5
        ypos 1.05
        linear 100.0 ypos -6.28
    $ renpy.pause (110, hard=True)

    stop music fadeout 3

    hide screen ts_good_credits_scr_3
    hide screen ts_good_credits_scr_33

    scene black with dissolve2

    pause 1

    $ TS.Screens(ts_null_transform)

    $ persistent.badendmenuperedglitch = False
    $ persistent.badendmenuskipglitch = False
    $ persistent.badendmenu = False
    $ persistent.carter2menu = False
    $ persistent.carter3menu = False
    $ persistent.goodendmenu = True

    return


label bad_credits_ts_label:

    python: # ОБНОВЛЯЕМ RPC
        try:
            rpc.update(state="Финал",details="Титры",large_image="credits",start=time.time())
        except AssertionError:
            pass

    $ persistent.rpclabel = "999"

    stop music fadeout 3
    scene black with ed_night_dis

    play music ts_bad_credits

    $ Chapter("True Story", time=3.25)
    $ Chapter("True Story", time=3.25)

    $ Chapter("  Моя история\nподошла к концу", time=3.25)
    $ Chapter("  Моя история\nподошла к концу", time=3.25)

    $ Chapter("Тебя устроил исход?", time=3.25)
    $ Chapter("Тебя устроил исход?", time=3.25)

    $ Chapter("Правда?", time=3.25)

    scene ts_l5_glitch_pizdets at ts_coridor_glitch
    show m_rectstatic zorder 0
    show zatemnenie
    with ed_night_dis_faster

    $ TS.Screens(ts_showscreens)

    show ts_credits_bergen_1 at Glitch(_fps=120., glitch_strength=.3):
        xpos 0.2 ypos 0.2 alpha 0.0 subpixel True
        ease 1.0 xpos 0.2 ypos 0.4 alpha 1.0
    
    show screen ts_good_credits_scr_1
    show screen ts_good_credits_scr_11

    pause 5

    $ TS.Screens(ts_hidescreens)

    show ts_credits_bergen_1 at Glitch(_fps=120., glitch_strength=.3):
        xpos 0.2 ypos 0.4 alpha 1.0 subpixel True
        ease 1.0 xpos 0.2 ypos 0.2 alpha 0.0

    show screen ts_good_credits_scr_1
    show screen ts_good_credits_scr_11

    pause 1.0

    scene ts_club_glitch_pizdets at ts_coridor_glitch
    show m_rectstatic zorder 0
    show zatemnenie
    with ed_night_dis_faster

    hide screen ts_good_credits_scr_1
    hide screen ts_good_credits_scr_11

    $ TS.Screens(ts_showscreens)

    show ts_credits_mad_1 at Glitch(_fps=120., glitch_strength=.3):
        xpos 0.2 ypos 0.2 alpha 0.0 subpixel True
        ease 1.0 xpos 0.2 ypos 0.4 alpha 1.0
    
    show screen ts_good_credits_scr_2
    show screen ts_good_credits_scr_22

    pause 5

    $ TS.Screens(ts_hidescreens)

    show ts_credits_mad_1 at Glitch(_fps=120., glitch_strength=.3):
        xpos 0.2 ypos 0.4 alpha 1.0 subpixel True
        ease 1.0 xpos 0.2 ypos 0.2 alpha 0.0
    
    show screen ts_good_credits_scr_2
    show screen ts_good_credits_scr_22

    pause 1.0

    scene ts_kitchen_glitch_pizdets at ts_coridor_glitch
    show m_rectstatic zorder 0
    show zatemnenie
    with ed_night_dis_faster

    hide screen ts_good_credits_scr_2
    hide screen ts_good_credits_scr_22

    $ TS.Screens(ts_showscreens)

    show ts_credits_bergen_1 at Glitch(_fps=120., glitch_strength=.3):
        xpos 0.2 ypos 0.2 alpha 0.0 subpixel True
        ease 1.0 xpos 0.2 ypos 0.4 alpha 1.0
    
    show screen ts_good_credits_scr_3
    show screen ts_good_credits_scr_33

    pause 5

    $ TS.Screens(ts_hidescreens)

    show ts_credits_bergen_1 at Glitch(_fps=120., glitch_strength=.3):
        xpos 0.2 ypos 0.4 alpha 1.0 subpixel True
        ease 1.0 xpos 0.2 ypos 0.2 alpha 0.0
    
    show screen ts_good_credits_scr_3
    show screen ts_good_credits_scr_33

    pause 1.0

    scene vse_pizda_monike:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 2.5
        ease 5.0 xpos 0.66 ypos 0.44 rotate 44
        ease 5.0 xpos 0.7 ypos 1.0 zoom 3 rotate -22
        ease 5.0 xpos 0.5 ypos 0.0 zoom 2.5 rotate 0
        ease 5.0 xpos 0.8 ypos 0.75 rotate 22
        ease 0.66 zoom 4
        ease 1.0 zoom 2.5
        ease 5.0 xpos 0.5 ypos 0.5 rotate 0
        repeat

    show noise:
        alpha 0.25

    show black zorder 5 at ts_black_glitch
    show blackout_exh
    #show anim_exhausted

    with ed_night_dis_faster

    show credits ts_credits zorder 6:
        xalign 0.5
        ypos 1.05
        linear 100.0 ypos -6.28
    $ renpy.pause (110, hard=True)

    stop music fadeout 3

    hide screen ts_good_credits_scr_3
    hide screen ts_good_credits_scr_33

    scene black with dissolve2

    pause 1

    $ TS.Screens(ts_null_transform)

    $ persistent.badendmenuperedglitch = True
    $ persistent.badendmenuskipglitch = False
    $ persistent.badendmenu = True
    $ persistent.carter2menu = False
    $ persistent.carter3menu = False
    $ persistent.goodendmenu = False

    return

screen ts_good_credits_scr_1:
    text "{size=+35}{font=[cit_font]}Идея:{/font}{/size}" xalign 0.5 yalign 0.5

screen ts_good_credits_scr_11:
    text "{size=+35}{font=[cit_font]}BERGEN{/font}{/size}" xalign 0.5 yalign 0.65

screen ts_good_credits_scr_2:
    text "{size=+35}{font=[cit_font]}Сценарий:{/font}{/size}" xalign 0.65 yalign 0.5

screen ts_good_credits_scr_22:
    text "{size=+35}{font=[cit_font]}Maddie, The Mad{/font}{/size}" xalign 0.7 yalign 0.65

screen ts_good_credits_scr_3:
    text "{size=+35}{font=[cit_font]}Визуал:{/font}{/size}" xalign 0.5 yalign 0.5

screen ts_good_credits_scr_33:
    text "{size=+35}{font=[cit_font]}BERGEN{/font}{/size}" xalign 0.5 yalign 0.65