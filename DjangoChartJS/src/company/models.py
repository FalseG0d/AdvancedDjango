from django.db import models

# Create your models here.
class Company(models.Model):
    name=models.CharField(max_length=20)
    profit=models.FloatField()

    def __str__(self):
        return "{} with {}".format(self.name,self.profit)