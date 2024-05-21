from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("ceci est la page d'accueil")