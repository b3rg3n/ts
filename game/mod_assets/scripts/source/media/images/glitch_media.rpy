# TRUE STORY GLITCH STUFF
# by @b3rg3n
# Since 2024

#SPRITE's
#КАОРИ
image kaori 22a1g = im.Composite((960, 960), (0, 0), ts_spr + "hime/glitch/2.webp", (0, 0), ts_spr + "hime/glitch/aaa.webp")
image kaori 22a2g = im.Composite((960, 960), (0, 0), ts_spr + "hime/glitch/2a.webp", (0, 0), ts_spr + "hime/glitch/aa.webp")
image kaori 22a3g = im.Composite((960, 960), (0, 0), ts_spr + "hime/glitch/2b.webp", (0, 0), ts_spr + "hime/glitch/a.webp")

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

image sayori 3b111 = im.Composite((960, 960), (0, 0), ts_spr + "sayori/glitch/3b1.webp")
image sayori 3b222 = im.Composite((960, 960), (0, 0), ts_spr + "sayori/glitch/3b2.webp")
image sayori 3b333 = im.Composite((960, 960), (0, 0), ts_spr + "sayori/glitch/3b3.webp")

image sayori_glitch_pizdets:
    "sayori 3b111"
    0.03 # Задержка
    "sayori 3b333"
    0.03 # Задержка
    "sayori 3b222"
    0.03 # Задержка
    "sayori 3b111"
    0.03 # Задержка
    "sayori 3b333"
    0.03 # Задержка
    repeat # Не убирать

image hiroto 3b111 = im.Composite((960, 960), (0, 0), ts_spr + "hiroto/glitch/b1.webp")
image hiroto 3b222 = im.Composite((960, 960), (0, 0), ts_spr + "hiroto/glitch/b2.webp")
image hiroto 3b333 = im.Composite((960, 960), (0, 0), ts_spr + "hiroto/glitch/b3.webp")

image hiroto_glitch_pizdets:
    "hiroto 3b111"
    0.03 # Задержка
    "hiroto 3b333"
    0.03 # Задержка
    "hiroto 3b222"
    0.03 # Задержка
    "hiroto 3b111"
    0.03 # Задержка
    "hiroto 3b333"
    0.03 # Задержка
    repeat # Не убирать

#BG's
image ts_l51 = ts_bg + "glitch/l51.webp"
image ts_l52 = ts_bg + "glitch/l52.webp"
image ts_l53 = ts_bg + "glitch/l53.webp"

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

image ts_club1 = ts_bg + "glitch/club1.webp"
image ts_club2 = ts_bg + "glitch/club2.webp"
image ts_club3 = ts_bg + "glitch/club3.webp"

image ts_club_glitch_pizdets:
    "ts_club1"
    0.03 # Задержка
    "ts_club3"
    0.03 # Задержка
    "ts_club2"
    0.03 # Задержка
    "ts_club1"
    0.03 # Задержка
    "ts_club3"
    0.03 # Задержка
    repeat # Не убирать

image ts_kitchen1 = ts_bg + "glitch/kitchen1.webp"
image ts_kitchen2 = ts_bg + "glitch/kitchen2.webp"
image ts_kitchen3 = ts_bg + "glitch/kitchen3.webp"

image ts_kitchen_glitch_pizdets:
    "ts_kitchen1"
    0.03 # Задержка
    "ts_kitchen3"
    0.03 # Задержка
    "ts_kitchen2"
    0.03 # Задержка
    "ts_kitchen1"
    0.03 # Задержка
    "ts_kitchen3"
    0.03 # Задержка
    repeat # Не убирать