# 과자

arr = list(map(int, input().split()))

num = arr[0] * arr[1] - arr[2]
if num < 0:
    print(0)
else:
    print(num)
