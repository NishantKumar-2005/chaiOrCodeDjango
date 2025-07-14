from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def about(request):
    return HttpResponse("This is the about page of the Chai or Django project.")

def contact(request):
    return HttpResponse("This is the contact page of the Chai or Django project.")