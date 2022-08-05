n = int(input("Please Enter a number: "))

while True:
    print("Press 1 if you want to compute the sum: ")
    print("Press 2 if you want to compute the product: ")
    print("Press -1 to exit:")

    choice = int(input())
    if choice == 1:
        sum = 0
        for i in range(1, n+1):
            sum += i
        
        print("Sum is: " + str(sum))

    elif choice == 2:
        product = 1
        for i in range(1, n+1):
            product *= i

        print("Product is: " + str(product))

    elif choice == -1:
        print("Thank you.. goodbye!")
        break

    else: 
        print("Invalid input, please try again!!") 


