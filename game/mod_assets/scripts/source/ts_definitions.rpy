# TRUE STORY BG's
# by @b3rg3n
# Since 2024

init:
###ЦГ
    image ts_anarchy = Image(ts_images + "anarchy/anarchisty.webp")
    image ts_anarchy1 = Image(ts_images + "anarchy/anarchisty11.webp")


    image ts_intro_1 = ts_images + "intro/intro1.webp"
    image ts_intro_2 = ts_images + "intro/intro2.webp"
    image ts_intro_3 = ts_images + "intro/intro3.webp"
    image ts_intro_31 = ts_images + "intro/intro31.webp"
    image ts_intro_4 = ts_images + "intro/intro4.webp"

    image ts_menu_art_carter2_night = ts_images + "intro/menu/menu_art_night.webp"

    image ts_menu_art_carter2_night1 = ts_images + "intro/menu/menu_art_night1.webp"

    image ts_menu_art3_night = ts_images + "intro/menu/ts_menu_art3_night.webp"

    image mon_piano = ts_images + "intro/menu/mon_piano.webp"
    image mon_piano_glitch = ts_images + "intro/menu/mon_piano_glitch.webp"
    image mon_piano_glitch1 = ts_images + "intro/menu/mon_piano_glitch1.webp"
    image mon_piano_glitch2 = ts_images + "intro/menu/mon_piano_glitch2.webp"
    image mon_piano_glitch3 = ts_images + "intro/menu/mon_piano_glitch3.webp"

    image mon_piano_another = ts_images + "intro/menu/mon_piano_another.webp"
    image mon_piano_another_glitch = ts_images + "intro/menu/mon_piano_another_glitch.webp"
    image mon_piano_another_glitch1 = ts_images + "intro/menu/mon_piano_another_glitch1.webp"
    image mon_piano_another_glitch2 = ts_images + "intro/menu/mon_piano_another_glitch2.webp"
    image mon_piano_another_glitch3 = ts_images + "intro/menu/mon_piano_another_glitch3.webp"

    image mon_piano_start = ts_cg + "mon_piano_start.webp"

    image yurec_pizdec1 = ts_cg + "yurec_pizdec/v1.webp"
    image yurec_pizdec2 = ts_cg + "yurec_pizdec/v2.webp"
    image yurec_pizdec3 = ts_cg + "yurec_pizdec/v3.webp"
    image yurec_pizdec4 = ts_cg + "yurec_pizdec/v4.webp"
    image yurec_pizdec5 = ts_cg + "yurec_pizdec/v5.webp"
    image yurec_pizdec6 = ts_cg + "yurec_pizdec/v6.webp"
    image yurec_pizdec7 = ts_cg + "yurec_pizdec/v7.webp"
    image yurec_pizdec8 = ts_cg + "yurec_pizdec/v8.webp"
    image yurec_pizdec9 = ts_cg + "yurec_pizdec/v9.webp"

###GLITCH
    image natsuki_pizdec = ts_cg + "glitch_kolhoz/natsuki_pizdec.webp"
    image natsuki_pizdec1 = ts_cg + "glitch_kolhoz/natsuki_pizdec1.webp"
    image natsuki_pizdec2 = ts_cg + "glitch_kolhoz/natsuki_pizdec2.webp"
    image natsuki_pizdec3 = ts_cg + "glitch_kolhoz/natsuki_pizdec3.webp"
    image natsuki_pizdec4 = ts_cg + "glitch_kolhoz/natsuki_pizdec4.webp"

    image natsuki_pizdec5 = LiveComposite((1280,720), (0,0), ts_cg + "pustota.webp", (882,325), "n_rects1", (732,400), "n_rects2", (850,475), "n_rects3")


###CREDITS
    image ts_credits_mad_1 = ts_images + "credits/ts_credits_mad_1.webp"
    image ts_credits_mad_2 = ts_images + "credits/ts_credits_mad_2.webp"
    image ts_credits_mad_3 = ts_images + "credits/ts_credits_mad_3.webp"
    image ts_credits_mad_4 = ts_images + "credits/ts_credits_mad_4.webp"

    image ts_credits_bergen_1 = ts_images + "credits/ts_credits_bergen_1.webp"
    image ts_credits_bergen_2 = ts_images + "credits/ts_credits_bergen_2.webp"
    image ts_credits_bergen_3 = ts_images + "credits/ts_credits_bergen_3.webp"
    image ts_credits_bergen_4 = ts_images + "credits/ts_credits_bergen_4.webp"

###БГ

    image ts_light_off_corridor = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "light_off_corridor.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "light_off_corridor.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "light_off_corridor.webp") )

    image ts_club = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "club.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "club.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "club.webp") )

    image ts_bathroom = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "bathroom.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "bathroom.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "bathroom.webp") )

#
    image ts_pianoend = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "music_club.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "music_club.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "music_club.webp") )

    image ts_living_room_night = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "living_room_night.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "living_room_night.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "living_room_night.webp") )

    image ts_living_room_late_night = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "living_room_late_night.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "living_room_late_night.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "living_room_late_night.webp") )

    image ts_living_room_late = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "living_room_late.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "living_room_late.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "living_room_late.webp") )

    image ts_living_room = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "living_room_day.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "living_room_day.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "living_room_day.webp") )

    image ts_entrance_day = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "entrance_day.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "entrance_day.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "entrance_day.webp") )

    image ts_hotel = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "hotel.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "hotel.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "hotel.webp") )

    image ts_notebook_glitch = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "notebook-glitch.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "notebook-glitch.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "notebook-glitch.webp") )

    image ts_notebook = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "notebook.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "notebook.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "notebook.webp") )

    image ts_sayori_bedroom = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "sayori_bedroom.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "sayori_bedroom.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "sayori_bedroom.webp") )

    image ts_city_day = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "city_day.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "city_day.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "city_day.webp") )

    image ts_vhod_nolight = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "entrance_nolight.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "entrance_nolight.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "entrance_nolight.webp") )

    image ts_vhod_night = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "entrance_night.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "entrance_night.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "entrance_night.webp") )

    image ts_street_late = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "street_late.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "street_late.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "street_late.webp") )

    image ts_street = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "astreet.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "astreet.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "astreet.webp") )

    image ts_stairs = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "stairs.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "stairs.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "stairs.webp") )

    image ts_school_gate_evening = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "school_gate_evening.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "school_gate_evening.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "school_gate_evening.webp") )

    image ts_school_gate_day = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "school_gate_day.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "school_gate_day.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "school_gate_day.webp") )

    image ts_school_courtyard_day = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "school_courtyard_day.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "school_courtyard_day.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "school_courtyard_day.webp") )

    image ts_school_bathroom2 = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "school_bathroom2.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "school_bathroom2.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "school_bathroom2.webp") )

    image ts_school_bathroom1 = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "school_bathroom1.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "school_bathroom1.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "school_bathroom1.webp") )

    image ts_school_bathroom = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "school_bathroom.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "school_bathroom.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "school_bathroom.webp") )

    image ts_sakura = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "sakura.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "sakura.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "sakura.webp") )

    image ts_residential = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "residential.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "residential.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "residential.webp") )

    image ts_l5old = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "l5old.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "l5old.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "l5old.webp") )

    image ts_l5 = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "l5.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "l5.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "l5.webp") )

    image ts_kitchen = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "kitchen.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "kitchen.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "kitchen.webp") )

    image ts_house2_night = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "house2_night.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "house2_night.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "house2_night.webp") )

    image ts_house_monika_evening = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "house_monika_evening.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "house_monika_evening.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "house_monika_evening.webp") )

    image ts_house = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "house.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "house.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "house.webp") )

    image ts_gym = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "gym_n.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "gym_n.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "gym_n.webp") )

    image ts_gost_sunset = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "gost_sunset.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "gost_sunset.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "gost_sunset.webp") )

    image ts_gost_night = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "gost_night.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "gost_night.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "gost_night.webp") )

    image ts_gost = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "gost.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "gost.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "gost.webp") )

    image ts_darkbed = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "darkbed.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "darkbed.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "darkbed.webp") )

    image ts_corridor = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "corridor.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "corridor.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "corridor.webp") )

    image ts_club2re = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "club2re.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "club2re.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "club2re.webp") )

    image ts_class = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "class.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "class.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "class.webp") )

    image ts_bedroom = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "bedroom.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "bedroom.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "bedroom.webp") )

    image ts_corridorrev = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "corridorrev.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "corridorrev.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "corridorrev.webp") )

    image ts_stairsre = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "stairsre.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "stairsre.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "stairsre.webp") )

    image ts_street1 = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "street1.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "street1.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "street1.webp") )

    image ts_jstreet = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "jstreet.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "jstreet.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "jstreet.webp") )

    image ts_closet = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "closet.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "closet.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "closet.webp") )

    image ts_cafeteria = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "cafeteria-rain.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "cafeteria-rain.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "cafeteria-rain.webp") )

###ЗАБЛЮРЕНО НАХОЙ
    image ts_club_blur = im.Blur(ts_bg + "club.webp", 3.0)
    image ts_club_blur9 = im.Blur(ts_bg + "club.webp", 9.0)

###ОВЕРЛЕИ
    image ts_club_rain_ovr = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ovr/club_rain_ovr.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ovr/club_rain_ovr.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ovr/club_rain_ovr.webp") )

    image ts_club_rain_ovr1 = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ovr/club_rain_ovr1.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ovr/club_rain_ovr1.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ovr/club_rain_ovr1.webp") )

    image ts_living_room_rain_ovr = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ovr/living_room_rain_ovr.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ovr/living_room_rain_ovr.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ovr/living_room_rain_ovr.webp") )

    image ts_class_rain_ovr = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ovr/class_rain_ovr.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ovr/class_rain_ovr.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ovr/class_rain_ovr.webp") )

    image ts_corridor_rain_ovr = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ovr/corridor_rain_ovr.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ovr/corridor_rain_ovr.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ovr/corridor_rain_ovr.webp") )

    image ts_shkola_rain = ts_bg + "courtyard-rain.webp"
    image ts_street_rain = ts_bg + "street7.webp"

    image ts_house_rain_ovr = ts_bg + "ovr/house_rain_ovr.webp"
    image ts_shkola_rain_ovr = ts_bg + "ovr/shkola_rain_ovr.webp"
    image ts_street_rain_ovr = ts_bg + "ovr/street_rain_ovr.webp"

###ЛОГО ХУЙНИ
    image ts_logo = "mod_assets/source/images/gui/ts_logo.webp"
    image ts_logo_menu = "mod_assets/source/images/gui/ts_logo_menu.webp"

###ШЕЙДЕРЫ

    image ts_class_rain = ts_bg + "ovr/class_rain.webp"
    image ts_living_room_rain = ts_bg + "ovr/living_room_rain.webp"
    image ts_club_rain = ts_bg + "ovr/club_rain.webp"
    image ts_club_rain1 = ts_bg + "ovr/club_rain1.webp"
    image ts_corridor_rain = ts_bg + "ovr/ts_corridor_rain.webp"

    image ts_class_rain_shader = RainOnWindow("ts_class_rain", width = 1280, height = 720, rainamount = 0.25)
    image ts_living_room_rain_shader = RainOnWindow("ts_living_room_rain", width = 1280, height = 720, rainamount = 0.25)
    image ts_club_rain_shader = RainOnWindow("ts_club_rain", width = 1280, height = 720, rainamount = 0.25)
    image ts_corridor_rain_shader = RainOnWindow("ts_corridor_rain", width = 1280, height = 720, rainamount = 0.25)
    image ts_club_rain_shader1 = RainOnWindow("ts_club_rain1", width = 1280, height = 720, rainamount = 0.25)
    
###ШРИФТЫ

    define cit_font = ts_fonts + "captureit.ttf"
    define ts_nvl_font2 = ts_fonts + "life.ttf"
    define pizdec_font = ts_fonts + "Surfbars.otf"
    define adv_font = ts_fonts + "ADVENTURE.ttf"
    define shl_font = ts_fonts + "SHLAPAKSCRIPT.otf"
    define ink_font = ts_fonts + "INKFREE.ttf"
    define sc_font = ts_fonts + "SCOTCH.ttf"
    define ts_main_font_hueta = ts_fonts + "captureit.ttf"
    define prologue_font = ts_fonts + "Unageo-Light.ttf"
    define ts_atomic = ts_fonts + "cyr.ttf"

# TRUE STORY VIDEO
###МЕНЮШКИ
    image ts_menu_vid = Movie(fps=24, size = (1280, 720), play=ts_videosos + "jm.webm")
    image ts_menu_vid_night = Movie(fps=24, size = (1280, 720), play=ts_videosos + "mr.webm")
    image ts_menu_vid_sunset = Movie(fps=24, size = (1280, 720), play=ts_videosos + "mn.webm")
    image ts_menu_bad_end = Movie(fps=24, size = (1280, 720), play=ts_videosos + "bad_end_menu.ogv")
    image ts_razrab_menu = Movie(fps=24, size = (1280, 720), play=ts_videosos + "menu_video.ogm")
###БГ

    image ts_living_room_telek_stas = Movie(fps=24, size = (1280, 720), play=ts_telek + "stas.webm")
    image ts_living_room_telek_putin = Movie(fps=24, size = (1280, 720), play=ts_telek + "interview.webm")
    image ts_living_room_telek_sudba_night = Movie(fps=24, size = (1280, 720), play=ts_telek + "sudba_night.webm")
    image ts_living_room_telek_sudba_day = Movie(fps=24, size = (1280, 720), play=ts_telek + "sudba.webm")

    image ts_nebo_fon_bgshka_suka = Movie(fps=24, size = (1280, 720), play=ts_telek + "nebo_pasmurnoe.webm")