def rotate(mylist):
    list3 = mylist[2:] + mylist[:2]
    return list3


list = [1,2,3,4,5,6]
print(rotate(list))