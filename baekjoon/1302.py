# 베스트셀러

import operator

N = int(input())

dic = {}
for i in range(N):
    book = input()

    if book not in dic:
        dic[book] = 1
    else:
        dic[book] = dic[book] + 1

dic = dict(sorted(dic.items()))
dic = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
print(dic[0][0])
