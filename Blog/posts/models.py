from email.policy import default
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from taggit.managers import TaggableManager
from django.contrib.auth.models import User


class Post(models.Model):

    STATUS_CHOICE = (
        ('DRAFT', 'Draft'),
        ('PUBLISHED', 'Published')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    title = models.CharField(max_length=50)
    text_field = models.TextField()
    slug = models.SlugField(max_length=250, default='')
    status = models.CharField(max_length=50, choices=STATUS_CHOICE)
    tags = TaggableManager(blank=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
           return reverse('post_details',
                          args=[self.pk])

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    text_input = models.TextField()
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)


    def __str__(self):
        return f"Comment made by {self.name} on {self.post}."