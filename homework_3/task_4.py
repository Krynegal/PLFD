s = "Maybe not today, maybe not tomorrow, but one day i'll become the greatest actor"

res = dict()
for c in s.lower():
    if str.isalpha(c) and not str.isspace(c):
        if c in res:
            res[c] += 1
        else:
            res[c] = 1

print(res)
