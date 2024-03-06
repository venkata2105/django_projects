<<<<<<< HEAD
from django.db import models


# Create your models here.

class Book_Model(models.Model):
    name = models.CharField(max_length=25)
    author = models.CharField(max_length=20)
    page_count = models.BigIntegerField()

    def __str__(self):
        return self.name

=======
from django.db import models


# Create your models here.

class Book_Model(models.Model):
    name = models.CharField(max_length=25)
    author = models.CharField(max_length=20)
    page_count = models.BigIntegerField()

    def __str__(self):
        return self.name

>>>>>>> 1d221d9c65af698a7761a514f421d3a52566b2c1
