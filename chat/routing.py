from django.urls import re_path
from .consumers import chatConsumer

websocket_patterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$',chatConsumer.as_asgi()),
]