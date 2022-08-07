def for_loop_sum(my_list):
    sum = 0
    for n in my_list:
        sum += n
    return sum


list = [1, 2, 3, 4, 5]
print(for_loop_sum(list))


#=============================================

def while_loop_sum(my_list):
    index = 0
    sum = 0
    while index < len(my_list):
        sum += my_list[index]
        index += 1
    return "sum is: {0}" .format(sum)


print(while_loop_sum(list))

#=============================================

def recursion_sum(my_list):
    if len(my_list) == 0:
        return 0

    else:
        return my_list[0] + recursion_sum(my_list[1:])
              


print(recursion_sum(list))

