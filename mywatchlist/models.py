from django.db import models

# Create models here.
class MyWatchlist(models.Model):
    watched = models.TextField()
    title = models.CharField(max_length=30)
    rating = models.IntegerField()
    release_date = models.CharField(max_length=18)
    review = models.TextField()