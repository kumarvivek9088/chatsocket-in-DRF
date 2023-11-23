"""
ASGI config for chatweb project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from chat.routing import websocket_patterns
from .custom_auth import CustomAuthMiddleware
# from channels.auth import AuthMiddlewareStack

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatweb.settings')

# application = get_asgi_application()
application = ProtocolTypeRouter(
    {
        "http" : get_asgi_application(),
        "websocket" : AllowedHostsOriginValidator(
            CustomAuthMiddleware(
                URLRouter(
                    websocket_patterns
                )
            )
        )
    }
)
