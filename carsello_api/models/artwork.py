from django.db import models


class Artwork(models.Model):
    title = models.CharField(max_length=50)
    image = models.URLField()
    year = models.PositiveIntegerField(null=False)
    price = models.PositiveIntegerField()
