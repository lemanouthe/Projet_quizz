from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def login(request):
    return render(request, 'pages/login.html')

def home(request):
    return render(request, 'pages/index.html')


def profil(request):
    return render(request, 'pages/profil.html')

def quizz(request):

    # qcm = Question.objects.filter(statut=True)
    # paginator = Paginator(qcm, 1)
    # page = request.GET.get('page')
    # question = paginator.get_page(page)

    # data = {
    #     'qcm': question,
    # }
    return render(request, 'pages/quizz.html', data)

def deconnexion(request):
    logout(request)

    return redirect('login')