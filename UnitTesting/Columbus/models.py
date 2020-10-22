from django.db import models

# Create your models here.
class Name(models.Model):
    name=models.CharField(max_length=20)
    completed=models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def mark_completed(self):
        self.completed=True
        try:
            self.save()
        except:
            return False

        return True