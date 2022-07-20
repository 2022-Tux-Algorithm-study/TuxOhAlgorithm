# 열 개씩 끊어 출력하기

words = input()

count = 0
for word in words:
    print(word, end="")
    count += 1

    if count == 10:
        print()
        count = 0
