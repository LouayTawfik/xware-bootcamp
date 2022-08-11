class Course:
    def __init__(self) -> None:
        self.courses = []

    def createCourse(self, courseNum):
        for i in range(courseNum):
            course = {}
            course['id'] = input("Please enter Course id number " + str(i + 1) + ": ")
            course['name'] = input("Please enter Course name number " + str(i + 1) + ": ")
            course['duration'] = input("Please enter Course duration number " + str(i + 1) + ": ")

            self.courses.append(course)


    def readCourse(self):
        return self.courses


    def readSpecificCourseInfo(self, courseNum):
        courseInfoNum = int(input("Please choose the Course you want to read: "))
        courseInfoNum -= 1

        for i in range(courseNum):
            if i == courseInfoNum:
                key = input("Please choose the name of Subject info you want to read: ")
                return self.courses[courseInfoNum][key]


    def updateSpecificCourseInfo(self, courseNum):
        choosenCourseNum = int(input("Please choose the Course you want to update: "))
        choosenCourseNum -= 1

        for i in range(courseNum):
            if i == choosenCourseNum:
                key = input("Please choose the name of Subject info you want to update: ")
                self.courses[i][key] = input("Please enter new " + key + " for the choosen Course: ")
                print(f"The Course ", key, " is updated successfully")