from college import Subject

class Professor:
    def __init__(self) -> None:
        self.professors = []

    def createProfessor(self, profNum):
        for i in range(profNum):
            professor = {}

            professor['id'] = input("Please enter Professor id number " + str(i + 1) + ": ")
            professor['name'] = input("Please enter Professor name number " + str(i + 1) + ": ")
            professor['age'] = input("Please enter Professor age number " + str(i + 1) + ": ")
            professor['salary'] = input("Please enter Professor salary number " + str(i + 1) + ": ")

            professor['sub_id'] = input("Please enter the subject id: ")
            professor['course_id'] = input("Please enter the course id: ")
            

            self.professors.append(professor)


    def readProfessor(self):
        return self.professors


    def readProfessor_Subject(self, subjects):
        for professor in self.professors:
            for subject in subjects:
                if professor['sub_id'] == subject['id']:
                    print("Linking Professors to Subjects: ")
                    print((professor))
                    print(subject)


    def readProfessor_Course(self, courses):
        for professor in self.professors:
            for course in courses:
                if professor['course_id'] == course['id']:
                    print("Linking Prossors to Courses: ")
                    print(professor)
                    print(course)



    def readSpecificProfessorInfo(self, profNum):
        professorInfoNum = int(input("Please choose the Professor you want to read: "))
        professorInfoNum -= 1

        for i in range(profNum):
            if i == professorInfoNum:
                key = input("Please choose the name of Professor info you want to read: ")
                return self.professors[professorInfoNum][key]


    def updateSpecificProfessorInfo(self, profNum):
        choosenProfNum = int(input("Please choose the Professor you want to update: "))
        choosenProfNum -= 1

        for i in range(profNum):
            if i == choosenProfNum:
                key = input("Please choose the name of Professor info you want to update: ")
                self.professors[i][key] = input("Please enter new " + key + " for the choosen Professor: ")
                print(f"The Professor ", key, " is updated successfully")