from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
# Create your views here.
def state(request):
    return render(request,"home/state.html")

