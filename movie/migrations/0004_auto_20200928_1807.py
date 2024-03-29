# Generated by Django 2.2.12 on 2020-09-28 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20200925_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='Fragment',
            field=models.CharField(max_length=1000, null=True, verbose_name='Film Fragmanı'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='actor_image',
            field=models.ImageField(null=True, upload_to='', verbose_name='Aktör Fotoğrafı'),
        ),
    ]
