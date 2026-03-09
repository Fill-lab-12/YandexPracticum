name = input()
locker = int(input())

group = locker // 100  
bed = (locker // 10) % 10  
child = locker % 10  

print(f"""Группа №{group}. 
{child}. {name}. 
Шкафчик: {locker}. 
Кроватка: {bed}.""")