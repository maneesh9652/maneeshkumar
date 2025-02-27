from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login


def signup(request):
    if request.method == 'POST':
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Account created successfully')
            return redirect(reverse('login'))  # Using reverse to dynamically get the URL
        else:
            messages.error(request, 'Form is not valid')
    else:
        fm = UserCreationForm()
    return render(request, 'sign.html', {'form': fm})


def login1(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            user = fm.cleaned_data['username']
            password = fm.cleaned_data['password']
            User = authenticate(request, username=user, password=password)
            if User is not None:
                login(request,User)
                return redirect(reverse('profile'))
        else:
                messages.error(request, 'Username or password is incorrect')
    else:
            fm = AuthenticationForm()
            return render(request,'login.html',{'form':fm})

def profile(request):
    if request.user.is_authenticated:
     return render(request,'profile.html',{'user':request.user})

def python(request):
    return render(request,'python.html')
def java(request):
    return render(request,'java.html')
def javascript(request):
    return render(request,'javascript.html')
def django(request):
    return render(request,'django.html')
def html(request):
    return render(request,'html.html')







