from django.db import models


class Order(models.Model):
    buyer = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    total = models.PositiveIntegerField(null=False)
    date_time = models.DateTimeField(auto_now_add=True)
    item = models.ForeignKey('Artwork', on_delete=models.DO_NOTHING)
    paypal_order_id = models.CharField(max_length=75)
    
