print("=== Напишите в начале программы однострочный комментарий: 3st program ===") # Задача 3 - Школьная загадка
print('Результат = ', str(3) +"st"+ " program") # результат действия
print("\n=== Выведите на экран(в консоль) результат:  2 умноженное на 2 плюс 2 без приоритета. ===")
a = 2*2+2
print('Результат (А) = ', str(a))
print("\n=== 2 умноженное на 2 плюс 2 с приоритетом для сложения. ===")
b = 2*(2+2)
print('Результат (Б) = ', str(b))
print("\n=== результат сравнения этих двух выражений. ===")

print( 'Результат сравнения (a==b) = ', str(a==b))
res="нет результата" # присвоение начального значения

if (a==b):
    res = "A равно Б"
elif (a>b):
    res = "А больше Б"
else:
    res = "А меньше Б"

print( 'Результат сравнения вербальный = ', res)