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
def check_list(int_list: list, func_name: str):
    def correct_elem(number):  # Проверка значения на принадлежность к типу int|float.
        global err_count  # Наводимся на глобальную переменную.
        nonlocal func_name  # Наводимся на переменную функции check_list
        try:
            if not isinstance(number, int | float):
                raise IncorrectListElementType(f'Неправильный тип элемента списка для функции {func_name} ', element)
            else:
                return number  # Штатный возврат.
        except IncorrectListElementType as exc:
            print(
                f'{"\n" if err_count == 0 else ""}{exc.message} - {exc.value}')  # Если это первая ошибка ставим перед ней \n
            err_count += 1  # Увеличиваем счетчик ошибок.
            return 'err'  # Если ошибка - возвращаем err.

    res = []  # Определяем список возврата.

    for element in int_list:
        if correct_elem(element) != 'err':  # Если элемент не ошибочный - добавляем его в результирующий список.
            res.append(element)
    return res


def apply_all_func(int_list, *functions):  # Функция высшего порядка. Функция высшего порядка-это та функция,
    # которая в качестве аргументов может принимать другие функции.
    #print(int_list)
    global err_count  # Ориентируем глобальную переменную
    err_count = 0  # Обнуляем значение.
    return {func.__name__: func(check_list(int_list, func.__name__)) for func in functions}  # Переменная result
                                                                                        # в данной конструкции не нужна.


# === Прогон ===
err_count = 0  # Определяем переменную.
print(apply_all_func([6, 20,'r', 15, 9], max, min), end='')

print(apply_all_func([6, 20,15, 9], len, sum, sorted), end='')

print('\n\n=== Конец обработки === ')
