def createStudent(_Students, studentNum):
    for i in range(studentNum):
        student = {}
        student['id'] = input("Please enter Student id number " + str(i + 1) + ": ")
        student['name'] = input("Please enter Student name number " + str(i + 1) + ": ")
        student['phone'] = input("Please enter Student phone number " + str(i + 1) + ": ")
        student['age'] = input("Please enter Student age number " + str(i + 1) + ": ")
        

        _Students.append(student)


def readStudent(_Students):
    print(_Students)


def readSpecificStudentInfo(_Students, studentNum):
    studentInfoNum = int(input("Please choose the Student you want to read: "))
    studentInfoNum -= 1

    for i in range(studentNum):
        if i == studentInfoNum:
            key = input("Please choose the name of Student info you want to read: ")
            print(_Students[studentInfoNum][key])


def updateSpecificStudentInfo(_Students, studentNum):
    choosenStudentNum = int(input("Please choose the Student you want to update: "))
    choosenStudentNum -= 1

    for i in range(studentNum):
        if i == choosenStudentNum:
            key = input("Please choose the name of Student info you want to update: ")
            _Students[i][key] = input("Please enter new " + key + " for the choosen Student: ")