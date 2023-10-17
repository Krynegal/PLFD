# Вместо цикла for, который проверяет симметрию для каждого, можно использовать цикл while, чтобы найти наибольшую симметричную последовательность. Профитнее на больших последовательностях.
# Можно вместо add.append(*a[:i][::-1]) использвать срез add+= a[i][::-1], немного упростит код


a = list()
add = list()

digits_num = int(input("Кол-во чисел: "))
for i in range(digits_num):
    a.append(int(input(f"Число: ")))

for i in range(len(a)):
    if a[i:] == a[i:][::-1]:
        add.append(*a[:i][::-1])
        break

print(f"Последовательность: {a}\n"
      f"Нужно приписать чисел: {len(add)}\n"
      f"Сами числа: {add}")


#Вариант кода

a = list()
add = list()

digits_num = int(input("Кол-во чисел: "))
for i in range(digits_num):
    a.append(int(input(f"Число: ")))

for i in range(len(a)):
    if a[i:] == a[i:][::-1]:
        add.extend(a[:i][::-1])
        break

print(f"Последовательность: {a}\n"
      f"Нужно приписать чисел: {len(add)}\n"
      f"Сами числа: {add}")
