# 세로읽기

word_list = []
for i in range(5):
    word_list.append(list(input()))

max_size = max(len(word_list[0]), len(word_list[1]), len(word_list[2]), len(word_list[3]), len(word_list[4]))
str_list = ['' for i in range(max_size)]

for word in word_list:
    for j in range(len(word)):
        str_list[j] += word[j]

for i in str_list:
    print(i, end="")
