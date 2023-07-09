from django.db import models


class Artwork(models.Model):
    title = models.CharField(max_length=50)
    image = models.URLField()
    date = models.DateField(null=False)
    price = models.IntegerField()
