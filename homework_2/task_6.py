a, b = list(), list()

for i in range(3):
    a.append(int(input(f"Введите {i + 1}-е число для первого списка: ")))

for i in range(7):
    b.append(int(input(f"Введите {i + 1}-е число для второго списка: ")))

print(f"Первый список:{a}\n"
      f"Второй список:{b}\n"
      f"Новый первый список с уникальными элементами:{list(set(a + b))}")
