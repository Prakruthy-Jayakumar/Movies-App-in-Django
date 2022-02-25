from django.http import HttpResponse
from django.shortcuts import render, redirect
from .form import MovieForm
from .models import Movies



def index(request):
    obj = Movies.objects.all()
    context = {
        'movie_list': obj
    }
    return render(request,'index.html',context)

def details(request, movie_id):
    movie_data = Movies.objects.get(id=movie_id)
    return render(request,'detail.html',{'movie_dict':movie_data})


def addition(request):
    if request.method == 'POST':
        movie_name =  request.POST.get('name')
        movie_desc =  request.POST.get('desc')
        movie_year =  request.POST.get('year')
        movie_img =  request.FILES['img']
        movies_lists = Movies(name = movie_name, desc = movie_desc, year = movie_year, img = movie_img)
        movies_lists.save()
        return redirect('/')
    return render(request,'add.html')

def update(request,id):
    movie = Movies.objects.get(id = id)
    form = MovieForm(request.POST or None, request.FILES, instance = movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'movie':movie, 'form':form})

def delete(request, id):
    if request.method == 'POST':
        movie = Movies.objects.get(id = id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')