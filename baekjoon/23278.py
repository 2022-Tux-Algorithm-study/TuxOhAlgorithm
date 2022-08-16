# 영화 평가

N, L, M = map(int, input().split())

score_list = list(map(int, input().split()))
score_list.sort()

score_list = score_list[L:]
score_list = score_list[:len(score_list) - M]

print(sum(score_list) / len(score_list))
