n = int(input()) # Общий вес 
m = int(input()) # Руб. за 1 кг
k1 = int(input()) # Первый вид котлет сколько стоит
k2 = int(input()) # Второй вид котлет сколько стоит

x = n * (m - k2) // (k1 - k2)
y = n - x
print(x, y)

# Формула
# K1x + K2y = MN
# K1x + K2(n-x) = MN
# K1x + K2n - K2x = MN
# (K1 - K2)x = MN - K2n
# x = (MN - K2n) / (K1 - K2)
# y = N - x так как x + y = n, а значит y - оставшееся
