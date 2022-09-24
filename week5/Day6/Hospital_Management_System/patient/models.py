from django.db import models
from django.utils.translation import gettext_lazy as _



class Address(models.Model):
    governorate = models.CharField(max_length=100, null=False)
    city = models.CharField(max_length=100, null=False)
    line_1 = models.CharField(max_length=100, null=False)
    line_2 = models.CharField(max_length=100, null=False)




class Patient(models.Model):
    full_name = models.CharField(max_length=100, null=False)
    age = models.IntegerField(null=False)
    national_id = models.CharField(max_length=15, null=False)
    email = models.CharField(max_length=100, null=False)
    phone1 = models.CharField(max_length=15, null=False)
    phone2 = models.CharField(max_length=15, null=False)

    class Gender(models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')
    
    gender = models.CharField(max_length=2 ,null=False, choices=Gender.choices, default=Gender.MALE)

    def is_upperclass(self):
        return self.gender in {
            self.Gender.MALE,
            self.Gender.FEMALE
        }
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)



class Examination(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    diagnosis = models.CharField(max_length= 100, null=False)
    treatment = models.CharField(max_length = 100, null=False)
    examination_date = models.TimeField(null=False) 





