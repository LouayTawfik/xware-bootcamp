def larg(my_list):
    largest_number = max(my_list)
    return largest_number


list = [5, 8, 40, 1, 65, 10]
print("Largest number is: {0}" .format(larg(list)))



#======================================================
#Another Solution:

def larg(my_list):
    max = 0
    for num in my_list:
        if num  > max:
            max = num

    return "Largest number is: {0}" .format(max)

print(larg(list))




