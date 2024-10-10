from django.shortcuts import render
from .models import MovieInfo
from .forms import MovieForm

# Create your views here.


def list(request):
    movie_set = MovieInfo.objects.all()

    return render(request,'list.html',{'mov':movie_set})

def edit(request,pk):
    instance_to_be_edited = MovieInfo.objects.get(pk=pk)
    if request.POST:
        title = request.POST.get('title')
        year = request.POST.get('year')
        description = request.POST.get('description')
        instance_to_be_edited.title = title
        instance_to_be_edited.year = year
        instance_to_be_edited.description = description
        instance_to_be_edited.save()

        
        movie_set = MovieInfo.objects.all()

        return render(request,'list.html',{'mov':movie_set})




    frm = MovieForm(instance=instance_to_be_edited)

    return render(request,'create.html',{'frm':frm})

def home(request):
    sample ={
        'list': [

            'god_father.jpg',
            'aadu_1.webp',
            'god_father.jpg'



        ]
    }
    return render(request,'home.html',sample)

def movies(request):
    mov_dict = {
        'items':[
           {
        'title':'godfather',
        'summary':'story of an underworld king',
        'year':'2003',
        'sucess':False,
        'img':'god_father.jpg'
        },
        {
        'title':'titanic',
        'summary':'story of an underworld king',
        'year':'2003',
        'sucess':True,
        'img':'titanic.jpg'
        },
        {
        'title':'aadu',
        'summary':'',
        'year':'2003',
        'sucess':True,
        'img':'aadu_1.webp'
        } 
        ]
    }
    return render(request,'edit.html',mov_dict)
    

def create(request):
    
    frm = MovieForm()
    if request.POST:
        """
        title = request.POST.get('title')
        year = request.POST.get('year')
        description = request.POST.get('description')  
        MovieInfo_obj = MovieInfo(title=title,year=year,description=description)
        MovieInfo_obj.save()   """
        frm = MovieForm(request.POST)
        if frm.is_valid():
            frm.save()

        else:
            frm = MovieForm()

    
    return render(request,'create.html',{'frm':frm})  

def delete(request,pk):
    instance = MovieInfo.objects.get(pk=pk)
    instance.delete()
    movie_set = MovieInfo.objects.all()
    return render(request,'list.html',{'mov':movie_set})  



