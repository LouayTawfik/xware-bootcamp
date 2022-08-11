from django.shortcuts import render
from django.http import HttpResponse


def create_faculty(request):
    return HttpResponse('Faculty Created')

def update_faculty(request):
    return HttpResponse('Faculty Updated')

def delete_faculty(request):
    return HttpResponse('Faculty Deleted')

def retrieve_faculty(request):
    return HttpResponse('Faculty Retrieved')







