from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
# Create your views here.
def photo(request):
    return render(request,"photo/photo.html")
