# 프로그래머스 K번째 수

def solution(array, commands):
    answer = []

    for command in commands:
        ary = array[command[0] - 1:command[1]]
        ary.sort()
        answer.append(ary[command[2] - 1])

    return answer
