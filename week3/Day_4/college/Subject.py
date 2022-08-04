def createSubject(_Subjects, subNum):
    for i in range(subNum):
        subject = {}
        subject['id'] = input("Please enter subject id number " + str(i + 1) + ": ")
        subject['name'] = input("Please enter subject name number " + str(i + 1) + ": ")
        subject['code'] = input("Please enter subject code number " + str(i + 1) + ": ")

        _Subjects.append(subject)


def readSubject(_Subjects):
    print(_Subjects)


def readSpecificSubjectInfo(_Subjects, subNum):
    subInfoNum = int(input("Please choose the Subject you want to read: "))
    subInfoNum -= 1

    for i in range(subNum):
        if i == subInfoNum:
            key = input("Please choose the name of Subject info you want to read: ")
            print(_Subjects[subInfoNum][key])


def updateSpecificSubInfo(_Subjects, subNum):
    choosenSubNum = int(input("Please choose the Subject you want to update: "))
    choosenSubNum -= 1

    for i in range(subNum):
        if i == choosenSubNum:
            key = input("Please choose the name of Subject info you want to update: ")
            _Subjects[i][key] = input("Please enter new " + key + " for the choosen Subject: ")
