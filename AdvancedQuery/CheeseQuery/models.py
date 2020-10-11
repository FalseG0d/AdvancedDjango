from django.db import models

# Create your models here.

class Place(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Cheese(models.Model):
    name=models.CharField(max_length=20)
    quality=models.IntegerField(default=5)
    place=models.ForeignKey(Place,on_delete=models.CASCADE)

    def __str__(self):
        return self.name