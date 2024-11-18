print("=== Атрибуты и методы объекта. ====\n")


# Задача "Магические здания":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче.
# Необходимо дополнить класс House следующими специальными методами:
# 1.__len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
# 2.__str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".
# === Классы ===
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
# __str__
print(h1)
print(h2)
# __len__
print(len(h1))
print(len(h2))
print('\n=== Конец обработки === ')
