# Вместо двух циклов for для ввода размера коньков и ног людей, можно использовать один цикл и запрашивать данные поочередно
# Можно избавиться от сортировки списков a и b, так как она не обязательна в данной задаче. Просто проходи по списку "ног" и коньков в порядке ввода

a, b = list(), list()

n = int(input("Кол-во коньков: "))
for i in range(n):
    size = int(input(f"Размер {i + 1}-й пары: "))
    a.append(size)

people_num = int(input("Кол-во людей: "))
for i in range(people_num):
    foot_size = int(input(f"Размер ноги {i + 1}-го человека: "))
    b.append(foot_size)

a.sort()
b.sort()

cnt = 0
for i in range(len(b)):
    if b[i] <= a[i]:
        cnt += 1

print("Наибольшее кол-во людей, которые могут взять ролики:", cnt)

#Вариант решения по комментариям

skates, feet = [], []

n = int(input("Кол-во коньков: "))
for i in range(n):
    size = int(input(f"Размер {i + 1}-й пары: "))
    skates.append(size)

people_num = int(input("Кол-во людей: "))
for i in range(people_num):
    foot_size = int(input(f"Размер ноги {i + 1}-го человека: "))
    feet.append(foot_size)

cnt = 0
for i in range(people_num):
    if feet[i] in skates:
        cnt += 1
