# 중복 빼고 정렬하기

N = int(input())
arr = list(map(int, input().split()))

num_set = set(arr)
arr = list(num_set)
arr.sort()

for i in arr:
    print(i, end=" ")