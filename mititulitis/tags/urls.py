from django.urls import path
from .views import CreateTag, UpdateTag, DeleteTag, GetTagList, GetTag

BASE_PATH = "tags/"

urlpatterns = [
    path(BASE_PATH + "create/", CreateTag.as_view()),
    path(BASE_PATH + "get/<int:pk>/", GetTag.as_view()),
    path(BASE_PATH, GetTagList.as_view()),
    path(BASE_PATH + "update/<int:pk>/", UpdateTag.as_view()),
    path(BASE_PATH + "delete/<int:pk>/", DeleteTag.as_view()),
]
