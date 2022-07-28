# NN

N, M = input().split()
M = int(M)
s = ''
flag = True

for i in range(int(N)):
  s += N
  if len(s) > M:
    print(s[:M])
    flag = False
    break

if flag:
  print(s)
