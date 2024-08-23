# TRUE STORY OPTIONS
# by @b3rg3n
# since 2024

python early:
    config.allow_duplicate_labels = True

define config.developer = True # РЕЖИМ РАЗРАБОТЧИКА БЕЗ СДК
define config.version = "1.1"
define ts_version = "22.08.2024"

define config.name = _("True Story")
define config.save_directory = None
define build.name = "truestory"
define gui.show_name = False
define config.has_sound = True
define config.has_music = True
define config.has_voice = True
define config.enter_transition = cLinearBlur(0.5)
define config.exit_transition = cLinearBlur(0.5)
define config.intra_transition = ImageDissolve(ts_anim + "transit/wipeleft.webp", 0.5, ramplen=64)
define config.after_load_transition = MultipleTransition([False, ImageDissolve(ts_anim + "transit/wipeleft.webp", 0.5, ramplen=64), Solid("#000"), Pause(0.25), Solid("#000"), ImageDissolve(ts_anim + "transit/wipeleft.webp", 0.5, ramplen=64), True])
define config.end_game_transition = Fade(1.5, 1, 2)
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)
define config.window = "auto"
default preferences.text_cps = 50
default preferences.afm_time = 15
define config.window_icon = ts_images + "gui/window_icon.png"
define config.layers = [ 'master', 'transient', 'screens', 'overlay', 'front' ]

define config.image_cache_size = 64
define config.predict_statements = 50
define config.menu_clear_layers = ["front"]

define gui.about = _p("""
""")