from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'pages/login.html')

def home(request):
    return render(request, 'pages/index.html')

def profil(request):
    return render(request, 'pages/profil.html')

def quizz(request):
    return render(request, 'pages/quizz.html')