import time  # импортируем time.sleep
from random import randint  # импортируем функцию randint

print("=== Дополнительное практическое задание по модулю.====")


# Задание "Слишком древний шифр":
# Вы отправились в путешествие на необитаемый остров и конечно же в очередной вылазке в джунгли вы попали в ловушку
# местному племени (да-да, классика "Индиана Джонса").
# К вашему удивлению, в племени были неплохие математики и по совместительству фантазёры.
# Вы поняли это, когда после долгих блужданий перед вами появились ворота (выход из ловушки) с двумя каменными
# вставками для чисел.
# В первом поле камни с числом менялись постоянно (от 3 до 20) случайным образом, а второе было всегда пустым.
# К вашему счастью рядом с менее успешными и уже неговорящими путешественниками находился папирус, где были написаны
# правила для решения этого "ребуса". (Как жаль, что они поняли это так поздно :( ).
# Во вторую вставку нужно было написать те пары чисел друг за другом, чтобы число из первой вставки было кратно
# (делилось без остатка) сумме их значений.
# Все пароли для чисел от 3 до 20 (для сверки):
# 3 - 12
# 4 - 13
# 5 - 1423
# 6 - 121524
# 7 - 162534
# 8 - 13172635
# 9 - 1218273645
# 10 - 141923283746
# 11 - 11029384756
# 12 - 12131511124210394857
# 13 - 112211310495867
# 14 - 1611325212343114105968
# 15 - 1214114232133124115106978
# 16 - 1317115262143531341251161079
# 17 - 11621531441351261171089
# 18 - 12151811724272163631545414513612711810
# 19 - 118217316415514613712811910
# 20 - 13141911923282183731746416515614713812911
# Примечания:
# Можно использовать как цикл for, так и цикл while
# Первое число не входит в одно из чисел пары
# Пары чисел подбираются от 1 до 20 для текущего числа.
# *********************************************************************************************************

def indy_work(code=0):  # Определяем возвращаемую функцию indy_work.
    res_code = []  # Определяем результирующий список.
    #is_code = []  # Определяем список найденных пар.
    for i in range(1, code):  # Внешний цикл перебора опорных чисел. Для числа 10 опорные числа будут 1..9.
        for j in range(i+1, code):  # Внутренний цикл чисел перебора. Для числа 10 числа перебора будут 2..9.
            # Условия выбора пары:
            # - code нацело делится на (i+j).
            if (code % (i + j) == 0) :# and (f'{j}|{i}' not in is_code) and (i != j):  # Условие выбора пары.
                res_code.extend([str(i), str(j)])  # Заносим пару в результирующий список
                # (в виде str для последующего str.join().
                #is_code.append(f'{i}|{j}')  # Формируем список найденных пар вида '1|2'.
    return ''.join(res_code)  # Для формирования результирующего кода - склеиваем все элементы результирующего списка
    # между собой через использование str.join().


# Считаем, что замок работал 10 раз и выдавал случайный код 1 раз в три секунды.
for i in range(10):  # Формируем цикл из 10 проходов.
    rand_code = randint(3, 20)  # Получаем случайное целое число в диапазоне от 3 до 20.
    #rand_code = i+3
    print(f' Вывод целого случайного числа из диапазона (3-20) - {rand_code}')  # Вывод случайного числа.
    print(' Пароль найден - {}'.format(indy_work(rand_code)))  # Вывод полученного кода.
    time.sleep(3)  # Тайм-аут 3 секунды.

print("Обработка завершена")  # Обработка завершена.
