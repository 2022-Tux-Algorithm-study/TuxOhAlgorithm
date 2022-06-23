# 2진수 8진수

n = list(input())
n.reverse()

length = 3
list_8 = []

for i in range(0, len(n), length):
    sum_8 = 0
    arr = n[i:i+length]

    for j, k in enumerate(arr):
        sum_8 += int(k) * (2 ** j)

    list_8.append(str(sum_8))

list_8.reverse()
str_8 = ""
for i in list_8:
    str_8 += i

print(str_8)
