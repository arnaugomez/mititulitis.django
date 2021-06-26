from django.urls import path
from .views.post_views import GetLatestPosts, CreatePost, GetPost, GetPostsByUser, UpdatePost, DeletePost, \
    GetPostsLikedByUser
from .views.like_views import CreateLike, DeleteLike

POSTS_BASE_URL = "posts/"
LIKES_BASE_URL = "likes/"

urlpatterns = [
    # Posts
    path(POSTS_BASE_URL + "latest/", GetLatestPosts.as_view()),
    path(POSTS_BASE_URL + "get/slug/<slug:slug>", GetPost.as_view()),
    path(POSTS_BASE_URL + "get/author/<int:pk>", GetPostsByUser.as_view()),
    path(POSTS_BASE_URL + "get/liked-by/<int:pk>", GetPostsLikedByUser.as_view()),
    path(POSTS_BASE_URL + "create/", CreatePost.as_view()),
    path(POSTS_BASE_URL + "update/<int:pk>", UpdatePost.as_view()),
    path(POSTS_BASE_URL + "delete/<int:pk>", DeletePost.as_view()),
    # Likes
    path(LIKES_BASE_URL + "create/", CreateLike.as_view()),
    path(LIKES_BASE_URL + "delete/<int:pk>", DeleteLike.as_view())
    # Comments
]
