from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    # There might be more types in the future
    POST_TYPES = (("TUTORIAL", "Tutorial"), ("QUESTION", "Question"), ("LINK", "Link"))

    title = models.CharField(max_length=200)
    slug = models.SlugField(verbose_name="Slug (title of the post in kebab-case)")
    link = models.URLField(max_length=200, blank=True)
    post_type = models.CharField(max_length=50, choices=POST_TYPES, verbose_name="Type of post")
    body = models.TextField(verbose_name="Main content (supports Markdown!)", blank=True)
    created = models.DateTimeField(auto_now_add=True)
    # img = models.ImageField()

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    tags = models.ManyToManyField(
        "tags.Tag",
        blank=True,
        related_name="posts",
    )
    remixed_from = models.ForeignKey(
        "Post", on_delete=models.SET_NULL, blank=True, null=True, related_name="remixes"
    )

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="likes")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"User {self.user.username} liked post \"{self.post.title}\""


class Comment(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(verbose_name="Main content (supports Markdown!)")
    created = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="comments")
    comment = models.ForeignKey(
        "Comment", on_delete=models.CASCADE, related_name="comments"
    )

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
