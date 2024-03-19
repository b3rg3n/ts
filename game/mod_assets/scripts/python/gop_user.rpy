init python:
    import os
    import getpass

init:
#ГОПАЕМ ЮЗЕРНАЙМ
    if renpy.android or renpy.ios:
        $ user = "Игрок"
    if renpy.linux:
        $ user = getpass.getuser()
    else:
        $ user = os.environ.get('username')