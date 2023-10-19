from rest_framework import serializers

from service_management.models import Service
from .models import Reservation, EmailConfirmation


class ReservationSerializer(serializers.ModelSerializer):
    additional_services = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all(), many=True)

    class Meta:
        model = Reservation
        fields = '__all__'


class EmailConfirmationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailConfirmation
        fields = '__all__'
