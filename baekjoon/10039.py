# 평균 점수

arr = []
for i in range(5):
    num = int(input())
    if num < 40:
        arr.append(40)
    else:
        arr.append(num)

print(round(sum(arr) / 5))
