from pprint import pprint
print("=== Режимы открытия файлов. ====\n")

# Задача "Учёт товаров.":
# Необходимо реализовать 2 класса Product и Shop, с помощью которых будет производиться запись в файл с продуктами.
# Объекты класса Product будут создаваться следующим образом - Product('Potato', 50.0, 'Vagetables') и обладать
# следующими свойствами:
# 1.Атрибут name - название продукта (строка).
# 2.Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
# 3.Атрибут category - категория товара (строка).
# 4.Метод __str__, который возвращает строку в формате '<название>, <вес>, <категория>'. Все данные в строке
# разделены запятой с пробелами.
# Объекты класса Shop будут создаваться следующим образом - Shop() и обладать следующими свойствами:
# 1.Инкапсулированный атрибут __file_name = 'products.txt'.
# 2.Метод get_products(self), который считывает всю информацию из файла __file_name, закрывает его и возвращает
# единую строку со всеми товарами из файла __file_name.
# 3.Метод add(self, *products), который принимает неограниченное количество объектов класса Product.
# Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию).
# Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине' .
# Примечания:
# 1.Не забывайте при записи в файл добавлять спец. символ перехода на следующую строку в конце - '\n'.
# 2.При проверке на существование товара в методе add можно вызывать метод get_products для получения текущих продуктов.
# 3.Не забывайте закрывать файл вызывая метод close() у объектов файла.
# *********************************************************************************************
# Классы
class Product: # Продукты - Product('Potato', 50.0, 'Vagetables')
    def __init__(self,name:str,weight:float,category:str):
        self.name=name # Название продукта (строка).
        self.weight=weight # общий вес товара (дробное число) (5.4, 52.8 и т.п.).
        self.category = category # категория товара (строка).

    def __str__(self): # возвращает строку в формате '<название>, <вес>, <категория>'. Все данные в строке
                        # разделены запятой с пробелами.
        return f'{self.name}, {self.weight}, {self.category}'

class Shop: # Магазин
    __file_name='products.txt' # Инкапсулированный атрибут __file_name = 'products.txt'.

    def init_file(self): # Метод затирки файла ( >file )
        file = open(self.__file_name, 'w')
        file.write('')
        file.close()

    def get_products(self,cls=False): # Cчитывает всю информацию из файла __file_name, закрывает его и возвращает
                            # единую строку со всеми товарами из файла __file_name
        file = open(self.__file_name,'r')
        res=file.read().split('\n') # Создаем пром список строк файла.
        file.close()
        res_cls=[Product(*x.split(',')) for x in res if x!=''] # Преобразуем список res в список классов Product
        return res_cls if cls else print(*res, sep='\n') # Отправляем потребителю либо список объектов Product res_cls либо
                                                         # выводим отформатированный текст списка res.

    def add(self, *products): # Принимает неограниченное количество объектов класса Product.
        file = open(self.__file_name, 'a')
        curr_products = self.get_products(True)
        for product in products:
            if any(x for x in curr_products if x.name==product.name): # Проверка на задвоенность.
                print(f'Продукт {product.name} уже есть в магазине.')
            else:
                file.write(f'{product}\n')
        file.close()

print('=== Прогон ===')
s1 = Shop()
#s1.init_file() # Для проведения первого запуска - раскомментируйте. Для проведения второго - закомментируйте.
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2) # __str__
#s1.get_products()
s1.add(p1, p2, p3)
s1.get_products()

print('\n=== Конец обработки === ')