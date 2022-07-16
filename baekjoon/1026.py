# 보물

N = int(input())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1.sort()
arr2.sort(reverse=True)

s = 0
for i in range(len(arr1)):
    s += arr1[i] * arr2[i]

print(s)
