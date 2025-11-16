from django.db import models

# Create your models here.
class Platform(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)

    def __str__(self):
        return self.title