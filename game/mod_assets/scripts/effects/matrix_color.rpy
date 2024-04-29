# TRUE STORY SPRITES TIME
# by @b3rg3n
# SINCE 2024

# КАК ЮЗАТЬ ЭТУ ПОЕБЕНЬ:
# НУЖНЫ ДНЕВНЫЕ СПРАЙТЫ? $ ts_day_time()
# НОЧНЫЕ $ ts_night_time()
# НЕ НОЧНЫЕ, НО И НЕ ДНЕВНЫЕ $ ts_sunset_time()

# ТАК ЖЕ И С ОБЕСЦВЕТОМ

init python:
    def ts_day_time():
        persistent.sprite_time='day'
    def ts_sunset_time():
        persistent.sprite_time='sunset'
    def ts_night_time():
        persistent.sprite_time='night'

    def ts_uncolorize_off():
        persistent.uncolorize='none'
    def ts_uncolorize_lite():
        persistent.uncolorize='lite'
    def ts_uncolorize_full():
        persistent.uncolorize='full'

init:
    default persistent.sprite_time = 'day'
    default persistent.uncolorize = 'none'