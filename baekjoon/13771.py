# Presents

N = int(input())

arr = []
for i in range(N):
    num = input()
    num1, num2 = num.split('.')
    arr.append([num, int(num1 + num2)])

arr.sort(key=lambda x:x[1])
print(arr[1][0])
