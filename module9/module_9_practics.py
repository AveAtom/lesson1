# 1 - написать функцию, которая возвращает функцию повторения двух первых символов n раз.
# 2 - создать массив функций и применить все функции поочередно к аргументу.
# 3 - применить все функции поочередно к массиву аргументов.

animal = 'мишка'
animals = ['зайка', 'мишка', 'бегемотик', 'самолетик']

# 1

def dec_for_3(func):  # Декоратор для реализации п. 3
    def wrapper(*args, **kwargs):
        if repetitions:  # Если repetitions не None (выполняется п.2) - заполняем список result_3 по п. 3
            result_3.extend([func(x) for x in
                             animals])  # Отправляем массив animals в текущую функцию и результат добавляем в список result_3.
        return func(*args, **kwargs)  # Отправляем штатный ответ.

    return wrapper


def gen_repeat(n):
    @dec_for_3  # Определяем декоратор
    def repeat(animal):
        return (animal[:2] + '-') * n + animal

    return repeat


repetitions = None # Определяем для штатной работы декоратора.
result_3 = [] # Результирующий список по п.3
test_1 = gen_repeat(1)
test_2 = gen_repeat(2)

print(test_1(animal))
print(test_2(animal))
print(f'#1 result_3 = {result_3}')  # Список по п.3 не сформирован.

# 2 + 3
repetitions = [gen_repeat(n) for n in range(1, 4)]
print(repetitions)

result = [func(animal) for func in repetitions]
print(result)
print(f'#2 result_3 = {result_3}')  # Список по п.3 сформирован.
