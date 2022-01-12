# Author: CCG 1/12/22

even_list = []

def even_id(lst):
    for index, value in enumerate(lst):
        if int(value) % 2 != 0:
            even_list.append(index)
            even_list.append(value)
    print(even_list)

test_lst = [1,2,3,4,5,6]

even_id(test_lst)