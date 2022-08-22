# 백대열

n, m = map(int, input().split(":"))
original_n = n
original_m = m

while m != 0:
    n, m = m, n % m

print(str(original_n // n) + ":" + str(original_m // n))
