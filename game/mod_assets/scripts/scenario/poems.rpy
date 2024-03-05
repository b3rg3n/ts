# TRUE STORY POEMS
# written by @Maddie, The Mad & @Dan Salvato
# ported from ddlc by @b3rg3n
# original style by @Dan Salvato

init python:
    class Poem:
        def __init__(self, author="", title="", text="", yuri_2=False, yuri_3=False):
            self.author = author
            self.title = title
            self.text = text
            self.yuri_2 = yuri_2
            self.yuri_3 = yuri_3

    poem_y1 = Poem(
    author = "yuri",
    title = "Призрак на свету",
    text = """\
Локоны мои блестят в янтарном свете,
В нём купаясь.
Я нашла:
Всего один фонарь прошёл сквозь время, сквозь года,
Лишь для того, чтоб будущего тени раскрасили больным зелёно-синим его жар.
Я им омыта. Я спокойна; вдыхаю воздух настоящего, из прошлого глядя.
Мерцает свет.
В ответ мерцаю я."""
    )

    poem_test = Poem(
    author = "monika",
    title = "С другой стороны",
    text = """\
Вдоль дороги\n
я вижу\n
девочку одну\n\n
И вижу,\n
как копает она\n
к центру Земли\n\n\n
Копает всё дальше, копает сильнее
Бурит она сквозь почву и магму
Чтоб Солнце увидеть с другой стороны\n\n

У дороги\n
говорю я\n
с девочкой одной\n\n
Она даёт мне\n
лопату\n
чтобы с ней я вместе копала\n\n
Не смею я задавать ей вопросы
О намерениях её и обо всём остальном
Лишь жестом показала\n
копать вместе с ней\n\n

У дороги\n
копаем мы\n
свой собственный путь\n\n
До земли\n
где можем мы\n
Солнце увидеть\n
с другой стороны\n\n\n
После тысячи лет темноты
Она мне наконец предоставила
Возможность солнце увидеть\n\n\n\n\n\n\n\n\n
с другой стороны"""
    )

image paper = "mod_assets/source/images/bg/poem/poem.webp"
image paper_glitch = LiveComposite((1280, 720), (0, 0), "paper_glitch1", (0, 0), "paper_glitch2")
image paper_glitch1 = "mod_assets/source/images/bg/poem/poem-glitch1.webp"
image paper_glitch2:
    "mod_assets/source/images/bg/poem/poem-glitch2.webp"
    block:
        yoffset 0
        0.05
        yoffset 20
        0.05
        repeat


transform paper_in:
    truecenter
    alpha 0
    linear 1.0 alpha 1

transform paper_out:
    alpha 1
    linear 1.0 alpha 0

screen poem(currentpoem, paper="paper"):
    style_prefix "poem"
    vbox:
        add paper
    viewport id "vp":
        child_size (710, None)
        mousewheel True
        draggable True
        has vbox
        null height 40
        if currentpoem.author == "yuri":
            if currentpoem.yuri_2:
                text "[currentpoem.title]\n\n[currentpoem.text]" style "yuri_text"
            elif currentpoem.yuri_3:
                text "[currentpoem.title]\n\n[currentpoem.text]" style "yuri_text_3"
            else:
                text "[currentpoem.title]\n\n[currentpoem.text]" style "yuri_text"
        elif currentpoem.author == "sayori":
            text "[currentpoem.title]\n\n[currentpoem.text]" style "sayori_text"
        elif currentpoem.author == "natsuki":
            text "[currentpoem.title]\n\n[currentpoem.text]" style "natsuki_text"
        elif currentpoem.author == "monika":
            text "[currentpoem.title]\n\n[currentpoem.text]" style "monika_text"
        null height 100
    vbar value YScrollValue(viewport="vp") style "poem_vbar"



style poem_vbox:
    xalign 0.5
style poem_viewport:
    xanchor 0
    xsize 720
    xpos 280
style poem_vbar is vscrollbar:
    xpos 1000
    yalign 0.5

    ysize 700





style yuri_text:
    font "mod_assets/source/fonts/poemdreest/y1.ttf"
    size 28
    color "#000"
    outlines []

style yuri_text_2:
    font "mod_assets/source/fonts/poemdreest/y2.ttf"
    size 26
    color "#000"
    outlines []

style yuri_text_3:
    font "mod_assets/source/fonts/poemdreest/y3.ttf"
    size 20
    color "#000"
    outlines []
    justify True

style natsuki_text:
    font "mod_assets/source/fonts/poemdreest/n1.ttf"
    size 28
    color "#000"
    outlines []
    line_leading 1

style sayori_text:
    font "mod_assets/source/fonts/poemdreest/s1.ttf"
    size 22
    color "#000"
    outlines []

style monika_text:
    font "mod_assets/source/fonts/poemdreest/m1.ttf"
    size 22
    color "#000"
    outlines []

label showpoem(poem=None, music=True, track=None, revert_music=True, img=None, where=i11, paper=None):
    if poem == None:
        return
    play sound page_turn
    window hide
    if paper:
        show screen poem(poem, paper=paper)
    else:
        show screen poem(poem)
    if not persistent.first_poem:
        $ persistent.first_poem = True
        show expression "mod_assets/source/images/gui/poem_dismiss.webp" as poem_dismiss:
            xpos 1050 ypos 590
    with Dissolve(1)
    $ pause()
    if img:
        $ renpy.hide(poem.author)
        $ renpy.show(img, at_list=[where])
    hide screen poem
    hide poem_dismiss
    with Dissolve(.5)
    window auto
    return
