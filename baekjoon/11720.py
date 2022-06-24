# 숫자의 합

N = int(input())
num_str = input()

num_sum = 0
for i in num_str:
    num_sum += int(i)

print(num_sum)