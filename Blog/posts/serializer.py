from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['user', 'title', 'text_field']

    def create(self, validated_data):
        return Post.objects.create(**validated_data)
