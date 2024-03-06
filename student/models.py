from django.db import models

# Create your models here.


class Student_data(models.Model):
    name = models.CharField(max_length=20)
    branch = models.CharField(max_length=20)
    roll_no = models.IntegerField()

    def __str__(self):
        return self.name


class top_marks(models.Model):
    name = models.ForeignKey(Student_data, on_delete=models.CASCADE)
    marks = models.IntegerField()
    
    def __str__(self):
        return self.name

