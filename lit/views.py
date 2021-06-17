from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
# Create your views here.
def lit(request):
    return render(request,"home/lit.html")
