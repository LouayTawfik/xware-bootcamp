from django.db import models


class Professor(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField
    salary = models.IntegerField
    sub_id = models.IntegerField
    

