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

    build.archive("ts_engine", "all")
    build.archive("ts_image", "all")
    build.archive("ts_audio", "all")
    build.archive("ts_video", "all")
    build.archive("ts_font", "all")

    build.classify("game/**.jpg", "ts_image")
    build.classify("game/**.jpeg", "ts_image")
    build.classify("game/**.webp", "ts_image")
    build.classify("game/**.png", "ts_image")

    build.classify("game/**.rpyc", "ts_engine")
    build.classify("game/**.rpy", "ts_engine")

    build.classify("game/**.pyc", "ts_engine")
    build.classify("game/**.py", "ts_engine")

    build.classify("game/**.wav", "ts_audio")
    build.classify("game/**.mp3", "ts_audio")
    build.classify("game/**.ogg", "ts_audio")

    build.classify("game/**.otf", "ts_font")
    build.classify("game/**.ttf", "ts_font")

    build.classify("game/**.webm", "ts_video")
    build.classify("game/**.ogv", "ts_video")
    build.classify("game/**.ogm", "ts_video")

    build.documentation('*.html')
    build.documentation('*.txt')
