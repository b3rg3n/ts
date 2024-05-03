# TRUE STORY DISSOLVE's (некоторые взял у Хайта и Endless Horizon)
# by @b3rg3n
# Since 2024

init:
###ТРАНЗИТЫ
    define ts_pixel = Pixellate(0.3, 5)
    define flash = Fade(.25, 0, .75, color="#fff")
    define dissolve2 = Dissolve(2.0)
    define dspr = Dissolve(.2)
    define flash_red = Fade(1, 0, 1, color="#e11")
    define dissolve4 = Dissolve(4)
###ТРАНЗИТЫ IMAGE
    define ed_night_dis = ImageDissolve(ts_anim + "transit/ed_night_dis.webp", 5.0) # ЭФФЕКТ СГОРАЮЩЕЙ БУМАГИ
    define ed_night_dis_faster = ImageDissolve(ts_anim + "transit/ed_night_dis.webp", 2.5) # ЭФФЕКТ СГОРАЮЩЕЙ БУМАГИ
    define poplil_pacan = ImageDissolve(ts_anim + "transit/wow_blya.webp", 1.66) # ЭФФЕКТ ПЕРЛИВАНИЯ КРОВИ
    define poplil_pacan1 = ImageDissolve(ts_anim + "transit/wow_blya.webp", 6.66) # ЭФФЕКТ ПЕРЛИВАНИЯ КРОВИ
    define awrain = ImageDissolve(ts_anim + "transit/awrain.webp", 1.5, 60, reverse=False) # ЭФФЕКТ СМЫВА ДОЖДЁМ
    define awrain2 = ImageDissolve(ts_anim + "transit/awrain.webp", 4.5, 80, reverse=False) # ЭФФЕКТ СМЫВА ДОЖДЁМ
    define wipeleft = ImageDissolve(ts_anim + "transit/wipeleft.webp", 0.5, ramplen=64)
    define wipeleft_scene = MultipleTransition([
        False, ImageDissolve(ts_anim + "transit/wipeleft.webp", 0.5, ramplen=64),
        Solid("#000"), Pause(0.25),
        Solid("#000"), ImageDissolve(ts_anim + "transit/wipeleft.webp", 0.5, ramplen=64),
        True])
