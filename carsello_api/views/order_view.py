from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from carsello_api.models import Order
from rest_framework.decorators import action

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', "ordered_item", "created", "customer_email", "customer_name", "customer_paypal_id", "order_amount", "order_status", "payment_id", "payment_protection", "payment_status",
                  "paypal_order_id", "reference_id", "shipping_city", "shipping_country_code", "shipping_state", "shipping_street_address", "shipping_zipcode", "order_status")


class CreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', "ordered_item", "created", "customer_email", "customer_name", "customer_paypal_id", "order_amount", "order_status", "payment_id", "payment_protection", "payment_status",
                  "paypal_order_id", "reference_id", "shipping_city", "shipping_country_code", "shipping_state", "shipping_street_address", "shipping_zipcode", "order_status", "shipped")


class OrderView(ViewSet):
    def list(self, request):
        orders = Order.objects.all()
        serialized = OrderSerializer(orders, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    def create(self, request):
        serialized = OrderSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)
        serialized.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        order = Order.objects.get(pk=pk)
        order.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    @action(methods=["PUT"], detail=True)
    def mark_shipped(self, request, pk=None):
        order = Order.objects.get(pk=pk)
        order.shipped = True
        order.save()