def merge_sorted_list(my_list1, my_list2):
    list3 = []
    for element1, element2 in zip(my_list1, my_list2):
        list3 += [element1, element2]

    return sorted(list3)


list1 = [1, 4, 6]
list2 = [2, 3, 5]

list3 = merge_sorted_list(list1, list2)
print(list3)