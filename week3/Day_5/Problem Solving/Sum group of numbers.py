"""
Program Discription:

- asks the user to enter a number and prints the sum of the numbers 1 to n

"""

#asks the user to enter a number which will be stored in variable "n"
n = int(input("Please enter a number: "))

sum = 0
for i in range(1, n+1):
    sum += i

print(sum)
