# OX퀴즈

N = int(input())

for i in range(N):
  oxStr = input()
  currOx = 0
  count = 0
  
  for ox in oxStr:
    if ox == 'O':
      count += 1
      currOx += count
    else:
      count = 0
  print(currOx)
