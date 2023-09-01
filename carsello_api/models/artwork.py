from django.db import models
import json
import ast



class Artwork(models.Model):
    title = models.CharField(max_length=50)
    primary_image = models.URLField()
    year = models.PositiveIntegerField(null=False)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default=1)
    dimensions = models.CharField(max_length=50, null=True)
    support_images = models.JSONField(blank=True, null=True)
    sort_index = models.PositiveIntegerField(blank=True, null=True, default=None)
    range = models.PositiveIntegerField(blank=True, null=True)
    class Meta:
        permissions = (("quantity_decrement", "can decrease quantity of product after purchase"),)
