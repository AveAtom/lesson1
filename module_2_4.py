print("=== Цикл for. Элементы списка. Полезные функции в цикле.====")
# Задача "Всё не так уж просто":
# Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Используя этот список составьте второй список primes содержащий только простые числа.
# А так же третий список not_primes, содержащий все не простые числа.
# Выведите списки primes и not_primes на экран(в консоль).
# Пункты задачи:
# 1. Создайте пустые списки primes и not_primes.
# 2. При помощи цикла for переберите список numbers.
# 3. Напишите ещё один цикл for (вложенный), где будут подбираться делители для числа из 1ого цикла.
# 4. Отметить простоту числа можно переменной is_prime, записав в неё значение True перед проверкой.
# 5. В процессе проверки на простоту записывайте числа из списка numbers в списки primes и not_primes
# в зависимости от значения переменной is_prime после проверки (True - в prime, False - в not_prime).
# 6. Выведите списки primes и not_primes на экран(в консоль).
# Примечания:
# Учтите, что число 1 не является ни простым, ни составным числом, поэтому оно отсутствует в конечных списках.
# Для проверки на простоту числа вам нужно убедиться, что выбранное число не делиться ни на что в диапазоне
# от 2 до этого числа(не включительно).
# Попробуйте оптимизировать(ускорить) процесс выяснения простоты числа при помощи оператора break,
# когда найдёте делитель. (Не обязательно)
# Переменные меняющее своё булево состояние на противоположное в процессе проверки, как is_prime, в кругах
# разработчиков называются переменными-флагами(flag).

numbers = [x for x in range(1, 16)]  # Заполнение numbers [1..15].
print(f'numbers = {numbers}')  # Вывод списка numbers.
primes = []  # Определение primes.
not_primes = []  # Определение not_primes.
for i in numbers:  # Перебираем список numbers.
    if i != 1:  # Исключаем из обработки 1.
        is_prime = True  # Переключаем флаг в состояние True.
        for j in range(2, i):  # Проверяем деление числа i без остатка на последовательность чисел от 2 до i-1.
            if i % j == 0:
                is_prime = False  # Если i делится без остатка, то оно не простое.
                break  # Прерываем проверку для ускорения обработки.
        if is_prime:  # Значение флага для i определено. Начинаем заполнение списков primes и not_primes.
            primes.append(i)  # Число простое - добавляем i в список primes.
        else:
            not_primes.append(i)  # Число не простое - добавляем i в список not_primes.

print(f'Primes: {primes}')  # Выводим список простых чисел.
print(f'Not Primes: {not_primes}')  # Выводим список не простых чисел.
