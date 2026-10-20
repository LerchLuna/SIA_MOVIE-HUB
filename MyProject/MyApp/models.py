from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    release_year = models.IntegerField()
    status = models.CharField(max_length=100)
    rating = models.IntegerField()
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.title

