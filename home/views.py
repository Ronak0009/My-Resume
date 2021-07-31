from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request,no,*args):
    print(no)
    context={
        'number':no,
    }
    return render(request,"home/home.html",context)

def home_horizontal_view(request,no,*args):
    print(no)
    context={
        'number':no,
    }
    return render(request,"home/home-horizontal.html",context)

def home_slider(request,*args):
    return render(request,"home/slider.html")

def navbar(request,*args):
    return render(request,"home/navbar.html")