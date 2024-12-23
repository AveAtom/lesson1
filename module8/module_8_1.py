print("=== Try и Except. ====\n")


# Задание "Программистам всё можно.":
# Пора разрушать шаблоны привычного нам Python! Вот вас раздражает, что мы не можем сложить число(int) и строку(str)?
# Давайте исправим это недоразумение!
#
# Реализуйте следующую функцию:
# 1.add_everything_up, будет складывать числа(int, float) и строки(str)
#
# Описание функции:
# add_everything_up(a, b) принимает a и b, которые могут быть как числами(int, float), так и строками(str).
# TypeError - когда a и b окажутся разными типами (числом и строкой), то возвращать строковое представление этих двух
# данных вместе (в том же порядке). Во всех остальных случаях выполнять стандартные действия.
#
# Примечания:
# 1.Конструкции try-except в функции выполняют строго ту обработку, которая написана в задании (обращайте на важность
# порядка передачи данных).
# 2.Если хотите дополнить функции своими исключениями или написать отдельно дополнительно собственные функции -
# это не запрещено, мы не против, чтобы вы больше экспериментировали. Но в первую очередь выполните поставленную задачу.
# ***********************************************************************************************************
# === Функции ===
def add_everything_up(a, b):
    try:
        return round(a + b, 3)  # Возвращаем итог сложения a+b
    except TypeError:
        return f'{a}{b}'  # Если ошибка типа - возвращаем конкатенацию a и b


# === Прогон ===
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

print('\n=== Конец обработки === ')
