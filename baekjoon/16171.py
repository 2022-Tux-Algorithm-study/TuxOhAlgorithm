# 나는 친구가 적다 (Small)

mixed_str = input()
search_str = input()

alpha_str = ''

for s in mixed_str:
    if 48 <= ord(s) <= 57:
        continue
    else:
        alpha_str += s

if search_str in alpha_str:
    print(1)
else:
    print(0)
