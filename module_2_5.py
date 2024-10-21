print("=== Функции в Python.Функция с параметром.====")


# Задача "Матрица воплоти":
# Напишите функцию get_matrix с тремя параметрами n, m и value, которая будет создавать матрицу(вложенный список)
# размерами n строк и m столбцов, заполненную значениями value и возвращать эту матрицу в качестве результата работы.
# Пункты задачи:
# 1.Объявите функцию get_matrix и напишите в ней параметры n, m и value.
# 2.Создайте пустой список matrix внутри функции get_matrix.
# 3.Напишите первый(внешний) цикл for для кол-ва строк матрицы, n повторов.
# 4.В первом цикле добавляйте пустой список в список matrix.
# 5.Напишите второй(внутренний) цикл for для кол-ва столбцов матрицы, m повторов.
# 6.Во втором цикле пополняйте ранее добавленный пустой список значениями value.
# 7.После всех циклов верните значение переменной matrix.
# 8.Выведите на экран(консоль) результат работы функции get_matrix.
# Примечания:
# 1.Вложенный список - это строка матрицы, элементы вложенных списков(глубже) - это столбцы матрицы.
# 2.В случае передачи аргумента со значением 0 или меньше, будет возвращаться пустой список.
# ********************************************************************************************
# Дополнение: добавлю обработку функции при вызове без параметров.
# При вызове функции без параметров - отдается пустой список.

def get_matrix(n=0, m=0, value=0):  # Определение возвращаемой функции get_matrix
    matrix = []  # Определение локальной переменной matrix
    for i in range(n):  # Формируем внешний цикл 1-n (index: 0-(n-1))
        matrix.append(list(value for j in range(m)))  # Формируем внутренний цикл и результат
        # (список из m элементов value) добавляем в matrix
    return matrix  # Возвращаем matrix


# Результат работы функции get_matrix
result1 = get_matrix(2, 2, 10)  # Обращение к функции get_matrix с параметрами
result2 = get_matrix(3, 5, 42)  # Обращение к функции get_matrix с параметрами
result3 = get_matrix(4, 2, 13)  # Обращение к функции get_matrix с параметрами
result4 = get_matrix()  # Обращение к функции get_matrix без параметров
# Вывод результата работы функции get_matrix
print(f'result1 - {result1}')
print(f'result2 - {result2}')
print(f'result3 - {result3}')
print(f'result4 - {result4}')
