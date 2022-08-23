# 수열의 변화

n, k = map(int, input().split())
a = list(map(int, input().split(",")))

b = []
for j in range(k):
    for i in range(len(a)-1):
        b.append(a[i+1] - a[i])
    a = b
    b = []

for i, num in enumerate(a):
    if i == (len(a)-1):
        print(num)
    else:
        print(num, end=",")
