from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
# Create your views here.
def country(request):
    return render(request,"home/country.html")