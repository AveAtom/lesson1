from idlelib.iomenu import encoding
from os import listdir
from os.path import isfile, join
from re import sub

print("=== Оператор 'with'. ====")

#
# Задача "Найдёт везде.":
# Напишите класс WordsFinder, объекты которого создаются следующим образом:
# WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).
# Объект этого класса должен принимать при создании неограниченного количество названий файлов и записывать их в
# атрибут file_names в виде списка или кортежа.
#
# Также объект класса WordsFinder должен обладать следующими методами:
# get_all_words - подготовительный метод, который возвращает словарь следующего вида:
# {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
# Где:
# 1.'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
# 2.['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле.
# Алгоритм получения словаря такого вида в методе get_all_words:
# 1.Создайте пустой словарь all_words.
# 2.Переберите названия файлов и открывайте каждый из них, используя оператор with.
# 3.Для каждого файла считывайте единые строки, переводя их в нижний регистр (метод lower()).
# 4.Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - '] в строке. (тире обособлено пробелами,
# это не дефис в слове).
# 5.Разбейте эту строку на элементы списка методом split(). (разбивается по умолчанию по пробелу)
# 6.В словарь all_words запишите полученные данные, ключ - название файла, значение - список из слов этого файла.
#
# find(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение -
# позиция первого такого слова в списке слов этого файла.
# count(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение -
# количество слова word в списке слов этого файла.
# В методах find и count пользуйтесь ранее написанным методом get_all_words для получения названия файла и списка его слов.
# Для удобного перебора одновременно ключа(названия) и значения(списка слов) можно воспользоваться методом словаря - item().
#
# for name, words in get_all_words().items():
#   # Логика методов find или count
#   Примечания:
#
# 1.Регистром слов при поиске можно пренебречь.('teXT' ~ 'text')
# 2.Решайте задачу последовательно - написав один метод, проверьте результаты его работы.
# ***************************************************************************************************************
# === Классы ===
class ValidationError(Exception):  # Для перехвата ошибок переопределяем класс ValidationError
    pass


class WordsFinder:
    __PATH = "./files/"  # Папка, где находятся исходные файлы.

    def __new__(cls, *args, **kwargs):  # Проверка на наличие файла.
        list_files = [f for f in listdir(cls.__PATH) if
                      isfile(join(cls.__PATH, f))]  # Создаем список файлов в папке __PATH
        if len(args) == 0:
            print(f'=== Список файлов в директории {cls.__PATH} ===')
            print(*list_files, sep='\n')  # Вывод списка файлов
            raise ValidationError("=== Не задан ни один файл! ===")
        else:
            for file in args:
                if file in list_files:
                    pass
                else:
                    print(f'=== Список файлов в директории {cls.__PATH} ===')
                    print(*list_files, sep='\n')  # Вывод списка файлов
                    raise ValidationError(f"=== Файл {file} не найден в каталоге {cls.__PATH} ===")
            return super(WordsFinder, cls).__new__(cls)

    def __init__(self, *files):  # WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).
        self.file_names = [*files]  # Формируем список файлов.

    def get_all_words(self):  # Подготовительный метод, который возвращает словарь следующего вида:
        # {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
        all_words = dict()  # Определяем итоговый словарик.
        for file in self.file_names:
            res = []  # Обнуляем промежуточный список res
            with open(self.__PATH + file, 'r',
                      encoding='utf-8') as curr_file:  # Открываем файл на чтение. Курсор файла на нуле.
                list_file = curr_file.read().split('\n')  # Переводим построчно содержимое файла в список list_file
                # Чистим от шелухи и создаем промежуточный список res.
                clear_list = lambda dirt_list: [x for x in dirt_list if x !=''] # Чистим от пустых элементов в списке после отшелушивания.
                dump = [res := res + clear_list(sub(r' - ', '', sub(r'[,.=!?;:]+', '', x.lower())).split(' ')) for x in list_file]
            all_words.update({str(file): res})  # Формируем итоговый словарик.
        return all_words


    def find(self,
             word: str):  # метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение -
        # позиция первого такого слова в списке слов этого файла.
        res = dict()  # Определяем итоговый словарик.
        for key, value in (
        all_words := self.get_all_words()).items():  # Используем get_all_words для формирования исходного словаря.
            if word.lower() in value:  # Есть ли слово в списке? (оптимизируем код)
                res.update({key: value.index(word.lower()) + 1})  # Формируем итоговый словарик
            else:
                res.update({key: 0})  # Сразу присваиваем 0 (оптимизация)
        return res

    def count(self, word: str):
        res = dict()  # Определяем итоговый словарик.
        for key, value in (
        all_words := self.get_all_words()).items():  # Используем get_all_words для формирования исходного словаря.
            if word.lower() in value:  # Есть ли слово в списке? (оптимизируем код)
                res.update({key: len([x for x in value if word.lower() == x])})  # Формируем итоговый словарик
            else:
                res.update({key: 0})  # Сразу присваиваем 0 (оптимизация)
        return res


# === Прогон ===
try:
    # === Проверочные варианты ===
    finder1 = WordsFinder('Mother Goose - Monday’s Child.txt')
    print(f'\n=== Вариант: {", ".join(finder1.file_names)} ===')
    # #print(finder1.__dict__)
    print(finder1.get_all_words())  # Все слова
    print(finder1.find('Child'))
    print(finder1.count('Child'))
    del finder1

    finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
    print(f'\n=== Вариант: {", ".join(finder1.file_names)} ===')
    print(finder1.get_all_words())
    print(finder1.find('captain'))
    print(finder1.count('captain'))
    del finder1

    finder1 = WordsFinder('Rudyard Kipling - If.txt', )
    print(f'\n=== Вариант: {", ".join(finder1.file_names)} ===')
    print(finder1.get_all_words())
    print(finder1.find('if'))
    print(finder1.count('if'))
    del finder1

    finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                          'Rudyard Kipling - If.txt',
                          'Mother Goose - Monday’s Child.txt')
    print(f'\n=== Вариант: {", ".join(finder1.file_names)} ===')
    print(finder1.get_all_words())
    print(finder1.find('the'))
    print(finder1.count('the'))
    del finder1

    # === Прогон основной ===
    finder2 = WordsFinder('test_file.txt')
    print(f'\n=== Вариант: {", ".join(finder2.file_names)} ===')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

except ValidationError as e:
    print(e)
    print('\n=== Конец обработки (ошибка)  === ')
    exit()

print('\n=== Конец обработки === ')
