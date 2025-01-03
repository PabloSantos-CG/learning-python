f_list = [1, 2, 3, 4, 5, 6, 7]
l_list = [1, 2, 3, 4]

def sum_of_lists(l1, l2):
    min_length = min(len(f_list), len(l_list))
    return [ l1[i] + l2[i] for i in range(min_length)]

print(sum_of_lists(f_list, l_list))