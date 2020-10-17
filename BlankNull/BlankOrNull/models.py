from django.db import models

# Create your models here.

class Book(models.Model):
    name=models.CharField(max_length=20)
    author=models.CharField(max_length=20)
    about=models.TextField(blank=True)
    publish_date=models.DateField(null=True,blank=True)

    def __str__(self):
        return self.name