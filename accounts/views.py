from accounts.forms import CreateUserform
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .decorators import allowed_users, unauthenticated_user
# Create your views here.
from .models import *
from django.contrib.auth.decorators import login_required

@unauthenticated_user
def registerPage(request):
    
    form= CreateUserform()
    if request.method == 'POST':
        form= CreateUserform(request.POST)
        if form.is_valid():
            new_user=form.save()
            user= form.cleaned_data.get("username")
            messages.success(request, 'Account has been created for ' + user)
            return redirect('Login')

    context = {'form':form}
    return render(request, 'accounts/register.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user= authenticate( username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Home')
        else:
            messages.info(request, 'Username or Password is incorrect')


    context = {}
    return render(request, 'accounts/Login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('/')

def home(request):
    return render(request, 'accounts/dashboard.html')

def clubs(request):
    return render(request, 'accounts/clubs.html')

def gallery(request):
    return render(request,'accounts/gallery.html')

@login_required(login_url='Login')
def club1(request):
    return render(request,'accounts/club1.html')


@login_required(login_url='Login')

def club2(request):
    return render(request,'accounts/club2.html')


@login_required(login_url='Login')
def club3(request):
    return render(request,'accounts/club3.html')


@login_required(login_url='Login')
def club4(request):
    return render(request,'accounts/club4.html')


@login_required(login_url='Login')

def club5(request):
    return render(request,'accounts/club5.html')


@login_required(login_url='Login')

def club6(request):
    return render(request,'accounts/club6.html')


@login_required(login_url='Login')

def club7(request):
    return render(request,'accounts/club7.html')


@login_required(login_url='Login')

def club8(request):
    return render(request,'accounts/club8.html')


@login_required(login_url='Login')

def club9(request):
    return render(request,'accounts/club9.html')


@login_required(login_url='Login')

def club10(request):
    return render(request,'accounts/club10.html')


@login_required(login_url='Login')

def club11(request):
    return render(request,'accounts/club11.html')


@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin'])
def club12(request):
    return render(request,'accounts/club12.html')


@login_required(login_url='Login')
@allowed_users(allowed_roles=['admin'])
def club13(request):
    return render(request,'accounts/club13.html')