# 박사 과정

N = int(input())

for i in range(N):
    s = input()
    if '+' in s:
        a, b = map(int, s.split("+"))
        print(a + b)
    else:
        print("skipped")
