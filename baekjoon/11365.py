# !밀비 급일

while True:
    s = input()
    if s == 'END':
        break

    s = list(s)
    s.reverse()

    for i in s:
        print(i, end="")

    print()
