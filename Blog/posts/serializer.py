from rest_framework import serializers
from .models import Post, Comment
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    class Meta:
        model = Post
        fields = ['user', 'title', 'text_field', 'tags']

    def create(self, validated_data):
        return Post.objects.create(**validated_data)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['name', 'text_input', 'email', 'post']

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)
