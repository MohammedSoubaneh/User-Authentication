from django.urls import path
from .views import CommentPost,TagView,RecentPostView, PostView, PostDetailView, SharePost

urlpatterns = [
    path('', PostView.as_view(), name='get_posts' ),
    path('tag/<slug:tag_slug>/', TagView.as_view(), name='post_list_by_tag'),
    path('details/<int:pk>/', PostDetailView.as_view(), name='post_details'),
    path('share/<int:pk>/', SharePost.as_view(), name='share'),
    path('comment/<int:pk>/', CommentPost.as_view(), name='comment'),
    path('recent-posts', RecentPostView.as_view(), name='recent-posts'),
]