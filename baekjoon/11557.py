# Yangjojang of The Year

T = int(input())

for i in range(T):
    N = int(input())
    college_list = []
    for j in range(N):
        college_name, num = input().split()
        num = int(num)
        college_list.append([college_name, num])

    college_list.sort(key=lambda x:x[1], reverse=True)
    print(college_list[0][0])
