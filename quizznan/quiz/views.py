from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . import models

# Create your views here.

def login(request):
    return render(request, 'pages/login.html')

def home(request):
    return render(request, 'pages/index.html')

def profil(request):
    return render(request, 'pages/profil.html')

def quizz(request):
    return render(request, 'pages/quizz.html')

def deconnexion(request):
    logout(request)

    return redirect('login')