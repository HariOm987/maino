from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request, 'home.html')

def SignupPage(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        passs=request.POST.get('pass')
        cpass=request.POST.get('cpass')
        
        if passs!=cpass:
            return redirect("signup")
        else:
            my_user=User.objects.create_user(name,email,passs)
            my_user.save()

            return redirect('login')

    return render (request, 'index.html')

def LoginPage(request):
    if request.method=='POST':
        name=request.POST.get('name')
        passs=request.POST.get('pass')
        user=authenticate(request,username=name,password=passs)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')

    return render (request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')