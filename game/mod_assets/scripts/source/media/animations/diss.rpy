# TRUE STORY DISSOLVE's
# by @b3rg3n
# Since 2024

init:
###ТРАНЗИТЫ
    define ed_flash_red1 = Fade(1, 0, 1, color="#e11")
    define ed_alpha_diss_fast = Dissolve(0.5, alpha=True)
    define flash = Fade(.25, 0, .75, color="#fff")
    define dissolve2 = Dissolve(2.0)
    define dspr = Dissolve(.2)
    define dis = Dissolve(0.5, alpha=True)
    define ed_flash_red = Fade(0.3, 0.0, 0.2, color='#F80000')
    define flash2 = Fade(2, 2, 2, color="#fff")
    define flash_red = Fade(1, 0, 1, color="#e11")
    define flash_red2 = Fade(2, 2, 2, color="#e11")
    define flash2_red = Fade(0.5, 0, 0.5, color="#f11")
    define flash_pink = Fade(1, 0, 1, color="#e25")
    define flash_fast = Fade(0.25, 0, 0.75, color="#fff")
    define flash_fast2 = Fade(0.05, 0, 0.35, color="#fff")
    define flash_fast_red = Fade(0.25, 0, 0.75, color="#ff0000")
    define flash_fast_red2 = Fade(0.05, 0, 0.75, color="#ff0000")
    define fade_red = Fade(2, 2, 2, color="#f11")
    define fade3 = Fade(1.5, 0, 1.5)
    define fade2 = Fade(1, 0, 1)
    define hell_dissolve = Dissolve(50)
    define dissolve3 = Dissolve(3)
    define dissolve4 = Dissolve(4)
    define dissolve_fast = Dissolve(0.5)
    define dissolve_long = Dissolve(100)
    define flash_cyan = Fade(1, 0, 1, color="#1fa")
###ТРАНЗИТЫ IMAGE
    define ed_earth_draw = ImageDissolve(ts_anim + "transit/ed_earth_draw.webp", 3.0) # ЭФФЕКТ ЗЕМЛИ ОБВАЛ
    define ed_lap = ImageDissolve(ts_anim + "transit/ed_lap.webp", 2.0) # ЭФФЕКТ ЧАСОВ
    define ed_night_dis = ImageDissolve(ts_anim + "transit/ed_night_dis.webp", 5.0) # ЭФФЕКТ СГОРАЮЩЕЙ БУМАГИ
    define ed_night_dis_faster = ImageDissolve(ts_anim + "transit/ed_night_dis.webp", 2.5) # ЭФФЕКТ СГОРАЮЩЕЙ БУМАГИ
    define poplil_pacan = ImageDissolve(ts_anim + "transit/wow_blya.webp", 1.66) # ЭФФЕКТ ПЕРЛИВАНИЯ КРОВИ
    define poplil_pacan1 = ImageDissolve(ts_anim + "transit/wow_blya.webp", 6.66) # ЭФФЕКТ ПЕРЛИВАНИЯ КРОВИ
    define awrain = ImageDissolve(ts_anim + "transit/awrain.webp", 1.5, 60, reverse=False) # ЭФФЕКТ СМЫВА ДОЖДЁМ
    define awrain2 = ImageDissolve(ts_anim + "transit/awrain.webp", 4.5, 80, reverse=False) # ЭФФЕКТ СМЫВА ДОЖДЁМ
    define awrain3 = ImageDissolve(ts_anim + "transit/awrain.webp", 0.5, 30, reverse=False) # ЭФФЕКТ СМЫВА ДОЖДЁМ
    define awwhole = ImageDissolve(ts_anim + "transit/awwhole.webp", 4.5, 60, reverse=False) # ЭФФЕКТ СИМПЛ ДИМПЛ БЛЯДЬ АХАХА
    define awbhole = ImageDissolve(ts_anim + "transit/awbhole.webp", 3.5, 60, reverse=True) # ЭФФЕКТ СИМПЛ ДИМПЛ БЛЯДЬ АХАХА
    define diam = ImageDissolve(im.Tile(ts_anim + "transit/pattern.webp"), 1.1, 1) # КРИСТАЛЛ
    define fdiam = ImageDissolve(im.Tile(ts_anim + "transit/pattern.webp"), 0.4, 1) # КРИСТАЛЛ
    define fulldiam = MultipleTransition([False,fdiam,(ts_anim + "digi1.webp"),fdiam,True]) # КРИСТАЛЛ
    define gopr = ImageDissolve(im.Tile(ts_anim + "transit/blackout_go.webp"), 0.95, 1) # ПОВОРОТНЫЙ ПЕРЕКЛЮЧАТЕЛЬ
    define gopr2 = ImageDissolve(im.Tile(ts_anim + "transit/blackout_go.webp"), 1.4, 1) # ПОВОРОТНЫЙ ПЕРЕКЛЮЧАТЕЛЬ
    define clock_l = ImageDissolve(im.Tile(ts_anim + "transit/clock_l.webp"), 0.95, 1) # ПОВОРОТНЫЙ ПЕРЕКЛЮЧАТЕЛЬ
    define joff_l = MultipleTransition([False, clock_l, Solid("#000"), clock_l, True]) # ПОВОРОТНЫЙ ПЕРЕКЛЮЧАТЕЛЬ
    define clock_r = ImageDissolve((ts_anim + "transit/clock_r.webp"), 2.5, 50, reverse=False) # ПОВОРОТНЫЙ ПЕРЕКЛЮЧАТЕЛЬ
    define joff_r = MultipleTransition([False, clock_r, Solid("#000"), clock_r, True]) # ПОВОРОТНЫЙ ПЕРЕКЛЮЧАТЕЛЬ
    define blind_d = ImageDissolve(im.Tile(ts_anim + "transit/roof_ks.webp"), 1.3) # Жалюзи а ля KS
    define blinds_l = ImageDissolve(im.Tile(ts_anim + "transit/roof_ks2.webp"), 0.6) # Жалюзи а ля KS
    define blinds_r = ImageDissolve(im.Tile(ts_anim + "transit/roof_ks3.webp"), 0.7) # Жалюзи а ля KS
    define blinds_ud = ImageDissolve((ts_anim + "transit/blackout_ud.webp"), 0.3) # Жалюзи а ля KS
    define blind_l = MultipleTransition([False,blinds_l,Solid("#011"),blinds_r,True]) # Жалюзи а ля KS
    define blind_r = MultipleTransition([False,blinds_r,Solid("#011"),blinds_l,True]) # Жалюзи а ля KS
    define touch = ImageDissolve(im.Tile(ts_anim + "transit/pattern2.webp"), 0.9, 1) # РАЗНОЕ
    define dspq = Dissolve(0.04, alpha=True) # РАЗНОЕ
    define dsps = Dissolve(3.0, alpha=True) # РАЗНОЕ
    define guess_on = ImageDissolve((ts_anim + "transit/blackpalm.webp"), 0.25, ramplen=256, reverse=True) # РАЗНОЕ
    define guess_off = ImageDissolve((ts_anim + "transit/blackpalm.webp"), 0.3, ramplen=256) # РАЗНОЕ
    define wipeleft = ImageDissolve(ts_anim + "transit/wipeleft.webp", 0.5, ramplen=64)
    define wipeleft_scene = MultipleTransition([
        False, ImageDissolve(ts_anim + "transit/wipeleft.webp", 0.5, ramplen=64),
        Solid("#000"), Pause(0.25),
        Solid("#000"), ImageDissolve(ts_anim + "transit/wipeleft.webp", 0.5, ramplen=64),
        True])
