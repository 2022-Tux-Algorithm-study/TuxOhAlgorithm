# 수 정렬하기 2

from sys import stdin

N = int(stdin.readline())

num_list = []
for i in range(N):
    num_list.append(int(stdin.readline()))

num_list.sort()

for num in num_list:
    print(num)
