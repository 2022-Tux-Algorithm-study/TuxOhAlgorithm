# 단어 정렬

N = int(input())

str_list = []
for i in range(N):
    str_list.append(input())

str_set = set(str_list)
str_list = list(str_set)
str_list.sort()
str_list.sort(key=lambda x:len(x))

for i in str_list:
    print(i)
