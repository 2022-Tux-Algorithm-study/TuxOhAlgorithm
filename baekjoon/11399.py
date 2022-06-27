# ATM

N = int(input())
arr = list(map(int, input().split()))

list_time = []
for time in arr:
    list_time.append(time)

list_time.sort()

sum_time = 0
for i in range(N):
    for j in range(i + 1):
        sum_time += list_time[j]

print(sum_time)
