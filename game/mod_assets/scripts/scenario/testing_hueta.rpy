# ХУЕТА ДЛЯ ТЕСТОВ
label testing_label_blya:

    python: # ОБНОВЛЯЕМ RPC
        try:
            rpc.update(state=glitchtext(12),details="Снова что-то мутит",large_image="logogovna",start=time.time())
        except AssertionError:
            pass

    #$ _window_show(dissolve)

    #image bg ext_beach_gray:
    #    'bg ext_beach_day'
    #    im.Grayscale("images/bg/ext_beach_day.jpg") with Dissolve(5)

    #image bg ext_library_red = im.Recolor("images/bg/ext_library_day.jpg", 139, 0, 0, 170)
    #image bg int_pantry_dark = im.MatrixColor(ed_images + "/bg/int_pantry.jpg", im.matrix.tint(0.35, 0.35, 0.35))
    #image bg int_storage_ruined_dark = im.MatrixColor(ed_images + "/bg/int_storage_ruined.jpg", im.matrix.tint(0.25, 0.25, 0.25))

    #image cg ed_another_camp:
    #    choice:
    #        'bg ext_bus_red' with Dissolve(3)
    #    choice:
    #        'bg ext_camp_entrance_red' with Dissolve(3)
    #    choice:
    #        'bg ext_road_red' with Dissolve(3)
    #    choice:
    #        'bg ext_sea_red' with Dissolve(3)
    #    choice:
    #        'bg ext_square_red' with Dissolve(3)
    #    choice:
    #        'bg ext_house_of_mt_red' with Dissolve(3)
    #    pause 2
    #    repeat

    #image anim ed_aidpost:
    #    contains:
    #        'bg int_aidpost_gray' with ed_blot8
    #        pause 8
    #        'bg int_aidpost_red' with ed_blot8
    #        pause 8
    #        repeat
    #    subpixel True
    #    anchor (0.5, 0.5)
    #    pos (0.5, 0.5)
    #    zoom 1
    #    ease 10 zoom 2.1
    #    block:
    #        linear 20 rotate 360
    #        rotate 0
    #        repeat
#    $ ed_blot8 = ImageDissolve(ed_images + "gui/dissolves/ed_blot.jpg", 8.0)
#    show ed_un_d2_smile_pioneer_2_night:
#        align (0.5, 0.5) zoom 1.2 alpha 1
#        ease 1 zoom 0.9 alpha 0

#    show ed_sl_kowai_night at ts_move(x1=0.15,x2=-0.5)
#    show ed_sh_kowai_night at ts_move(t=1.75,x1=0.9,x2=1.5)
#    show ed_el_kowai_night at ts_move(t=2.625,x1=0.6,x2=1.5)

#    show ed_mt_mite at ts_move(t=2,x1=-0.6,x2=0.4)
#    show ed_sl_fly at ts_move(t=2,x1=-0.4,x2=0.6)

    scene ts_club
    m "Ты готов?"
    window hide
    play sound ts_glitch5
    show nat_pizdos
    show natsuki_pizdec5
    pause 2.3
    stop sound
    hide nat_pizdos
    hide natsuki_pizdec5
    "Ахуеть, да?"

    play ambience rain_in
    scene ts_club_rain_shader
    show ts_club_rain_ovr

    m "Пиздатые шейдеры."

    scene ts_living_room_rain_shader
    show ts_living_room_rain_ovr

    m "Ещё пизже."

    play ambience rain_out

    scene ts_shkola_rain
    show ts_rain

    m "Анимация."

    scene ts_street_rain
    show ts_rain

    m "Ещё анимация."

    return

    scene ts_club
    m "Тест"
    $ ts_uncolorize_lite()
    m "чуток обесцветили"
    $ ts_uncolorize_full()
    m "Вообще пиздец"
    $ ts_uncolorize_off()
    "Убрал"
    scene ts_corridor
    $ ts_uncolorize_lite()
    m "чуток обесцветили"
    $ ts_uncolorize_full()
    m "Вообще пиздец"
    $ ts_uncolorize_off()
    "Убрал"
    scene ts_house
    $ ts_uncolorize_lite()
    m "чуток обесцветили"
    $ ts_uncolorize_full()
    m "Вообще пиздец"
    $ ts_uncolorize_off()
    "Убрал"
    scene ts_house_monika_evening
    $ ts_uncolorize_lite()
    m "чуток обесцветили"
    $ ts_uncolorize_full()
    m "Вообще пиздец"
    $ ts_uncolorize_off()
    "Убрал"

    show elena a at ln11
    "без"
    $ ts_sunset_time()
    "чуток"
    $ ts_night_time()
    "ночь"
    $ ts_day_time()
    "день"

    show elena a1 at ln11
    "без"
    $ ts_sunset_time()
    "чуток"
    $ ts_night_time()
    "ночь"
    $ ts_day_time()
    "день"

    show elena b at ln11
    "без"
    $ ts_sunset_time()
    "чуток"
    $ ts_night_time()
    "ночь"
    $ ts_day_time()
    "день"

    show elena q at ln11
    "без"
    $ ts_sunset_time()
    "чуток"
    $ ts_night_time()
    "ночь"
    $ ts_day_time()
    "день"

    return

    $ TS.Screens(ts_hidescreens)
    " {w=1.0}{nw}"

    scene ts_club with dissolve:
        blur 9.0

    $ TS.Screens(ts_showscreens)

    if not persistent.first_poem:
        $ persistent.first_poem = True
        show expression "mod_assets/source/images/gui/poem_dismiss.webp" as poem_dismiss:
            xpos 1050 ypos 590

    play sound page_turn

    show screen poem(poem_test)

    pause

    play sound page_turn
    $ TS.Screens(ts_hidescreens)
    pause 1.0
    hide screen poem
    hide poem_dismiss
    scene ts_club with dissolve
    show monika 2bn at rn11

    $ TS.Screens(ts_showscreens)

    m "Ахуенно, я считаю."
    m "Пиздатый блюр."

    show elena a test at rn11
    pause

    $ ts_day_time()

    pause

    $ ts_sunset_time()

    pause
##############
    $ TS.Screens(ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake))
    $ pps = 5

    play sound slender

    show ts_club_glitch_pizdets zorder 4 at ts_coridor_glitch
    show black zorder 5 at ts_black_glitch
    show blackout_exh zorder 5
    show anim_exhausted zorder 5
    show m_rectstatic zorder 5
    show natsuki_demon_glitch_pizdets zorder 6 at Glitch(_fps=1000.)

    pause 2.5

    stop sound

    scene ts_club
    show natsuki 1a at i11

    "Ахуеть"
###############
    return

    window hide
    play music td
    show s_kill_bg2
    show s_kill2
    show s_kill_bg as s_kill_bg at s_kill_bg_start
    show s_kill as s_kill at s_kill_start
    pause 3.75
    show s_kill_bg2 as s_kill_bg
    show s_kill2 as s_kill
    pause 0.01

    play sound s_kill_glitch1
    show s_kill_bg2 as bg1 at br_glitches(_fps=160, glitch_strength=1)
    $ renpy.pause(0.25, hard=True)
    stop sound

    hide s_kill_bg
    hide s_kill
    show s_kill_bg_zoom zorder 1
    show s_kill_bg2_zoom zorder 1
    show s_kill_zoom zorder 3
    show s_kill2_zoom zorder 3
    show s_kill as s_kill_zoom_trans zorder 3:
        truecenter
        alpha 0.5
        zoom 2.0 xalign 0.5 yalign 0.05
        pause 0.5
        dizzy(1, 1.0)
    pause 2.0
    show noise zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.25
    show vignette zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.75
    pause 1.5
    show anarchy_glitch_logo zorder 2 at ts_coridor_glitch
    pause 1.5

    play sound s_kill_glitch1
    show anarchy_glitch_logo as bg1 at br_glitches(_fps=160, glitch_strength=1) zorder 2
    $ renpy.pause(0.25, hard=True)
    stop sound
    hide anarchy_glitch_logo

    pause 4.0

    play sound s_kill_glitch1
    show anarchy_glitch_logo as bg1 at br_glitches(_fps=160, glitch_strength=1) zorder 2
    $ renpy.pause(0.25, hard=True)
    stop sound
    hide anarchy_glitch_logo

    hide anarchy_glitch_logo
    show splash_glitch2 zorder 2
    show splash_glitch_m zorder 2
    show splash_glitch_n zorder 2
    show splash_glitch_y zorder 2
    pause 0.75
    hide white
    hide splash_glitch2
    hide splash_glitch_m
    hide splash_glitch_n
    hide splash_glitch_y
    show exception_bg zorder 2
    show fake_exception zorder 2:
        xpos 0.1 ypos 0.05
    show fake_exception2 zorder 2:
        xpos 0.1 ypos 0.15
    pause 6.0

    stop music fadeout 4
    play sound coldazvuk
    pause 4.3
    scene black
    pause 2


    return














    window hide

    show exception_bg zorder 2
    show fake_exception zorder 2:
        xpos 0.1 ypos 0.05
    show fake_exception2 zorder 2:
        xpos 0.1 ypos 0.15

    "..."

    $ TS.Screens(ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake))
    $ pps = 5

    play sound_loop psy_fast_3

    show anarchy_glitch_logo zorder 4 at ts_coridor_glitch
    show black zorder 5 at ts_black_glitch
    show blackout_exh zorder 5
    show anim_exhausted zorder 5
    show m_rectstatic zorder 5

    "Ну типа..."

    hide fake_exception
    hide fake_exception2
    hide exception_bg

    #scene ts_class
    #show sayori 1a at t61
    #show monika 1a at t62
    #show yuri 1a at t63
    #show kaori 22a at t64
    #show natsuki 1a at t65
    #show hiroto 1a at t66

    show sayori 1a at t11:
        shader "example.gradient"
        u_gradient_left (1.0, 0.0, 0.0, 1.0)
        u_gradient_right (0.0, 0.0, 1.0, 1.0)

    "Так?"

    show ts_street_rain
    "Хуй"
    scene black
    show ts_school_gate_day_rain
    "хуй"
    scene black
    show ts_city_day_rain
    "елда"

    hide sayori

    show yuri 1a at Glitch(_fps=20., color_range1="c00a", color_range2="f00", glitch_strength=.5)

    "Хуй"

    hide yuri

    show natsuki 1a at Glitch(_fps=1000.)
    "Ускорим анимацию."
    hide natsuki
    show kaori 22a at Glitch(_fps=1000., glitch_strength=.3)
    "Усилим эффект."
    hide kaori
    show hiroto 1a at Glitch(_fps=1000., glitch_strength=.3, color_range1="#0a00", color_range2="0f0")

    "Пизда"

    hide hiroto

    pause 1
    scene ts_class at ts_blur_zadnika
    show zatemnenie_light
    with Dissolve(1.0)
    pause 1

    show chess1 at ts_chess_move_up
    pause 1

    $ TS.Screens(ts_showscreens)

    m "Пришло моё время..."

    show monika 1a onlayer front at t11

    "хуй"

    show ts_club at ts_coridor_glitch
    show monika 1a at t11
    show black zorder 5 at ts_black_glitch
    show blackout_exh
    show anim_exhausted

    $ TS.Screens(ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake))

    show m_rectstatic zorder 0

    m 1b "Хуй"

    m 2a "Пизда"

    return