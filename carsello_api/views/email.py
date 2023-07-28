from django.core.mail import send_mail
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

# send_mail(
# subject, REQUIRED
# message, REQUIRED
# from_email, 
# recipient_list,
# fail_silently=False, 
# auth_user=None, 
# auth_password=None, 
# connection=None,
# html_message=None)

@api_view(['POST'])
@permission_classes([AllowAny])
def send_email(request):
    liz = User.objects.get(pk=1)
    email = liz.email
    print(request)
    print(email)
    return Response(None, status=status.HTTP_204_NO_CONTENT)