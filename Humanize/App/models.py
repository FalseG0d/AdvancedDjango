from django.db import models

# Create your models here.
class Record(models.Model):
    apnumber=models.IntegerField()
    intcomma=models.IntegerField()
    intword=models.IntegerField()
    naturalday=models.DateField()
    naturaltime=models.DateTimeField()
    ordinal=models.IntegerField()