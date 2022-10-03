from django.urls import path
from .views import PostView

urlpatterns = [
    path('', PostView.as_view(), name='get_posts' ),
]