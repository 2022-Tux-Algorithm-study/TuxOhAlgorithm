# 시험 점수

minguk = list(map(int, input().split()))
manse = list(map(int, input().split()))

a = sum(minguk)
b = sum(manse)
if a >= b:
    print(a)
elif b > a:
    print(b)
