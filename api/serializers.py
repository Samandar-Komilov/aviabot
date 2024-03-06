from rest_framework import serializers
from .models import New


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ['id', 'title', 'image', 'subtitle', 'created_at']