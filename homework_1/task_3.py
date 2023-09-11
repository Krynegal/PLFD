x, y, z = map(int, input("Введите три числа: ").split())

print(f"Результат: {round(((x ** 5 + 7) / (abs(-6) * y)) ** (1 / 3) / (7 - z % y), 3)}")
