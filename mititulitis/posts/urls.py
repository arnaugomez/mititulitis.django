from django.urls import path
from .views.post_views import GetLatestPosts, CreatePost, GetPost, GetPostsOfUser, UpdatePost, DeletePost, \
    GetPostsLikedByUser
from .views.like_views import CreateLike, DeleteLike
from .views import comment_views

POSTS_BASE_URL = "posts/"
LIKES_BASE_URL = "likes/"
COMMENTS_BASE_URL = "comments/"

urlpatterns = [
    # Posts
    path(POSTS_BASE_URL + "latest/", GetLatestPosts.as_view()),
    path(POSTS_BASE_URL + "get/slug/<slug:slug>/", GetPost.as_view()),
    path(POSTS_BASE_URL + "get/author/<int:pk>/", GetPostsOfUser.as_view()),
    path(POSTS_BASE_URL + "get/liked-by/<int:pk>/", GetPostsLikedByUser.as_view()),
    path(POSTS_BASE_URL + "create/", CreatePost.as_view()),
    path(POSTS_BASE_URL + "update/<int:pk>/", UpdatePost.as_view()),
    path(POSTS_BASE_URL + "delete/<int:pk>/", DeletePost.as_view()),
    # Likes
    path(LIKES_BASE_URL + "create/", CreateLike.as_view()),
    path(LIKES_BASE_URL + "delete/<int:pk>/", DeleteLike.as_view()),
    # Comments
    path(COMMENTS_BASE_URL + "create/", comment_views.CreateComment.as_view()),
    path(COMMENTS_BASE_URL + "get/post/<int:pk>/", comment_views.GetCommentsOfPost.as_view()),
    path(COMMENTS_BASE_URL + "get/comment/<int:pk>/", comment_views.GetCommentsOfPost.as_view()),
    path(COMMENTS_BASE_URL + "get/user/<int:pk>/", comment_views.GetCommentsOfUser.as_view()),
    path(COMMENTS_BASE_URL + "get/user/<int:pk>/", comment_views.GetCommentsOfUser.as_view()),
    path(COMMENTS_BASE_URL + "update/<int:pk>", comment_views.UpdateComment.as_view()),
    path(COMMENTS_BASE_URL + "delete/<int:pk>", comment_views.DeleteComment.as_view()),
]
