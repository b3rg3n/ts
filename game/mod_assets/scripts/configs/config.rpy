# TRUE STORY OPTIONS
# by @b3rg3n
# since 2024

python early:
    config.allow_duplicate_labels = True
    #config.framebuffer_vsync = False
    #config.max_fps = 0
    #config.refresh_rate = 360
    #config.framerate = 1000

define config.name = _("True Story")
define gui.show_name = False
define config.version = "1.0"

define gui.about = _p("""
""")

define build.name = "truestory"
define config.has_sound = True
define config.has_music = True
define config.has_voice = True
define config.enter_transition = ImageDissolve(("mod_assets/source/images/anim/transit/blackpalm.webp"), 0.25, ramplen=256, reverse=True)
define config.exit_transition = ImageDissolve(("mod_assets/source/images/anim/transit/blackpalm.webp"), 0.3, ramplen=256)
define config.intra_transition = ImageDissolve(im.Tile("mod_assets/source/images/anim/transit/pattern.webp"), 0.4, 1)
define config.after_load_transition = MultipleTransition([False, ImageDissolve("mod_assets/source/images/anim/transit/wipeleft.webp", 0.5, ramplen=64), Solid("#000"), Pause(0.25), Solid("#000"), ImageDissolve("mod_assets/source/images/anim/transit/wipeleft.webp", 0.5, ramplen=64), True])
define config.end_game_transition = Fade(1.5, 1, 2)
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)
define config.window = "auto"
default preferences.text_cps = 50
default preferences.afm_time = 15
define config.save_directory = "truestory"
define config.window_icon = "mod_assets/source/images/gui/window_icon.png"
define config.layers = [ 'master', 'transient', 'screens', 'overlay', 'front' ]

define config.image_cache_size = 64
define config.predict_statements = 50
define config.menu_clear_layers = ["front"]

define config.developer = True # РЕЖИМ РАЗРАБОТЧИКА БЕЗ СДК