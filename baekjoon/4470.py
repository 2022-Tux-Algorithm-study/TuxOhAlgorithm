# 줄번호

N = int(input())
s_list = []

for i in range(N):
    s_list.append(input())

for i in range(len(s_list)):
    print(str(i + 1) + ". " + s_list[i])
