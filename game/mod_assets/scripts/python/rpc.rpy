# TRUE STORY DISCORD RPC
# by @b3rg3n
# since 2024

init python:
    from pypresence import DiscordNotFound # ИМПОРТИРУЕМ НУЖНУЮ ОШИБКУ ПИТОНА (ЛЕЖАТ В python-packages)
    from pypresence import Presence # ИМПОРТИРУЕМ НУЖНУЮ ФУНКЦИЮ ПИТОНА (ЛЕЖАТ В python-packages)
    import time # ИМПОРТИРУЕМ ВРЕМЯ ДЛЯ СЧЁТЧИКА

    rpc = Presence("1162284314239701062") # ID ХУЕТЫ

    if persistent.rpc_mode:
        try:
            rpc.connect() # ПОДКЛЮЧЕНИЕ К ДС
        except DiscordNotFound:
            pass
        except ConnectionRefusedError:
            pass
    else:
        pass

    def ts_rpc_splash():
        if persistent.rpc_mode:
            try:
                if _preferences.language == "english":
                    rpc.update(state="In game",details="Looking at splash screen",large_image="logogovna",start=time.time())
                else:
                    rpc.update(state="В игре",details="Просмотр заставки",large_image="logogovna",start=time.time())
            except AssertionError:
                pass
        else:
            pass

    def ts_rpc_main_menu():
        if persistent.rpc_mode:
            try:
                if _preferences.language == "english":
                    rpc.update(state="In game",details="Main Menu",large_image="logogovna",start=time.time())
                else:
                    rpc.update(state="В игре",details="Главное меню",large_image="logogovna",start=time.time())
            except AssertionError:
                pass
        else:
            pass

    def ts_rpc_carter0():
        if persistent.rpc_mode:
            try:
                if _preferences.language == "english":
                    rpc.update(state="Act I | Prologue",details="In The Beginning",large_image="prologue",start=time.time())
                else:
                    rpc.update(state="Акт I | Пролог",details="Предыстория",large_image="prologue",start=time.time())
            except AssertionError:
                pass
        else:
            pass

    def ts_rpc_carter1():
        if persistent.rpc_mode:
            try:
                if _preferences.language == "english":
                    rpc.update(state="Act I | Chapter I",details="Searching. Sayori",large_image="aonecone",start=time.time())
                else:
                    rpc.update(state="Акт I | Глава I",details="Поиски. Сайори",large_image="aonecone",start=time.time())
            except AssertionError:
                pass
        else:
            pass

    def ts_rpc_carter2():
        if persistent.rpc_mode:
            try:
                if _preferences.language == "english":
                    rpc.update(state="Act I | Chapter II",details="Searching. Yuri",large_image="aonectwo",start=time.time())
                else:
                    rpc.update(state="Акт I | Глава II",details="Поиски. Юри",large_image="aonectwo",start=time.time())
            except AssertionError:
                pass
        else:
            pass

    def ts_rpc_carter3():
        if persistent.rpc_mode:
            try:
                if _preferences.language == "english":
                    rpc.update(state="Act I | Chapter III",details="Searching. Natsuki",large_image="aonecthree",start=time.time())
                else:
                    rpc.update(state="Акт I | Глава III",details="Поиски. Нацуки",large_image="aonecthree",start=time.time())
            except AssertionError:
                pass
        else:
            pass

    def ts_rpc_carter4():
        if persistent.rpc_mode:
            try:
                if _preferences.language == "english":
                    rpc.update(state="Act I | Chapter IV",details="Is All Good?",large_image="aonecfour",start=time.time())
                else:
                    rpc.update(state="Акт I | Глава IV",details="Всё же хорошо?",large_image="aonecfour",start=time.time())
            except AssertionError:
                pass
        else:
            pass

    def ts_rpc_carter5():
        if persistent.rpc_mode:
            try:
                if _preferences.language == "english":
                    rpc.update(state="Act II | Chapter I",details="Welcome Back, Monika!",large_image="atwocone",start=time.time())
                else:
                    rpc.update(state="Акт II | Глава I",details="С возвращением, Моника!",large_image="atwocone",start=time.time())
            except AssertionError:
                pass
        else:
            pass

    def ts_rpc_carter6():
        if persistent.rpc_mode:
            try:
                if _preferences.language == "english":
                    rpc.update(state="Act II | Chapter II",details="Broadening Horizons",large_image="atwoctwo",start=time.time())
                else:
                    rpc.update(state="Акт II | Глава II",details="Новые начинания",large_image="atwoctwo",start=time.time())
            except AssertionError:
                pass
        else:
            pass

    def ts_rpc_carter7():
        if persistent.rpc_mode:
            try:
                if _preferences.language == "english":
                    rpc.update(state="Act II | Chapter III",details="Feather Expansion",large_image="atwocthree",start=time.time())
                else:
                    rpc.update(state="Акт II | Глава III",details="Пробы пера",large_image="atwocthree",start=time.time())
            except AssertionError:
                pass
        else:
            pass

    def ts_rpc_carter8():
        if persistent.rpc_mode:
            try:
                if _preferences.language == "english":
                    rpc.update(state="Act II | Chapter IV",details="Calm before the storm",large_image="atwocfour",start=time.time())
                else:
                    rpc.update(state="Акт II | Глава IV",details="Затишье перед бурей",large_image="atwocfour",start=time.time())
            except AssertionError:
                pass
        else:
            pass

    def ts_rpc_carter9():
        if persistent.rpc_mode:
            try:
                if _preferences.language == "english":
                    rpc.update(state="Act III | Chapter I",details="Welcome Back... Again?",large_image="atwocfour",start=time.time())
                else:
                    rpc.update(state="Акт III | Глава I",details="С возвращением... Снова?",large_image="atwocfour",start=time.time())
            except AssertionError:
                pass
        else:
            pass

    def ts_rpc_carter10():
        if persistent.rpc_mode:
            try:
                if _preferences.language == "english":
                    rpc.update(state="Act III | Chapter II",details="Descent To Madness",large_image="atwocthree",start=time.time())
                else:
                    rpc.update(state="Акт III | Глава II",details="Спуск в безумие",large_image="atwocthree",start=time.time())
            except AssertionError:
                pass
        else:
            pass

    def ts_rpc_carter11():
        if persistent.rpc_mode:
            try:
                if _preferences.language == "english":
                    rpc.update(state="Act III | Chapter III",details="More Of The Same",large_image="aonecthree",start=time.time())
                else:
                    rpc.update(state="Акт III | Глава III",details="Порочный круг",large_image="aonecthree",start=time.time())
            except AssertionError:
                pass
        else:
            pass

    def ts_rpc_carter12():
        if persistent.rpc_mode:
            try:
                if _preferences.language == "english":
                    rpc.update(state="Epilogue",details="Into The Abyss",large_image="aonecthree",start=time.time())
                else:
                    rpc.update(state="Эпилог",details="В бездну",large_image="aonecthree",start=time.time())
            except AssertionError:
                pass
        else:
            pass

    def ts_rpc_carter13():
        if persistent.rpc_mode:
            try:
                if _preferences.language == "english":
                    rpc.update(state="Epilogue",details="Just a dream...",large_image="aonectwo",start=time.time())
                else:
                    rpc.update(state="Эпилог",details="Всего лишь сон...",large_image="aonectwo",start=time.time())
            except AssertionError:
                pass
        else:
            pass

    def ts_rpc_credits():
        if persistent.rpc_mode:
            try:
                if _preferences.language == "english":
                    rpc.update(state="Finale",details="Credits",large_image="credits",start=time.time())
                else:
                    rpc.update(state="Финал",details="Титры",large_image="credits",start=time.time())
            except AssertionError:
                pass
        else:
            pass

    def ts_rpc_development():
        if persistent.rpc_mode:
            try:
                if _preferences.language == "english":
                    rpc.update(state=glitchtext(12),details="Doing stuff again",large_image="logogovna",start=time.time())
                else:
                    rpc.update(state=glitchtext(12),details="Снова что-то мутит",large_image="logogovna",start=time.time())
            except AssertionError:
                pass
        else:
            pass