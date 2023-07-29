from django.core.mail import send_mail, EmailMessage
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import threading

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

# MY ATTEMPT
# @api_view(['POST'])
# @permission_classes([AllowAny])
# def send_email(request):
#     liz = User.objects.get(pk=1)
#     email = liz.email
#     message1 = (
#         request.data['subject'],
#         request.data['message'],
#         "sjbyard91@gmail.com",
#         ["sjbyard91@gmail.com"]
#     )
#     if request.data['subject'] is not None and request.data['message'] is not None:
#         send_mail(request.data['subject'], request.data['message'],
#                   "sjbyard91@gmail.com", ["sjbyard91@gmail.com"])
#         print(request.data)
#     return Response(None, status=status.HTTP_204_NO_CONTENT)


# class EmailThread(threading.Thread):
#     def __init__(self, subject, html_content):
#         self.subject = subject
#         # self.recipient_list = [settings.EMAIL_HOST_USER]
#         self.html_content = html_content
#         threading.Thread.__init__(self)
    
#     def run(self):
#         msg = EmailMessage(self.subject, self.html_content)
#         msg.recipients = [settings.EMAIL_HOST_USER]
#         msg.content_subtype = 'html'
#         msg.send()

# @csrf_exempt
# def send_email(subject, html_content):
# # def send_email(request):
#     # EmailThread(request.data['subject'], request.dat['message']).start()
#     EmailThread(subject, html_content).start()



# class EmailThread(threading.Thread):
#     def __init__(self, subject, html_content, recipient_list, sender):
#         self.subject = subject
#         self.recipient_list = recipient_list
#         self.html_content = html_content
#         self.sender = sender
#         threading.Thread.__init__(self)

#     def run(self):
#         msg = EmailMessage(self.subject, self.html_content, self.sender, self.recipient_list)
#         msg.content_subtype = 'html'
#         msg.send()

# @api_view(['POST'])
# @csrf_exempt
# def send_email(request):
#     EmailThread(request.data['subject'], request.data['message'], request.data['recipient_list'], 'sjbyard91@gmail.com').start()
#     return Response(None, status=status.HTTP_204_NO_CONTENT)
