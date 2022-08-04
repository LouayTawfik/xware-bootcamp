def createCourse(_Courses, courseNum):
    for i in range(courseNum):
        course = {}
        course['id'] = input("Please enter Course id number " + str(i + 1) + ": ")
        course['name'] = input("Please enter Course name number " + str(i + 1) + ": ")
        course['duration'] = input("Please enter Course duration number " + str(i + 1) + ": ")

        _Courses.append(course)


def readCourse(_Course):
    print(_Course)


def readSpecificCourseInfo(_Course, courseNum):
    courseInfoNum = int(input("Please choose the Course you want to read: "))
    courseInfoNum -= 1

    for i in range(courseNum):
        if i == courseInfoNum:
            key = input("Please choose the name of Subject info you want to read: ")
            print(_Course[courseInfoNum][key])


def updateSpecificCourseInfo(_Course, courseNum):
    choosenCourseNum = int(input("Please choose the Course you want to update: "))
    choosenCourseNum -= 1

    for i in range(courseNum):
        if i == choosenCourseNum:
            key = input("Please choose the name of Subject info you want to update: ")
            _Course[i][key] = input("Please enter new " + key + " for the choosen Course: ")