faculty = {}

def createFaculty(Faculty):
    faculty['name'] = input("Please Enter Faculty name: ")
    faculty['P_id'] = input("Please Enter Professor id: ")
    faculty['D_id'] = input("Please Enter Department id: ")
    Faculty.append(faculty)


def readFaculty(Faculty):
    print(Faculty)

    

def readFaculty_Professor(Faculty, _Professors):
    for _faculty in Faculty:
        for professor in _Professors:
            if _faculty['P_id'] == professor['id']:
                print("Linking Professors to Faculty: ")
                print(_faculty)
                print(professor)


def readFaculty_Department(Faculty, _Department):
    for _faculty in Faculty:
        for department in _Department:
            if _faculty['D_id'] == department['id']:
                print("Linking Departments to Faculty: ")
                print(_faculty)
                print(department)

def updateFaculty(Faculty):
    faculty['name'] = input("Please Enter new Faculty name: ")
    Faculty[0] = faculty





    





