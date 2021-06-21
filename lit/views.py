from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import Sahitya
# Create your views here.
def lit(request):
    allPost=Sahitya.objects.all()
    context={'allPost':allPost}
    return render(request,"lit/lit.html",context)
