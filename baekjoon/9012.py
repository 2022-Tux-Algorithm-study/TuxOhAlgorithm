# 괄호

T = int(input())

for i in range(T):
    stack = []
    flag = True
    vps_arr = list(input())

    for pr in vps_arr:
        if pr == '(':
            stack.append(pr)
        if pr == ')':
            if len(stack) == 0:
                flag = False
            else:
                stack.pop()

    if len(stack) > 0:
        flag = False

    if flag:
        print("YES")
    else:
        print("NO")
