n1 = int(input("Введите двухзначное число: "))
n2 = int(input("Введите трехзначное число: "))

print(f"Сумма для {n1}: {n1 // 10 + n1 % 10}\n"
      f"Произведение для {n1}: {n1 // 10 * (n1 % 10)}\n"
      f"Сумма для {n2}: {n2 // 100 + n2 // 10 % 10 + n2 % 10}\n"
      f"Произведение для {n2}: {n2 // 100 * (n2 // 10 % 10) * (n2 % 10)}")