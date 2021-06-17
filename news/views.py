from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
# Create your views here.
def news(request):
    return render(request,"home/index.html")
def newsPost(request):
    return render(request,"home/index.html")
