from rest_framework import generics, authentication, permissions
from django.contrib.auth.models import User
from .models import Profile
from .serializers import ProfileSerializer


class GetProfileOfUser(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        user = User.objects.get(id=self.kwargs.get("pk", -1))
        return Profile.objects.filter(user=user)


class UpdateProfile(generics.UpdateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
