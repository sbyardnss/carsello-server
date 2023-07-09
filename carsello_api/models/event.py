from django.db import models
from django.utils.timezone import now


class Event(models.Model):
    title = models.CharField(max_length=50, null=False)
    location = models.CharField(max_length=100, null=False)
    # date = models.DateField(null=False, auto_now=False,
    #                         auto_now_add=False, default=date.today)
    # time = models.TimeField(null=False, auto_now=False,
    #                         auto_now_add=False, default=now)
    date_time = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, default=now)
    image = models.URLField(null=True)
    link = models.URLField(null=True)
    details = models.CharField(null=True, max_length=200)
    price = models.FloatField(null=True)

