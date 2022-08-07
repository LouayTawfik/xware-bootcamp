def is_exist(my_list, element):
    if element in my_list:
        result = "exist"
    else:
        result = "not exist"

    return result


list = ["this", "is", "an", "awesome", "list"]
user_input = input("Enter the element you looking for: ")
print(is_exist(list, user_input))