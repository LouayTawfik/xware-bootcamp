from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField
    address = models.CharField(max_length=100)
    email = models.EmailField
    ssn = models.CharField(max_length=20)

    

class Phone(models.Model):
    phone_1 = models.CharField(11)
    phone_2 = models.CharField(11)


class Links(models.Model):
    student_links = models.ForeignKey(Student,  on_delete=models.CASCADE)
    facebook = models.URLField()
    twitter = models.URLField()
    github = models.URLField()
