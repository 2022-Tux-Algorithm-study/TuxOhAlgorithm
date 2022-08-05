# 10부제

N = input()
num_list = list(input())

count = 0
for num in num_list:
    if num == N:
        count += 1

print(count)
