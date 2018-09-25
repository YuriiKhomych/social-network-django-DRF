from rest_framework import serializers
from .models import Post


class AllPostSerializer(serializers.ModelSerializer):
    """Class based on Post model and
    describes the all fields from Post model.
    """
    class Meta:
        model = Post
        fields = ('post_body', 'author', 'liked_by', 'added')


class PostCreateSerializer(serializers.ModelSerializer):
    """Class based on Post model and describes the
    interface for creating new Post.
    User can write only post body,
    author and data will add automatically.
    """
    class Meta:
        model = Post
        fields = ('post_body')
