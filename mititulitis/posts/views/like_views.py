from rest_framework import generics
from rest_framework import authentication, permissions
from ..serializers import LikeSerializer
from ..models import Like


class CreateLike(generics.CreateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class DeleteLike(generics.DestroyAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


