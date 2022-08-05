n = int(input("Please enter a number: "))


for i in range(2, n+1):
    for j in range(1, n+1):
        product = i * j
        print(str(i) + " * " + str(j) + " = " + str(product), end = ' \n')
        if j == n:
            print("====================================")


