# 모음의 개수

while True:
    s = input()
    if s == '#':
        break
    count = 0

    for ch in s:
        if ch in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            count += 1

    print(count)
