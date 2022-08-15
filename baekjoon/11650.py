# 좌표 정렬하기

N = int(input())

xy_list = []
for i in range(N):
    x, y = map(int, input().split())
    xy_list.append([x, y])
  
xy_list.sort(key=lambda x:(x[0], x[1]))

for xy in xy_list:
    print(xy[0], xy[1])
