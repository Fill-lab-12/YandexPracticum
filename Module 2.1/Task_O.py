h = int(input())
m = int(input())
t = int(input())
total_minutes = h * 60 + m + t

total_minutes %= 1440
h = total_minutes // 60
m = total_minutes % 60

houre = h // 10
houre1 = h % 10

minutes = m // 10
minutes1 = m % 10

print(f"{houre}{houre1}:{minutes}{minutes1}")