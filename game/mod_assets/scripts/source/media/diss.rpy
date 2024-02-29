# TRUE STORY DISSOLVE's
# by @b3rg3n
# Since 2024

init:
###АНИМАЦИИ И ТРАНЗИТЫ
    define wipeleft = ImageDissolve("mod_assets/source/images/anim/transit/wipeleft.webp", 0.5, ramplen=64)


    define wipeleft_scene = MultipleTransition([
        False, ImageDissolve("mod_assets/source/images/anim/transit/wipeleft.webp", 0.5, ramplen=64),
        Solid("#000"), Pause(0.25),
        Solid("#000"), ImageDissolve("mod_assets/source/images/anim/transit/wipeleft.webp", 0.5, ramplen=64),
        True])

###ТРАНЗИТЫ
    define ed_flash_red = Fade(1, 0, 1, color="#e11")
    define ed_alpha_diss_fast = Dissolve(0.5, alpha=True)
    define flash = Fade(.25, 0, .75, color="#fff")
    define dissolve2 = Dissolve(2.0)
    define dspr = Dissolve(.2)
    define dis = Dissolve(0.5, alpha=True)
    define flash2 = Fade(2, 2, 2, color="#fff")
    define flash_red = Fade(1, 0, 1, color="#e11")
    define flash_red2 = Fade(2, 2, 2, color="#e11")
    define flash_fast = Fade(0.25, 0, 0.75, color="#fff")
    define flash_fast2 = Fade(0.05, 0, 0.35, color="#fff")
    define flash_fast_red = Fade(0.25, 0, 0.75, color="#ff0000")
    define flash_fast_red2 = Fade(0.05, 0, 0.75, color="#ff0000")
    define fade3 = Fade(1.5, 0, 1.5)
    define fade2 = Fade(1, 0, 1)
    define hell_dissolve = Dissolve(50)
    define dissolve3 = Dissolve(3)
    define dissolve4 = Dissolve(4)
    define dissolve_fast = Dissolve(0.5)
    define dissolve_long = Dissolve(100)
###ТРАНЗИТЫ IMAGE
    define ed_earth_draw = ImageDissolve("mod_assets/source/images/anim/transit/ed_earth_draw.webp", 3.0) # ЭФФЕКТ ЗЕМЛИ ОБВАЛ
    define ed_lap = ImageDissolve("mod_assets/source/images/anim/transit/ed_lap.webp", 2.0) # ЭФФЕКТ ЧАСОВ
    define ed_night_dis = ImageDissolve("mod_assets/source/images/anim/transit/ed_night_dis.webp", 5.0) # ЭФФЕКТ СГОРАЮЩЕЙ БУМАГИ
    define poplil_pacan = ImageDissolve("mod_assets/source/images/anim/transit/wow_blya.webp", 1.66) # ЭФФЕКТ ПЕРЛИВАНИЯ КРОВИ
    define poplil_pacan1 = ImageDissolve("mod_assets/source/images/anim/transit/wow_blya.webp", 6.66) # ЭФФЕКТ ПЕРЛИВАНИЯ КРОВИ
    define awrain = ImageDissolve("mod_assets/source/images/anim/transit/awrain.webp", 1.5, 60, reverse=False) # ЭФФЕКТ СМЫВА ДОЖДЁМ
    define awrain2 = ImageDissolve("mod_assets/source/images/anim/transit/awrain.webp", 4.5, 80, reverse=False) # ЭФФЕКТ СМЫВА ДОЖДЁМ
    define awrain3 = ImageDissolve("mod_assets/source/images/anim/transit/awrain.webp", 0.5, 30, reverse=False) # ЭФФЕКТ СМЫВА ДОЖДЁМ
    define awwhole = ImageDissolve("mod_assets/source/images/anim/transit/awwhole.webp", 4.5, 60, reverse=False) # ЭФФЕКТ СИМПЛ ДИМПЛ БЛЯДЬ АХАХА
    define awbhole = ImageDissolve("mod_assets/source/images/anim/transit/awbhole.webp", 3.5, 60, reverse=True) # ЭФФЕКТ СИМПЛ ДИМПЛ БЛЯДЬ АХАХА
###ЭФФЕКТ ТРИПА
    image trip1MVWWW777 = "mod_assets/source/images/anim/trip/trip1MVWWW777.webp" # КОСОЁБИТ ПАЦАНА
    image trip2MVWWW777 = "mod_assets/source/images/anim/trip/trip2MVWWW777.webp" # КОСОЁБИТ ПАЦАНА
    image trip3MVWWW777 = "mod_assets/source/images/anim/trip/trip3MVWWW777.webp" # КОСОЁБИТ ПАЦАНА
###ЭФФЕКТ ПСИХОЗА
    image et_rage1 = "mod_assets/source/images/anim/rage/et_rage1.webp" # Я ЩАС УБЬЮ ВСЕХ БЛЯТЬ
    image et_rage2 = "mod_assets/source/images/anim/rage/et_rage2.webp" # Я ЩАС УБЬЮ ВСЕХ БЛЯТЬ
    image et_rage3 = "mod_assets/source/images/anim/rage/et_rage3.webp" # Я ЩАС УБЬЮ ВСЕХ БЛЯТЬ
    image et_rage4 = "mod_assets/source/images/anim/rage/et_rage4.webp" # Я ЩАС УБЬЮ ВСЕХ БЛЯТЬ
###ОВРЕЛЕИ
    image zatemnenie = Image("mod_assets/source/images/anim/zatemnenie.webp") # ЗАТЕМНЕНИЕ СРЕДНЕЕ
    image zatemnenie_light = Image("mod_assets/source/images/anim/zatemnenie_light.webp") # ЗАТЕМНЕНИЕ ЛЁГКОЕ
    image blood = "mod_assets/source/images/anim/ovr/blood.webp" # КРОВЬ ПО БОКАМ ЭКРАНА
    image sl_blkg_LW0607 = "mod_assets/source/images/anim/ovr/sl_blkg_LW0607.webp" # ЦАРАПИНА НА ЕБАЛЕ
    image dark_LW0607 = "mod_assets/source/images/anim/ovr/dark_LW0607.webp" # СИЛЬНОЕ ЗАТЕМНЕНИЕ
    image blood_LW0607 = "mod_assets/source/images/anim/ovr/blood_LW0607.webp" # КРОВЬ НА ЭКРАНЕ
###ГУИ
    image sktwarn1 = "mod_assets/source/images/anim/disk/sktwarn1.webp" # ПЕРВЫЙ ДИСКЛЕЙМЕР
    image sktwarn2 = "mod_assets/source/images/anim/disk/sktwarn2.webp" # ВТОРОЙ ДИСКЛЕЙМЕР
###ОВЕРЛЕИ ТЕКСТА ПСИХОЗ
    image aw_afd_dth1_1 = "mod_assets/source/images/anim/text/aw_afd_dth1_1.webp" # НЕ ВЕРЬ ЕЙ
    image aw_afd_dth1_2 = "mod_assets/source/images/anim/text/aw_afd_dth1_2.webp" # НЕ ВЕРЬ ЕЙ
    image aw_afd_dth1_3 = "mod_assets/source/images/anim/text/aw_afd_dth1_3.webp" # НЕ ВЕРЬ ЕЙ
    image aw_afd_ky1_1 = "mod_assets/source/images/anim/text/aw_afd_ky1_1.webp" # СДОХНИ
    image aw_afd_ky1_2 = "mod_assets/source/images/anim/text/aw_afd_ky1_2.webp" # СДОХНИ
    image aw_afd_ky1_3 = "mod_assets/source/images/anim/text/aw_afd_ky1_3.webp" # СДОХНИ
###ДЛЯ ПИЗДЯРЕВА
    image hitmarkermlg_LW0607 = "mod_assets/source/images/anim/pizdelka/hitmarkermlg_LW0607.webp" # ХИТМАРКЕР
    image dlya_ebalaMVWWW777 = "mod_assets/source/images/anim/pizdelka/dlya_ebalaMVWWW777.webp" # РУКА ПРАВАЯ
    image dlya_ebalaleftMVWWW777 = "mod_assets/source/images/anim/pizdelka/dlya_ebalaleftMVWWW777.webp" # РУКА ЛЕВАЯ
    image hernya_kakaya_toMVWWW777 = "mod_assets/source/images/anim/pizdelka/hernya_kakaya_toMVWWW777.webp" # ЭФФЕКТ ДИНАМИКИ
    image kulak_LW0607 = "mod_assets/source/images/anim/pizdelka/kulak_LW0607.webp" # КУЛАК ЛЕВЫЙ
    image kulak2_LW0607 = "mod_assets/source/images/anim/pizdelka/kulak2_LW0607.webp" # КУЛАК ПРАВЫЙ
    image dlya_ebala_LW0607 = "mod_assets/source/images/anim/pizdelka/dlya_ebala_LW0607.webp" # РУКА ПРАВАЯ
    image dlya_ebalaleft_LW0607 = "mod_assets/source/images/anim/pizdelka/dlya_ebalaleft_LW0607.webp" # РУКА ЛЕВАЯ
###АНИМАЦИЯ ЗАКРЫТИЯ/ОТКРЫТИЯ ЗЕНЕК
    image anim blink_down = "mod_assets/source/images/anim/zenki/blink_down.webp" # ВЕРНХНИЕ ВЕКИ
    image anim blink_up = "mod_assets/source/images/anim/zenki/blink_up.webp" # НИЖНИЕ ВЕКИ