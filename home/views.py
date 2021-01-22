from django.shortcuts import render
from .models import Tutorial

def about(request):
    tutorials=Tutorial.objects.all()
    return render(request,'home/about.html',{'tutorials':tutorials})

def contact(request):
    return render(request,'home/contact.html')