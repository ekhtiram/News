#from django import forms
#from django.contrib.auth import authenticate
#from django.contrib.auth.models import User
#
#class UserForm(forms.ModelForm):
#    password = forms.CharField(widget=forms.PasswordInput)
#
#    class Meta:
#        model = User
#        fields = ['username','password']
from django import forms
from .models import gridapp

class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'K. Adı',
        max_length = 32
    )
    email = forms.EmailField(
        required = True,
        label = 'E-mail',
        max_length = 100,
    )
    password = forms.CharField(
        required = True,
        label = 'Şifre',
        max_length = 32,
        min_length = 8,
        widget = forms.PasswordInput()
    )

class gridappForm(forms.ModelForm):
    class Meta:
        model = gridapp
        fields = ("Baslik","Alt_baslik","Ekleyen","Icerik","Resim")
