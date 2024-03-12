init:
#ГОПАЕМ ЮЗЕРНАЙМ
    if renpy.android or renpy.ios:
        $ user = "Игрок"
    else:
        $ user = os.environ.get('username')