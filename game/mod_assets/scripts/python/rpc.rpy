# TRUE STORY DISCORD RPC
# by @b3rg3n
# since 2024

init python:
    from pypresence import Presence
    import time

    rpc = Presence("1162284314239701062") # ID ХУЕТЫ
    rpc.connect() # ПОДКЛЮЧЕНИЕ К ДС

# КАК ЮЗАТЬ ЭТУ ПОЕБЕНЬ:
#
#    python:
#        rpc.update(state="Акт I | Глава I",details="Поиски. Сайори",large_image="logogovna",start=time.time())
#
# ЭТО ВСЁ ВСТАВИТЬ В НУЖНЫЙ ЛЕЙБЛ
# state - ВТОРАЯ СТРОКА
# details - ПЕРВАЯ СТРОКА
# large_image - КАРТИНКА АКТИВНОСТИ В ДС