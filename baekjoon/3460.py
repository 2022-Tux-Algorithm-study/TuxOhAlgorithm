# 이진수

T = int(input())

for i in range(T):
    s = int(input())
    bi = format(s, 'b')
    n = len(bi)

    one_list = []
    for j, b in enumerate(bi):
        if b == '1':
            one_list.append(n - j - 1)

    one_list.reverse()
    for n in one_list:
        print(n, end=" ")
    print()
