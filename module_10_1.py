print("=== Создание потоков. ====\n")

# Задача "Потоковая запись в файлы":
# Необходимо создать функцию wite_words(word_count, file_name), где word_count - количество записываемых слов,
# file_name - название файла, куда будут записываться слова.
# Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий файл
# с прерыванием после записи каждого на 0.1 секунду.
# Сделать паузу можно при помощи функции sleep из модуля time, предварительно импортировав её: from time import sleep.
# В конце работы функции вывести строку "Завершилась запись в файл <название файла>".
#
# После создания файла вызовите 4 раза функцию wite_words, передав в неё следующие значения:
# 1.10, example1.txt
# 2.30, example2.txt
# 3.200, example3.txt
# 4.100, example4.txt
# После вызовов функций создайте 4 потока для вызова этой функции со следующими аргументами для функции:
# 1.10, example5.txt
# 2.30, example6.txt
# 3.200, example7.txt
# 4.100, example8.txt
# Запустите эти потоки методом start не забыв, сделать остановку основного потока при помощи join.
# Также измерьте время затраченное на выполнение функций и потоков. Как это сделать рассказано в лекции к домашнему заданию.
# Примечания:
# 1.Не переживайте, если программа выполняется долго, учитывая кол-во слов, максимальное время выполнения
# в потоках не должно превышать ~20 секунд, а в функциях ~34 секунды.
# 2.Cледует заметить, что запись в example8.txt завершилась раньше, чем в example7.txt,
# т.к. потоки работали почти одновременно.
# *************************************************************************************
# Дополнение: перевел потоки в состояние демона, чтобы показать, что главный поток действительно на паузе.
from time import sleep
from datetime import datetime
import threading

# === Начальные данные ===
data = (10, 30, 200, 100)


# === Функции ===
# Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий файл
# с прерыванием после записи каждого на 0.1 секунду.
def write_words(word_count: int, file_name: str):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i + 1}\n')
            sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')


# === Прогон ===
start = datetime.now()
threads = []  # Список потоков.
for i in range(4):
    write_words(data[i], f'example{i + 1}.txt')
    threads.append(threading.Thread(target=write_words, args=(data[i], f'example{i + 5}.txt',),
                                    daemon=True))  # Формируем список потоков.
end = datetime.now()
print(f'Работа потоков {end - start}')  # Время работы основного потока.
start = datetime.now()
for thread in threads:  # Запускаем потоки.
    thread.start()
print(threading.enumerate())
print(threading.current_thread())
for thread in threads:  # Блокируем работу основного потока до завершения выполнения всех дополнительных потоков.
    thread.join()
end = datetime.now()
print(f'Работа потоков {end - start}')  # Время работы через потоки.
print(threading.enumerate()) # Проверка состояния потоков.
print('\n=== Конец обработки === ')
