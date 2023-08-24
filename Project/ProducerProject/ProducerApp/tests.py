from django.test import TestCase
from .serializers import MessageSerializer
from .models import  MessageModel
from rest_framework.response import Response
from django.http import request
from rest_framework import status
from .views import MessageSender

class SendMessage(TestCase):
    def send_message(self):
        message = {
            "message":"Deneme"
        }

        serializer = MessageSerializer(data=message)

        if serializer.is_valid():
            try:
                self.assertEqual(status.HTTP_200_OK, "Operation Succsessfull")
                
            except Exception:
                self.assertEqual(status.HTTP_400_BAD_REQUEST ,"Operation Failed")