from email.policy import default
from django.db import models
from django.utils import timezone
from django.conf import settings


class Post(models.Model):

    STATUS_CHOICE = (
        ('DRAFT', 'Draft'),
        ('PUBLISHED', 'Published')
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    title = models.CharField(max_length=50)
    text_field = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='publish', default='')
    status = models.CharField(max_length=50, choices=STATUS_CHOICE)
    
    def __str__(self):
        return self.title