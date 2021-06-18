from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from news.models import Post
# Create your views here.
def news(request):
    allPosts=Post.objects.all()
    # print(allPosts)
    context={'allPosts':allPosts}
    return render(request,"home/news.html",context)
def newsPost(request):
    return render(request,"home/index.html")
