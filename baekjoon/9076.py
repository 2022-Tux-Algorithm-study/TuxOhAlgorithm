# 점수 집계

N = int(input())

for i in range(N):
    score_list = []
    score_list = list(map(int, input().split()))

    score_list.sort()
    score_list = score_list[1:4]
    if abs(score_list[0] - score_list[2]) >= 4:
        print("KIN")
    else:
        print(sum(score_list))
