# 홀수

s = 0
odd_list = []
for i in range(7):
    n = int(input())
    if n % 2 != 0:
        s += n
        odd_list.append(n)

if len(odd_list) == 0:
    print(-1)
else:
    print(s)
    print(min(odd_list))
