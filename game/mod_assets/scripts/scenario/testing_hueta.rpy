# ХУЕТА ДЛЯ ТЕСТОВ
label testing_label_blya:
    scene ts_club
    $ persistent.sprite_time = "day"
    show sayori 4z at t41
    show yuri 4f at t42
    show monika 1f at t43
    show natsuki 2e at t44
    "day"

    $ persistent.sprite_time = "cloudly"
    "cloudly"
    $ persistent.sprite_time = "sunset"
    "sunset"
    $ persistent.sprite_time = "night"
    "night"
    python: # ОБНОВЛЯЕМ RPC
        try:
            rpc.update(state=glitchtext(12),details="Снова что-то мутит",large_image="logogovna",start=time.time())
        except AssertionError:
            pass

    #$ persistent.sprite_time = "day"

    #$ persistent.sprite_time = "clodly"

    #$ persistent.sprite_time = "sunset"

    #$ persistent.sprite_time = "night"

    $ persistent.uncolorize = "none"

    #$ persistent.uncolorize = "lite"

    #$ persistent.uncolorize = "full"

    scene ts_emergency_room
    show ts_emergency_room_anim
    "Стандарт"
    hide ts_emergency_room_anim
    show ts_emergency_room_anim4
    "Быстрее"

    #python:
    #    import plyer

    #    plyer.notification.notify( message='Кампуктер скоро перезагрузится...',
    #        app_name='True Story',
            #app_icon='sample.jpg',
    #        title='Вешайся', )

    "Всё, пизда"

    show sayori 3o at f11
    show ts_glaza

    "23"

    "щас крашнет"
    #$ winerrorsuka()
    "ну?"

    show screen dialog("truestory.exe\n\nВ файлах скрипта обнаружена критическая ошибка. Попробуйте ещё раз.", ok_action=Return())



    "а этот"
    hide screen dialog
    scene ts_club
    show yuri 2l at i31
    show sayori 4s at i32
    show natsuki 1y at i33
    "Хуй"
    window hide
    show layer master at ZoomTransitionInto()
    pause 0.5
    scene ts_bathroom at ZoomTransitionExodus()
    pause 1.2
    "test"
    show ts_yrec_kill_nahui_suicide_blya at left
    show ts_sayori_zalagala_chereshnya:
        align (0.5, 0.15)
    show ts_maloletka_pozvonok_sloman_nahui at right
    $ persistent.uncolorize = "none"
    "ewfe"
    scene ts_club with memglitchbolee

    "fefke"
    $ persistent.ingame_pizda = False
    "офф"
    show layer screens at ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake)
    $ persistent.ingame_pizda = True
    "он"
    show layer screens at ts_null_transform
    $ persistent.ingame_pizda = False
    "офф"
##############
    show layer screens at ts_shake(ts_bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), ts_xypos(0.5,0.5,0.0), ts_super_shake)

    play sound slender
    $ persistent.ingame_pizda = True
    show ts_club_glitch_pizdets zorder 4 at ts_coridor_glitch
    show black zorder 5 at ts_black_glitch
    show blackout_exh zorder 5
    show anim_exhausted zorder 5
    show m_rectstatic zorder 5
    show natsuki ghost3 zorder 6 at Glitch(_fps=1000.)

    pause 2.5

    stop sound

    $ persistent.ingame_pizda = False

    scene ts_club
    show natsuki 1a at i11

    "Ахуеть"
###############
    return