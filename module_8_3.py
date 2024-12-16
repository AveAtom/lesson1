from gevent.pool import pass_value

print("=== Создание исключений. ====\n")


# Задача "Некорректность.":
#
# Создайте 3 класса (2 из которых будут исключениями):
# Класс Car должен обладать следующими свойствами:
# 1.Атрибут объекта model - название автомобиля (строка).
# 2.Атрибут объекта __vin - vin номер автомобиля (целое число). Уровень доступа private.
# 3.Метод __is_valid_vin(vin_number) - принимает vin_number и проверяет его на корректность. Возвращает True,
# если корректный, в других случаях выбрасывает исключение. Уровень доступа private.
# 4.Атрибут __numbers - номера автомобиля (строка).
# 5.Метод __is_valid_numbers(numbers) - принимает numbers и проверяет его на корректность. Возвращает True,
# если корректный, в других случаях выбрасывает исключение. Уровень доступа private.
# 6.Классы исключений IncorrectVinNumber и IncorrectCarNumbers, объекты которых обладают атрибутом message - сообщение,
# которое будет выводиться при выбрасывании исключения.
#
# Работа методов __is_valid_vin и __is_valid_numbers:
# __is_valid_vin
# 1.Выбрасывает исключение IncorrectVinNumber с сообщением 'Некорректный тип vin номер', если передано не целое число.
# (тип данных можно проверить функцией isinstance).
# 2.Выбрасывает исключение IncorrectVinNumber с сообщением 'Неверный диапазон для vin номера', если переданное число
# находится не в диапазоне от 1000000 до 9999999 включительно.
# 3.Возвращает True, если исключения не были выброшены.
# __is_valid_numbers
# 1.Выбрасывает исключение IncorrectCarNumbers с сообщением 'Некорректный тип данных для номеров', если передана
# не строка. (тип данных можно проверить функцией isinstance).
# 2..Выбрасывает исключение IncorrectCarNumbers с сообщением 'Неверная длина номера', переданная строка должна
# состоять ровно из 6 символов.
# 3.Возвращает True, если исключения не были выброшены.
#
# ВАЖНО!
# Методы __is_valid_vin и __is_valid_numbers должны вызываться и при создании объекта (в __init__ при объявлении
# атрибутов __vin и __numbers).
#
# Примечания:
# 1.Для выбрасывания исключений используйте оператор raise
# ********************************************************************************************************************
# === Классы ===
class IncorrectVinNumber(Exception):  # Класс обработки исключения по Vin номеру.
    def __init__(self, message, vin_number):
        self.message = message  # Описание исключения.
        self.vin_number = vin_number  # Обрабатываемый параметр.


class IncorrectCarNumbers(Exception):  # Класс обработки исключения по номеру машины.
    def __init__(self, message, car_number):
        self.message = message  # Описание исключения.
        self.car_number = car_number  # Обрабатываемый параметр.


class Car:
    def __init__(self, model: str = "", vin_number: int = 0, car_number: str = ""):
        self.model = model  # Модель машины
        self.__vin = vin_number if self.__is_valid_vin(vin_number) else 0  # Vin номер с проверкой.
        self.__numbers = car_number if self.__is_valid_numbers(car_number) else ""  # Номер машины с проверкой.

    def __is_valid_vin(self, vin_number) -> bool:  # Проверка Vin номера.
        if not isinstance(vin_number, int):  # Если передано не целое число.
            raise IncorrectVinNumber(f'Некорректный тип vin номер {type(vin_number)}', vin_number)
        elif not (1000000 <= vin_number <= 9999999):  # Если переданное число находится не в диапазоне
            # от 1000000 до 9999999 включительно.
            raise IncorrectVinNumber('Неверный диапазон для vin номера', vin_number)
        else:
            return True

    def __is_valid_numbers(self, car_number) -> bool:  # Проверка номера машины.
        if not isinstance(car_number, str):  # Если передана не строка.
            raise IncorrectCarNumbers(f'Некорректный тип данных для номеров {type(car_number)}', car_number)
        elif len(car_number) != 6:  # Переданная строка должна состоять ровно из 6 символов.
            raise IncorrectCarNumbers('Неверная длина номера', car_number)
        else:
            return True


# === Прогон ===
try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message, exc.vin_number, sep=' - ')
except IncorrectCarNumbers as exc:
    print(exc.message, exc.car_number, sep=' - ')
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message, exc.vin_number, sep=' - ')
except IncorrectCarNumbers as exc:
    print(exc.message, exc.car_number, sep=' - ')
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message, exc.vin_number, sep=' - ')
except IncorrectCarNumbers as exc:
    print(exc.message, exc.car_number, sep=' - ')
else:
    print(f'{third.model} успешно создан')

print('\n=== Конец обработки === ')
