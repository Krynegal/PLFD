a = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж',
     'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п',
     'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш',
     'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

b = str(input())
for i in b:
    k = a[a.index(i) + 3]
    print(k, end='')
