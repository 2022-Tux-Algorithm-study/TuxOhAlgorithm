# 수 뒤집기

T = int(input())

for i in range(T):
    flag = True

    arr = input()
    first_num = int(arr)

    arr = list(arr)
    arr.reverse()
    second_num = ''
    for num in arr:
        second_num += num
    second_num = int(second_num)

    num = first_num + second_num

    nm = list(str(num))
    for j in range(len(nm) // 2):
        if nm[j] != nm[len(nm) - 1 - j]:
            flag = False
    if flag:
        print("YES")
    else:
        print("NO")
