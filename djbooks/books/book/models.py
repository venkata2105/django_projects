from django.db import models


# Create your models here.

class Book_Model(models.Model):
    name = models.CharField(max_length=25)
    author = models.CharField(max_length=20)
    page_count = models.BigIntegerField()

    def __str__(self):
        return self.name

