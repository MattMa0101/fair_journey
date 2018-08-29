from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http.response import HttpResponse

# Create your views here.
def index(request):
    html = TemplateResponse(request, 'index.html')
    return HttpResponse(html.render())

def map(request):
    html = TemplateResponse(request, 'map.html')
    return HttpResponse(html.render())

def service(request):
    html = TemplateResponse(request, 'services.html')
    return HttpResponse(html.render())

def project(request):
    html = TemplateResponse(request, 'project.html')
    return HttpResponse(html.render())

def contact(request):
    html = TemplateResponse(request, 'contact.html')
    return HttpResponse(html.render())

def about(request):
    html = TemplateResponse(request, 'about.html')
    return HttpResponse(html.render())