from django.shortcuts import render

from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, HttpResponseForbidden

from patient.models import Examination, Patient
from .form import Register_Doctor_Model, Login_Doctor_Model, Home_Page_Form, RESET_PASSWORD_Form
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.db.models import Q


class Register_Doctor_View(View):
    def get(self, request):
        form = Register_Doctor_Model()
        return render(request, 'doctor/register.html', {
            'form': form
        })

    def post(self, request):
        form = Register_Doctor_Model(request.POST)
        if form.is_valid():
            user = form.save()

            return render(request, 'doctor/register.html', {
                'result': 'valid',
                'user': user,
                'form': form
            })
        
        else:
            return render(request, 'doctor/register.html', {
                'result': 'Sorry data is not valid!',
                'form': form
            })


class Login_Doctor_View(View):
    def get(self, request):
        return render(request, 'doctor/login.html')
        
        
    def post(self, request):
        user = authenticate(
            username = request.POST['username'],
            password = request.POST['password']
        )

        if user is not None:
            login(request, user)
            # patient_id = request.POST['patient_id']
            return render(request, 'doctor/login.html', {
                'logged': True,
            })

        return render(request, 'doctor/login.html', {
            'error': 'username or password is incorrect!',
            'result': user 
        })


class RESET_PASSWORD_VIEW(View):
    def get(self, request):
        return render(request, 'doctor/reset-password.html')

    def post(self, request):
        form = RESET_PASSWORD_Form(request.POST)
        if form.is_valid():
            try:
                u = User.objects.get(username=form.cleaned_data['username'])

                u.set_password(request.POST['password'])

                u.save()

                return render(request, 'doctor/reset-password.html', {
                    'is_valid': True,
                    'result': 'Your username has updated successfully!!'
                })

            except:
                return render(request, 'doctor/reset-password.html',{
                    'is_found': False,
                    'error': 'sorry this username is incorrect'
                })

        else:
            return render(request, 'doctor/reset-password.html', {
                'is_valid': False,
                'error': 'sorry data is not valid',
            })


class Doctor_Logout_View(View):
    def get(self, request):
        logout(request)

        return HttpResponseRedirect('http://127.0.0.1:8000/doctor/login/')


class Home_Page_View(View):
    def get(self, request:HttpRequest):
        if not request.user.is_authenticated:
            return HttpResponseForbidden('Sorry you are not allowed from accessing the home page')

        else:
            return render(request, 'doctor/home_page.html')

    def post(self, request):
        form = Home_Page_Form(request.POST)
        if form.is_valid():
            try:
                patients = Patient.objects.all()
                examinations = Examination.objects.all()

                patient = Patient.objects.get(Q(full_name=form.cleaned_data['full_name']) | Q(national_id=form.cleaned_data['national_id']) | Q(email=form.cleaned_data['email']) | Q(phone1=form.cleaned_data['phone1']))
                patients_list = []
                examinations_list = []


                for patient in patients:
                    for examination in examinations:
                        examinations_list.append({
                            'patient_id': examination.patient_id,
                            'diagnosis': examination.diagnosis,
                            'treatment': examination.treatment,
                            'examination_date': examination.examination_date,
                        })
                    patients_list.append({
                        'address_id': patient.address_id,
                    })

                return render(request, 'doctor/home_page.html', {
                    'is_valid': True,
                    'examination_info': examinations_list,
                    'patient_info': patients_list,
                })

            except Exception as e:
                print(e)
                return render(request, 'doctor/home_page.html', {
                    'is_found': False,
                    'error': 'sorry patient not found'
                })

        else:
            return render(request, 'doctor/home_page.html', {
                'is_valid': False
            })




