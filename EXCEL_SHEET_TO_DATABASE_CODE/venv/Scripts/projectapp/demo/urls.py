from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    
    path('',views.home,name= 'home'),
    path('upload/',views.simple_upload,name= 'simple_upload'),
    

]