from django.urls import path 
from core.views import * 

urlpatterns = [
    path('' , index , name='index'),
    path('about' , about , name='about'),
    path('gallery' , gallery , name='gallery'),
    path('upload' , upload , name='upload'),
]