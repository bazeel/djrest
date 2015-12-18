from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Message
from .serializer import MessageSerializer


class MessageList(APIView):

    def get(self, request, format=None):
        print request.user.id
        messages = Message.objects.filter(user__id=request.user.id, success=True).order_by('-date_sent')
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)
