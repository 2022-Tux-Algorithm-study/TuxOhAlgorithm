# 17배

N = input()

dec = 0
for i in range(len(N)):
    dec += int(N[i]) * (2 ** (len(N) - i - 1))

dec = dec * 17
print(format(dec, 'b'))
