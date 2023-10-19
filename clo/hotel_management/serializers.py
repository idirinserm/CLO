from rest_framework import serializers

from service_management.models import Service
from .models import Hotel, Room


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    services = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all(), many=True)

    class Meta:
        model = Room
        fields = '__all__'
