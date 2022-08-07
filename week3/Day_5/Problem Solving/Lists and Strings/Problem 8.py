import math

def on_all(low, high):
    counter = 0
    for num in range(low, high + 1):
        root = math.sqrt(num)
        if int(root + 0.5) ** 2 == num:
            counter += 1
            print(num)

        if counter == 12:
            print("counter is: {0}" .format(counter))
            break

low = 1
high = 200
on_all(low, high)
