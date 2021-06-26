from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import authentication, permissions

from ..models import Comment, Post
from ..serializers import CommentSerializer


class CreateComment(generics.CreateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class GetCommentsOfPost(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post = Post.objects.get(id=self.kwargs.get("pk", -1))
        return post.comments.all()


class GetCommentsOfComment(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        comment = Comment.objects.get(id=self.kwargs.get("pk", -1))
        return comment.comments.all()


class GetCommentsOfUser(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        comment = User.objects.get(id=self.kwargs.get("pk", -1))
        return comment.comments.all()


class UpdateComment(generics.UpdateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class DeleteComment(generics.DestroyAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
