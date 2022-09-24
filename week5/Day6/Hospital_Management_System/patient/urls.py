from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.Create_Patient_View.as_view()),
    path('show/', views.Show_Patient_View.as_view()),
    path('update/<int:id>', views.Update_Patient_View.as_view()),
    path('delete/', views.Delete_Patient_View.as_view()),
    path('examination_create/', views.Create_Examination_View.as_view()),
    path('examination_show/', views.Show_Examination_View.as_view()),
    path('examination_update/', views.Update_Examination_View.as_view()),
    path('examination_delete/', views.Delete_Examination_View.as_view()),
]