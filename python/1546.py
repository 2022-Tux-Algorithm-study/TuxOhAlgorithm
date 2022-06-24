# 평균

N = int(input())

score_list = list(map(int, input().split()))

M = max(score_list)
sum_num = 0

for i in range(len(score_list)):
    score_list[i] = score_list[i] / M * 100
    sum_num += score_list[i]

print(sum_num / N)
