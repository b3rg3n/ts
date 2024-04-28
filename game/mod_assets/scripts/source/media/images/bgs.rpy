# TRUE STORY BG's
# by @b3rg3n
# Since 2024

init:
###БГ
    image ts_bathroom = ts_bg + "bathroom.webp"
    image ts_bedroom = ts_bg + "bedroom.webp"
    image ts_class = ts_bg + "class.webp"
    image ts_club = ts_bg + "club.webp"
    image ts_club2re = ts_bg + "club2re.webp"
    image ts_corridor = ts_bg + "corridor.webp"
    image ts_darkbed = ts_bg + "darkbed.webp"
    image ts_gost = ts_bg + "gost.webp"
    image ts_gost_night = ts_bg + "gost_night.webp"
    image ts_gost_sunset = ts_bg + "gost_sunset.webp"
    image ts_gym = ts_bg + "gym_n.webp"
    image ts_house = ts_bg + "house.webp"
    image ts_house_monika_evening = ts_bg + "house_monika_evening.webp"
    image ts_house2_night = ts_bg + "house2_night.webp"
    image ts_kitchen = ts_bg + "kitchen.webp"
    image ts_l5 = ts_bg + "l5.webp"
    image ts_l5old = ts_bg + "l5old.webp"
    image ts_living_room = ts_bg + "living_room_day.webp"
    image ts_living_room_late = ts_bg + "living_room_late.webp"
    image ts_living_room_late_night = ts_bg + "living_room_late_night.webp"
    image ts_living_room_night = ts_bg + "living_room_night.webp"
    image ts_pianoend = ts_bg + "music_club.webp"
    image ts_residential = ts_bg + "residential.webp"
    image ts_sakura = ts_bg + "sakura.webp"
    image ts_school_bathroom = ts_bg + "school_bathroom.webp"
    image ts_school_bathroom1 = ts_bg + "school_bathroom1.webp"
    image ts_school_bathroom2 = ts_bg + "school_bathroom2.webp"
    image ts_school_courtyard_day = ts_bg + "school_courtyard_day.webp"
    image ts_school_gate_day = ts_bg + "school_gate_day.webp"
    image ts_school_gate_evening = ts_bg + "school_gate_evening.webp"
    image ts_stairs = ts_bg + "stairs.webp"
    image ts_street = ts_bg + "astreet.webp"
    image ts_street_late = ts_bg + "street_late.webp"
    image ts_vhod_night = ts_bg + "entrance_night.webp"
    image ts_vhod_nolight = ts_bg + "entrance_nolight.webp"
    image ts_city_day = ts_bg + "city_day.webp"
    image ts_sayori_bedroom = ts_bg + "sayori_bedroom.webp"
    image ts_notebook = ts_bg + "notebook.webp"
    image ts_notebook_glitch = ts_bg + "notebook-glitch.webp"
    image ts_entrance_day = ts_bg + "entrance_day.webp"
    image ts_hotel = ts_bg + "hotel.webp"

###ЗАБЛЮРЕНО НАХОЙ
    image ts_club_blur = im.Blur(ts_bg + "club.webp", 3.0)
    image ts_club_blur9 = im.Blur(ts_bg + "club.webp", 9.0)

###ЛОГО ХУЙНИ
    image ts_logo = "mod_assets/source/images/gui/ts_logo.webp"
    image ts_logo_menu = "mod_assets/source/images/gui/ts_logo_menu.webp"

###ШЕЙДЕРЫ
    image ts_city_day_rain = RainOnWindow("ts_city_day", width = 1280, height = 720, rainamount = 1.0)
    image ts_school_gate_day_rain = RainOnWindow("ts_school_gate_day", width = 1280, height = 720, rainamount = 1.0)
    image ts_street_rain = RainOnWindow("ts_street", width = 1280, height = 720, rainamount = 1.0)