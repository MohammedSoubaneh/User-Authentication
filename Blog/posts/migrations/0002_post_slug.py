# Generated by Django 4.1.1 on 2022-10-03 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='', max_length=250, unique_for_date='publish'),
        ),
    ]