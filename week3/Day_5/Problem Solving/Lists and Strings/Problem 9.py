def concatinate_lists(my_list1, my_list2):
    for element in my_list2:
        my_list1.append(element)
    return my_list1


my_list1 = ['a', 'b', 'c']
my_list2 = [1, 2, 3]
print(concatinate_lists(my_list1, my_list2))
