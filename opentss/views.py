from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.template import Template, Context
from django.template.loader import render_to_string
import datetime


# Create your views here.
def home(request):
    return TemplateResponse(request,'home.html')


def index(request):
    now = datetime.datetime.now()
    testvariable = "this is a variable from python!"

    #fp = open('index.html')
    #t = Template(fp.read())
    #fp.close()

    #html = t.render(Context({now}))
    html = render_to_string('index.html', {'now': now,'testv':testvariable})

    #return TemplateResponse(request,'index.html')
    return HttpResponse(html)


def login(request):
    return TemplateResponse(request, 'login.html')


def register(request):
    return TemplateResponse(request, 'register.html')
