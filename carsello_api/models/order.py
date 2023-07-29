from django.db import models


class Order(models.Model):
    ordered_item = models.ForeignKey('Artwork', null=True, on_delete=models.SET_NULL, related_name='sold_art')
    paypal_order_id = models.CharField(max_length=75)
    created = models.CharField(max_length=75)
    customer_paypal_id = models.CharField(max_length=50)
    customer_email = models.CharField(max_length=75)
    customer_name = models.CharField(max_length=50)
    order_amount = models.PositiveIntegerField(null=False)
    payment_id = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=25)
    payment_protection = models.CharField(max_length=25)
    reference_id = models.CharField(max_length=50)
    shipping_street_address = models.CharField(max_length=75)
    shipping_city = models.CharField(max_length=25)
    shipping_state = models.CharField(max_length=10)
    shipping_country_code = models.CharField(max_length=10)
    shipping_zipcode = models.CharField(max_length=25)
    order_status = models.CharField(max_length=25)

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
