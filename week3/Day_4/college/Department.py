class Department:
     def __init__(self) -> None:
          self.departments = []

     def createDepartment(self, depNum):
          for i in range(depNum):
               dep = {}
               dep['id'] = input("Please enter Department id number " + str(i + 1) + ": ")
               dep['name'] = input("Please enter Department name number " + str(i + 1) + ": ")

               self.departments.append(dep)


     def readDepartment(self):
          return self.department


     def readSpecificDep(self, depNum):
          depInfoNum = int(input("Please choose the number of the Department that you want to read: "))
          depInfoNum -= 1

          for i in range(depNum):
               if i == depInfoNum:
                    key = input("Please enter the name of info you want to read: ")
                    return self.departments[depInfoNum][key]


     def updateSpecificDepInfo(self, depNum):
          choosenDepNum = int(input("Choose the number of the Department you want to update: "))
          choosenDepNum -= 1

          for i in range(depNum):
               if i == choosenDepNum:
                    key = input("Please enter the name of info you want to update: ")
                    self.departments[i][key] = input("Please enter new Department " + key + " for the choosen Department: ")
                    print(f"The Department ", key, " is updated successfully")

               




        
