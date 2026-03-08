a = int(input())
b = int(input())

a1 = a % 10 
a2 = (a // 10) % 10
a3 = a // 100

b1 = b % 10
b2 = (b // 10) % 10
b3 = b // 100

r1 = (a1 + b1) % 10
r2 = (a2 + b2) % 10
r3 = (a3 + b3) % 10

print(r3 * 100 + r2 * 10 + r1)