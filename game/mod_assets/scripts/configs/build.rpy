# TRUE STORY BUILD CONFIG
# by @b3rg3n
# since 2024
init python:

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**.md', None)
    build.classify('**.rpyb', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rar', None)
    build.classify('**.zip', None)
    build.classify('**.7z', None)
    build.classify('game/mod_assets/scripts/.vscode/**', None)
    build.classify('game/cache/**', None)
    build.classify('game/tl/**', None)
    build.classify('game/renpy-ActionEditor3-master/**', None)

    build.archive("truestory", "all")
    build.archive("scripts", "all")

    build.classify("game/**.jpg", "truestory")
    build.classify("game/**.jpeg", "truestory")
    build.classify("game/**.webp", "truestory")
    build.classify("game/**.png", "truestory")

    build.classify("game/**.rpyc", "scripts")
    build.classify("game/**.rpy", "scripts")

    build.classify("game/**.pyc", "scripts")
    build.classify("game/**.py", "scripts")

    build.classify("game/**.wav", "truestory")
    build.classify("game/**.mp3", "truestory")
    build.classify("game/**.ogg", "truestory")

    build.classify("game/**.otf", "truestory")
    build.classify("game/**.ttf", "truestory")

    build.classify("game/**.webm", "truestory")
    build.classify("game/**.ogv", "truestory")
    build.classify("game/**.ogm", "truestory")

    build.documentation('*.html')
    build.documentation('*.txt')
