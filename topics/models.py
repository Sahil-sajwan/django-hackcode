from django.db import models

class Topic(models.Model):
    title=models.CharField(max_length=100)
    detail=models.TextField()

    def __str__(self):
        return self.title
