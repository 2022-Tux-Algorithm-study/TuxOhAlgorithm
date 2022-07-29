# 모음의 개수

s = input()

count = 0
for char in s:
  if char in ['a', 'e', 'i', 'o', 'u']:
    count += 1

print(count)
