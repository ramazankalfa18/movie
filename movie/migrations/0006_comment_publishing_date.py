# Generated by Django 2.2.12 on 2020-09-28 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='publishing_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Oluşturma tarihi'),
        ),
    ]