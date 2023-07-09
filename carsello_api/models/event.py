from datetime import date
from django.db import models
from django.utils.timezone import now


class Event(models.Model):
    title = models.CharField(max_length=50, null=False)
    location = models.CharField(max_length=100, null=False)
    date = models.DateField(null=False, auto_now=False,
                            auto_now_add=False, default=date.today)
    time = models.TimeField(null=False, auto_now=False,
                            auto_now_add=False, default=now)
    image = models.URLField(null=True)
    link = models.URLField(null=True)

