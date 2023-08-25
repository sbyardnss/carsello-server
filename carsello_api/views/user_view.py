from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


# user = User.objects.get(pk=1)
# user.set_password('lc')
# user.save()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'password', 'username')

class UserView(ViewSet):
    def update(self, request, pk=None):
        username = request.data['confirmUsername']
        # password = request.data['confirmPassword']
        user = User.objects.get(pk=pk)
        print(user.password)
        # authenticated_user = authenticate(username=username, password=password)
        # If authentication was successful, respond with their token
        # if user is not None:
            # user = User.objects.get(user=authenticated_user)
        user.username = request.data['username']
        user.set_password = request.data['password']
        user.first_name = request.data['firstName']
        user.last_name = request.data['lastName']
        user.save()
        serialized = UserSerializer(user, many=False)
        return Response(serialized.data, status=status.HTTP_204_NO_CONTENT)
        # else:
        #     # Bad login details were provided. So we can't log the user in.
        #     data = {'msg': "incorrect credentials"}
        #     return Response(data, status=status.HTTP_400_BAD_REQUEST)
    def list(self, request):
        users =User.objects.all()
        serialized = UserSerializer(users, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

