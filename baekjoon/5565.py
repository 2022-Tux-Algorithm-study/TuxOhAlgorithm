# 영수증

total_cost = int(input())
arr = []

for i in range(9):
    arr.append(int(input()))

print(total_cost - sum(arr))
