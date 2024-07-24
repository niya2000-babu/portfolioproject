from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def indexfun(request):
    context = {}
    template = loader.get_template('indexaa.html')
    return HttpResponse(template.render(context, request))

def aboutpg(request):
    context = {}
    template = loader.get_template('aboutpg.html')
    return HttpResponse(template.render(context, request))

def resume(request):
    context = {}
    template = loader.get_template('resumepg.html')
    return HttpResponse(template.render(context, request))

def cert(request):
    context = {}
    template = loader.get_template('cer.html')
    return HttpResponse(template.render(context, request))

def cont(request):
    context = {}
    template = loader.get_template('contact.html')
    return HttpResponse(template.render(context, request))