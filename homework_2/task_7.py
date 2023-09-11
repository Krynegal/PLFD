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
