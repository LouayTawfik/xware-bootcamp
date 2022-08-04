def createDepartment(_Departments, depNum):
     for i in range(depNum):
          department = {}
          department['id'] = input("Please enter Department id number " + str(i + 1) + ": ")
          department['name'] = input("Please enter Department name number " + str(i + 1) + ": ")

          _Departments.append(department)

     

def readDepartment(_Departments):
     print(_Departments)


def readSpecificDep(_Departments, depNum):
     depInfoNum = int(input("Please choose the number of the Department that you want to read: "))
     depInfoNum -= 1

     for i in range(depNum):
          if i == depInfoNum:
               key = input("Please enter the name of info you want to read: ")
               print(_Departments[depInfoNum][key])


def updateSpecificDepInfo(_Departments, depNum):
     choosenDepNum = int(input("Choose the number of the Department you want to update: "))
     choosenDepNum -= 1

     for i in range(depNum):
          if i == choosenDepNum:
               key = input("Please enter the name of info you want to update: ")
               _Departments[i][key] = input("Please enter new Department " + key + " for the choosen Department: ")

               




        
