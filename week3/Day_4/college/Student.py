class Student:
    def __init__(self) -> None:
        self.students = []

    def createStudent(self, studentNum):
        for i in range(studentNum):
            student = {}
            student['id'] = input("Please enter Student id number " + str(i + 1) + ": ")
            student['name'] = input("Please enter Student name number " + str(i + 1) + ": ")
            student['phone'] = input("Please enter Student phone number " + str(i + 1) + ": ")
            student['age'] = input("Please enter Student age number " + str(i + 1) + ": ")
            

            self.students.append(student)


    def readStudent(self):
        return self.students


    def readSpecificStudentInfo(self, studentNum):
        studentInfoNum = int(input("Please choose the Student you want to read: "))
        studentInfoNum -= 1

        for i in range(studentNum):
            if i == studentInfoNum:
                key = input("Please choose the name of Student info you want to read: ")
                return self.students[studentInfoNum][key]


    def updateSpecificStudentInfo(self, studentNum):
        choosenStudentNum = int(input("Please choose the Student you want to update: "))
        choosenStudentNum -= 1

        for i in range(studentNum):
            if i == choosenStudentNum:
                key = input("Please choose the name of Student info you want to update: ")
                self.students[i][key] = input("Please enter new " + key + " for the choosen Student: ")
                print(f"The Student ", key, " is updated successfully")