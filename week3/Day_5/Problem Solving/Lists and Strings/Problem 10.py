def combine_lists(my_list1, my_list2):
    # list3 =  [list (a) for a in zip(my_list1, my_list2)]
    # return list (zip(my_list1, my_list2))
    list3 = []
    for element1, element2 in zip(my_list1, my_list2):
        list3 += [element1, element2] 
        
    return list3


my_list1 = ['a', 'b', 'c']
my_list2 = [1, 2, 3]

result = combine_lists(my_list1, my_list2)
print(result)

