# Generated by Django 2.2.12 on 2020-09-23 09:57

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor_name', models.CharField(max_length=150, null=True, verbose_name='Aktör Adı')),
                ('position', models.CharField(max_length=150, null=True, verbose_name='Director/Producer/Writer/Actor and Actress')),
                ('country', models.CharField(max_length=150, null=True, verbose_name='Ülke :')),
                ('actor_image', models.ImageField(null=True, upload_to='', verbose_name='Aktör Fotoğrafı')),
                ('dateofbirth', models.DateField(null=True, verbose_name='Doğum tarihi :')),
                ('Biography', ckeditor.fields.RichTextField(max_length=20000, null=True, verbose_name='Biyografi ')),
            ],
            options={
                'verbose_name': 'Actor',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=150, null=True, verbose_name='Film ismi')),
                ('movie_content', ckeditor.fields.RichTextField(max_length=2000, null=True, verbose_name='Film açıklama ')),
                ('release_date', models.DateField(null=True, verbose_name='Film çıkış tarihi')),
                ('imdb_reyting', models.CharField(max_length=10, null=True)),
                ('image', models.ImageField(null=True, upload_to='static/images', verbose_name='Fotoğraf')),
                ('publishing_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Oluşturma tarihi')),
                ('created', models.BooleanField(default=True, null=True, verbose_name='Film yayındamı')),
                ('runtime', models.CharField(max_length=50, null=True, verbose_name='film Süresi')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('url', models.CharField(max_length=1000, null=True, verbose_name='Film Url')),
                ('actor', models.ManyToManyField(related_name='Movie', to='movie.Actor', verbose_name='actor')),
                ('category', models.ManyToManyField(related_name='Movie', to='movie.Category', verbose_name='Kategori')),
            ],
            options={
                'verbose_name': 'Film',
                'verbose_name_plural': 'Filmler',
            },
        ),
    ]
