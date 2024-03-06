from django.shortcuts import redirect
from .serializers import NewsSerializer, UserSerializer
from .models import New
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate


class UserLoginView(APIView):
     def post(self, request):
          username = request.data.get('username')
          password = request.data.get('password')
          user = authenticate(username=username, password=password)
          if user:
               serializer = UserSerializer(user)
               return redirect('/admin/')
          else:
               return Response({'error': 'Invalid credentials!'}, status=status.HTTP_401_UNAUTHORIZED)


class NewsList(generics.ListAPIView):
     queryset = New.objects.all()
     serializer_class = NewsSerializer
     permission_classes = [permissions.AllowAny]