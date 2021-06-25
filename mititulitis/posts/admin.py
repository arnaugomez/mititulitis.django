from django.contrib import admin
from .models import Post, Like, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "post_type", "remixed_from")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("created",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("title", "created")
