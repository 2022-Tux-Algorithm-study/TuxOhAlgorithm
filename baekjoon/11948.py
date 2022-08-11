# 과목선택

one_list = []
one_list.append(int(input()))
one_list.append(int(input()))
one_list.append(int(input()))
one_list.append(int(input()))

two_list = []
two_list.append(int(input()))
two_list.append(int(input()))

one_list.sort(reverse=True)
one_list = one_list[:3]

n_sum = sum(one_list) + max(two_list)
print(n_sum)
