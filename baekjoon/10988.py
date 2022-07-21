# 팰린드롬인지 확인하기

word = input()

flag = True
for i in range(len(word) // 2):
    if word[i] != word[len(word) - 1 - i]:
        flag = False
        break

if flag:
    print(1)
else:
    print(0)
