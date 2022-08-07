input_user = int(input("Enter a number: "))
list = []

number = str(input_user)

for i in range(len(number)):
    list.append(int(number[i]))

print(list)