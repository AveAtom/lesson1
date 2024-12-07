print("=== Различие атрибутов класса и экземпляра. ====\n")


# Задача "История строительства":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Перегрузка операторов".
# В классе House создайте атрибут houses_history = [], который будет хранить названия созданных объектов.
# Правильней вписывать здание в историю сразу при создании объекта, тем более можно удобно обращаться к атрибутам
# класса используя ссылку на сам класс - cls.
# Дополните метод __new__ так, чтобы:
# 1.Название объекта добавлялось в список cls.houses_history.
# 2.Название строения можно взять из args по индексу.
# Также переопределите метод __del__(self) в котором будет выводиться строка:
# "<название> снесён, но он останется в истории"
# Создайте несколько объектов класса House и проверьте работу методов __del__ и __new__, а также значение атрибута
# houses_history.
# Примечания:
# 1.Более подробно о работе метода __new__ можно узнать здесь.
# https://docs.python.org/3/reference/datamodel.html#object.__new__
# 2.В методе __new__ можно обращаться к атрибутам текущего класса при помощи параметра cls.
# *****************************************************************************************************************
# Дополнение:
# 1 Хочу, чтобы в конце программы выходила надпись: "Конец обработки", но из-за переопределения __del__ данная надпись
# появляется предпоследней. Поэтому вывод данной надписи переносим в __del__ и вводим счетчик экземпляров counter.
# Когда counter = 0 - все экземпляры удалены, а значит - конец обработки.

# === Классы ===
class ValidationError(Exception):  # Для перехвата ошибок конструкцией try - except переопределяем класс ValidationError
    pass


class House:
    # ---- Начало изменений по модулю module_5_4.py ----------------------

    houses_history = []  # Создаем атрибут который будет хранить названия созданных объектов.
    counter = 0  # Создаем атрибут экземпляров класса.

    # ---- Конец изменений по модулю module_5_4.py
    head = 1

    # ---- Начало изменений по модулю module_5_4.py ----------------------

    def __new__(cls, *args, **kwargs):  # Переопределяем метод __new__
        cls.houses_history.append(args[0])  # Добавляем в атрибут название созданного объекта (name)
        return object.__new__(cls)

    # ---- Конец изменений по модулю module_5_4.py
    def __init__(self, name='Пустырь', number_of_floor=0):
        self.name = name  # создаем атрибут объекта наименование объекта
        self.number_of_floor = number_of_floor  # создаем атрибут число этажей
        self.floor = (
            'этажей', 'этаж', *('этажа' for x in range(3)), *('этажей' for x in range(5)))  # спряжение слова этаж
        self.say_info()  # Инфо строка активации класса
        # ---- Начало изменений по модулю module_5_4.py ----------------------

        House.counter += 1  # Увеличиваем счетчик экземпляров класса.

        # ---- Конец изменений по модулю module_5_4.py

    # ---- Начало изменений по модулю module_5_2.py
    def __str__(self):  # Возвращает строку: "Название: <название>, кол-во этажей: <этажи>".
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floor}'

    def __len__(self):  # Возвращает кол-во этажей здания self.number_of_floors.
        return self.number_of_floor

    # ---- Конец изменений по модулю module_5_2.py --------------------------------------
    # ---- Начало изменений по модулю module_5_3.py

    def __eq__(self, other):  # ==
        if isinstance(other, House):
            return self.number_of_floor == other.number_of_floor
        else:
            raise ValidationError('Значения должны принадлежать классу House')

    def __lt__(self, other):  # <
        if isinstance(other, House):
            return self.number_of_floor < other.number_of_floor
        else:
            raise ValidationError('Значения должны принадлежать классу House')

    def __le__(self, other):  # <=
        if isinstance(other, House):
            return self.number_of_floor <= other.number_of_floor
        else:
            raise ValidationError('Значения должны принадлежать классу House')

    def __gt__(self, other):  # >
        if isinstance(other, House):
            return self.number_of_floor > other.number_of_floor
        else:
            raise ValidationError('Значения должны принадлежать классу House')

    def __ge__(self, other):  # >=
        if isinstance(other, House):
            return self.number_of_floor >= other.number_of_floor
        else:
            raise ValidationError('Значения должны принадлежать классу House')

    def __ne__(self, other):  # !=
        if isinstance(other, House):
            return self.number_of_floor != other.number_of_floor
        else:
            raise ValidationError('Значения должны принадлежать классу House')

    def __add__(self, other):
        if isinstance(other, int | House):
            if isinstance(other, int):
                self.number_of_floor += other
            else:
                self.number_of_floor += other.number_of_floor
            return self  # Для сохранения оригинального типа возвращаем оригинальный класс.
        else:
            raise ValidationError('Значение должно быть либо целым числом либо принадлежать классу House')

    def __iadd__(self, other):
        if isinstance(other, int | House):
            return self.__add__(other)  # Метод __iadd__не обязательно описывать заново, достаточно
            # вернуть значение вызова __add__.
        else:
            raise ValidationError('Значение должно быть либо целым числом либо принадлежать классу House')

    def __radd__(self, other):
        if isinstance(other, int | House):
            return self.__add__(other)  # Метод __radd__ не обязательно описывать заново,
            # достаточно вернуть значение вызова __add__.
        else:
            raise ValidationError('Значение должно быть либо целым числом либо принадлежать классу House')

    # ---- Конец изменений по модулю module_5_3.py -------------------------
    # ---- Начало изменений по модулю module_5_4.py ----------------------

    def __del__(self):  # Переопределяем метод удаления экземпляра
        print(f'{self.name} снесён, но он останется в истории.')
        House.counter -= 1  # Уменьшаем счетчик экземпляров класса.
        if House.counter == 0:  # Если равен нулю - конец обработки
            print('\n=== Конец обработки === ')

    # ---- Конец изменений по модулю module_5_4.py
    def say_floor(self):  # Обработка спряжения слова этаж в зависимости от количества этажей
        if self.number_of_floor != 0:  # Если этажей не ноль
            if 10 <= self.number_of_floor % 100 < 20:  # Если число в диапазоне от 10 до 19
                return f'{self.number_of_floor} этажей'
            else:  # Во всех других случаях - floor[последняя цифра]
                return f'{self.number_of_floor} {self.floor[self.number_of_floor % 10]}'
        else:
            return '0 этажей и он еще в стадии строительства'  # Если 0

    def say_info(self):  # Создает инфо строку активации класса.
        print(f'Добро пожаловать в {self.name}. Высота нашего комплекса {self.say_floor()}.')

    def go_to(self, new_floor=0):  # Эмулирует подъем на лифте
        if 0 < new_floor <= self.number_of_floor:  # Если разрешенное значение.
            for i in range(1, new_floor + 1):  # Эмуляция подъема.
                print(i)
        else:  # Если не разрешенное значение.
            print('Такого этажа не существует.')


# === Прогон ===
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

# print('\n=== Конец обработки === ')
