s = "hello"
k = "*"


def row():
    for _ in range(len(s) + 2):
        print(k, end="")


row()
print("\n" + k + s + k)
row()
