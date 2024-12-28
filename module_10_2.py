print("=== Потоки на классах. ====\n")

# Задача "За честь и отвагу!":
# Создайте класс Knight, наследованный от Thread, объекты которого будут обладать следующими свойствами:
# 1.Атрибут name - имя рыцаря. (str)
# 2.Атрибут power - сила рыцаря. (int)
# А также метод run, в котором рыцарь будет сражаться с врагами:
# 1.При запуске потока должна выводится надпись "<Имя рыцаря>, на нас напали!".
# 2.Рыцарь сражается до тех пор, пока не повергнет всех врагов (у всех потоков их 100).
# 3.В процессе сражения количество врагов уменьшается на power текущего рыцаря.
# 4.По прошествию 1 дня сражения (1 секунды) выводится строка "<Имя рыцаря> сражается <кол-во дней>...,
# осталось <кол-во воинов> воинов."
# 5.После победы над всеми врагами выводится надпись "<Имя рыцаря> одержал победу спустя <кол-во дней> дней(дня)!"
# Как можно заметить нужно сделать задержку в 1 секунду, инструменты для задержки выберите сами.
# Пункты задачи:
# 1.Создайте класс Knight с соответствующими описанию свойствами.
# 2.Создайте и запустите 2 потока на основе класса Knight.
# 3.Выведите на экран строку об окончании битв.
# **********************************************************************************************************
import threading
import time


# === Классы ===
class Knight(threading.Thread):
    __NUMBER_OF_ENEMIES = 100  # Число врагов.

    @staticmethod
    def print_line(x):
        threading.Thread(target=print, args=(x,)).start()

    def __init__(self, name: str, power: int):
        threading.Thread.__init__(self)
        self.name = name  # Имя рыцаря
        self.power = power  # Сила рыцаря

    def battle(self, name, power, enemies):  # Описываем битву.
        day_of_battle=0 # Определяем счетчик дней битвы.
        while enemies:  # Когда враги еще есть - битва продолжается.
            time.sleep(1)  # Обсчет битвы только через секунду.
            day_of_battle += 1  # Прошел еще один день битвы.
            enemies -= power  # Уменьшаем кол-во врагов на силу рыцаря.
            if enemies < 0:  # Если кол-во врагов в отрицательную величину - враги кончились
                enemies = 0
            # Статистика очередного дня битвы.
            self.print_line(f'{name}, сражается {day_of_battle} день(дня)... осталось {enemies} воинов')
        return day_of_battle

    def run(self):
        self.print_line(f'{self.name} на нас напали!')
        day_of_battle = self.battle(self.name, self.power, self.__NUMBER_OF_ENEMIES)
        self.print_line(f'{self.name} одержал победу спустя {day_of_battle} дней(дня)!')


# === Прогон ===
# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

# Вывод строки об окончании сражения
print('\n=== Сражение закончилось. === ')
