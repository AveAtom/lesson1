print("=== Организация программ и методы строк ===")
#Написать программу на языке Python с использованием Pycharm для работы с методами строк и организации программ.
my_string = input(" Введите мою строку: ") # Создайте переменную my_string и присвойте ей значение строки с произвольным
                                            # текстом (функция input()).
print(" Количество символов (пробелы учитываются) в моей строке:",len(my_string)) #Вывести количество символов
                                                                                    # введённого текста
#3. Работа с методами строк: Используя методы строк, выполните следующие действия:
print(" Моя строка в верхнем регистре:", my_string.upper()) # Выведите строку my_string в верхнем регистре.
print(" Моя строка в нижнем регистре:", my_string.lower()) # Выведите строку my_string в нижнем регистре.
print(" Моя строка в нижнем регистре:", my_string.replace(' ','') )# Измените строку my_string,
                                                                                    # удалив все пробелы
print(" Первый символ моей строки:", my_string[0]) #Выведите первый символ строки my_string.
print(" Последний символ моей строки:", my_string[-1]) #Выведите последний символ строки my_string.