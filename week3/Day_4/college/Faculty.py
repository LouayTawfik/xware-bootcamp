class Faculty:
    
    def __init__(self) -> None:
     self.fac = []
     self.faculty = {}
     self.fac.append(self.faculty)

    def createFaculty(self, proNum, dNum):
        self.faculty['name'] = input("Please Enter Faculty name: ")
        for prof in range(proNum):
            self.faculty['P_id'] = input("Please Enter Professor id: ")
        for dep in range(dNum):
            self.faculty['D_id'] = input("Please Enter Department id: ")
       

        print("Faculty is created Successfully!!")


    def readFaculty(self):
        return(self.faculty)

    

    def readFaculty_Professor(self, professors):
        for _faculty in self.faculty:
            for professor in professors:
                if _faculty['P_id'] == professor['id']:
                    print("Linking Professors to Faculty: ")
                    print(_faculty)
                    print(professor)


    def readFaculty_Department(self, department):
        for _faculty in self.faculty:
            for department in department:
                if _faculty['D_id'] == department['id']:
                    print("Linking Departments to Faculty: ")
                    print(_faculty)
                    print(department)

    def updateFaculty(self):
        for key, value in self.faculty.items():
            self.faculty[key] = input(f"Please Enter new Faculty {key}: ")
            print(f"The Faculty ", key, " is updated successfully")
            





    





