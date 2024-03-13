# TRUE STORY GLITCH STUFF
# by @b3rg3n
# Since 2024

#SPRITE's
#КАОРИ
image kaori 22a1g = im.Composite((960, 960), (0, 0), get_image("spr/hime/glitch/2.webp"), (0, 0), get_image("spr/hime/glitch/aaa.webp"))
image kaori 22a2g = im.Composite((960, 960), (0, 0), get_image("spr/hime/glitch/2a.webp"), (0, 0), get_image("spr/hime/glitch/aa.webp"))
image kaori 22a3g = im.Composite((960, 960), (0, 0), get_image("spr/hime/glitch/2b.webp"), (0, 0), get_image("spr/hime/glitch/a.webp"))

image kaori_glitch_pizdets:
    "kaori 22a1g"
    0.03 # Задержка
    "kaori 22a3g"
    0.03 # Задержка
    "kaori 22a2g"
    0.03 # Задержка
    "kaori 22a1g"
    0.03 # Задержка
    "kaori 22a3g"
    0.03 # Задержка
    repeat # Не убирать

#BG's
image ts_l51 = get_image("bg/glitch/l51.webp")
image ts_l52 = get_image("bg/glitch/l52.webp")
image ts_l53 = get_image("bg/glitch/l53.webp")

image ts_l5_glitch_pizdets:
    "ts_l51"
    0.03 # Задержка
    "ts_l53"
    0.03 # Задержка
    "ts_l52"
    0.03 # Задержка
    "ts_l51"
    0.03 # Задержка
    "ts_l53"
    0.03 # Задержка
    repeat # Не убирать