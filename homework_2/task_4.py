guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print(f"Сейчас на вечеринке {len(guests)} человек: {guests}")
    user_input = input("Гость пришёл или ушёл? ")
    guest_name = input("Имя гостя: ")
    if user_input == "пришёл":
        if len(guests) == 6:
            print(f"Прости, {guest_name}, но мест нет.")
            continue
        guests.append(guest_name)
        print(f"Привет, {guest_name}")
    elif user_input == "ушёл":
        guests.remove(guest_name)
        print(f"Пока, {guest_name}")
    elif user_input == "Пора спать":
        print("Вечеринка закончилась, все легли спать.")
        break
