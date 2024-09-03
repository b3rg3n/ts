# TRUE STORY KOLHOZ GALLERY
# ГОПНУЛ У DREAMTALE
# СО СВОИМИ НАРАБОТКАМИ, ЕСТЕСТВЕННО БЛЯТЬ
# Since 2024
init python:

    g = Gallery()

    page = 0
    gallery_mode = "cg"

    g.locked_button = "mod_assets/source/images/gui/gallery/not_opened_idle.webp"
    g.navigation = False

    rows = 4
    cols = 2
    cells = rows * cols

    gallery_cg = [
    "ts_mon_maman_2", "ts_mon_maman_3", "ts_mon_maman_4",
    "ts_mon_maman_5", "ts_mon_maman_6", "ts_mon_maman_8",
    "yurec_pizdec1", "yurec_pizdec2", "yurec_pizdec3",
    "yurec_pizdec4", "yurec_pizdec5", "yurec_pizdec6",
    "yurec_pizdec8", "yurec_pizdec9"
    ]

    gallery_bg = [
    "ts_bathroom", "ts_club", "ts_bedroom", "ts_city_day",
    "ts_closet", "ts_class", "ts_club2re", "ts_corridor", "ts_corridorrev",
    "ts_sayori_house", "ts_sky_fon", "ts_hotel_rec", "ts_office",
    "ts_roof", "ts_kitchen_night", "ts_waiting_room",
    "ts_hospital_corridor", "ts_hospital_room", "ts_emergency_room",
    "ts_darkbed", "ts_entrance_day", "ts_entrance_night", "ts_entrance_nolight", "ts_gost",
    "ts_gost_night", "ts_gost_sunset", "ts_house", "ts_house_monika_evening",
    "ts_kitchen", "ts_l5", "ts_l5old", "ts_light_off_corridor",
    "ts_living_room_late", "ts_living_room_night",
    "ts_pianoend", "ts_residential", "ts_sakura", "ts_sayori_bedroom", "ts_school_bathroom",
    "ts_school_bathroom1", "ts_school_bathroom2", "ts_school_courtyard_day", "ts_school_gate_day",
    "ts_school_gate_evening", "ts_stairs", "ts_stairsre", "ts_street_late"
    ]

init 101 python:

    for cg in gallery_cg:
        g.button(cg)
        g.image(im.Crop("mod_assets/source/images/cg/"+cg+".webp" , (0,0,1280,720)))
        g.unlock(cg)

    for bg in gallery_bg:
        g.button(bg)
        g.image(im.Crop("mod_assets/source/images/bg/"+bg+".webp" , (0,0,1280,720)))
        g.unlock(bg)

    g.transition = fade

screen gallery:

    tag menu
    modal True

    $ gallery_table = []
    if gallery_mode == "cg":
        $ gallery_table = gallery_cg
    else:
        $ gallery_table = gallery_bg

    $ len_table = len(gallery_table)

    frame background ts_anim + "zatemnenie.webp":
        if gallery_mode == "cg":
            textbutton translation_new["BG"] style "log_button" text_style "settings_link" xalign 0.5 yalign 0.92 activate_sound start_sound_suka hover_sound button_menu action (SetVariable('gallery_mode', "bg"), SetVariable('page', 0), ShowMenu("gallery")) at ts_preferences_anim
        elif gallery_mode == "bg":
            textbutton translation_new["CG"] style "log_button" text_style "settings_link" xalign 0.5 yalign 0.92 activate_sound start_sound_suka hover_sound button_menu action (SetVariable('gallery_mode', "cg"), SetVariable('page', 0), ShowMenu("gallery")) at ts_preferences_anim

        textbutton translation_new["Back"] style "log_button" text_style "settings_link" xalign 0.015 yalign 0.92 activate_sound start_sound_suka hover_sound button_menu action Return() at ts_preferences_anim

        grid rows cols xpos 0.09 ypos 0.18:
            $ cg_displayed = 0
            $ next_page = page + 1
            if next_page > int(len_table/cells):
                $ next_page = 0
            for n in range(0, len_table):
                if n < (page+1)*cells and n>=page*cells:
                    python:
                        if gallery_mode == "cg":
                            _t = im.Crop("mod_assets/source/images/cg/"+gallery_table[n]+".webp" , (0,0,1280,720))
                        elif gallery_mode == "bg":
                            _t = im.Crop("mod_assets/source/images/bg/"+gallery_table[n]+".webp" , (0,0,1280,720))
                        th = im.Scale(_t, 213, 120)
                        img = im.Composite((224,131),(5,5),im.Alpha(th,0.9),(0,0),im.Image("mod_assets/source/images/gui/gallery/thumbnail_idle.webp"))
                        imgh = im.Composite((224,131),(5,5),th,(0,0),im.Image("mod_assets/source/images/gui/gallery/thumbnail_hover.webp"))
                    add g.make_button(gallery_table[n], "mod_assets/source/images/gui/gallery/blank.webp", None, imgh, img, style="blank_button", bottom_margin=50, right_margin=50) at ts_preferences_anim
                    $ cg_displayed += 1

                    if n+1 == len_table:
                        $ next_page = 0

            for j in range(0, cells-cg_displayed):
                null

        if page != 0:
            imagebutton auto "mod_assets/source/images/gui/dialogue_box/backward_%s.webp" yalign 0.5 xalign 0.01 activate_sound start_sound_suka hover_sound button_menu action (SetVariable('page', page-1), ShowMenu("gallery")) at ts_preferences_anim
        imagebutton auto "mod_assets/source/images/gui/dialogue_box/forward_%s.webp" yalign 0.5 xalign 0.99 activate_sound start_sound_suka hover_sound button_menu action (SetVariable('page', next_page), ShowMenu("gallery")) at ts_preferences_anim

        python:
            def abc(n,k):
                l = float(n)/float(k)
                if l-int(l) > 0:
                    return int(l)+1
                else:
                    return l
            pages = str(page+1)+"/"+str(int(abc(len_table,cells)))
        text pages style "settings_link" xalign 0.985 yalign 0.92 at ts_preferences_anim
