# 0 = not cute / 1 = cute

N = int(input())
count_0 = 0
count_1 = 0

for i in range(N):
    if int(input()) == 0:
        count_0 += 1
    else:
        count_1 += 1

if count_0 > count_1:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")
