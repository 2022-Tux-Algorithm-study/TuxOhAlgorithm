# 단어 뒤집기

N = int(input())

for i in range(N):
  str_list = input().split()

  for str in str_list:
    str = list(str)
    str.reverse()
    for j in str:
      print(j, end="")
    print(" ", end="")
  print()
