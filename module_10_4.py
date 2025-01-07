print("=== Очереди для обмена данными между потоками. ====\n")

# Задача "Потоки гостей в кафе.":
# Необходимо имитировать ситуацию с посещением гостями кафе.
# Создайте 3 класса: Table, Guest и Cafe.
# Класс Table:
# 1.Объекты этого класса должны создаваться следующим способом - Table(1)
# 2.Обладать атрибутами number - номер стола и guest - гость, который сидит за этим столом (по умолчанию None)
# Класс Guest:
# 1.Должен наследоваться от класса Thread (быть потоком).
# 2.Объекты этого класса должны создаваться следующим способом - Guest('Vasya').
# 3.Обладать атрибутом name - имя гостя.
# 4.Обладать методом run, где происходит ожидание случайным образом от 3 до 10 секунд.
# Класс Cafe:
# 1.Объекты этого класса должны создаваться следующим способом - Cafe(Table(1), Table(2),....)
# 2.Обладать атрибутами queue - очередь (объект класса Queue) и tables - столы в этом кафе (любая коллекция).
# 3.Обладать методами guest_arrival (прибытие гостей) и discuss_guests (обслужить гостей).
# Метод guest_arrival(self, *guests):
# 1.Должен принимать неограниченное кол-во гостей (объектов класса Guest).
# 2.Далее, если есть свободный стол, то сажать гостя за стол (назначать столу guest), запускать поток гостя и
# выводить на экран строку "<имя гостя> сел(-а) за стол номер <номер стола>".
# 3.Если же свободных столов для посадки не осталось, то помещать гостя в очередь queue и
# выводить сообщение "<имя гостя> в очереди".
# Метод discuss_guests(self):
# Этот метод имитирует процесс обслуживания гостей.
# 1.Обслуживание должно происходить пока очередь не пустая (метод empty) или хотя бы один стол занят.
# 2.Если за столом есть гость(поток) и гость(поток) закончил приём пищи(поток завершил работу - метод is_alive),
# то вывести строки "<имя гостя за текущим столом> покушал(-а) и ушёл(ушла)" и "Стол номер <номер стола> свободен".
# Так же текущий стол освобождается (table.guest = None).
# 3.Если очередь ещё не пуста (метод empty) и стол один из столов освободился (None), то текущему столу присваивается
# гость взятый из очереди (queue.get()). Далее выводится строка "<имя гостя из очереди> вышел(-ла) из очереди и сел(-а)
# за стол номер <номер стола>"
# 4.Далее запустить поток этого гостя (start)
# Таким образом мы получаем 3 класса на основе которых имитируется работа кафе:
# 1.Table - стол, хранит информацию о находящемся за ним гостем (Guest).
# 2.Guest - гость, поток, при запуске которого происходит задержка от 3 до 10 секунд.
# 3.Cafe - кафе, в котором есть определённое кол-во столов и происходит имитация прибытия гостей (guest_arrival) и
# их обслуживания (discuss_guests).
# **************************************************************************************************************
# Дополнение:
# - Введен контроль гостей (гостей < столов )
# - Введен контроль длинны очереди (гостей - столов > очереди).
# - Если список посетителей длинный, а очередь короткая (пробуем ставить __MAX_QUEUE = 4), то в конце выясняем - кто не поел.

import threading
import time
from queue import Queue
from random import randint


# === Классы ===
class FullQueue(Exception): # Исключение при заполненности очереди.
    pass


class Table: # Cтол, хранит информацию о находящемся за ним гостем (Guest).
    def __init__(self, number: int): # Инициализация экземпляра класса.
        self.number = number # Номер стола.
        self.guest = None # Ссылка на объект гостя.


class Guest(threading.Thread): # Гость, поток, при запуске которого происходит задержка от 3 до 10 секунд.
    def __init__(self, name): # Инициализация экземпляра класса.
        threading.Thread.__init__(self)
        self.name = name # Имя гостя.
        self.table = 0 # Номер стола за которым гость сидит.

    def run(self):
        time.sleep(randint(3, 10)) # Время нахождения гостя за столом.
        Cafe.print_line(f'{self.name} (Стол № {self.table})  покушал(-а) и ушёл(ушла).')


class Cafe:
    __MAX_QUEUE = 10 # Длинна очереди.
    @staticmethod
    def print_line(x): # Для вывода каждой строчки в консоли в отдельную строчку.
        cv.acquire()
        threading.Thread(target=print, args=(x,)).start()
        cv.release()

    def __init__(self, *tables: [Table]): # Инициализация экземпляра класса.
        self.tables = tables # Список объектов столов.
        self.queue = Queue(maxsize=self.__MAX_QUEUE) # Очередь для гостей.

    def guest_arrival(self, *guests:[Guest]): # Метод прибытия гостей.
        gen_guest = (guest for guest in guests) # Создаем генератор по списку гостей.
        i_queue = self.queue.qsize()# Счетчик очереди.
        #print('=== Очередь ===', i_queue)
        list_tables = [table for table in self.tables if table.guest is None] # Получаем список свободных столов.
        try:
            for table in list_tables: # Если есть свободный стол, то сажаем гостя за стол (назначать столу guest),
                    # запускаем поток гостя.
                guest = next(gen_guest) # Запускаем итерацию.
                table.guest = guest # Сажаем гостя за свободный стол.
                guest.table = table.number # Выдаем гостю номерок.
                list_guests.remove(guest) # Удаляем посетителей получивших место из списка желающих поесть.
                Cafe.print_line(f'{guest.name} сел(-а) за стол номер {table.number}.')
                guest.start() # Запускаем поток гостя.

            for guest in gen_guest: # Свободные столы закончились - заполняем очередь.
                if i_queue==self.__MAX_QUEUE: # Если очередь заполнилась - вызываем исключение.
                    raise FullQueue('=== Очередь заполнена. ===')
                self.queue.put(guest) # Заполняем очередь.
                list_guests.remove(guest) # Удаляем посетителей получивших место из списка желающих поесть.
                Cafe.print_line(f'{guest.name} в очереди.')
                i_queue += 1 # Увеличиваем счетчик очереди.
            Cafe.print_line('=== Всех распределили. ===')
            #print('=== Очередь ===', self.queue.qsize())

        except StopIteration as exc:
            Cafe.print_line('=== Гости закончились. ===')
        except FullQueue as exc:
            Cafe.print_line(exc)

    def discuss_guests(self): # Метод обслуживания гостей.
        i_count=1 # Счетчик занятых столов.
        while i_count>0 or not self.queue.empty(): # Обработка запускается если за столами сидят или очередь - не пуста.
            i_count=0 # Счетчик занятых столов.
            for table in self.tables :
                if not table.guest is None: # Если за столом сидят.
                    i_count+=1 # Увеличение счетчика занятых столов.
                    if not table.guest.is_alive(): # Если посетитель ушел.
                        Cafe.print_line(f'Стол номер {table.number} свободен.')
                        if not self.queue.empty(): # Если очередь не пуста.
                            table.guest = self.queue.get() # Садим за стол первого в очереди (FIFO)
                            table.guest.start() # Запускаем поток.
                            table.guest.table=table.number # Даем номерок.
                            Cafe.print_line(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}.')
                            if self.queue.empty():
                                Cafe.print_line('=== Очередь пуста. ===')
                        else:
                            table.guest = None



# === Прогон ===
cv = threading.Condition()
# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
list_guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*list_guests)
# Обслуживание гостей
cafe.discuss_guests()
print('\n=== Ресторан закрыт. ===')
print('\nКто хотел поесть:', guests_names)
print('Кто не поел:',list([x.name for x in list_guests]))
print('\n=== Конец обработки. === ')
