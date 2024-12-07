print("=== Пространство имен. ====\n")


#
# Создайте новый проект в PyCharm
# Запустите созданный проект
# Ваша задача:
# 1.Создайте новую функцию test_function
# 2.Создайте внутри test_function другую функцию - inner_function, Эта функция должна печатать значение
# "Я в области видимости функции test_function"
# 3.Вызовите функцию inner_function внутри функции test_function
# 4.Попробуйте вызывать inner_function вне функции test_function и посмотрите на результат выполнения программы
# *************************************************************************************************************
# === Функции ===
def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()


test_function()  # Вызываем функцию inner_function внутри функции test_function
try:
    inner_function()  # Пробуем вызывать inner_function вне функции test_function
except NameError:
    print("\nОбнаружена ошибка в вызове функции inner_function() ")

print('=== Конец обработки === ')
