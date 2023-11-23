from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from .serializers import userSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import AccessToken,RefreshToken
from rest_framework.response import Response
from django.contrib.auth import authenticate
# Create your views here.

class signup(APIView):
    def post(self,request):
        request.data['password'] = make_password(request.data['password'])
        serializer = userSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=request.data['username'])
            token = AccessToken.for_user(user)
            return Response({"token":str(token),"success": True,"data": serializer.data })
        
        return Response({"error": serializer.error_messages})
            


class signin(APIView):
    def post(self,request):
        user = authenticate(username = request.data['username'], password = request.data['password'])
        if user:
            token = RefreshToken.for_user(user)
            return Response({"success":True, "token": str(token.access_token),"username": request.data['username']})
        
        return Response({"success":False,"message":"username or password is incorrect"})