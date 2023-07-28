from django.db import models


class Order(models.Model):
    buyer = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    total = models.PositiveIntegerField(null=False)
    date_time = models.DateTimeField(auto_now_add=True)
    item = models.ForeignKey('Artwork', on_delete=models.DO_NOTHING)
    paypal_order_id = models.CharField(max_length=75)
    
# ordered_item (fk)

# paypal_id charfield
# create_time charfield
# customer_id charfield
# customer_email charfield
# customer_name charfield
# order_amount positiveInteger
# payment_id charfield?
# payment_status charfield
# payment_protection charfield
# payment_status charfield
# reference_id charfield
# shipping_street_address charfield
# shipping_city char
# shipping_state char
# shipping_country char
# shipping_zipcode char
# order_status char
