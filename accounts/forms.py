from django import forms
from django.contrib.auth import authenticate

#class RegisterForm(templates.login):
#    username = forms.CharField(max_length=100, label='Kullanıcı Adı')
#    password1 = forms.CharField(max_length=100, label='Parola', widget=forms.PasswordInput)
#    password2 = forms.CharField(max_length=100, label='Parola Doğrulama', widget=forms.PasswordInput)

#    class Meta:
#        model = User
#       fields = [
#            'username',
#            'password1',
#            'password2',
#        ]

#    def clean_password2(self):
#        password1 = self.cleaned_data.get('password1')
#        password2 = self.cleaned_data.get('password2')
#        if password1 and password2 and password1 != password2:
#            raise forms.ValidationError("Parolalar Eslesmiyor!")
#        return password2

#class LoginForm(templates.login):
#    username = forms.CharField(max_length=100, label='Kullanıcı Adı')
#    password = forms.CharField(max_length=100, label='Parola', widget=forms.PasswordInput)
#
#    class Meta:
#        model = User
#        fields = [
#            'username',
#            'password',
#        ]

    #def clean_password2(self):
    #    password1 = self.cleaned_data.get('password1')
    #    password2 = self.cleaned_data.get('password2')
    #    if password1 and password2 and password1 != password2:
    #        raise forms.ValidationError("Parolalar Eslesmiyor!")
    #    return password2
