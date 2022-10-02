from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_posts, name='get_posts' ),
]