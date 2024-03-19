# TRUE STORY DISCORD RPC
# by @b3rg3n
# since 2024

init python:
    from pypresence import DiscordNotFound # ИМПОРТИРУЕМ НУЖНУЮ ОШИБКУ ПИТОНА (ЛЕЖАТ В python-packages)
    from pypresence import Presence # ИМПОРТИРУЕМ НУЖНУЮ ФУНКЦИЮ ПИТОНА (ЛЕЖАТ В python-packages)
    import time # ИМПОРТИРУЕМ ВРЕМЯ ДЛЯ СЧЁТЧИКА

    rpc = Presence("1162284314239701062") # ID ХУЕТЫ
    try:
        rpc.connect() # ПОДКЛЮЧЕНИЕ К ДС
    except DiscordNotFound:
        pass
    except ConnectionRefusedError:
        pass

# КАК ЮЗАТЬ ЭТУ ПОЕБЕНЬ:
#
#    python: # ОБНОВЛЯЕМ RPC
#        try:
#            rpc.update(state="Акт I | Глава I",details="Поиски. Сайори",large_image="logogovna",start=time.time())
#        except AssertionError:
#            pass
#
# ЭТО ВСЁ ВСТАВИТЬ В НУЖНЫЙ ЛЕЙБЛ
# state - ВТОРАЯ СТРОКА
# details - ПЕРВАЯ СТРОКА
# large_image - КАРТИНКА АКТИВНОСТИ В ДС

label after_load: # ВОСКРЕШЕНИЕ RPC ПРИ ЗАГРУЗКЕ
    if persistent.rpclabel == "0":
            python: # ОБНОВЛЯЕМ RPC
                try:
                    rpc.update(state="Акт I | Пролог",details="Предыстория",large_image="prologue",start=time.time())
                except AssertionError:
                    pass
    elif persistent.rpclabel == "1":
            python: # ОБНОВЛЯЕМ RPC
                try:
                    rpc.update(state="Акт I | Глава I",details="Поиски. Сайори",large_image="aonecone",start=time.time())
                except AssertionError:
                    pass
    elif persistent.rpclabel == "2":
            python: # ОБНОВЛЯЕМ RPC
                try:
                    rpc.update(state="Акт I | Глава II",details="Поиски. Юри",large_image="aonectwo",start=time.time())
                except AssertionError:
                    pass
    elif persistent.rpclabel == "3":
            python: # ОБНОВЛЯЕМ RPC
                try:
                    rpc.update(state="Акт I | Глава III",details="Поиски. Нацуки",large_image="aonecthree",start=time.time())
                except AssertionError:
                    pass
    elif persistent.rpclabel == "4":
            python: # ОБНОВЛЯЕМ RPC
                try:
                    rpc.update(state="Акт I | Глава IV",details="Всё же хорошо?",large_image="aonecfour",start=time.time())
                except AssertionError:
                    pass
    elif persistent.rpclabel == "5":
            python: # ОБНОВЛЯЕМ RPC
                try:
                    rpc.update(state="Акт II | Глава I",details="С возвращением, Моника!",large_image="atwocone",start=time.time())
                except AssertionError:
                    pass

    elif persistent.rpclabel == "999":
            python: # ОБНОВЛЯЕМ RPC
                try:
                    rpc.update(state="Финал",details="Титры",large_image="credits",start=time.time())
                except AssertionError:
                    pass
