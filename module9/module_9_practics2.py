# Задача - есть функция, которая возвращает результат введения числа a в степень b
# Нужно ускорить ее, чтобы она не делала повторные вычисления.
from functools import lru_cache,wraps

# def func1(f, *args, **kwargs):  # Нужна для определения получено ли значение из функции или из кэша.
#     hits = f.cache_info().hits  # Запоминаем текущее значение счетчика. Спонсор cache_info().hits - lru_cache().
#     res = f(*args, **kwargs)
#     if f.cache_info().hits > hits:  # Если значение изменилось - значит оно бралось из кэша.
#         print(f'Выполняем функцию с аргументами ({args[0]},{args[1]}) ')
#         res = f'Функция уже была выполнена раньше, ответ={res}'
#     else:
#         res = f'Функция выполнилась, ответ = {res}'
#
#     return res
def dec_lru(f):
    @wraps(f)
    def wrapper(*args):
        global hits,info
        res = f(*args)

        if f.cache_info().hits>hits:
            print(f'Выполняем функцию с аргументами ({','.join(map(str,args))}) ')
            res = f'Функция уже была выполнена раньше, ответ={res}'
        else:
            res = f'Функция выполнилась, ответ = {res}'
        hits = f.cache_info().hits
        info = f.cache_info()
        return res
    return wrapper

@dec_lru
@lru_cache(maxsize=32)
# В качестве кэширующего декоратора используем lru_cache() из модуля functools
def func(a, b):
    """ Docs a**b """
    print(
        f'Выполняем функцию с аргументами ({a},{b}) ')  # Не будет выполняться, если бралось из кэша (перехват lru_cache).
    return a ** b


# print(func1(func, 3, 5), '\n')
# print(func1(func, 3, 4), '\n')
# print(func1(func, 3, 2), '\n')
# print(func1(func, 3, 5), '\n')
# print(func1(func, 3, 4), '\n')
# print(func1(func, 3, 5), '\n')
hits=0
info=None
print(func(3,5),'\n')
print(func(3,4),'\n')
print(func(3,2),'\n')
print(func(3,5),'\n')
print(func(3,4),'\n')
print(func(3,5),'\n')

print(info)
print(func.__doc__,func.__name__)