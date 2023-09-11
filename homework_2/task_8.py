people_count = int(input("Кол-во человек: "))
step = int(input("Какое число в считалке? "))
people = [*range(1, people_count + 1)]
pointer, offset = 0, 1

while True:
    print("\nТекущий круг людей:", people)
    print("Начало счёта с номера", people[pointer % len(people)])
    pointer += step - offset
    offset += 1
    kicked = people[pointer % len(people)]
    print(f"Выбывает человек под номером {kicked}")
    people.remove(kicked)
    if len(people) == 1:
        print(f"Остался человек под номером {people[0]}")
        break
