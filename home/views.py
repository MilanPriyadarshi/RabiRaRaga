from django.shortcuts import render
from django.http import HttpResponse
from home.models import Contact
from news.models import Post
from lit.models import Sahitya
# Create your views here.
def home(request):
    post=Post.objects.order_by('sno')[:4]
    context={'post':post}
    return render(request,"home/index.html",context)
def contact(request):
    if request.method =='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content=request.POST['content']
        # print(name,email,phone,content)
        if len(name)<2 or len(email)<4 or len(phone)<10 or len(content)<5:
            print("failed")
        else:
            contact=Contact(name=name, email=email,phone=phone,content=content)
            contact.save()
            # return HttpResponse("Submitted Successfully")
    #         messages.success(request,"Your form submitted Successfully")
    return render(request,"home/contact.html")

def about(request):
    return render(request,"home/about.html")

def search(request):
    query=request.GET['query']
    if len(query)>78:
        allPosts = []
    else:
        allPosts=Post.objects.filter(title__icontains=query)
    params={'allPosts':allPosts , 'query':query}
    return render(request,"home/search.html",params)

