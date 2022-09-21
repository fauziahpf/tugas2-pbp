from django.db import models

# Create models here.
class MyWatchlist(models.Model):
    watched = models.CharField(max_length=15)
    title = models.CharField(max_length=30)
    rating = models.IntegerField()
    release_date = models.DateField()
    review = models.TextField()