for i in range(1, 101):
    if i % i == 0 or i % 1 == 0:
        if i == 2 or not i % 2 == 0:
            print("Result is: " + str(i) )