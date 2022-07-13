# 상근날드

arr1 = []
arr2 = []
for i in range(3):
    arr1.append(int(input()))

for j in range(2):
    arr2.append(int(input()))

arr1.sort()
arr2.sort()
print(arr1[0] + arr2[0] - 50)
