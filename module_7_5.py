# Используем from для оптимизации кода.
from os.path import join, dirname, getsize, getmtime
from os import walk
from time import localtime, strftime

print("=== Файлы в операционной системе. ====")

# Цель задания:
# Освоить работу с файловой системой в Python, используя модуль os.
# Научиться применять методы os.walk, os.path.join, os.path.getmtime, os.path.dirname, os.path.getsize и использование
# модуля time для корректного отображения времени.
# Задание:
# Создайте новый проект или продолжите работу в текущем проекте.
# 1.Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
# 2.Примените os.path.join для формирования полного пути к файлам.
# 3.Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
# 4.Используйте os.path.getsize для получения размера файла.
# 5.Используйте os.path.dirname для получения родительской директории файла.
# Комментарии к заданию:
# Ключевая идея – использование вложенного for
# for root, dirs, files in os.walk(directory):
#   for file in files:
#     filepath = ?
#     filetime = ?
#     formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
#     filesize = ?
#     parent_dir = ?
#     print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time},
#     Родительская директория: {parent_dir}')
# Так как в разных операционных системах разная схема расположения папок, тестировать
# проще всего в папке проекта (directory = “.”)
# Пример возможного вывода:
# Обнаружен файл: main.py, Путь: ./main.py, Размер: 111 байт, Время изменения: 11.11.1111 11:11, Родительская директория.
# ********************************************************************************************************************8
# directory = getcwd()
directory = '.'  # Точка осмотра.
for root, dirs, files in walk(directory):

    for dir in dirs:  # Отображаем директории.
        print(f'Обнаружена директория: {dir}')

    for file in files:  # Отображаем файлы.
        filepath = join(root, file)  # Полный путь к файлу.
        filetime = getmtime(file)  # Время изменения файла.
        formatted_time = strftime("%d.%m.%Y %H:%M",
                                  localtime(filetime))  # Отформатированное значение времени изменения файла.
        filesize = getsize(file)  # Рвзмер файла.
        parent_dir = dirname(filepath)  # Директория расположения файла.
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time},'
              f' Родительская директория: {parent_dir}')

    break  # нужно для оптимизации процесса (иначе начинают вылезать служебные/скрытые объекты)

print('\n=== Конец обработки === ')
