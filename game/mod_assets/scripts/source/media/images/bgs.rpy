# TRUE STORY BG's
# by @b3rg3n
# Since 2024

init:
###БГ

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


###ЗАБЛЮРЕНО НАХОЙ
    image ts_club_blur = im.Blur(ts_bg + "club.webp", 3.0)
    image ts_club_blur9 = im.Blur(ts_bg + "club.webp", 9.0)

###ОВЕРЛЕИ
    image ts_club_rain_ovr = ts_bg + "ovr/club_rain_ovr.webp"
    image ts_club_rain = ts_bg + "ovr/club_rain.webp"

    image ts_living_room_rain_ovr = ts_bg + "ovr/living_room_rain_ovr.webp"
    image ts_living_room_rain = ts_bg + "ovr/living_room_rain.webp"

    image ts_shkola_rain = ts_bg + "courtyard-rain.webp"
    image ts_street_rain = ts_bg + "street7.webp"


###ЛОГО ХУЙНИ
    image ts_logo = "mod_assets/source/images/gui/ts_logo.webp"
    image ts_logo_menu = "mod_assets/source/images/gui/ts_logo_menu.webp"

###ШЕЙДЕРЫ
    #image ts_city_day_rain = RainOnWindow("ts_city_day", width = 1280, height = 720, rainamount = 1.0)
    #image ts_school_gate_day_rain = RainOnWindow("ts_school_gate_day", width = 1280, height = 720, rainamount = 1.0)
    #image ts_street_rain = RainOnWindow("ts_street", width = 1280, height = 720, rainamount = 1.0)
    image ts_club_rain_shader = RainOnWindow("ts_club_rain", width = 1280, height = 720, rainamount = 1.0)
    image ts_living_room_rain_shader = RainOnWindow("ts_living_room_rain", width = 1280, height = 720, rainamount = 1.0)

