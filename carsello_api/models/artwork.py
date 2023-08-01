from django.db import models
import json


class Artwork(models.Model):
    title = models.CharField(max_length=50)
    primary_image = models.URLField()
    year = models.PositiveIntegerField(null=False)
    price = models.PositiveIntegerField()
    sold = models.BooleanField(default=False)
    quantity = models.PositiveIntegerField(default=1)
    dimensions = models.CharField(max_length=50, null=True)
    support_images = models.TextField(blank=True, null=True)

# added support images and defs. and changed image field name to primary_image
def get_support_images_list(self):
    if self.support_images:
        try:
            urls = json.loads(self.support_images)
            return [{url} for url in urls]
        except json.JSONDecodeError as e:
            print("JSON Decode Error:", e)
    return []


def set_support_images(self, images):
    self.support_images = json.dumps(images)
