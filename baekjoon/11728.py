# 배열 합치기

N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

sort_list = A + B
sort_list.sort()

for i in sort_list:
    print(i, end=" ")
