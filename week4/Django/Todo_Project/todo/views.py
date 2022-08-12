from pickle import GET
from django.shortcuts import render
from django.http import HttpResponse
from .form import Create_User
from .models import *

def todo_create(request):
    return render(request, 'todo/create_todo.html')

def todo_update(request):
    return HttpResponse('Updated todo')

def todo_delete(request):
    return HttpResponse('Deleted todo')

def todo_retrieve(request):
    return HttpResponse('Todo Retrieved')



def user_create(request):
    if request.method == "GET":
        return render(request, 'todo/create_user.html')
    else:
        form = Create_User(request.POST)
        if form.is_valid():
            user = User(
                name = form.cleaned_data['user_name'],
                email = form.cleaned_data['user_email'],
                age = form.cleaned_data['user_age']
            )
            user.save()
            # print(user.age)
            
            return HttpResponse('Your Data is valid')
        else:
            return HttpResponse('Your Data is not valid')

def user_update(request):
    return HttpResponse('Updated User')

def user_delete(request):
    return HttpResponse('Deleted User')

def user_retrieve(request):
    return HttpResponse('User Retrieved')


    
