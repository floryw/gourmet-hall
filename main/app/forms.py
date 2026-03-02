from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 



class RegisterForm(UserCreationForm):
     
    fio = forms.CharField(label="ФИО", max_length=100)
    phone = forms.CharField(label="Телефон", max_length=100)

    class Meta:
         model = User
         fields = ["username", "password1", "password2", "fio", "phone", "email"]



