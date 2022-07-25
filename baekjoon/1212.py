# 8진수 2진수

a = input()

first = True
for num in a:
    num = int(num)
    arr = []
    count = 0
    while num != 0:
        arr.append(num % 2)
        num = num // 2
        count += 1

    if not first:
        for i in range(3 - count):
            arr.append(0)

    arr.reverse()
    for i in arr:
        print(i, end="")

    if len(arr) == 0:
        print(0)

    first = False
