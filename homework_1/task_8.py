a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

minimum = min(a, b, c)
maximum = max(a, b, c)
middle = a + b + c - minimum - maximum

print(minimum, middle, maximum)
