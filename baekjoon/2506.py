# 점수 계산

N = int(input())
score = list(map(int, input().split()))

total_score = 0
count = 0

for i in score:
    if i == 1:
        count += 1
        total_score += count
    else:
        count = 0

print(total_score)
