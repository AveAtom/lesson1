print("=== Доступ к свойствам родителя. Переопределение свойств. ====\n")


# Задача "Изменять нельзя получать.":
# В этой задаче мы реализуем классы транспорта, в которых нельзя будет просто так поменять цвет, мощность двигателя и
# прочие свойства, т.к. в реальной жизни это чаще всего делается не владельцем, а в специальных сервисах.
# Да, узнать значения этих свойств мы сможем, но вот изменить - нет.
# Вам необходимо создать 2 класса: Vehicle и Sedan, где Vehicle - это любой транспорт, а Sedan(седан) -
# наследник класса Vehicle.
# I. Каждый объект Vehicle должен содержать следующие атрибуты объекта:
# 1.Атрибут owner(str) - владелец транспорта. (владелец может меняться)
# 2.Атрибут __model(str) - модель (марка) транспорта. (мы не можем менять название модели)
# 3.Атрибут __engine_power(int) - мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
# 4.Атрибут __color(str) - название цвета. (мы не можем менять цвет автомобиля своими руками)
# А так же атрибут класса:
# 1.Атрибут класса __COLOR_VARIANTS, в который записан список допустимых цветов для окрашивания. (Цвета написать свои)
# 2.Каждый объект Vehicle должен содержать следующий методы:
# 3.Метод get_model - возвращает строку: "Модель: <название модели транспорта>"
# 4.Метод get_horsepower - возвращает строку: "Мощность двигателя: <мощность>"
# 5.Метод get_color - возвращает строку: "Цвет: <цвет транспорта>"
# 6.Метод print_info - распечатывает результаты методов (в том же порядке): get_model, get_horsepower, get_color;
# а так же владельца в конце в формате "Владелец: <имя>"
# 7.Метод set_color - принимает аргумент new_color(str), меняет цвет __color на new_color, если он есть
# в списке __COLOR_VARIANTS, в противном случае выводит на экран надпись: "Нельзя сменить цвет на <новый цвет>".
# Взаимосвязь методов и скрытых атрибутов:
# 1.Методы get_model, get_horsepower, get_color находятся в одном классе с соответствующими им атрибутами:
# __model, __engine_power, __color. Поэтому атрибуты будут доступны для методов.
# 2.Атрибут класса __COLOR_VARIANTS можно получить обращаясь к нему через объект(self).
# 3.Проверка в __COLOR_VARIANTS происходит не учитывая регистр ('BLACK' ~ 'black').
# II. Класс Sedan наследуется от класса Vehicle, а так же содержит следующие атрибуты:
# 1.Атрибут __PASSENGERS_LIMIT = 5 (в седан может поместиться только 5 пассажиров)
# Пункты задачи:
# 1.Создайте классы Vehicle и Sedan.
# 2.Напишите соответствующие свойства в обоих классах.
# 3.Не забудьте сделать Sedan наследником класса Vehicle.
# 4.Создайте объект класса Sedan и проверьте, как работают все его методы, взяты из класса Vehicle.
# Примечания:
# 1.Обращайте особое внимание на условия задачи: что является атрибутом класса, а что атрибутом объекта.
# 2.Методы, где описано получение/перезапись каких-либо атрибутов рекомендуется начинать со слов get и set соответственно.
# Такие методы часто используются для доступа к скрытым атрибутам и позволяют написать дополнительную логику(код)
# при их получении/изменении.
# 3.Не забывайте использовать self при обращении к атрибутам объекта.
# 4.Константные(постоянные) значения в Python принято писать полностью в верхнем регистре (капсом), как в случае
# списка цветов или количеством пассажиров.
# ***************************************************************************************************************
# === Классы ===
class ValidationError(Exception):  # Для перехвата ошибок переопределяем класс ValidationError
    pass


class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner=""):
        self.owner = owner  # владелец транспорта. (владелец может меняться)
        self.__model = ""  # модель (марка) транспорта. (мы не можем менять название модели)
        self.__engine_power = 0  # мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
        self.__color = ""  # название цвета. (мы не можем менять цвет автомобиля своими руками)

    # Для записи данных в закрытые атрибуты используем отдельные методы set_
    def set_model(self, model):
        self.__model = model

    def set_power(self, power):
        self.__engine_power = power

    def set_color(self,
                  new_color=""):  # Принимает аргумент new_color(str), меняет цвет __color на new_color, если он есть
        # в списке __COLOR_VARIANTS, в противном случае выводит на экран надпись:
        # "Нельзя сменить цвет на <новый цвет>".
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'\nНельзя сменить цвет на {new_color}.')

    # Для получения данных из закрытых атрибутов используем методы get_
    def get_model(self):  # Возвращает строку: "Модель: <название модели транспорта>"
        return self.__model

    def get_horsepower(self):  # Возвращает строку: "Мощность двигателя: <мощность>"
        return self.__engine_power

    def get_color(self):  # Возвращает строку: "Цвет: <цвет транспорта>"
        return self.__color

    # Метод отображения информации о машине
    def print_info(self):  # Распечатывает результаты методов (в том же порядке): get_model, get_horsepower, get_color;
        # а так же владельца в конце в формате "Владелец: <имя>"
        print(f'\nМодель: {self.get_model()}')
        print(f'Мощность двигателя: {self.get_horsepower()}')
        print(f'Цвет: {self.get_color()}')
        print(f'Владелец: {self.owner}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5  # В седан может поместиться только 5 пассажиров

    def __init__(self, owner, model, color, power):
        super().__init__()
        self.owner = owner
        self.set_model(model)
        self.set_power(power)
        self.set_color(color)


# === Прогон ===
# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
print(f'Содержимое экземпляра - {vehicle1.__dict__}')
# Изначальные свойства
vehicle1.print_info()
# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
# Проверяем что поменялось
vehicle1.print_info()

print('\n=== Конец обработки === ')
