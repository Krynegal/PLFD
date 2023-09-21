# НОД
def calculate_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if x % i == 0 and y % i == 0:
            hcf = i
    return hcf


# НОК
def calculate_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if greater % x == 0 and greater % y == 0:
            lcm = greater
            break
        greater += 1
    return lcm


print(calculate_lcm(44, 26))
print(calculate_hcf(44, 26))
