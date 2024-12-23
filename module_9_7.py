print("=== Декораторы. ====\n")


# Задание:
# Напишите 2 функции:
# 1.Функция, которая складывает 3 числа (sum_three)
# 2.Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и
# "Составное" в противном случае.
#
# Примечания:
# Не забудьте написать внутреннюю функцию wrapper в is_prime
# Функция is_prime должна возвращать wrapper
# @is_prime - декоратор для функции sum_three
# ***************************************************************************************************
# === Классы ===
class IsIntException(Exception):
    pass
# === Функции ===
def is_prime(func): # Декоратор на целевую функцию sum_three().
    def wrapper(*args): # Замыкатель внутри декоратора.
        try: # Проверяем тип входящих значений.
            res = func(*args) # Получаем результат функции.
        except IsIntException as exc:
            print(exc)
            return ''
        # Цикл перебирает возможные делители числа от двойки до половины проверяемого числа, ибо проверять числа дальше
        # просто нет смысла, так как любое число нацело делится максимум на половину себя.
        print("Составное") if [i for i in range(2, (res//2)+1) if res%i ==0] else print("Простое") # Определяем -  простой
        # ли результат или составной.
        return res # Возвращаем результат работы целевой функции.

    return wrapper # Возвращаем замыкатель.

@is_prime # Объявление декоратора.
def sum_three(a:int=0,b:int=0,c:int=0) ->int: # Функция суммы трех целых чисел.
    if len([x for x in (a,b,c) if isinstance(x,int)])!=3:
        raise IsIntException("Числа должны быть целыми.")
    return a+b+c
# === Прогон ===
result = sum_three(2, 3, 6)
print(result)

print('\n=== Конец обработки === ')
