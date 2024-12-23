from random import randint  # импортируем функцию randint

print("=== Пространство имён.====")


# Задача "Счётчик вызовов":
# Порой необходимо отслеживать, сколько раз вызывалась та или иная функция. К сожалению, в Python не предусмотрен подсчёт вызовов автоматически.
# Давайте реализуем данную фишку самостоятельно!
#
# Вам необходимо написать 3 функции:
# Функция count_calls подсчитывающая вызовы остальных функций.
# Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре,
# строку в нижнем регистре.
# Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке,
# False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
#
# Пункты задачи:
# 1.Создать переменную calls = 0 вне функций.
# 2.Создать функцию count_calls и изменять в ней значение переменной calls. Эта функция должна вызываться
# в остальных двух функциях.
# 3.Создать функцию string_info с параметром string и реализовать логику работы по описанию.
# 4.Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
# 5.Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.
# 6.Вывести значение переменной calls на экран(в консоль).
#
# Примечания:
# 1.Для использования глобальной переменной внутри функции используйте оператор global.
# 2.Для функции is_contains лучше привести и искомую строку и все строки в списке в один регистр.
# 3.Файл module_3_1.py и загрузите его на ваш GitHub репозиторий. В решении пришлите ссылку на него.
# ****************************************************************************************************
# === Функции ====
# Функция подсчитывающая вызовы остальных функций.
def count_calls():
    global calls
    calls += 1


# Функция принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре,
# строку в нижнем регистре.
def string_info(string=""):
    count_calls()  # Вызываем функцию счетчик.
    return tuple([len(string), string.upper(), string.lower()])  # Возвращаем результат по условию задачи.


# Функция принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке,
# False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
def is_contains(string="", *list_to_search):  # python плохо принимает явно определяемые изменяемые коллекции
    # в аргументы. Поэтому использую *args
    count_calls()  # Вызываем функцию счетчик.
    return string.upper() in list(list_to_search)  # Возвращаем результат по условию задачи.


# === Исходные данные ======
calls = 0  # Создаем переменную calls = 0 вне функций.
list_of_words = ['hello', 'apple', 'something', 'yeah', 'nope', 'lalala']  # Список исходных слов
list_of_search = list(x.upper() for x in list_of_words)  # Список слов для поиска.
random_list = ['Hello', 'apPle', 'soMething', 'YeAH', 'clone', 'pineapple', 'nOpe', 'lalAla', 'NoT']  # Список слов
# для выбора рандомизатором

# === Основная обработка
# Вызываем каждую функцию случайным образом от 3 до 20 раз
calls_rand = randint(3, 20)  # Определяем случайно число вызовов функции.
for i in range(calls_rand):
    print(' String_info() result : {}'.format(string_info(random_list[randint(0, 8)])))  # Результат работы функции

print(
    f'= For function string_info() Реальное число вызовов = {calls_rand} , Число вызовов по функции (calls) = {calls}')

calls = 0
calls_rand = randint(3, 20)  # Определяем случайно число вызовов функции.
print(
    f'\n Список для проверки слова (list_of_search) - {list_of_search}')  # Выводи список слов по которому ведем поиск.

for i in range(calls_rand):
    word_rand = random_list[randint(0, 8)]  # Выбираем случайным образом слово для работы функции.
    # Результат работы функции.
    print(f' is_contains() result for word - {word_rand}', is_contains(word_rand, *list_of_search), sep=' => ')

print(f'for function is_contains() Реальное число вызовов = {calls_rand} , Число вызовов по функции (calls) = {calls}')

print(' Конец обработки.')  # Конец обработки.
