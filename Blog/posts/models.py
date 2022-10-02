from django.db import models
from django.conf import settings

class Post(models.Model):

    STATUS_CHOICE = (
        ('DRAFT', 'Draft'),
        ('PUBLISHED', 'Published')
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    title = models.CharField(max_length=50)
    text_field = models.TextField()
    status = models.CharField(choice=STATUS_CHOICE)