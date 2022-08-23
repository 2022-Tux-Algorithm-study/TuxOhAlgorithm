# 뒤집힌 덧셈

def rev(x):
    x = list(str(x))
    x.reverse()

    s = ''
    for i in x:
        s += i
    return int(s)

x, y = map(int, input().split())
xySum = rev(x) + rev(y)
print(rev(xySum))
