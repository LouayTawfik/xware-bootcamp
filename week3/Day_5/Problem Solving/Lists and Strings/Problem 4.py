def odd_positition(my_list):
    for index, element in enumerate(my_list):
        if not (index % 2 == 0):
            print(element, end=' ')
    print()


list = [5, 8, 40, 1, 65, 10, 32, 7, 34, 90]
odd_positition(list)





