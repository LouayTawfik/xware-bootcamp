import re
from django.forms import IntegerField, TextInput
from django import forms
from . models import Patient, Address



class Address_Model(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['governorate', 'city', 'line_1', 'line_2']

class Create_Patient_Form(forms.Form):
    full_name = forms.CharField(max_length=100, required=True)
    age = forms.IntegerField(required=True)
    national_id = forms.CharField(max_length=15, required=True)
    email = forms.CharField(max_length=100, required=True)
    phone1 = forms.CharField(max_length=15, required=True)
    phone2 = forms.CharField(max_length=15, required=True)
    gender = forms.ChoiceField(required=True, choices=[('M', 'Male'), ('F', 'Female')])
    address_id = forms.IntegerField()



class Update_Patient_Form(forms.Form):
    full_name = forms.CharField(max_length=100, required=True)
    age = forms.IntegerField(required=True)
    national_id = forms.CharField(max_length=15, required=True)
    email = forms.CharField(max_length=100, required=True)
    phone1 = forms.CharField(max_length=15, required=True)
    phone2 = forms.CharField(max_length=15, required=True)
    address_id = forms.IntegerField()



class Create_Examination_Form(forms.Form):
    patient_id = forms.IntegerField()
    diagnosis = forms.CharField(max_length= 100)
    treatment = forms.CharField(max_length=100)
    examination_date = forms.TimeField()



class Update_Examination_Form(forms.Form):
    patient_id = forms.IntegerField()
    diagnosis = forms.CharField(max_length=100)
    treatment = forms.CharField(max_length=100)
    examination_date = forms.TimeField()








