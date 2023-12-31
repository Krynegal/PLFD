# 1. Создание словаря
# Создать пустой словарь
info = dict()

# Добавить значения для ключей "фио", "дата_рождения", "место_рождения"
info["фио"] = "Сенякин Андрей Юрьевич"
info["дата_рождения"] = "03.04.2001"
info["место_рождения"] = "г. Тюмень"

# Напечатать словарь
print(info)

# Создать ключ "хобби" со значением = список из строк -
# наименований хобби (например "плавание" и т.д.)
info["хобби"] = ["плавание", "хобби хорсинг"]

# Добавить "программирование" в список хобби
info["хобби"].append("программирование")

# Создать ключ "животные" со значением = кортеж из строк -
# имен домашних животных (например "кошка Мурка" и т.д.)
info["животные"] = ("кошка Мурка", "пес Барбос")

# Создать ключ "ЕГЭ" и поместить в него пустой словарь
info["ЕГЭ"] = dict()

# В словарь info["ЕГЭ"] добавить информацию о сданных экзаменах,
# где ключ - наименование предмета, а значение - количество баллов
info["ЕГЭ"]["математика"] = 96
info["ЕГЭ"]["русский язык"] = 97
info["ЕГЭ"]["литература"] = 98

# Добавить экзамен, который не был сдан, после чего удалить его
info["ЕГЭ"]["физкультура"] = 0
info["ЕГЭ"].pop("физкультура")

# Создать ключ "вузы" и поместить в него пустой словарь
info["вузы"] = dict()

# В словарь info["вузы"] добавить информацию о вузах,
# где ключ - аббревиатура вуза, а значение -
# количество баллов для специальности, на которую хотели поступить
info["вузы"]["МИСИС"] = 299
info["вузы"]["МГУ"] = 109

# 2. Вывод на экран
print("Данные:")
# Получившийся словарь
print(info)

# Список экзаменов ЕГЭ в алфавитном порядке
# (используйте метод ``keys()``, преобразовав результат в кортеж)
exams = (info["ЕГЭ"].keys())
print("Предметы:", sorted(exams))
# Список вузов в алфавитном порядке
uni = (info["вузы"].keys())
print("Вузы:", sorted(uni))

# 3. Ответы на вопросы
print("\nОтветы на вопросы:")

# Выделить имя из info["фио"]
name = info["фио"].split()[1]
# Начинается на гласную? (True/False)
starts_with_vowel = name[0].lower() in "аоуыэяёюие"
print("* мое имя начинается на гласную букву:", starts_with_vowel)

# Выделить месяц из info["дата_рождения"]
month = info["дата_рождения"].split(".")[1]
# Родился зимой или летом? (True/False)
born_in_winter_or_summer = month in ['11', '12', '01', '06', '07', '08']
print("* родился летом или зимой:", born_in_winter_or_summer)

# Количество хобби и первое из них
hobbies_count = info["хобби"][0]
print("* у меня {} хобби, первое \"{}\"".format(len(info["хобби"]), hobbies_count))

# Количество сданных экзаменов
print("* после окончания школы сдавал {} экз.".format(len(info["ЕГЭ"])))

# Сумма баллов по экзаменам
sum_mark = sum(info["ЕГЭ"].values())
print("* сумма баллов = {}".format(sum_mark))

# Максимальный балл среди сданных
max_mark = max(info["ЕГЭ"].values())
print("* макс. балл = {}".format(max_mark))

# Количество вузов, в которые Вы проходите по баллам
vuz_count = 0
for v in info["вузы"].values():
    if sum_mark >= v:
        vuz_count += 1
print("* кол-во вузов в которые прохожу: {}".format(vuz_count))
