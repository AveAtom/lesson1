print("=== Перегрузка операторов. ====\n")
# Задача "Нужно больше этажей":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Специальные методы класса".
# Необходимо дополнить класс House следующими специальными методами:
# 1.__eq__(self, other) - должен возвращать True, если количество этажей одинаковое у self и у other.
# 2.Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=) должны присутствовать в классе и возвращать
# результаты сравнения по соответствующим операторам. Как и в методе __eq__ в сравнении участвует кол-во этажей.
# 3.__add__(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
# 4.__radd__(self, value), __iadd__(self, value) - работают так же как и __add__ (возвращают результат его вызова).
# Остальные методы арифметических операторов, где self - x, other - y:
# Следует заметить, что other может быть не только числом, но и вообще любым объектом другого класса.
# Для более точной логики работы методов __eq__, __add__  и других методов сравнения и арифметики перед выполняемыми
# действиями лучше убедиться в принадлежности к типу при помощи функции isinstance:
# isinstance(other, int) - other указывает на объект типа int.
# isinstance(other, House) - other указывает на объект типа House.
# Примечания:
# 1.Методы __iadd__ и __radd__ не обязательно описывать заново, достаточно вернуть значение вызова __add__.
# 2.Более подробно о работе всех перечисленных методов можно прочитать здесь и здесь.
# === Классы ===
class ValidationError(Exception): # Для перехвата ошибок конструкцией try - except переопределяем класс ValidationError
    pass
class House:
    def __init__(self, name='Пустырь', number_of_floor=0):
        self.name = name  # создаем атрибут объекта наименование объекта
        self.number_of_floor = number_of_floor  # создаем атрибут число этажей
        self.floor = (
            'этажей', 'этаж', *('этажа' for x in range(3)), *('этажей' for x in range(5)))  # спряжение слова этаж
        self.say_info()  # Инфо строка активации класса

    def __str__(self):  # Возвращает строку: "Название: <название>, кол-во этажей: <этажи>".
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floor}'

    def __len__(self):  # Возвращает кол-во этажей здания self.number_of_floors.
        return self.number_of_floor

    # ----Дополнение к текущей задаче

    def __eq__(self, other): # ==
        if isinstance(other,House):
            return self.number_of_floor == other.number_of_floor
        else:
            raise ValidationError('Значения должны принадлежать классу House')

    def __lt__(self, other): # <
        if isinstance(other,House):
            return self.number_of_floor < other.number_of_floor
        else:
            raise ValidationError('Значения должны принадлежать классу House')

    def __le__(self, other): # <=
        if isinstance(other,House):
            return self.number_of_floor <= other.number_of_floor
        else:
            raise ValidationError('Значения должны принадлежать классу House')

    def __gt__(self, other): # >
        if isinstance(other,House):
            return self.number_of_floor > other.number_of_floor
        else:
            raise ValidationError('Значения должны принадлежать классу House')

    def __ge__(self, other): # >=
        if isinstance(other,House):
            return self.number_of_floor >= other.number_of_floor
        else:
            raise ValidationError('Значения должны принадлежать классу House')

    def __ne__(self, other): # !=
        if isinstance(other,House):
            return self.number_of_floor != other.number_of_floor
        else:
            raise ValidationError('Значения должны принадлежать классу House')

    def __add__(self, other):
        if isinstance(other,int):
            self.number_of_floor += other
            return self # Для сохранения оригинального типа возвращаем оригинальный класс.
        else:
            raise ValidationError('Значение должно быть целым числом')

    def __iadd__(self, other):
        if isinstance(other,int):
            self.number_of_floor += other
            return self # Для сохранения оригинального типа возвращаем оригинальный класс.
        else:
            raise ValidationError('Значение должно быть целым числом')

    def __radd__(self, other):
        if isinstance(other,int|House):
            if isinstance(other,int):
                self.number_of_floor+=other
            else:
                self.number_of_floor+=other.number_of_floor
            return self # Для сохранения оригинального типа возвращаем оригинальный класс.
        else:
            raise ValidationError('Значение должно быть либо целым числом либо принадлежать классу House')

    # -------------------------------------------------------------------------------------------------
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
h2 = House('ЖК Акация', 20)
print(h1)
print(h2)
try:
    print(h1 == h2)  # __eq__
    h1 = h1 + 10  # __add__
    print(h1)
    print(h1 == h2)
    h1 += 10  # __iadd__
    print(h1)
    h2 = 10 + h2  # __radd__
    print(h2)
    print(h1 > h2)  # __gt__
    print(h1 >= h2)  # __ge__
    print(h1 < h2)  # __lt__
    print(h1 <= h2)  # __le__
    print(h1 != h2)  # __ne__
except ValidationError as e:
    print(e)
