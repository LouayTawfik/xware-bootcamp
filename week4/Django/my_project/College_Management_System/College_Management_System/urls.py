"""College_Management_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from faculty.views import *
from department.views import *


urlpatterns = [
    path('admin/', admin.site.urls),

    path('faculty/create', create_faculty),
    path('faculty/update', update_faculty),
    path('faculty/delete', delete_faculty),
    path('faculty/retrieve', retrieve_faculty),



    path('department/create', create_department),
    path('department/update', update_department),
    path('department/delete', delete_department),
    path('department/retrieved', retrieve_department),
]
