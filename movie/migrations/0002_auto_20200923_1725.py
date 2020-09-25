# Generated by Django 2.2.12 on 2020-09-23 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actor',
            old_name='Biography',
            new_name='biography',
        ),
        migrations.AlterField(
            model_name='actor',
            name='actor_image',
            field=models.ImageField(null=True, upload_to='static/images/actor', verbose_name='Aktör Fotoğrafı'),
        ),
    ]