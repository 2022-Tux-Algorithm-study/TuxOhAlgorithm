# 문자열 반복

T = int(input())

for i in range(T):
    N, strAp = input().split()
    N = int(N)
    for j in strAp:
        print(j * N, end="")
    print("")
