from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from carsello_api.models import Artwork


class ArtworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artwork
        fields = ('id', 'title', 'price', 'image', 'year')


class CreateArtworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artwork
        fields = ['id', 'title', 'price', 'image', 'year']


class ArtworkView(ViewSet):
    """handles requests for Artwork"""

    def list(self, request):
        art = Artwork.objects.all()
        serialized = ArtworkSerializer(art, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        art = Artwork.objects.get(pk=pk)
        serialized = ArtworkSerializer(art, many=False)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def create(self, request):
        serialized = CreateArtworkSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)
        serialized.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        art = Artwork.objects.get(pk=pk)
        art.title = request.data['title']
        art.year = request.data['year']
        art.price = request.data['price']
        art.image = request.data['image']
        art.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        art = Artwork.objects.get(pk=pk)
        art.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)