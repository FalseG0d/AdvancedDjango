from django.db import models

# Create your models here.
class ComputerManager(models.Manager):
    def gaming(self):
        return self.filter(type_of='gaming')

    def beginner_ram(self, ram_size):
        return self.filter(ram_size=ram_size)

class Computer(models.Model):
    name = models.CharField(max_length=30)
    ram_size = models.PositiveIntegerField(default=0)
    type_of = models.CharField(max_length=10, blank=True)

    objects = ComputerManager()

    def __str__(self):
        return self.name