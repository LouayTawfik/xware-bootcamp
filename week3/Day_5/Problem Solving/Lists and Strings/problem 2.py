def reverse_list(my_list):
    return my_list[::-1]

list = [5, 8, 40, 1, 65, 10]
reversedList= reverse_list(list)
print("Reversed list: {0}" .format(reversedList))


#====================================================
#Another Solution:
result_List = []
for i in list[::-1]:
    result_List.append(i)
print(result_List)

                                    