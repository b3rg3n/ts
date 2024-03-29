# TRUE STORY SPLIT IMAGES
# by @b3rg3n
# SINCE 2024

init:
    image ts_hotel_split = "mod_assets/source/images/bg/split/hotel_split.webp"
    image ts_gost_split = "mod_assets/source/images/bg/split/gost_split.webp"

    image ts_gost_split_animated: # pause 0.99
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'ts_gost_split'
        parallel:
            ypos 1.5 alpha 0.0
            linear 0.99 ypos 1.0 alpha 1.0

    image ts_hotel_split_animated: # pause 0.99
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'ts_hotel_split'
        parallel:
            ypos 0.5 alpha 0.0
            linear 0.99 ypos 1.0 alpha 1.0 