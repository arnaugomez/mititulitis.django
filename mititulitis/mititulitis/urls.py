from django.contrib import admin
from django.urls import path, include

api_version = "api/v1/"

urlpatterns = [
    path("admin/", admin.site.urls),
    path(api_version, include("users.urls")),
    path(api_version, include("posts.urls")),
    path(api_version, include("tags.urls")),
]
