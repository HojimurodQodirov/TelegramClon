from django.urls import path
from .views import MessageListCreate, chat_view

urlpatterns = [
    path('messages/', MessageListCreate.as_view(), name='message-list-create'),
    path('chat/', chat_view, name='chat-view'),
]