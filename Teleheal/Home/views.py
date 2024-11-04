from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

def login_view(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render({}, request))  
