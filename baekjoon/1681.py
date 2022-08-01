# 줄 세우기

from sys import stdin

N, L = map(int, stdin.readline().split())
count = 0
num = 0

while count < N:
    num += 1
    if str(L) in str(num):
        continue
    else:
        count += 1

print(num)
