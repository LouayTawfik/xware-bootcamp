def createProfessor(_Professors, profNum):
    for i in range(profNum):
        professor = {}
        professor['id'] = input("Please enter Professor id number " + str(i + 1) + ": ")
        professor['name'] = input("Please enter Professor name number " + str(i + 1) + ": ")
        professor['age'] = input("Please enter Professor age number " + str(i + 1) + ": ")
        professor['salary'] = input("Please enter Professor salary number " + str(i + 1) + ": ")
        

        _Professors.append(professor)


def readProfessor(_Professors):
    print(_Professors)


def readSpecificProfessorInfo(_Professors, profNum):
    professorInfoNum = int(input("Please choose the Professor you want to read: "))
    professorInfoNum -= 1

    for i in range(profNum):
        if i == professorInfoNum:
            key = input("Please choose the name of Student info you want to read: ")
            print(_Professors[professorInfoNum][key])


def updateSpecificProfessorInfo(_Professors, profNum):
    choosenProfNum = int(input("Please choose the Professor you want to update: "))
    choosenProfNum -= 1

    for i in range(profNum):
        if i == choosenProfNum:
            key = input("Please choose the name of Professor info you want to update: ")
            _Professors[i][key] = input("Please enter new " + key + " for the choosen Professor: ")