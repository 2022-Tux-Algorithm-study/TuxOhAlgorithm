# 상수

num1, num2 = input().split()
num1_list = list(num1)
num2_list = list(num2)

num1_list.reverse()
num2_list.reverse()

new_num1 = ''
new_num2 = ''

for i in range(3):
    new_num1 += num1_list[i]
    new_num2 += num2_list[i]

new_num1 = int(new_num1)
new_num2 = int(new_num2)

if new_num1 > new_num2:
    print(new_num1)
else:
    print(new_num2)
