from django.db import models

# Create your models here.
class Order(models.Model):
    customer_name=models.CharField(max_length=20)
    item=models.CharField(max_length=30,null=True)
    price=models.FloatField(null=True)

    def __str__(self):
        return self.item