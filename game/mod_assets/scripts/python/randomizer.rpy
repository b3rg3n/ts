# РАНДОМАЙЗЕР ДЛЯ ПЕРЕМЕННЫХ
# by @b3rg3n
# Since 2024

init python:
    import random

    def generate_random_number():
        globals()['random_test_label'] = random.randint(1, 2) # ЗАПИСЫВАЕМ РАНДОМНОЕ ЗНАЧЕНИЕ

init:
    $ random_test_label = 0 # ЗАПИСЫВАЕМ ЗНАЧЕНИЕ В ПЕРЕМЕННУЮ

#    $ generate_random_number() # ВЫЗОВ ФУНКЦИИ НА ПЕРЕЗАПИСЬ ПЕРЕМЕННОЙ