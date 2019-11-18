from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
from . import models
from .models import *

# Create your views here.

def connexion(request):
    return render(request, 'pages/login.html')

def islogin(request,):
    
    postdata = json.loads(request.body.decode('utf-8'))
    
    # name = postdata['name']

    username = postdata['username']
    password = postdata['password']
    isSuccess=False

    user = authenticate(username=username, password=password)
    
    if user is not None and user.is_active:
        print("user is login")
        isSuccess = True
        login(request, user)
        datas = {
        'success':True,
        'username':username,
        'message':'Votre connection a reussi avec succes',
    }
        return JsonResponse(datas,safe=False) # page si connect
        
    else:
        data = {
        'success':False,
        'message':'Vos identifiants ne sont pas correcte',
        }
        return JsonResponse(data,safe=False)
    
    
    
    return JsonResponse(datas, safe=False)


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