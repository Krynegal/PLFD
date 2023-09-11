shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

name = input("Введите деталь: ")
chosen_detail_prices = [detail[1] for detail in shop if detail[0] == name]

print(f"Название детали: {name} \n"
      f"Кол-во деталей — {len(chosen_detail_prices)}\n"
      f"Общая стоимость — {sum(chosen_detail_prices)}")
