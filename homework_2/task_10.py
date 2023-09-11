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
