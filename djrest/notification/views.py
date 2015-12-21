from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MessageLog
from .serializer import MessageLogSerializer


class MessageLogList(APIView):

    def get(self, request, format=None):
        messages = MessageLog.objects.filter(user__id=request.user.id, success=True).order_by('-date_sent',
                                                                                              '-date_created')
        serializer = MessageLogSerializer(messages, many=True)
        return Response(serializer.data)
