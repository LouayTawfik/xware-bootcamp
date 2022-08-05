"""
Program Discription:

- asks the user to enter a number and prints multiples of three or five for n eg. 3,5,6,9,10,12,15 for n = 17

"""

n = int(input("Please enter a number: "))

sum = 0
print("[", end = ' ')
for i in range(1, n+1):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
        print(str(i), end = ' ')

print("]")
print("sum is: " + str(sum))

        