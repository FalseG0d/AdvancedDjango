from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField(max_length=20)
    dept=models.CharField(max_length=20)
    exp_score=models.IntegerField()

    def __str__(self):
        return self.name