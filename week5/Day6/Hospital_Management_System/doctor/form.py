from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class Register_Doctor_Model(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']

        help_texts = {
            'username': None
        }

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['password'] = make_password(
            cleaned_data['password']
        )
        return cleaned_data


class Login_Doctor_Model(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

        help_texts = {
            'username': None
        }




class Home_Page_Form(forms.Form):
    full_name = forms.CharField(max_length=100, required=False)
    national_id = forms.CharField(max_length=15, required=False)
    email = forms.EmailField(max_length=100, required=False)
    phone1 = forms.CharField(max_length=15, required=False)


class RESET_PASSWORD_Form(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(max_length=100, required=True)


       