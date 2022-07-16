# 오븐 시계

hour, minute = map(int, input().split())
time = int(input())

minute = minute + time
while minute >= 60:
    minute = minute - 60
    hour = hour + 1
    if hour >= 24:
        hour = hour - 24

print(hour, end=" ")
print(minute)
