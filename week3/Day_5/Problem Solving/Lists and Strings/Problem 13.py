def fibonacci():
    flag = 0
    for i in range(201):
        if i == 0:
            first = i
            print(first)

        elif i == 1:
            second = i
            print(second)
            flag = 1

        if flag == 1:
            next = first + second
            first = second
            second = next

            print(next)

        if i == 101:
            break


fibonacci()

