from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class UserView(ViewSet):
    def update(self, request):
        username = request.data['confirmUsername']
        password = request.data['confirmPassword']
        authenticated_user = authenticate(username=username, password=password)
        # If authentication was successful, respond with their token
        if authenticated_user is not None:
            user = User.objects.get(user=authenticated_user)
            user.username = request.data['username']
            user.password = request.data['password']
            user.first_name = request.data['firstName']
            user.last_name = request.data['lastName']
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        else:
            # Bad login details were provided. So we can't log the user in.
            data = {'msg': "incorrect credentials"}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
