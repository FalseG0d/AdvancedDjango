from django.db import models

# Create your models here.
class Record(models.Model):
    name=models.CharField(max_length=20)
    text=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return "/records/%i/" % self.id