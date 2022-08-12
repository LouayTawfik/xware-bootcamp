from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    age = models.IntegerField()


class Task(models.Model):
    user_task = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    discription = models.CharField(max_length=170)
    create_date = models.DateTimeField(auto_created=True)
    finished_date = models.DateTimeField()
    task_note = models.TextField()
