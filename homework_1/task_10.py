name = input("Введите название футбольной команды: ")

print(f"{name} - чемпион!")

print("-"*len(name))
print(f"длина: {len(name.lower())}")
print(f"'п' в названии: {'п' in name}")
print(f"кол-во символов 'а' в названии: {name.count('а')}")
