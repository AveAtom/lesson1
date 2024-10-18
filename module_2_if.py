print("=== Условная конструкция. Операторы if, elif, else.====")
# Задача "Все ли равны?":
#
# На вход программе подаются 3 целых числа и записываются в переменные first, second и third соответственно.
#
# Ваша задача написать условную конструкцию (из if, elif, else), которая выводит кол-во одинаковых чисел среди 3-х введённых.
# Пункты задачи:
#
# Если все числа равны между собой, то вывести 3
# Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
# Если равных чисел среди 3-х вообще нет, то вывести 0
# Используем конструкцию try:except:, чтобы отследить неправильный ввод (не любим красное в глаза).
err = 0
try:
    first, second, third = input("Введите через запятую три числа - ").split(',')  # Вводим три числа через запятую
    first = int(first)  # Проверяем, что введено целое число
    second = int(second)  # Проверяем, что введено целое число
    third = int(third)  # Проверяем, что введено целое число
except (ValueError) as er:
    print(er)
    err = 1
if err == 0:
    print("First - {0}, Second - {1}, Third - {2}".format(first, second, third))  # Показываем введенные числа
    # Варианты ответов: 0,2,3
    # Вариант без if
    res1 = int(first == second) * int(first == third) * 3 + int(first == second) * int(first != third) * 2 + \
           int(first == third) * int(first != second) * 2 + int(second == third) * int(second != first) * 2

    # Вариант с if
    res2 = 0
    if first == second and second == third:
        res2 = 3  # Самый редкий вариант (все равны)
    elif (first == second and first != third) or (first == third and first != second) or \
            (second == third and second != first):
        res2 = 2  # Рассматриваем все варианты, когда есть два одинаковых числа

    print("Количество одинаковых чисел (без if) - {}".format(res2))  # Показываем результат

    print("Количество одинаковых чисел (с if) - {}".format(res2))  # Показываем результат
else:
    print("Неправильный ввод данных!")  # в случае неправильного ввода.
