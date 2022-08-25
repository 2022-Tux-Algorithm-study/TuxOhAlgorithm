# 플러그

from sys import stdin

N = int(stdin.readline())
s = []
for i in range(N):
    s.append(int(stdin.readline()))

print(sum(s) - (N - 1))
