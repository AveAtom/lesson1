from math import inf

"""Модуль true_math() к module_4_1.py."""


def divide(first=1, second=1):
    """Функция true_math.divide() возвращает результат деления first на second, но когда в second записан 0 - возвращать бесконечность."""
    if second == 0:
        return inf  # Возвращает бесконечность
    else:
        return first / second  # Возвращаем деление first на second
