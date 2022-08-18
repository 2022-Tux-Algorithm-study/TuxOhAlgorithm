# 단어 공부

from collections import Counter
import operator

s = input()
s = s.upper()
s = list(s)

if len(s) == 1:
    print(s[0])
else:
    counter = dict(Counter(s))
    counter = sorted(counter.items(), key=operator.itemgetter(1), reverse=True)
    
    if counter[0][1] == counter[1][1]:
        print("?")
    else:
        print(counter[0][0])
