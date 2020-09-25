from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.contrib import admin
from .models import *
from django.utils.text import slugify
from django.db.models import Q


def actor(args):
    pass


def Actors(request):
    actor = Actor.objects.all()
    for i in actor:
        print(i.actor_image)
    context = {
        'actor': actor,
        'categories': categorifill(),

    }

    return render(request , 'actor.html', context)
def actordetail(request, id):
    actor_show = Actor.objects.get(id=id)
    context = {
        'actor_show': actor_show,
        'categories': categorifill(),

    }
    return render(request, 'actordetail.html', context)


def categorifill():
    categories = list(Category.objects.filter(~Q(name='Youtube')))

    sayac = 0
    new_movie = []
    for i in categories:
        sayac = sayac + 1
        film = Movie.objects.filter(category=i)
        if film:
            new_movie.append(categories[sayac - 1])

    return new_movie

def index(request):
    movies = Movie.objects.all().order_by("-id")
    movies.slug = slugify(movies)
    context ={
        'movies': movies,
        'categories': categorifill(),

    }
    return render(request, 'index.html',context)

def CategorySearch(request, id):
    category = Category.objects.get(id=id)
    movie_list = Movie.objects.filter(category__id__in=[id])

    print ("list-->", movie_list)
    categoriess = kategoridoldur()
    context={
        'category':category,
        'movie_list': movie_list,
        'categories':categoriess

    }
    return render(request, 'CategoryDetail.html', context)

def MovieShow(request,id):
    movie_show = Movie.objects.get(id=id)
    imbd = range(round(float(movie_show.imdb_reyting)))
    imbd_kalan = (10-(int(round(float(movie_show.imdb_reyting)))))
    context = {
        'movie_show': movie_show,
        'imbd': imbd,
        'imbd_kalan': range(imbd_kalan),
        'categories': categorifill(),


    }
    return render(request, "moviesingle.html", context)
