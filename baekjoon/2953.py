# 나는 요리사다

max_sum = 0
winner = 1
for i in range(5):
    a = list(map(int, input().split()))
    if max_sum < sum(a):
        max_sum = sum(a)
        winner = i + 1

print(winner, max_sum)
