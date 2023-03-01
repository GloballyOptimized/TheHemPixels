from django.shortcuts import render
from core.models import *

def index(request):
    return render(request , 'index.html')

def about(request):
    return render(request , 'about.html')

def gallery(request):
    all_images = Portfolio.objects.all()
    return render(request , 'gallery.html' ,{'all_images':all_images})

def upload(request):
    return render(request , 'upload.html')