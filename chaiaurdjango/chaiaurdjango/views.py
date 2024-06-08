from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Hello World , You are at chai aur code ")
    return render(request,'website/index.html')

def about(request):
     return render(request,"website/about.html")

def service(request):
     return render(request,"website/service.html")