name = input()
ent = int(input())
kg = int(input())
us = int(input())
eqal = ent * kg
change = us - eqal

print("Чек")
print(f"{name} - {kg}кг - {ent}руб/кг")
print(f"Итого: {eqal}руб")
print(f"Внесено: {us}руб")
print(f"Сдача: {change}руб")