from django.shortcuts import render
from rest_framework import generics
from .models import Message
from .serializers import MessageSerializer


class MessageListCreate(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


def chat_view(request):
    return render(request, 'chat.html')