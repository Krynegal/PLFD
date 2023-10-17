# Отличный подход с выбором словаря для хранения баланса, ну и вообще очень круто и лаконично

friends_num = int(input("Кол-во друзей: "))
taxes = int(input("Долговых расписок: "))
friends = dict().fromkeys([*range(1, friends_num + 1)], 0)

for i in range(taxes):
    print(f"\n{i + 1}-я расписка")
    to = int(input("Кому: "))
    by = int(input("От кого: "))
    amount = int(input("Сколько: "))
    friends[to] -= amount
    friends[by] += amount

print("Баланс друзей:")
for friend, money in friends.items():
    print(f"{friend} : {money}")
