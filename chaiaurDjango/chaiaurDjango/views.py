from django.http import HttpResponse 
from django.shortcuts import render 

def home(request):
    # return HttpResponse("Hello, World! You are at chai aur Django home page.") 
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("Hello, World! This is the about page for chai aur Django.") 


def contact(request):
    return HttpResponse("Hello, World! This is the contact page for chai aur Django.") 
