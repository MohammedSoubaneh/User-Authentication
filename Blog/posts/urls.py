from django.urls import path
from .views import PostView, PostDetailView, SharePost

urlpatterns = [
    path('', PostView.as_view(), name='get_posts' ),
    path('details/<int:pk>/', PostDetailView.as_view(), name='post_details'),
    path('share/<int:pk>/', SharePost.as_view(), name='share'),
]