# 나이순 정렬

N = int(input())

n_list = []
for i in range(N):
    age, name = input().split()
    age = int(age)
    n_list.append([age, name])

n_list.sort(key=lambda x:x[0])

for n in n_list:
    print(n[0], n[1])
