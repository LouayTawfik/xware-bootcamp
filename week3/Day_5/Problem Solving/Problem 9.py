import random

n = random.randint(0, 50)


temp = 0
counter = 0
while True:
    userInput = int(input("Please enter your guessing number: "))
    temp += userInput


    if temp % userInput == 0:
        counter += 1

    if n == userInput:
        print("Hoooraaayyy, you guessed it right!!")
        print("Number of multiple tries is: " + str(counter))
        break

    elif n > userInput:
        print("Your guessing is too small, Try again!")

    elif n < userInput:
        print("Your guessing is too high, Try again!")


    if userInput == -1:
        print("Sorry, Invalid input!!")
        break

    
    