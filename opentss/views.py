from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse


# Create your views here.
def home(request):
    return TemplateResponse(request,'home.html')


def index(request):
    return TemplateResponse(request,'index.html')


def login(request):
    return TemplateResponse(request, 'login.html')


def register(request):
    return  TemplateResponse(request, 'register.html')
