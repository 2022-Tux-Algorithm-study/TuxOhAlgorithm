# N번째 큰 수

N = int(input())

for i in range(N):
    n_list = list(map(int, input().split()))
    n_list.sort(reverse=True)
    print(n_list[2])
