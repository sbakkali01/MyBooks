from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('hello my G ')
# Create your views here.
