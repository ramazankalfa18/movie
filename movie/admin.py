from django.contrib import admin
from .models import Category
from .models import *


class Movieadmin(admin.ModelAdmin):
    list_display = ['movie_name','publishing_date' ,'image','created']
    list_display_links = ['publishing_date']
    list_filter = ['publishing_date']
    search_fields = ['movie_name', 'movie_content']


admin.site.register(Movie,Movieadmin)
admin.site.register(Category)
