from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect, HttpRequest, HttpResponseForbidden
from .form import Create_Examination_Form, Create_Patient_Form, Address_Model, Update_Patient_Form, Update_Examination_Form
from .models import *
from django.views import View
from django.contrib.auth import authenticate


class Create_Patient_View(View):
    def get(self, request:HttpRequest):
        if not request.user.is_authenticated:
            return HttpResponseForbidden('Sorry you are not allowed from listing patients')

        else:
            address_form = Address_Model()
            return render(request, 'patient/create.html', {
                'address_form': address_form
            })


    def post(self, request):
        form = Create_Patient_Form(request.POST)
        address_form = Address_Model(request.POST)
        if form.is_valid() and address_form.is_valid():
            try:

                address_form.save()
                address_id = Address.objects.get(id=form.cleaned_data['address_id'])
                
                patient = Patient(
                    full_name = form.cleaned_data['full_name'],
                    age = form.cleaned_data['age'],
                    national_id = form.cleaned_data['national_id'],
                    email = form.cleaned_data['email'],
                    phone1 = form.cleaned_data['phone1'],
                    phone2 = form.cleaned_data['phone2'],
                    gender = form.cleaned_data['gender'],
                    address_id = address_id
                )

                
                patient.save()
                
                print(form.errors)
                print(address_form.errors)
                return render(request, 'patient/create.html', {
                    'is_valid': True,
                    'patient': patient,
                })

            except Exception as e:
                print(e)
                print(form.errors)
                latest_id = Address.objects.latest('id')
                return render(request, 'patient/create.html', {
                    'exception': True,
                    'error': f'address id not found, Address data has been saved in address id = {latest_id.id}',
                })

           
        else:
            print(form.errors)
            print(address_form.errors)
            return render(request, 'patient/create.html', {
                'is_valid': False,
            })


class Show_Patient_View(View):
    def get(self, request: HttpRequest, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden('Sorry you are not allowed from listing patient')


        else:
            try:
                patient = Patient.objects.get(id=request.GET['id'])

                response = render(request, 'patient/show.html', {
                    'is_authenticated': True,
                    'patient': patient
                    # 'patients': patient_list,

                })

                return response

            except Exception as e:
                print(e)
                return HttpResponse('Sorry patient not found!')


class Update_Patient_View(View):
    def get(self, request:HttpRequest, id):
         if not request.user.is_authenticated:
            return HttpResponseForbidden('Sorry you are not allowed from listing patient')
         else:
            address_form = Address_Model()
            try:
                return render(request, 'patient/update.html', {
                    'address_form': address_form
                })

            except:
                return render(request, 'patient/update.html', {
                    'is_found': 'sorry id not found!'
                })


    def post(self, request):
        form = Update_Patient_Form(request.POST)
        
        

        if form.is_valid():
            try:
                address_id = Address.objects.get(id=form.cleaned_data['address_id'])
                print('helloooooo')
                new_patient = Patient.objects.get(request.GET['id'])
                print('hyhsjfkas')

                new_patient = Patient(
                    full_name = form.cleaned_data['full_name'],
                    age = form.cleaned_data['age'],
                    national_id = form.cleaned_data['national_id'],
                    email = form.cleaned_data['email'],
                    phone1 = form.cleaned_data['phone1'],
                    phone2 = form.cleaned_data['phone2'],
                    address_id = address_id.id
                )

                new_patient.save()

                return render(request, 'patient/update.html', {
                    'is_valid': 'yes',
                    'new_patient': new_patient


                })


            except Exception as e:
                print(e)
                return render(request, 'patient/update.html', {
                    'is_found': 'Sorry id is not found'
                })

        else:
            return render(request, 'patient/update.html', {
                'is_valid': 'no'
            })


class Delete_Patient_View(View):
    def get(self, request:HttpRequest, id=None):
        if not request.user.is_authenticated:
            return HttpResponseForbidden('Sorry you are not allowed from creating Examination')
        else:
            try:
                patient = Patient.objects.get(id=request.GET['id'])
                patient.delete()
                return render(request, 'patient/delete.html', {
                    'result': 'Patient Deleted'
                })

            except Exception as e:
                print(e)
                return render(request, 'patient/delete.html', {
                    'result': 'Patient id not found'
                })


class Create_Examination_View(View):
    def get(self, request:HttpRequest):
        if not request.user.is_authenticated:
            return HttpResponseForbidden('Sorry you are not allowed from creating Examination')

        else:
            return render(request, 'patient/examination_create.html')


    def post(self, request):
        form = Create_Examination_Form(request.POST)

        if form.is_valid():
            try:
                examination_patient = Patient.objects.get(id=form.cleaned_data['patient_id'])

                examination = Examination(
                    patient_id = examination_patient,
                    diagnosis = form.cleaned_data['diagnosis'],
                    treatment = form.cleaned_data['treatment'],
                    examination_date = form.cleaned_data['examination_date']
                )

                examination.save()

                return render(request, 'patient/examination_create.html', {
                    "is_valid": True,
                })

                

            except Exception as e:
                print(e)
                print(form.errors)
                return render(request, 'patient/examination_create.html', {
                    'is_found': False,
                    'error': 'Sorry patient id not found'
                })

        else:
            return render(request, 'patient/examination_create.html', {
                'is_valid': False
            })


class Show_Examination_View(View):
    def get(self, request: HttpRequest):
        if not request.user.is_authenticated:
            return HttpResponseForbidden('Sorry you are not allowed from listing Examination')

        
        examinations = Examination.objects.all()

        examination_list = []

        for examination in examinations:
            counter =0
            examination_list.append({
                'patient_id': examination.patient_id,
                'diagnosis': examination.diagnosis,
                'treatment': examination.treatment,
                'examination_date': examination.examination_date,
            })
            counter +=1

        response = render(request, 'patient/examination_show.html', {
            'is_authenticated': True,
            'counter': 'True',
            'examinations': examination_list,

        })

        return response


class Update_Examination_View(View):
    def get(self, request:HttpRequest):
        if not request.user.is_authenticated:
            return HttpResponseForbidden('Sorry you are not allowed from Updating Examinations')
        else:
            return render(request, 'patient/examination_update.html')

    
    def post(self, request):
        form = Update_Examination_Form(request.POST)

        if form.is_valid():
            try:
                patient_id = Patient.objects.get(id=form.cleaned_data['patient_id'])

                new_examination = Examination(
                    patient_id = patient_id,
                    diagnosis = form.cleaned_data['diagnosis'],
                    treatment = form.cleaned_data['treatment'],
                    examination_date = form.cleaned_data['examination_date']

                )

                new_examination.save()



                return render(request,'patient/examination_update.html', {
                    'is_valid': True
                })
            except:
                return render(request, 'patient/examination_update.html', {
                    'is_found': False,
                    'error': 'Sorry patient_id not found'
                })

        else:
            return render(request, 'patient/examination_update.html', {
                'is_valid': False
            })


class Delete_Examination_View(View):
    def get(self, request:HttpRequest, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden('Sorry you are not allowed from creating Examination')

        else: 
            try:
                examination = Examination.objects.get(id=request.GET['id'])
                examination.delete()
                return render(request, 'patient/examination_delete.html', {
                    'is_deleted': True,
                    'message': 'Examination has been deleted successfully'
                })

            except Exception as e:
                print(e)
                return render(request, 'patient/examination_delete.html', {
                    'is_found': False,
                    'error': 'sorry patient not found'
                })

        


        



