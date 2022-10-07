from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializer import PostSerializer, CommentSerializer
from .models import Post, Comment
from taggit.models import Tag

class PostView(APIView):
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'text_field']
    

    def get(self, request, tag_slug=None, format=None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    

class PostDetailView(APIView):
    
    def get(self, request, pk, format=None):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data, status.HTTP_200_OK)
    
    def put(self, request, pk, format=None):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class SharePost(APIView):
    def post(self, request, pk, format=None):
        post = Post.objects.get(pk=pk)
        form = request.data
        subject = f"{form['name']} has recommended you {post.title}"
        message = f"Check out {post.title} at {post.get_absolute_url}"
        send_mail(subject, message, "example@example.com", [form['to']])
        return Response(subject, status.HTTP_200_OK) 


class CommentPost(APIView):

    def get(self, request, pk, format=None):
        post = get_object_or_404(Post, pk=pk)
        comment = Comment.objects.filter(post=post)
        comment.post = post
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request, pk, format=None):
        post = get_object_or_404(Post, pk=pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(post=post)
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class TagView(APIView):
    def get(self, request, tag_slug, format=None):
        tags = get_object_or_404(Tag, slug=tag_slug)
        posts = Post.objects.filter(tags=tags)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
