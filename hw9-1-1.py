# Author: CCG 1/9/22

even_list = []

def even_id(lst):
    for index, value in lst:
        if int(index) // 2 == 0:
            even_list.append(value)
    return even_list

test_lst = [1,2,3,4,5,6]

print(even_id(test_lst))