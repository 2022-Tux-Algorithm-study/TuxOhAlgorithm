# 일곱 난쟁이

arr = []
for i in range(9):
    arr.append(int(input()))

arr.sort()
total_sum = sum(arr)
pass_index = []

for i in range(9):
    for j in range(i+1, 9):
        if (arr[i] + arr[j]) == (total_sum - 100):
            pass_index = [i, j]
            break
    if pass_index is []:
        break

for i in range(9):
    if i in pass_index:
        continue
    print(arr[i])
