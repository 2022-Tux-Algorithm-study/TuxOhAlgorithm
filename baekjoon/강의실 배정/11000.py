# 강의실 배정

from sys import stdin
import heapq

N = int(stdin.readline())

arr = []
for i in range(N):
    heapq.heappush(arr, list(map(int, stdin.readline().split())))

lecture_arr = []
for i in range(N):
    num = heapq.heappop(arr)

    if i == 0:
        heapq.heappush(lecture_arr, num[1])
        continue

    min_num = lecture_arr[0]
    if min_num <= num[0]:
        heapq.heappop(lecture_arr)

    heapq.heappush(lecture_arr, num[1])

print(len(lecture_arr))
