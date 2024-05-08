from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('hello maxime le suceur  ')
# Create your views here.
