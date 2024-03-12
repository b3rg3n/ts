# TRUE STORY SPRITES TRANSFORMS
# by @b3rg3n & @dansalvato
# Since 2024

transform ts_leftin(e=1.0, x=640, y=1.03, z=0.80):
    xcenter -300 yoffset 0 yanchor 1.0 ypos y zoom z*1.00 alpha 1.00 subpixel True
    easein e xcenter x

transform ts_rightin(e=1.0, x=640, y=1.03, z=0.80):
    xcenter 1400 yoffset 0 yanchor 1.0 ypos y zoom z*1.00 alpha 1.00 subpixel True
    easein e xcenter x

transform ts_leftout(e=1.0, x=640, y=1.03, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos y zoom z*1.00 alpha 1.00 subpixel True
    easein e xcenter -300

transform ts_rightout(e=1.0, x=640, y=1.03, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos y zoom z*1.00 alpha 1.00 subpixel True
    easein e xcenter 1400

transform tcommon(x=640, z=0.80): # ОБЩАЯ АНИМАЦИЯ ДОБАВЛЕНИЯ СПРАЙТА СО СДВИГОМ В СЛУЧАЕ ЗАМЕНЫ ПОЗИЦИИ
    yanchor 1.0 subpixel True
    on show:
        ypos 1.03
        zoom z*0.95 alpha 0.00
        xcenter x yoffset -20
        easein .25 yoffset 0 zoom z*1.00 alpha 1.00
    on replace:

        alpha 1.00
        parallel:
            easein .25 xcenter x zoom z*1.00
        parallel:
            easein .15 yoffset 0 ypos 1.03

transform tinstant(x=640, z=0.80): # ТОЖЕ САМОЕ, ЧТО И ВЫШЕ, ТОЛЬКО БЕЗ ДИССОЛВА И СДВИГА (РЕЗКАЯ)
    xcenter x yoffset 0 zoom z*1.00 alpha 1.00 yanchor 1.0 ypos 1.03

transform focus(x=640, z=0.80): # ЧУТЬ ПОДНИМАЕТ СПРАЙТ (ФОКУС)
    yanchor 1.0 ypos 1.03 subpixel True
    on show:

        zoom z*0.95 alpha 0.00
        xcenter x yoffset -20
        easein .25 yoffset 0 zoom z*1.05 alpha 1.00
        yanchor 1.0 ypos 1.03
    on replace:
        alpha 1.00
        parallel:
            easein .25 xcenter x zoom z*1.05
        parallel:
            easein .15 yoffset 0

transform sink(x=640, z=0.80): # СПРАЙТ ПРИСЕДАЕТ БЕЗ ВОЗВРАТА НА ИСХОДНУЮ
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .5 ypos 1.06

transform hop(x=640, z=0.80): # СПРАЙТ ПОДПРЫГИВАЕТ С ВОЗВРАТОМ НА ИСХОДНУЮ
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .1 yoffset -20
    easeout .1 yoffset 0

transform hopfocus(x=640, z=0.80): # ПРЫЖОК С УВЕЛИЧЕНИЕМ
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.05 alpha 1.00 subpixel True
    easein .1 yoffset -21
    easeout .1 yoffset 0

transform dip(x=640, z=0.80): # ПРИСЕДАЕТ И ВОЗВРАЩАЕТСЯ
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .25 yoffset 25
    easeout .25 yoffset 0

transform panic(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    parallel:
        ease 1.2 yoffset 25
        ease 1.2 yoffset 0
        repeat
    parallel:
        easein .3 xoffset 20
        ease .6 xoffset -20
        easeout .3 xoffset 0
        repeat


transform thide(z=0.80): # ПЛАВНО УХОДИТ В ПУСТОТУ
    subpixel True
    transform_anchor True
    on hide:

        easein .25 zoom z*0.95 alpha 0.00 yoffset -20

transform lhide: # ТО ЖЕ САМОЕ, ТОЛЬКО ВЛЕВО
    subpixel True
    on hide:
        easeout .25 xcenter -300

transform ts_move_up(y): # ПОДНИМАЕТСЯ СНИЗУ
    yoffset 300 subpixel True
    ease 0.3 yoffset 50
    ease 0.3 yoffset y

transform ts_move_down(y): # ПОДНИМАЕТСЯ СВЕРХУ
    yoffset y subpixel True
    ease 0.5 yoffset 800

transform ts_sprite_alpha(a=0.5):
    xcenter 640 yoffset 0 zoom 0.80 alpha a subpixel True
