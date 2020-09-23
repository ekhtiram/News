from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from django.template import loader
from django import forms
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.template import RequestContext
from .forms import gridappForm
from .models import gridapp
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib import messages # register-daki messages.error icin
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                return render(request, 'gridapp/kayit.html', {})
            else:
                messages.error(request, "Error")
                return HttpResponseRedirect('/register/')
    else:
        form = UserRegistrationForm()
    return render(request, 'gridapp/registration.html', {'form' : form})

@login_required
def home(request):
    if request.user.is_superuser:
        context = {'hosgeldin':'Merhaba, sevgili admin ',}
    else:
        context = {'hosgeldin':'Merhaba, Hoş geldiniz ',}
    return render(request, 'gridapp/home.html', context)

def giris(request):
    return render(request, 'gridapp/giris.html',{})

def login(request):
    return render(request, 'registration/login.html',{})

def logout(request):
    return render(request, 'registration/logged_out.html',{})

def password_reset(request):
    return render(request, 'registration/password_reset.html',{})

def password_reset_done(request):
    return render(request, 'registration/password_reset_done.html',{})

def password_reset_email(request):
    return render(request, 'registration/password_reset_email.html',{})

def password_reset_confirm(request):
    return render(request, 'registration/password_reset_confirm.html',{})

def password_reset_complete(request):
    return render(request, 'registration/password_reset_complete.html',{})

def notfound(request):
    return render(request, 'gridapp/Notfound.html',{})

def sil(request):
    return render(request, 'gridapp/sil.html',{})

def kayit(request):
    return render(request, 'gridapp/kayit.html',{})

@login_required
def haberekle(request):
    if request.method == 'POST':
        form = gridappForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/haberler/')
        else:
            print (form.errors)
    else:
        form = gridappForm()
    return render(request, 'gridapp/haberekle.html',{'form': form})

@login_required
def haberler(request):
    query_results = gridapp.objects.all()
    context = {'query_results':query_results,}
    return render(request, 'gridapp/haberler.html', context)

@login_required
def hesabim(request):
    return render(request, 'gridapp/hesabim.html',{})
