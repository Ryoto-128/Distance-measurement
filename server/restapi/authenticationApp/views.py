from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate
from django.db import transaction
from django.http import HttpResponse, Http404
from rest_framework import authentication, permissions, generics
from rest_framework_jwt.settings import api_settings
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.views import APIView
from .serializer import UserSerializer
from .models import User, UserManager


class UserRegister(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @transaction.atomic
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserGetInfoView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, format=None):
        return Response(data={
            'username': request.user.username,
            'email': request.user.email,
            },
            status=status.HTTP_200_OK)
        
class UserUpdateView(generics.UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer
    lookup_field = 'username'
    queryset = User.objects.all()

    def get_object(self):
        try:
            instance = self.queryset.get(username=self.request.user)
            return instance
        except User.DoesNotExist:
            raise Http404
        
class UserDeleteView(generics.DestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer
    lookup_field = 'username'
    queryset = User.objects.all()

    def get_object(self):
        try:
            instance = self.queryset.get(username=self.request.user)
            return instance
        except User.DoesNotExist:
            raise Http404