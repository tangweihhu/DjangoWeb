from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = eval(a) + eval(b)
    return HttpResponse(str(c))

def add2(request,a,b):
    c = eval(a) + eval(b)
    return HttpResponse(str(c))

def index(request):
    return render(request, 'home.html')