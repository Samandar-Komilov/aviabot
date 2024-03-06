from .serializers import NewsSerializer
from .models import New
from rest_framework import generics, permissions


class NewsList(generics.ListAPIView):
     queryset = New.objects.all()
     serializer_class = NewsSerializer
     permission_classes = [permissions.AllowAny]