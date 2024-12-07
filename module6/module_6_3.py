from random import randint

print("=== Доступ к свойствам родителя. Переопределение свойств. ====\n")


# Задача "Ошибка эволюции.":
# Замечали, что некоторые животные в нашем мире обладают странными и, порой, несовместимыми друг с другом свойствами?
# Например, утконос... Вроде есть клюв, но не птица. Вроде милый, а есть шипы на задних лапах. А ещё он откладывает
# яйца... Опустим факт о том, что они потеют молоком и попробуем не эволюционным способом создать нашего утконоса.
# Необходимо написать 5 классов:
# Animal - класс описывающий животных.
# Класс обладает следующими атрибутами:
# 1.live = True
# 2.sound = None - звук (изначально отсутствует)
# 3._DEGREE_OF_DANGER = 0 - степень опасности существа
# Объект этого класса обладает следующими атрибутами:
# 1._cords = [0, 0, 0] - координаты в пространстве.
# 2.speed = ... - скорость передвижения существа (определяется при создании объекта)
# И методами:
# 1.move(self, dx, dy, dz), который должен менять соответствующие координаты в _cords на dx, dy и dz в том же порядке,
# где множителем будет является speed. Если при попытке изменения координаты z в _cords значение будет меньше 0,
# то выводить сообщение "It's too deep, i can't dive :(" , при этом изменения не вносятся.
# 2.get_cords(self), который выводит координаты в формате: "X: <координаты по x>, Y: <координаты по y>, Z: <координаты по z>"
# 3.attack(self), который выводит "Sorry, i'm peaceful :)", если степень опасности меньше 5 и
# "Be careful, i'm attacking you 0_0" , если равно или больше.
# 4.speak(self), который выводит строку со звуком sound.
# Bird - класс описывающий птиц. Наследуется от Animal.
# Должен обладать атрибутом:
# 1.beak = True - наличие клюва
# И методом:
# 1.lay_eggs(self), который выводит строку "Here are(is) <случайное число от 1 до 4> eggs for you"
# AquaticAnimal - класс описывающий плавающего животного. Наследуется от Animal.
# В этом классе атрибут _DEGREE_OF_DANGER = 3.
# Должен обладать методом:
# 1.dive_in(self, dz) - где dz изменение координаты z в _cords. Этот метод должен всегда уменьшать
# координату z в _coords. Чтобы сделать dz положительным, берите его значение по модулю (функция abs).
# Скорость движения при нырянии должна уменьшаться в 2 раза, в отличии от обычного движения. (speed / 2)
# PoisonousAnimal - класс описывающий ядовитых животных. Наследуется от Animal.
# В этом классе атрибут _DEGREE_OF_DANGER = 8.
# Duckbill - класс описывающий утконоса. Наследуется от классов Bird, AquaticAnimal, PoisonousAnimal.
# Порядок наследования определите сами, опираясь на ниже приведённые примеры выполнения кода.
# Объект этого класса должен обладать одним дополнительным атрибутом:
# 1.sound = "Click-click-click" - звук, который издаёт утконос
# Примечания:
# 1.Будьте внимательней, когда вызываете методы классов родителей в классе наследнике при множественном наследовании:
# при обращении через super() методы будут искаться сначала в первом, потом во втором и т.д. классах по mro().
# 2.При определении порядка наследования обратите внимание на то, что утконос атакует "Be careful, i'm attacking you 0_0"
# ******************************************************************************************************
# Дополнение
# - dx,dy,dz - delta перемещения.
# - когда перемещение происходит через move - сухопутные.
# - когда перемещение происходит через dive_in - могут нырять.
# === Классы ===
class Animal:  # Класс описывающий животных.
    live = True  # Живой (Да/нет).
    sound = None  # Звук (изначально отсутствует).
    descr = ""  # Краткое описание
    _DEGREE_OF_DANGER = 0  # Степень опасности существа.
    dangers_cls = {}  # собираем значения _DEGREE_OF_DANGER со всех классов, которые наследуют данный класс

    def __init_subclass__(cls, **kwargs):  # для определения списка _DEGREE_OF_DANGER из каждого класса собираем
        # значения данного атрибута в словарь danger_cls в формате cls.__name__:cls._DEGREE_OF_DANGER.
        super().__init_subclass__(**kwargs)
        Animal.dangers_cls.update({cls.__name__: cls._DEGREE_OF_DANGER})

    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed
        self.danger = []

    def move(self, dx=0, dy=0, dz=0, dive=False):  # Меняет соответствующие координаты в _cords на dx, dy и dz
        # в том же порядке, где множителем будет является speed.
        # print(self._cords[2])
        if self._cords[2] + dz * (self.speed / 2) < 0 and not dive:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] += int(dz * (self.speed / 2 if dive else self.speed))

    def get_cords(self):  # Выводит координаты в формате.
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self):  # выводит "Sorry, i'm peaceful :)", если степень опасности меньше 5 и
        # "Be careful, i'm attacking you 0_0" , если равно или больше.
        # print(self.danger)
        max_danger = max(self.danger)  # Берем макс значения из списка Animal.danger
        if max_danger > 4:
            print(f"{self.descr}-атакует: Be careful, i'm attacking you 0_0")
        else:
            print(f"{self.descr}-атакует: Sorry, i'm peaceful :)")

    def speak(self):  # Выводит строку со звуком sound.
        print(f'Звук существа {self.descr} - {self.sound}')


class Bird(Animal):  # Класс описывающий птиц. Наследуется от Animal.

    beak = True

    def lay_eggs(self):  # Выводит строку "Here are(is) <случайное число от 1 до 4> eggs for you"
        print(f"Here are(is) {randint(3, 20)} eggs for you")


class AquaticAnimal(Animal):  # Класс описывающий плавающего животного. Наследуется от Animal.

    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):  # Этот метод должен всегда уменьшать координату z в _coords.
        # Скорость движения при нырянии должна уменьшаться в 2 раза.
        self.move(0, 0, (-1) * dz, True)
        # self.get_cords()


class PoisonousAnimal(Animal):  # Класс описывающий ядовитых животных. Наследуется от Animal.
    _DEGREE_OF_DANGER = 8


class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):  # Класс описывающий утконоса. Наследуется от классов
    # Bird, AquaticAnimal, PoisonousAnimal.
    dangers = []  # Список названий подчиненных классов.

    def __new__(cls, *args, **kwargs):
        cls.dangers = [x.__name__ for x in cls.mro()]  # Собираем в список dangers наименования всех классов с которыми
        # связан данный класс.
        return object.__new__(cls)

    def __init__(self, speed):
        super().__init__(speed)
        self.speed = speed
        self.danger = [self.dangers_cls[x] for x in self.dangers if x in self.dangers_cls]  # Собираем список опасностей
        # из подчиненных классов.
        self.sound = 'Click-click-click'
        self.descr = 'Утконос'


class AquaBird(Bird, AquaticAnimal):  # Для теста собираем водоплавающую птицу (утку)
    dangers = []  # Список названий подчиненных классов.

    def __new__(cls, *args, **kwargs):
        cls.dangers = [x.__name__ for x in cls.mro()]  # Собираем в список dangers наименования всех классов с которыми
        # связан данный класс.
        return object.__new__(cls)

    def __init__(self, speed):
        super().__init__(speed)
        self.speed = speed
        self.danger = [self.dangers_cls[x] for x in self.dangers if x in self.dangers_cls]  # Собираем список опасностей
        # из подчиненных классов.
        self.sound = 'Kryak-Kryak-Kryak'
        self.descr = 'Утка'


# === Прогон ===
db = Duckbill(10)  # утконос
duck = AquaBird(100)  # утка
print(Duckbill.mro())  # Наследование утконоса
print(AquaBird.mro())  # Наследование утки
print(db.__dict__)  # Атрибуты утконоса
print(duck.__dict__)  # Атрибуты утконоса
print('=== Прогон ===')
print(db.live)
print(db.beak)
db.speak()
duck.speak()
db.attack()  # Тест атаки для утконоса
duck.attack()  # Тест атаки для утки
print(f'=== Прогон {db.descr} ===')
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
print('Нырнула не как рыба')
db.move(0, 0, -10)  # нырнула не как рыба
db.get_cords()
print('Нырнула как рыба')
db.dive_in(6)  # нырнула как рыба
db.get_cords()
db.lay_eggs()

print('\n=== Конец обработки === ')
