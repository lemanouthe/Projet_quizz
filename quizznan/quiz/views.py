from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . import models

# Create your views here.

def login(request):
    return render(request, 'pages/login.html')

@login_required
def home(request):
    return render(request, 'pages/index.html')

@login_required
def profil(request):
    return render(request, 'pages/profil.html')

@login_required
def quizz(request):
    return render(request, 'pages/quizz.html')

@login_required
def epreuve(request):
    return render(request, 'pages/epreuve.html')

@login_required
def lesson(request):
    return render(request, 'pages/lesson.html')

def deconnexion(request):
    logout(request)

    return redirect('login')