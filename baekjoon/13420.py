# 사칙연산

T = int(input())

for i in range(T):
    num = input().split()
    num[0] = int(num[0])
    num[2] = int(num[2])
    num[4] = int(num[4])

    if num[1] == '+':
        if (num[0] + num[2]) == num[4]:
            print("correct")
        else:
            print("wrong answer")

    if num[1] == '-':
        if (num[0] - num[2]) == num[4]:
            print("correct")
        else:
            print("wrong answer")
    if num[1] == '*':
        if (num[0] * num[2]) == num[4]:
            print("correct")
        else:
            print("wrong answer")
    if num[1] == '/':
        if (num[0] / num[2]) == num[4]:
            print("correct")
        else:
            print("wrong answer")