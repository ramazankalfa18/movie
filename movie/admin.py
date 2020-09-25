from django.contrib import admin
from .models import Category
from .models import *


class Movieadmin(admin.ModelAdmin):
    list_display = ['movie_name','publishing_date' ,'image','created']
    list_display_links = ['publishing_date']
    list_filter = ['publishing_date']
    search_fields = ['movie_name', 'movie_content']
    prepopulated_fields = {'slug': ('movie_name',)}

class Actoradmin(admin.ModelAdmin):
        list_display = ['actor_name', 'dateofbirth', 'actor_image']

admin.site.register(Movie,Movieadmin)
admin.site.register(Category)
admin.site.register(Actor,Actoradmin)

