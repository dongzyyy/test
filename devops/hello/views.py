from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<p>Hello World, Hello Django</p>")
# Create your views here.
