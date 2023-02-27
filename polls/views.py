from django.shortcuts import render
from django.http import HttpResponse # Permite introducir repuesta HTTP

# Create your views here.

def index(request):
    return HttpResponse("Hello Jotas")

