# TRUE STORY BG's
# by @b3rg3n
# Since 2024
init:

    image ts_sayori_house = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_sayori_house.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_sayori_house.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_sayori_house.webp") )

    image ts_sky_fon = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_sky_fon.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_sky_fon.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_sky_fon.webp") )

    image ts_hotel_rec = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_hotel_rec.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_hotel_rec.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_hotel_rec.webp") )

    image ts_office = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_office.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_office.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_office.webp") )

    image ts_roof = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_roof.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_roof.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_roof.webp") )

    image ts_kitchen_night = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_kitchen_night.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_kitchen_night.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_kitchen_night.webp") )

    image ts_waiting_room = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_waiting_room.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_waiting_room.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_waiting_room.webp") )

    image ts_hospital_corridor = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_hospital_corridor.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_hospital_corridor.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_hospital_corridor.webp") )

    image ts_hospital_room = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_hospital_room.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_hospital_room.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_hospital_room.webp") )

    image ts_emergency_room = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_emergency_room.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_emergency_room.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_emergency_room.webp") )
#
    image ts_seaside_road_morning = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_seaside_road_morning.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_seaside_road_morning.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_seaside_road_morning.webp") )

    image ts_light_off_corridor = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_light_off_corridor.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_light_off_corridor.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_light_off_corridor.webp") )

    image ts_club = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_club.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_club.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_club.webp") )

    image ts_bathroom = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_bathroom.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_bathroom.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_bathroom.webp") )

#
    image ts_pianoend = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_music_club.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_music_club.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_music_club.webp") )

    image ts_living_room_night = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_living_room_night.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_living_room_night.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_living_room_night.webp") )

    image ts_living_room_late_night = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_living_room_late_night.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_living_room_late_night.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_living_room_late_night.webp") )

    image ts_living_room_late = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_living_room_late.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_living_room_late.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_living_room_late.webp") )

    image ts_living_room = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_living_room_day.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_living_room_day.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_living_room_day.webp") )

    image ts_entrance_day = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_entrance_day.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_entrance_day.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_entrance_day.webp") )

    image ts_hotel = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_hotel.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_hotel.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_hotel.webp") )

    image ts_notebook_glitch = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_notebook-glitch.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_notebook-glitch.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_notebook-glitch.webp") )

    image ts_notebook = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_notebook.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_notebook.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_notebook.webp") )

    image ts_sayori_bedroom = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_sayori_bedroom.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_sayori_bedroom.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_sayori_bedroom.webp") )

    image ts_city_day = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_city_day.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_city_day.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_city_day.webp") )

    image ts_vhod_nolight = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_entrance_nolight.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_entrance_nolight.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_entrance_nolight.webp") )

    image ts_vhod_night = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_entrance_night.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_entrance_night.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_entrance_night.webp") )

    image ts_street_late = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_street_late.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_street_late.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_street_late.webp") )

    image ts_street = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_astreet.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_astreet.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_astreet.webp") )

    image ts_stairs = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_stairs.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_stairs.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_stairs.webp") )

    image ts_school_gate_evening = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_school_gate_evening.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_school_gate_evening.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_school_gate_evening.webp") )

    image ts_school_gate_day = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_school_gate_day.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_school_gate_day.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_school_gate_day.webp") )

    image ts_school_courtyard_day = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_school_courtyard_day.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_school_courtyard_day.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_school_courtyard_day.webp") )

    image ts_school_bathroom2 = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_school_bathroom2.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_school_bathroom2.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_school_bathroom2.webp") )

    image ts_school_bathroom1 = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_school_bathroom1.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_school_bathroom1.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_school_bathroom1.webp") )

    image ts_school_bathroom = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_school_bathroom.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_school_bathroom.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_school_bathroom.webp") )

    image ts_sakura = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_sakura.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_sakura.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_sakura.webp") )

    image ts_residential = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_residential.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_residential.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_residential.webp") )

    image ts_l5old = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_l5old.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_l5old.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_l5old.webp") )

    image ts_l5 = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_l5.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_l5.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_l5.webp") )

    image ts_kitchen = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_kitchen.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_kitchen.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_kitchen.webp") )

    image ts_house2_night = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_house2_night.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_house2_night.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_house2_night.webp") )

    image ts_house_monika_evening = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_house_monika_evening.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_house_monika_evening.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_house_monika_evening.webp") )

    image ts_house = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_house.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_house.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_house.webp") )

    image ts_gym = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_gym_n.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_gym_n.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_gym_n.webp") )

    image ts_gost_sunset = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_gost_sunset.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_gost_sunset.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_gost_sunset.webp") )

    image ts_gost_night = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_gost_night.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_gost_night.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_gost_night.webp") )

    image ts_gost = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_gost.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_gost.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_gost.webp") )

    image ts_darkbed = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_darkbed.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_darkbed.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_darkbed.webp") )

    image ts_corridor = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_corridor.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_corridor.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_corridor.webp") )

    image ts_club2re = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_club2re.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_club2re.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_club2re.webp") )

    image ts_class = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_class.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_class.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_class.webp") )

    image ts_bedroom = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_bedroom.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_bedroom.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_bedroom.webp") )

    image ts_corridorrev = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_corridorrev.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_corridorrev.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_corridorrev.webp") )

    image ts_stairsre = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_stairsre.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_stairsre.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_stairsre.webp") )

    image ts_street1 = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_street1.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_street1.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_street1.webp") )

    image ts_jstreet = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_jstreet.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_jstreet.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_jstreet.webp") )

    image ts_closet = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_closet.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_closet.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_closet.webp") )

    image ts_cafeteria = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_cafeteria-rain.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ts_cafeteria-rain.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ts_cafeteria-rain.webp") )

###ЗАБЛЮРЕНО НАХОЙ
    image ts_club_blur = im.Blur(ts_bg + "ts_club.webp", 3.0)
    image ts_club_blur9 = im.Blur(ts_bg + "ts_club.webp", 9.0)

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

    image ts_corridor_rain_ovr1 = ConditionSwitch(
    "persistent.uncolorize=='lite'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ovr/corridor_rain_ovr1.webp"), im.matrix.saturation(.5, desat = (0.2126, 0.7152, 0.0722)) ),
    "persistent.uncolorize=='full'",im.MatrixColor( im.Composite((1280,720), (0,0), ts_bg + "ovr/corridor_rain_ovr1.webp"), im.matrix.saturation(.2, desat = (0.2126, 0.7152, 0.0722)) ),
    True,im.Composite((1280,720), (0,0), ts_bg + "ovr/corridor_rain_ovr1.webp") )


    image ts_shkola_rain = ts_bg + "ts_courtyard-rain.webp"
    image ts_street_rain = ts_bg + "ts_street7.webp"

    image ts_house_rain_ovr = ts_bg + "ovr/house_rain_ovr.webp"
    image ts_shkola_rain_ovr = ts_bg + "ovr/shkola_rain_ovr.webp"
    image ts_street_rain_ovr = ts_bg + "ovr/street_rain_ovr.webp"
