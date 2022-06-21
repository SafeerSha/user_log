from django.shortcuts import render, redirect
from pytz import timezone
from.models import user, lastlogin, lastlogout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import datetime


# Create your views here.
def index(request):
    ab = User.objects.filter(is_staff=False)
    return render(request, 'index.html',{'ab':ab})

def loginn(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'registration.html')

def registration(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['uname']
        email = request.POST['email']
        password = request.POST['pass'] 
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = name
        ui = user(user=myuser)
        ui.save()
        myuser.save()
        messages.success(request, 'successfully registered...')
        return redirect(loginn)   


def signin(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        pass1 = request.POST['pass']
        user = authenticate(username=uname, password=pass1)
        if user is not None:
            if lastlogin.objects.filter(user=user).exists():
                current_datetime = datetime.datetime.now()
                lastlogin.objects.update(user=user, lastlogin=current_datetime)
                login(request, user)
            else:
                login(request, user)
            return redirect(index)
        else:
            messages.success(request, 'Username or Password is Incorrect')
            return redirect(loginn)
    else:
        return redirect(index)

def signout(request, pk):
    logout(request)
    return redirect(index)