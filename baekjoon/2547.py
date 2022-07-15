# 사탕 선생 고창영

T = int(input())

for i in range(T):
    num_sum = 0
    input()
    N = int(input())
    for j in range(N):
        num_sum += int(input())
    if num_sum % N == 0:
        print("YES")
    else:
        print("NO")
