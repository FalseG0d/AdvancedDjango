from __future__ import unicode_literals

from django.db import models


class Comment(models.Model):
    name=models.CharField(max_length=20)
    company=models.CharField(max_length=20)
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

    def __str__(self):
        return self.name