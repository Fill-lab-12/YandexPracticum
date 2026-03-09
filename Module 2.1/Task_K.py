num = int(input())

a = num // 1000
b = num // 100 % 10
c = num // 10 % 10
d = num % 10

badc = f"{b}{a}{d}{c}"

print(badc)