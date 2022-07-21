# 첫 글자를 대문자로

N = int(input())

par_list = []
for i in range(N):
    par_list.append(input())

for par in par_list:
    par = par[0].upper() + par[1:]
    print(par)
