from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import Photo
# Create your views here.
def photo(request):
    allPhoto=Photo.objects.all()
    context={'allPhoto':allPhoto}
    return render(request,"photo/photo.html",context)
