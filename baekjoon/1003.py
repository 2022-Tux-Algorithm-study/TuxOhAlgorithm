# 피보나치 함수

T = int(input())

arr = [(1, 0), (0, 1)]

def fibonacci(n):
    for i in range(2, n + 1):
        arr.insert(i, (arr[i - 1][0] + arr[i - 2][0], arr[i - 1][1] + arr[i - 2][1]))

    return arr[n]


for i in range(T):
    N = int(input())
    a = fibonacci(N)
    print(a[0], a[1])
