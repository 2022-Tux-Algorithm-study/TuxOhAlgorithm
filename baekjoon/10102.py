# 개표

N = int(input())
a = 0
b = 0

vote_list = list(input())

for vote in vote_list:
  if vote == 'A':
    a += 1
  else:
    b += 1

if a > b:
  print("A")
elif b > a:
  print("B")
else:
  print("Tie")
