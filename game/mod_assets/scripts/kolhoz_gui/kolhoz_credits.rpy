# TRUE STORY SCREEN CREDITS
# by @b3rg3n
# Since 2024

init:

    $ style.credits = Style(style.default)
    $ style.credits.font  = "mod_assets/source/fonts/Surfbars.otf"
    $ style.credits.color = "#fff"
    $ style.credits.drop_shadow = [ (1, 1), (1, 1), (1, 1), (1, 1) ]
    $ style.credits.drop_shadow_color = "#000"
    $ style.credits.italic = False
    $ style.credits.bold = False
    $ style.credits.text_align = 0.5
    $ style.credits.xmaximum = 0.8

    image credits = ParameterizedText(style = "credits", size = 50)

    define ts_credits = "Оригинальная идея:\nBERGEN\n\nАвтор Сценария:\nMaddie, The Mad\n\nГлавный программист:\nBERGEN\n\nGUI:\nBERGEN\n\nВ моде использовались следующие BG:\nbedroom, class, club (club_skill), corridor,\nstreet, house, kitchen, residential,\nsayori_bedroom - Team Salvato\nmusic_club - Team Salvato/Serenity Forge\nschool_gate (day/evening), school_courtyard - Kimagure After\ngost (day), vhod (day/night/nolight),\nliving_room (day/late/night) - Nuxill#7870\ngym_n, lockers_n - Vanishing Point\ndarkbed - Alex#9077\nstairs - Kimagure After; edited by Nuxill#7870\nbathroom - Uncle Mugen\nclub2re - Wheatley#3103; edited by MalukahMaker#2907, TheMelodyofGaming#7515\n\nAll BG's polished by BERGEN\n\nСпрайты:\nExtended OC sprites - originally from Absolution Chapter One by BaryonGod\nКаори - Hime Sprites by Daikaju Fanboy/BlackRabbitArtworks\nСайра в пижаме - Wretched Team, Exit Music, Malukah\nПодруги Нацуки - Himari Sprites by Prox#9492; Elena Sprites by ItzTuna/Elenathebullimom\nХирото (папа Моники) - StormBlazed76\nМама Моники - originally Dr. Bug from Dimensions by chiffmonkey\n\nКомпозиторы:\nDan Salvato\nSergey Eybog\nBetween August and December\n\nВ моде также использовалась следующая музыка:\nHallucinator - Mosh\nPixies - Where is My Mind (piano cover)\nJurrivh - Suicide Note\nMoe Era OST - Final Scene Soft\n\nЗвуки:\nDDLC SFX\nEverlasting Summer SFX\nSeven Summer Days SFX\nfreesound.org\n\nПродолжение следует.\n\nЗа новостями\nпо дальнейшей разработке\nследите в нашем\n{a=https://discord.com/invite/8B3eKkU37q}Discord канале{/a}.\n\n\nКонец DEMO версии.\n\n\n\n\n\n\n"

label true_story_credits_label_blya:

    play music ts_soft fadein 4

    scene ts_sakura
    show zatemnenie_light
    show lepestki_krutyatsa
    with ed_night_dis

    if renpy.windows:
        python: # ОБНОВЛЯЕМ RPC
            rpc.update(state="Финал",details="Титры",large_image="logogovna",start=time.time())

    $ persistent.rpclabel = "999"

    show credits ts_credits:
        xalign 0.5
        ypos 1.05
        linear 180.0 ypos -4.0
    $ renpy.pause (190, hard=True)

    return