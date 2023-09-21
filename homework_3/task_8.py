low = 0
high = 100

while low <= high:

    mid = (high + low) // 2

    ans = input(f"Число равно, больше или меньше {mid} ?: ")
    if ans == "равно":
        print("вы загадали ", mid)
        break
    elif ans == "больше":
        low = mid + 1
    else:
        high = mid - 1
