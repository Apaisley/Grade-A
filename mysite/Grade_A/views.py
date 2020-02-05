from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Strain

def index(request):
    return HttpResponse(" Welcome to the Grade A website")


 

