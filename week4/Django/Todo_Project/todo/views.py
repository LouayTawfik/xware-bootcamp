from pickle import GET
from django.shortcuts import render
from django.http import HttpResponse
from .form import Create_User

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
        return HttpResponse('Created User')
    elif request == 'POST':
        return HttpResponse('')

def user_update(request):
    return HttpResponse('Updated User')

def user_delete(request):
    return HttpResponse('Deleted User')

def user_retrieve(request):
    return HttpResponse('User Retrieved')


    
