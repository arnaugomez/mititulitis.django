from rest_framework import serializers
from .models import Post, Like, Comment


class PostSerializer(serializers.ModelSerializer):
    likes_amount = serializers.SerializerMethodField(read_only=True)

    def get_likes_amount(self, post):
        return post.likes.count()

    class Meta:
        model = Post
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
