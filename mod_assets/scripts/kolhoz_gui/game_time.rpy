init python:
    import datetime
    persistent.game_last_time = datetime.datetime.now()
    if persistent.gametime is None:
        persistent.gametime = 0
    def show_gametime(st, at):
        t = datetime.datetime.now()
        dt = t - persistent.game_last_time
        persistent.game_last_time = t
        persistent.gametime += dt.total_seconds()
        minutes, seconds = divmod(int(persistent.gametime), 60)
        hours, minutes = divmod(minutes, 60)
        img = Text("{size=+15}{font=[cit_font]}%0*d:%0*d:%0*d{/font}{/size}" % (2, hours, 2, minutes, 2, seconds))
        return img, .1

init:

    image gametime = DynamicDisplayable(show_gametime)