from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"home/index.html")
def contact(request):
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
