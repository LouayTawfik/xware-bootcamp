def is_palindrome(user_input):
    if user_input == user_input[::-1]:
        print("A Palindrome")
    else:
        print("Not a Palindrome")



user_input = input("Enter a String: ")
is_palindrome(user_input)




#=====================================================

# # i = len(user_input) - 1
# for index, element in enumerate(user_input[::-1]):
#         if user_input[index] == element:
#             print("index : element {0} : {1}" .format(user_input.index(element) , element))
#             index -= 1
#             continue


#         elif  user_input[index] != element:
#             print("not a palindrome!")
#             break

#         print("it's a palindrome")

