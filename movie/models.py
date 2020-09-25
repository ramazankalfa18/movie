from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils.text import slugify



class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Movie(models.Model):
    movie_name = models.CharField ( max_length = 150,verbose_name='Film ismi',null=True)
    movie_content=RichTextField ( max_length = 2000,verbose_name='Film açıklama ',null=True)
    release_date = models.DateField(verbose_name='Film çıkış tarihi',null=True)
    imdb_reyting = models.CharField(max_length=10,null=True)
    image = models.ImageField(null=True,verbose_name='Fotoğraf',upload_to='static/images')
    publishing_date = models.DateTimeField(auto_now_add=True,verbose_name='Oluşturma tarihi',null=True)
    created = models.BooleanField(null=True, default=True,verbose_name='Film yayındamı')
    runtime = models.CharField (max_length = 50 , verbose_name='film Süresi', null=True)
    category = models.ManyToManyField('Category',verbose_name='Kategori',related_name='Movie')
    slug = models.SlugField(max_length=100,unique=True,null=False)
    url = models.CharField(max_length=1000 ,null=True, verbose_name="Film Url")
    actor = models.ManyToManyField('Actor',verbose_name='actor',related_name='Movie')

    def __str__(self):
        return self.movie_name

    def get_image_path(self):
        return self.image
    class Meta:
        verbose_name = 'Film'
        verbose_name_plural = 'Filmler'


class Actor(models.Model):
    actor_name = models.CharField( max_length=150 , verbose_name='Aktör Adı', null=True)
    position = models.CharField(max_length=150 , verbose_name='Director/Producer/Writer/Actor and Actress', null=True)
    country = models.CharField(max_length=150 , verbose_name='Ülke :', null=True)
    actor_image = models.ImageField(null=True, verbose_name='Aktör Fotoğrafı',upload_to='static/images/Actor')
    dateofbirth = models.DateField(verbose_name='Doğum tarihi :', null=True)
    biography = RichTextField(max_length = 20000,verbose_name='Biyografi ',null=True)

    def get_image_path(self):
        return self.actor_image

    def __str__(self):
        return self.actor_name

    class Meta:
        verbose_name = 'Actor'


