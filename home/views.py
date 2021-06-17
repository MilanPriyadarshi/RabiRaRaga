from django.shortcuts import render
from django.http import HttpResponse
from home.models import Contact
# Create your views here.
def home(request):
    return render(request,"home/index.html")
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
def photo(request):
    return render(request,"home/photo.html")
def country(request):
    return render(request,"home/country.html")
def state(request):
    return render(request,"home/state.html")
def lit(request):
    return render(request,"home/lit.html")
