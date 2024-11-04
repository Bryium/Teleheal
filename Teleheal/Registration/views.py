from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def register_view(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render({}, request))