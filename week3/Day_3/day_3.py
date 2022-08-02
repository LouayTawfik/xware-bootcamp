from re import I
from typing import List

salary = [4000, 3000, 1000, 2000]

def average(salary):
    max = salary[0]
    min = salary[len(salary) -1]
    i = 0

    while i < len(salary):
        if salary[i] > max:
            max = salary[i]

        elif salary[i] < min:
            min = salary[i]

        i += 1

    sum = 0
    i = 0
    while i < len(salary):
        if salary[i] == max or salary[i] == min:
            i += 1
            continue
        sum += salary[i]

        i += 1 
    
    print(sum)
    avg = 0
    avg = sum / (len(salary) - 2)
    print(avg)


average(salary)



