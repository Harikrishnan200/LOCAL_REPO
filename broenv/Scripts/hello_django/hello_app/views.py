from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def print_hello(request):
    return HttpResponse("hai hello")
  

def hai(request):
    movie_details = {
        'title':'godfather',
        'summary':'story of an underworld king',
        'year':'2003',
        'sucess':False
    }
    return render(request,'hello.html',movie_details)  

def movie_list(request):
        movie = { 
        'mov_list':[
        {
        'title':'godfather',
        'summary':'story of an underworld king',
        'year':'2003',
        'sucess':False
        },
        {
        'title':'titanic',
        'summary':'story of an underworld king',
        'year':'2003',
        'sucess':True
        },
        {
        'title':'aadu',
        'summary':'',
        'year':'2003',
        'sucess':True
        }





    ]
    }
        return render(request,'hello1.html',movie)