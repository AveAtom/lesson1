from inspect import currentframe

print("=== Введение в функциональное программирование. ====\n")


# Задача "Вызов разом.":
# Напишите функцию apply_all_func(int_list, *functions), которая принимает параметры:
# 1.int_list - список из чисел (int, float)
# 2.*functions - неограниченное кол-во функций (которые применимы к спискам, состоящим из чисел)
# Эта функция должна:
# 1.Вызвать каждую функцию к переданному списку int_list
# 2.Возвращать словарь, где ключом будет название вызванной функции, а значением - её результат работы со списком int_list.
# Пункты задачи:
# 1.В функции apply_all_func создайте пустой словарь results.
# 2.Переберите все функции из *functions.
# 3.При переборе функций записывайте в словарь results результат работы этой функции под ключом её названия.
# 4.Верните словарь results.
# 5.Запустите функцию apply_all_func, передав в неё список из чисел и набор других функций.
# Пример результата выполнения программы:
# В примере используются следующие функции:
# 1.min - принимает список, возвращает минимальное значение из него.
# 2.max - принимает список, возвращает максимальное значение из него.
# 3.len - принимает список, возвращает кол-во элементов в нём.
# 4.sum - принимает список, возвращает сумму его элементов.
# 5.sorted - принимает список, возвращает новый отсортированный список на основе переданного.
# Примечания:
# 1.Для того, чтобы взять название функции можно обратиться к атрибуту __name__
# 2.При попытке передачи, например, списка из строк, некоторые функции могут работать некорректно или вовсе не работать.
# Используйте списки чисел.
# ************************************************************************************************************
# Дополнение:
# - Поскольку в ТЗ словари должны идти друг за другом - вводим счетчик ошибок, который нужен для того что бы перед
#   первой строкой ошибки ставился ВК.
# - В ошибку вводим наименование функции к которой она принадлежит.
# - Ошибка не прерывает работу обработки ( ошибочные данные отбрасываются из списка).
# === Классы ===
class IncorrectListElementType(Exception):  # Обработчик ошибки типа.
    def __init__(self, message, value):
        self.message = message
        self.value = value


# === Функции ===

def apply_all_func(int_list, *functions):  # Функция высшего порядка. Функция высшего порядка-это та функция,
    # которая в качестве аргументов может принимать другие функции.
    err_count = 0  # Обнуляем значение.

    def check_list(element):
        nonlocal int_list, err_count
        try:
            if not isinstance(element, int | float):
                if element[0] != '#':  # Отсекаем имена функций, которые находятся в хвосте списка.
                    raise IncorrectListElementType(f'Неправильный тип элемента списка для функции {int_list[-1][1:]} ',
                                                   element)
                else:
                    return False
            else:
                return True
        except IncorrectListElementType as exc:
            print(
                f'{"\n" if err_count == 0 else ""}{exc.message} - {exc.value}')  # Если это первая ошибка ставим перед ней \n
            err_count += 1  # Увеличиваем счетчик ошибок.
            return False

    return {func.__name__: func(list(filter(check_list, int_list := int_list + ['#' + func.__name__]))) for func in
            functions}
    # Переменная result в данной конструкции не нужна. Передаем в функцию check_list имя функции через список.
    # Использовал конструкцию list(filter()) так как на выходе фильтра не список, а класс filter.(len - не работает)


# === Прогон ===

print(apply_all_func([6, 20, 'r', 15, 9], max, min), end='')

print(apply_all_func([6, 20, 15, 9], len, sum, sorted), end='')

print('\n\n=== Конец обработки === ')
