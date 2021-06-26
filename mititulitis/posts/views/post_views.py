from rest_framework import generics, authentication, permissions
from django.contrib.auth.models import User
from ..models import Post
from ..serializers import PostSerializer


class CreatePost(generics.CreateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class GetLatestPosts(generics.ListAPIView):
    queryset = Post.objects.order_by('-created')
    serializer_class = PostSerializer


class GetPost(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "slug"


class GetPostsByUser(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        user = User.objects.get(id=self.kwargs.get("pk", -1))
        return user.posts.all()


class GetPostsLikedByUser(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        user = User.objects.get(id=self.kwargs.get("pk", -1))
        return Post.objects.filter(likes__user=user)


class UpdatePost(generics.UpdateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class DeletePost(generics.DestroyAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
