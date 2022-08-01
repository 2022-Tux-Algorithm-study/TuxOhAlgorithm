# 부호

from sys import stdin

for i in range(3):
    N = int(stdin.readline())
    n_sum = 0
    for j in range(N):
        n_sum += int(stdin.readline())
        
    if n_sum < 0:
        print('-')
    elif n_sum > 0:
        print('+')
    else:
        print('0')
