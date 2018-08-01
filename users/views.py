# Create your views here.

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import User


def login_view(request):
    if(request.method == 'POST'):
        user_name = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect('/trial')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return render(request, 'login.html')
