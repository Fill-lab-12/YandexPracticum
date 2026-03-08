name = input()
price = int(input())
kg = int(input())
money = int(input())

total = price * kg
change = money - total

print("=" * 16 + "Чек" + "=" * 16)

ots_name = 35 - len("Товар:") - len(name)
print("Товар:" + " " * ots_name + name)

price_str = str(kg) + "кг * " + str(price) + "руб/кг"
ots_price = 35 - len("Цена:") - len(price_str)
print("Цена:" + " " * ots_price + price_str)

total_str = str(total) + "руб"
ots_total = 35 - len("Итого:") - len(total_str)
print("Итого:" + " " * ots_total + total_str)

money_str = str(money) + "руб"
ots_money = 35 - len("Внесено:") - len(money_str)
print("Внесено:" + " " * ots_money + money_str)

change_str = str(change) + "руб"
ots_change = 35 - len("Сдача:") - len(change_str)
print("Сдача:" + " " * ots_change + change_str)

print("=" * 35)