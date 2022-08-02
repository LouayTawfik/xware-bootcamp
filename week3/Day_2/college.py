from re import X, sub


Faculty = input("Please Enter Faculty Name:")

depNum = int(input("Please Enter Departments number: "))

Departments = {
    "name": [],
    "id": []
}


for key, value in Departments.items():
        for i in range(depNum):
            value += [input("Please Enter " + key + ":")]
            Departments[key] = value


profNum = int(input("Please Enter Professors number: "))

Professors = {
    "id": [],
    "name": [],
    "age": [],
    "salary": []
}

for key, value in Professors.items():
        for i in range(profNum):
            value += [input("Please Enter " + key + ":")]
            Professors[key] = value



studNum = int(input("Please Enter Students number: "))

Students = {
    "id": [],
    "name": [],
    "phone": [],
    "age": []
}

for key, value in Students.items():
        for i in range(studNum):
            value += [input("Please Enter " + key + ":")]
            Students[key] = value



subNum = int(input("Please Enter Subjects number: "))

Subjects = {
    "id": [],
    "name": [],
    "code": []
}

for key, value in Subjects.items():
    for i in range(subNum):
        value += [input("Please Enter " + key + ":")]
        Subjects[key] = value


courseNum = int(input("Please Enter Courses number: "))

Courses = {
    "id": [],
    "name": [],
    "duration": []
}

for key, value in Courses.items():
        for i in range(courseNum):
            value += [input("Please Enter " + key + ":")]
            Courses[key] = value



examNum = int(input("Enter Exams number: "))

Exams = {
    "id": [],
    "name": [],
    "duration": [],
    "time": [],
    "date": []
}

for key, value in Exams.items():
        for i in range(examNum):
            value += [input("Please Enter " + key + ":")]
            Exams[key] = value



print("Departments Info: " + str(Departments))
print("Professors Info: " + str(Professors))
print("Students Info: " + str(Students))
print("Subjects Info: " + str(Subjects))
print("Courses Info: " + str(Courses))
print("Exams Info: " + str(Exams))



  
