"""Модуль fake_math() к module_4_1.py"""


def divide(first=1, second=1):
    """Функция fake_math.divide() возвращает результат деления first на second, но когда в second записан 0 - возвращать строку 'Ошибка'."""
    if second == 0:
        return 'Ошибка'  # Возвращает Ошибка
    else:
        return first / second  # Возвращаем деление first на second
