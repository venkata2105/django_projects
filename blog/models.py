from typing import Any
from django.db import models


class User(models.Model):
    """User model for storing user information."""
    username: str = models.CharField(max_length=10)
    email: str = models.EmailField()
    password: str = models.CharField(max_length=10)

    def __str__(self) -> str:
        """String representation of the User model."""
        return self.username


class Post(models.Model):
    """Post model for storing blog post information."""
    title: str = models.CharField(max_length=25)
    content_post: str = models.TextField()
    author: User = models.ForeignKey(User, on_delete=models.CASCADE)
    category: str = models.CharField(max_length=10)
    created_date: Any = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """String representation of the Post model."""
        return self.title


class Comment(models.Model):
    """Comment model for storing comments on blog posts."""
    post: Post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author: User = models.ForeignKey(User, on_delete=models.CASCADE)
    content: str = models.TextField()
    created_date: Any = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        """String representation of the Comment model."""
        return f"{self.author} commented: {self.content}"
