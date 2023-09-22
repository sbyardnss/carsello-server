from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from carsello_api.permission import AllowSafe
from carsello_api.models import Artwork
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import AllowAny


class ArtworkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artwork
        fields = ('id', 'title', 'price', 'primary_image', 'year',
                  'support_images', 'dimensions', 'quantity', 'sort_index', 'range')


class CreateArtworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artwork
        fields = ['id', 'title', 'price', 'primary_image',
                  'year', 'support_images', 'dimensions', 'quantity', 'range']


class ArtworkView(ViewSet):
    """handles requests for Artwork"""
    permission_classes = [AllowSafe]

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
        self.check_object_permissions(request, serialized)
        serialized.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        art = Artwork.objects.get(pk=pk)
        art.title = request.data['title']
        art.year = request.data['year']
        art.price = request.data['price']
        art.primary_image = request.data['primary_image']
        art.support_images = request.data['support_images']
        art.quantity = request.data['quantity']
        art.range = request.data['range']
        self.check_object_permissions(request, art)
        # art.sort_index = request.data['sort_index']
        art.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        art = Artwork.objects.get(pk=pk)
        self.check_object_permissions(request, art)
        art.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    @action(methods=['put'], detail=False)
    def save_new_order(self, request):
        for art_id in request.data:
            art = Artwork.objects.get(pk=art_id)
            art.sort_index = request.data[art_id]
            self.check_object_permissions(request, art)
            art.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    # @permission_classes([AllowAny])
    # @action(methods=['put'], detail=True)
    # def set_sold(self, request, pk=None):
    #     art = Artwork.objects.get(pk=pk)
    #     art.sold = True
    #     art.save()
    #     return Response(None, status=status.HTTP_204_NO_CONTENT)

    # @permission_classes([AllowAny])
    @action(methods=['put'], detail=True)
    def quantity_decrement(self, request, pk=None):
        art = Artwork.objects.get(pk=pk)
        new_quantity = art.quantity-1
        art.quantity = new_quantity
        art.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
