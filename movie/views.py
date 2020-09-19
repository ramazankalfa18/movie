from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.contrib import admin
from .models import *
from django.utils.text import slugify
from django.db.models import Q

def index(request):
    movies = Movie.objects.all().order_by("-id")
    categories = list(Category.objects.filter(~Q(name='Youtube')))
    sayac = 0
    categoriess = []
    for i in categories:
        sayac = sayac + 1
        film = Movie.objects.filter(category=i)
        if film:
            categoriess.append(categories[sayac-1])


    movies.slug=slugify(movies)
    context ={
        'movies':movies,
        'categories': categoriess
    }
    return render(request, 'index.html',context)

def CategorySearch(request, id):
    category = Category.objects.get(id=id)
    print("id----->", category)
    movie_list = Movie.objects.filter(category__id__in=[id])
    print ("list-->", movie_list)
    context={
        'category':category,
        'movie_list': movie_list

    }
    return render(request, 'CategoryDetail.html', context)

def MovieShow(request,id):
    print("buraya geldi ıd si ----> ",id)
    movie_show = Movie.objects.get(id=id)
    print(movie_show.image)
    context = {
        'movie_show': movie_show
    }

    return render(request, "moviesingle.html",context)