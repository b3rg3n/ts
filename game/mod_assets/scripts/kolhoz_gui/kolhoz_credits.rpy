# TRUE STORY SCREEN CREDITS
# by @b3rg3n
# Since 2024

init:

    $ style.credits = Style(style.default)
    $ style.credits.font  = ts_fonts + "captureit.ttf"
    $ style.credits.color = "#fff"
    $ style.credits.drop_shadow = [ (1, 1), (1, 1), (1, 1), (1, 1) ]
    $ style.credits.drop_shadow_color = "#000"
    $ style.credits.italic = False
    $ style.credits.bold = False
    $ style.credits.text_align = 0.5
    $ style.credits.xmaximum = 0.8

    image credits = ParameterizedText(style = "credits", size = 50)

    define ts_credits = "Спасибо, что прошли полную версию мода!\n\nНадеемся, что мод оставил вам лишь приятные впечатления!\n\n\n\nФоновые изображения:\n\nTeam Salvato/Serenity Forge\nKimagure After\nNuxill\nUncle Mugen\nVanishingPoint\nи другие...\n\n\nСпрайты:\n\nOriginal DDLC Cast - Team Salvato\nExtended OC sprites - originally from Absolution by BaryonGod\nMonika Pajamas Sprite - SovietSpartan\nSayori Pajamas Sprite - WretchedTeam\nМира - Kuninobu Spritepack by certified cabbage, AjTheFunky\nКаори - Hime Spritepack by BlackRabbitArtworks\nХирото (папа Моники) - StormBlazed76\nМинами (мама Моники) - Mrs. Ida spritepack by kutaba_ree, SYwaves, Donkyhotay (originally appeared in Doki Doki Club Meetings by KrazyCaley)\nАдминистратор Сайка - originally Within's Monika's mom by u/BassPon3, StormBlazed76\nДиректор Раддан - originally Within's Monika's dad by u/BassPon3, StormBlazed76\nМагнолия Карлсен - originally Dr. Bug from Dimensions by chiffmonkey\n\n\nКомпозиторы:\n\nDan Salvato\nSergey Eybog\nBetween August and December\nThe Distorion\n\n\nВсе треки можно послушать в музыкальной комнате.\nТам же указаны точные названия.\n\n\nЗа код и способы реализации респектую лично:\n\nrmcj0\nSuperRage\nsalotor\ndreamtale\nNai@MakeVisualNovels\nFeniks\n\n\nЗаходите на наш \n{a=https://discord.com/invite/8B3eKkU37q}Discord сервер{/a},\n{a=https://vk.com/teamanarkhisty}группу в ВК{/a}\nи на наш {a=https://boosty.to/team_anarkhisty}Boosty{/a}.\n\n\n\n\nКонец.\n\n\n\n\n\n\n"

label good_credits_ts_label:

    python: # ОБНОВЛЯЕМ RPC
        try:
            rpc.update(state="Финал",details="Титры",large_image="credits",start=time.time())
        except AssertionError:
            pass

    $ persistent.rpclabel = "999"

    $ persistent.badendmenuperedglitch = False
    $ persistent.badendmenuskipglitch = False
    $ persistent.badendmenu = False
    $ persistent.carter2menu = False
    $ persistent.carter3menu = False
    $ persistent.goodendmenu = True

    stop music fadeout 3
    scene black with ed_night_dis

    play music ts_good_credits fadein 0.5
    pause 0.5#2

    $ Chapter("True Story", time=3.25)
    $ Chapter("True Story", time=3.25)

    $ Chapter("    Моя история\nподошла к концу", time=3.25)
    $ Chapter("    Моя история\nподошла к концу", time=3.25)

    $ Chapter("     Признавайся -\nтебе же понравилось", time=3.25)
    $ Chapter("     Признавайся -\nтебе же понравилось", time=3.25)

    $ Chapter("Правда?", time=3.25)

    scene ts_intro_move_1
    show zatemnenie_light
    with ed_night_dis_faster

    show layer screens at ts_showscreens

    show ts_credits_bergen_1 at ts_show_credits_videosos
    
    show screen ts_good_credits_scr_1
    show screen ts_good_credits_scr_11

    pause 5

    show layer screens at ts_hidescreens

    show ts_credits_bergen_1 at ts_hide_credits_videosos

    show screen ts_good_credits_scr_1
    show screen ts_good_credits_scr_11

    pause 1.0

    scene ts_intro_move_2
    show zatemnenie_light
    with ed_night_dis_faster

    hide screen ts_good_credits_scr_1
    hide screen ts_good_credits_scr_11

    show layer screens at ts_showscreens

    show ts_credits_mad_1 at ts_show_credits_videosos
    
    show screen ts_good_credits_scr_2
    show screen ts_good_credits_scr_22

    pause 5

    show layer screens at ts_hidescreens

    show ts_credits_mad_1 at ts_hide_credits_videosos
    
    show screen ts_good_credits_scr_2
    show screen ts_good_credits_scr_22

    pause 1.0

    scene ts_intro_move_3
    show zatemnenie_light
    with ed_night_dis_faster

    hide screen ts_good_credits_scr_2
    hide screen ts_good_credits_scr_22

    show layer screens at ts_showscreens

    show ts_credits_fedya_1 at ts_show_credits_videosos_fedya
    
    show screen ts_good_credits_scr_3
    show screen ts_good_credits_scr_33

    pause 5

    show layer screens at ts_hidescreens

    show ts_credits_fedya_1 at ts_hide_credits_videosos_fedya

    show screen ts_good_credits_scr_3
    show screen ts_good_credits_scr_33

    pause 1.0

    scene ts_sakura
    show zatemnenie_light
    show lepestki_krutyatsa
    with ed_night_dis

    pause 1.3

    show credits ts_credits:
        xalign 0.5
        ypos 1.05
        linear 100.0 ypos -6.28
    $ renpy.pause (75, hard=True)

    stop music fadeout 3

    hide screen ts_good_credits_scr_3
    hide screen ts_good_credits_scr_33

    scene black with dissolve2

    pause 1

    show layer screens at ts_null_transform

    return


label bad_credits_ts_label:

    python: # ОБНОВЛЯЕМ RPC
        try:
            rpc.update(state="Финал",details="Титры",large_image="credits",start=time.time())
        except AssertionError:
            pass

    $ persistent.rpclabel = "999"

    $ persistent.badendmenuperedglitch = True
    $ persistent.badendmenuskipglitch = False
    $ persistent.badendmenu = True
    $ persistent.carter2menu = False
    $ persistent.carter3menu = False
    $ persistent.goodendmenu = False

    stop music fadeout 3
    scene black with ed_night_dis

    play music ts_bad_credits

    $ Chapter("True Story", time=3.25)
    $ Chapter("True Story", time=3.25)

    $ Chapter("    Моя история\nподошла к концу", time=3.25)
    $ Chapter("    Моя история\nподошла к концу", time=3.25)

    $ Chapter("     Признавайся -\nтебе же понравилось", time=3.25)
    $ Chapter("     Признавайся -\nтебе же понравилось", time=3.25)

    $ Chapter("Правда?", time=3.25)

    scene ts_l5_glitch_pizdets at ts_coridor_glitch
    show m_rectstatic zorder 0
    show zatemnenie
    with ed_night_dis_faster

    show layer screens at ts_showscreens

    show bergencheek_pizdos:
        xpos 0.2 ypos 0.2 alpha 0.0 subpixel True
        ease 1.0 xpos 0.2 ypos 0.4 alpha 1.0
    
    show screen ts_good_credits_scr_1
    show screen ts_good_credits_scr_11

    pause 5

    show layer screens at ts_hidescreens

    show bergencheek_pizdos:
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

    show layer screens at ts_showscreens

    show vladick_pizdos:
        xpos 0.2 ypos 0.2 alpha 0.0 subpixel True
        ease 1.0 xpos 0.2 ypos 0.4 alpha 1.0
    
    show screen ts_good_credits_scr_2
    show screen ts_good_credits_scr_22

    pause 5

    show layer screens at ts_hidescreens

    show vladick_pizdos:
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

    show layer screens at ts_showscreens

    show fedya_pizdos:
        xpos 0.125 ypos 0.01 alpha 0.0 subpixel True
        ease 1.0 xpos 0.125 ypos 0.2 alpha 1.0
    
    show screen ts_good_credits_scr_3
    show screen ts_good_credits_scr_33

    pause 5

    show layer screens at ts_hidescreens

    show fedya_pizdos:
        xpos 0.125 ypos 0.2 alpha 1.0 subpixel True
        ease 1.0 xpos 0.125 ypos 0.01 alpha 0.0
    
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
    $ renpy.pause (75, hard=True)

    stop music fadeout 3

    hide screen ts_good_credits_scr_3
    hide screen ts_good_credits_scr_33

    scene black with dissolve2

    pause 1

    show layer screens at ts_null_transform

    return

screen ts_good_credits_scr_1:
    text translation_new["ts_credits_ending1"] style "credits_moda" size 75 text_align 0.5 yalign 0.5 xalign 0.65 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim

screen ts_good_credits_scr_11:
    text translation_new["ts_crd_mishlent"] style "credits_moda" size 75 text_align 0.5 yalign 0.65 xalign 0.6 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim

screen ts_good_credits_scr_2:
    text translation_new["ts_credits_ending2"] style "credits_moda" size 75 text_align 0.5 yalign 0.5 xalign 0.65 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim

screen ts_good_credits_scr_22:
    text translation_new["ts_crd_vladick"] style "credits_moda" size 75 text_align 0.5 yalign 0.65 xalign 0.7 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim

screen ts_good_credits_scr_3:
    text translation_new["ts_credits_ending3"] style "credits_moda" size 75 text_align 0.5 yalign 0.7 xalign 0.15 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim
    text translation_new["ts_credits_ending4"] style "credits_moda" size 75 text_align 0.5 yalign 0.7 xalign 0.85 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim

screen ts_good_credits_scr_33:
    text translation_new["ts_crd_fedya"] style "credits_moda" size 75 text_align 0.5 yalign 0.85 xalign 0.165 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim
    text translation_new["ts_crd_cgshki"] style "credits_moda" size 75 text_align 0.5 yalign 0.85 xalign 0.92 color "#FFFFFF" antialias True kerning 2 at ts_preferences_anim