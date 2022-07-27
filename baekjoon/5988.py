# 홀수일까 짝수일까

N = int(input())

for i in range(N):
  num = int(input())
  if num % 2 == 0:
    print("even")
  else:
    print("odd")
