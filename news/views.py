from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from news.models import Post
# Create your views here.
def news(request):
    allPosts=Post.objects.all()
    # print(allPosts)
    context={'allPosts':allPosts}
    return render(request,"news/news.html",context)
# def newsPost(request):
#     return render(request,"news/newsPost.html")
def newsPost(request,slug):
    post=Post.objects.filter(slug=slug).first()
    post.save()
    context={'post':post}
    return render(request,'news/newsPost.html',context)
