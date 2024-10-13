print("=== Неизменяемые и изменяемые объекты. Кортежи и списки ===")
# Написать программу на языке Python, используя Pycharm, для работы с неизменяемыми и изменяемыми объектами.

immutable_var = 1, 2, True,"String"# Создайте переменную immutable_var и присвойте ей кортеж из
                                                        # нескольких элементов разных типов данных
print("Immutable tuple - {}".format(immutable_var)) # Выполните операции вывода кортежа immutable_var на экран.
# Попытайтесь изменить элементы кортежа immutable_var. Объясните, почему нельзя изменить значения элементов кортежа.
# immutable_var[1]=1
print ("Значение 1 нельзя изменить так как кортеж является не изменяемым объектом (если в нем не находятся изменяемые объекты)")

mutable_list = [[x for x in range(3)],True]  # Создайте переменную mutable_list и присвойте ей список из нескольких элементов"
print("\nMutable list - {}".format(mutable_list))
mutable_list.append("Modified") # Измените элементы списка mutable_list
print("Mutable list после изменения - {}".format(mutable_list)) # Выведите на экран измененный список mutable_list
