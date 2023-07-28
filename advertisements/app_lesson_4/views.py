from django.shortcuts import render
from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse('Домашка по 4 занятию')

# Create your views here.
