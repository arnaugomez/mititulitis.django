from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    name = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    is_premium = models.BooleanField(default=False)
    # img = models.ImageField()

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    interests = models.ManyToManyField("tags.Tag", related_name="profiles")

    def __str__(self):
        return self.name
