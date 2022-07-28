# 8진수

n = list(input())
n = list(map(int, n))

if len(n) % 3 != 0:
  for i in range(3 - (len(n) % 3)):
    n.insert(0, 0)

count = 0
eight_num = 0
eight_str = ''

for num in n:
  eight_num += num * (2 ** (3 - count - 1))
  count += 1
  
  if count == 3:
    eight_str += str(eight_num)
    count = 0
    eight_num = 0

print(eight_str)
