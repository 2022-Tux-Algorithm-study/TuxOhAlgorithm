# 평균은 넘겠지

T = int(input())

for i in range(T):
    score_list = list(map(int, input().split()))
    avg = sum(score_list[1:]) / score_list[0]

    count = 0
    for j in range(score_list[0]):
        if score_list[j + 1] > avg:
            count += 1

    print('{:.3f}'.format(round(count / score_list[0] * 100, 3)) + "%")
