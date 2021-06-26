from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import Sahitya
# Create your views here.
def lit(request):
    allPost=Sahitya.objects.all()
    context={'allPost':allPost}
    return render(request,"lit/lit.html",context)

def litPost(request,slug):
    post=Sahitya.objects.filter(slug=slug).first()
    context={'post':post}
    return render(request,'lit/litPost.html',context)

