from django.db import models
#from django.contrib.auth.models import User


class User(models.Model):
    username = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.username

'''Post: Fields for title, content, author, category, created_date.
● Comment: Fields for post, author, content, created_date.
'''


class Post(models.Model):
    title = models.CharField(max_length=25, name="TITLE")
    content_post = models.TextField(name='CONTENT')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=10, name='CATEGORY')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.TITLE


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, name="AUTHOR")
    content = models.TextField(name='CONTENT')
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.AUTHOR} commented {self.CONTENT}"

