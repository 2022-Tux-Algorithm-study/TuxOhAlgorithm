# 콘테스트

arr = []
for i in range(20):
    arr.append(int(input()))

arr_W = arr[:10]
arr_K = arr[10:]

arr_W.sort(reverse=True)
arr_K.sort(reverse=True)

print(sum(arr_W[:3]), sum(arr_K[:3]))
