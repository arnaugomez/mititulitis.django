from rest_framework import generics
from .models import Tag
from .serializers import TagSerializer


class CreateTag(generics.CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class GetTag(generics.RetrieveAPIView):
    lookup_field = "slug"
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class GetTagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class UpdateTag(generics.UpdateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class DeleteTag(generics.DestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
