# Generated by Django 4.1.1 on 2022-10-07 00:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_post_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
    ]
