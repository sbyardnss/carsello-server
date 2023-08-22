from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from carsello_api.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'location', 'image', 'date', 'time', 'link', 'details', 'price')


class CreateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'location', 'image', 'date', 'time', 'link', 'details', 'price']


class EventView(ViewSet):
    """handles requests for Event"""

    def list(self, request):
        events = Event.objects.all()
        serialized = EventSerializer(events, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        event = Event.objects.get(pk=pk)
        serialized = EventSerializer(event, many=False)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def create(self, request):
        serialized = CreateEventSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)
        serialized.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        event = Event.objects.get(pk=pk)
        event.title = request.data['title']
        event.time = request.data['time']
        event.date = request.data['date']
        event.location = request.data['location']
        event.image = request.data['image']
        event.link = request.data['link']
        event.details = request.data['details']
        event.price = request.data['price']
        event.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        event = Event.objects.get(pk=pk)
        event.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)