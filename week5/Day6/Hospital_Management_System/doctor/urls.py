from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home_Page_View.as_view()),
    path('register/', views.Register_Doctor_View.as_view()),
    path('login/', views.Login_Doctor_View.as_view()),
    path('reset-password/', views.RESET_PASSWORD_VIEW.as_view()),
    # path('info/<int:id>/', views.Doctor_Detail_View.as_view()),
    path('logout/', views.Doctor_Logout_View.as_view()),
]