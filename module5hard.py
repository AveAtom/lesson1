import hashlib
from time import sleep

print("=== Классы и объекты. ====\n")


# Задание "Свой YouTube":
# Университет Urban подумывает о создании своей платформы, где будут размещаться дополнительные полезные ролики на тему
# IT (юмористические, интервью и т.д.). Конечно же для старта написания интернет ресурса требуются хотя бы базовые
# знания программирования.
# Именно вам выпала возможность продемонстрировать их, написав небольшой набор классов, которые будут выполнять похожий
# функционал на сайте.
# Всего будет 3 класса: UrTube, Video, User.
# Общее ТЗ:
# Реализовать классы для взаимодействия с платформой, каждый из которых будет содержать методы добавления видео,
# авторизации и регистрации пользователя и т.д.
# Подробное ТЗ:
# Каждый объект класса User должен обладать следующими атрибутами и методами:
# 1.Атрибуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
# Каждый объект класса Video должен обладать следующими атрибутами и методами:
# 1.Атрибуты: title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда остановки (изначально 0)),
# adult_mode(ограничение по возрасту, bool (False по умолчанию))
# Каждый объект класса UrTube должен обладать следующими атрибутами и методами:
# 1.Атрибуты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
# 2.Метод log_in, который принимает на вход аргументы: nickname, password и пытается найти пользователя в users
# с такими же логином и паролем. Если такой пользователь существует, то current_user меняется на найденного. Помните,
# что password передаётся в виде строки, а сравнивается по хэшу.
# 3.Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список,
# если пользователя не существует (с таким же nickname). Если существует, выводит на экран: "Пользователь {nickname}
# уже существует". После регистрации, вход выполняется автоматически.
# 4.Метод log_out для сброса текущего пользователя на None.
# 5.Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos, если с таким же
# названием видео ещё не существует. В противном случае ничего не происходит.
# 6.Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое
# слово. Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).
# 7.Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела),
# то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр.
# После текущее время просмотра данного видео сбрасывается.
# Для метода watch_video так же учитывайте следующие особенности:
# 1.Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
# 2.Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube. В противном случае выводить в консоль
# надпись: "Войдите в аккаунт, чтобы смотреть видео"
# 3.Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к. есть ограничения 18+.
# Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
# 4.После воспроизведения нужно выводить: "Конец видео"
# Примечания:
# Не забывайте для удобства использовать dunder(магические) методы: __str__, __repr__, __contains__, __eq__ и др.
# (повторить можно здесь)
# Чтобы не запутаться рекомендуется после реализации каждого метода проверять как он работает,
# тестировать разные вариации.
# ***************************************************************************************************************
# Поскольку в ТЗ сказано, что Каждый объект класса UrTube должен обладать следующими атрибутами и методами -
# предполагается, что атрибуты должны быть экземплярными (при определении используем self.)
# Дополнение:
# - В прогон добавлена проверка метода log_out()
# - В прогон добавлена проверка метода log_in()

# === Классы ===
class ValidationError(Exception):  # Для перехвата ошибок переопределяем класс ValidationError
    pass


class UrTube:

    def __init__(self):
        self.users = []  # Атрибуты: users(список объектов User),
        self.videos = []  # videos(список объектов Video),
        self.current_user = None  # current_user(текущий пользователь, User)

    def __contains__(self, item):  # для проверки наличия видео (полное совпадение) и пользователя (Nickname)
        if isinstance(item, Video):  # item принадлежит классу Video
            return True if len(["!" for x in self.videos if x.title == item.title]) != 0 else False
        elif isinstance(item, User):  # item принадлежит классу User
            return True if len(["!" for x in self.users if x.nickname == item.nickname]) != 0 else False
        else:
            raise ValidationError('Должны использоваться экземпляры классов User либо Video.')

    def __eq__(self, other=None):  # Это дичь. Я сложил сюда все типовые поисковые запросы
        if 1 < len(other) < 4:
            match other[0]:
                case 1:  # Поиск Video
                    return [x for x in self.videos if x.title == other[1]]
                case 2:  # Поиск пользователя по имени
                    return [x for x in self.users if x.nickname == other[1]]
                case 3: # Поиск названий по фрагменту
                    return [x.title for x in self.videos if x.title.lower().find(other[1]) != -1]
                case 4:  # Поиск User по nick и password
                    return [x for x in self.users if x.nickname == other[1] and x.password == other[2]]
                case _:
                    raise ValidationError('Значение [0] должно быть либо 1 либо 2 либо 3 либо 4')
        else:
            raise ValidationError('Значения должны быть в формате [1|2|3,<строка поиска>]|[4,nickname,password]')


    def register(self, nickname="", password="", age=0):  # метод регистрации. Особенности - при регистрации нового
        # пользователя автоматически происходит вход в систему под данным пользователем.
        if nickname == "":
            raise ValidationError('Поле логин должно быть заполнено.')
        if password == "":
            raise ValidationError('Поле пароль должно быть заполнено.')
        if age == 0:
            raise ValidationError('Поле возраст не должно равняться 0.')
        user = User(nickname, password, age)
        if user in self:  # Если такой пользователь уже существует (__contains__)
            print(f'Пользователь {nickname} уже существует.')
        else:
            self.users.append(user)
            self.current_user = user
        print(
            f'Количество зарегистрированных пользователей: {len(self.users)}. Текущий пользователь - {self.current_user.nickname}')

    def log_out(self):  # Метод выхода пользователя из системы
        self.current_user = None

    def log_in(self, nickname="", password=""):  # Метод входа пользователя в систему.
        if nickname == "":
            raise ValidationError('Поле логин должно быть заполнено.')
        if password == "":
            raise ValidationError('Поле пароль должно быть заполнено.')

        res = (self == [4, nickname, get_md5_of_string(password)])  # Поиск пользователя через __eq__ (дичь)
        if len(res) == 0:
            print('Введены неправильные значения имени или пароля пользователя.')
        else:
            self.current_user = res[0]
            print(f'Вход в систему под именем: {res[0].nickname}')

    def add(self, *args):  # Метод добавление видео в объект UrTube()
        counter_before = len(self.videos)
        for video in list(args):
            if isinstance(video, Video):
                if video in self:  # Проверка наличия видео с таким же именем (полное совпадение) (__contains__).
                    pass
                else:
                    self.videos.append(video)
            else:
                raise ValidationError('Все добавляемые объекты должен быть экземплярами класса Video ')
        counter_after = len(self.videos)
        print(f'Добавлено фильмов - {counter_after - counter_before}')

    def get_videos(self, item=""):  # Поиск названий видео по фрагменту без учета заглавных букв
        if item == "":  # если фрагмент пусто - отправляем пустой список.
            return []
        else:
            return self == [3, item.lower()]  # Поиск названий по фрагменту через __eq__ (дичь).


    def watch_video(self, item=""):  # Просмотр видео по запросу.
        if item == "":  # Если запрос пустой - выход с сообщением.
            print("Название видео должно быть не пустым")
        else:
            res_video = (self == [1, item])  # Отбираем объекты по строгому соответствию используя __eq__ (дичь)
            if len(res_video) == 0:  # Если ничего не найдено - выход с сообщением.
                print('Фильм не найден!')
                return
            if not self.current_user:  # Если пользователь не вошел в систему - выход с сообщением.
                print('Войдите в аккаунт, чтобы смотреть видео.')
            else:
                if res_video[
                    0].adult_mode:  # Если стоит флаг только для взрослых - проверяем возраст текущего пользователя
                    if self.current_user.age < 18:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу.")
                    else:
                        print(res_video[0], end='')


class Video:  # Атрибуты: title(заголовок, строка), duration(продолжительность, секунды),
    # time_now(секунда остановки (изначально 0))
    def __init__(self, title="", duration=0, adult_mode=False):
        if title == "":  # Проверка на пустой заголовок.
            raise ValidationError('Поле заголовок видео должно быть заполнено.')
        if duration == 0:  # Проверка на нулевую длительность ролика.
            raise ValidationError('Поле продолжительность видео не должно быть равной 0.')
        self.title = title
        self.time_now = 0
        self.duration = duration
        self.adult_mode = adult_mode

    def __str__(self):  # Проигрывание видео
        for i in range(1, self.duration + 1):  # Если проигрывать можно - проигрываем ролик.
            print(f'{i} ', end='')
            sleep(1)
        print('Конец видео')
        return ""


class User:  # Атрибуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
    def __init__(self, nickname="", password="", age=0):
        self.nickname = nickname
        self.password = get_md5_of_string(password)
        self.age = age

    def __str__(self):
        return self.nickname


# === Функции ===
def get_md5_of_string(input_string):  # Получить md5 hash
    return hashlib.md5(input_string.encode()).hexdigest()


# === Прогон ===
try:
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
    # Добавление видео
    ur.add(v1, v2)
    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))
    print(ur.get_videos('ПРОГ1234'))
    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    # ---- Дополнительная проверка
    ur.log_out()  # Проверка метода log_out
    ur.watch_video('Для чего девушкам парень программист?')
    ur.log_in('urban_pythonist', 'iScX4vIJClb9YQavjAgF')  # Проверка метода log_in
    # -----------------------------
    ur.watch_video('Для чего девушкам парень программист?')
    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)
    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
except ValidationError as e:
    print(e)
print('\n=== Конец обработки === ')
