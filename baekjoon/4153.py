# 직각삼각형

while(True):
    arr = list(map(int, input().split()))
    if 0 in arr:
        break

    arr.sort(reverse=True)

    if (arr[0] ** 2) == arr[1] ** 2 + arr[2] ** 2:
        print("right")
    else:
        print("wrong")
