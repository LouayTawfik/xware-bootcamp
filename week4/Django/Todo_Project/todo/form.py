from django import forms


class Create_User(forms.Form):
    user_name = forms.CharField(max_length=50, required=True, min_length=1)
    user_email = forms.EmailField(max_length=100)
    user_age = forms.IntegerField()
