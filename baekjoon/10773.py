# 제로

K = int(input())

stack = []

for i in range(K):
    num = input()
    if num == '0':
        stack.pop()
    else:
        stack.append(num)

n_sum = 0
for i in stack:
    n_sum += int(i)

print(n_sum)
