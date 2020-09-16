from django.db import models
from ckeditor.fields import RichTextField



class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Movie(models.Model):
    movie_name= models.CharField ( max_length = 150,verbose_name='Film ismi',null=True)
    movie_content=RichTextField ( max_length = 2000,verbose_name='Film açıklama ',null=True)
    release_date = models.DateField(verbose_name='Film çıkış tarihi',null=True)
    imdb_reyting = models.CharField(max_length=10,null=True)
    image = models.ImageField(null=True,verbose_name='Fotoğraf',upload_to='static/images')
    publishing_date = models.DateTimeField(auto_now_add=True,verbose_name='Oluşturma tarihi',null=True)
    created = models.BooleanField(null=True, default=True,verbose_name='Film yayındamı')
    runtime = models.CharField (max_length = 50 , verbose_name='film Süresi', null=True)
    Category = models.ManyToManyField('Category',verbose_name='Kategori',related_name='Movie')
   
    def __str__(self):
        return self.movie_name

    def get_image_path(self):
        return self.image
    
    class Meta:
        verbose_name = 'Film'
        verbose_name_plural = 'Filmler'

