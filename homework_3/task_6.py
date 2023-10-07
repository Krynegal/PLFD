def splitBySign(*numbers): #тут неотрицательные сортируются по убыванию, а отрицательные по возрастанию, а по условию нужно наоборот
    pos = []
    neg = []
    for n in numbers:
        if n >= 0:
            pos.append(n)
            continue
        neg.append(n)
    pos.sort(reverse=True)
    neg.sort()
    return pos, neg


print(splitBySign(1, -1, 0, 4, 23, -99))
