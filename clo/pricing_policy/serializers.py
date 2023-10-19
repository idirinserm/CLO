from rest_framework import serializers
from .models import PricePolicy


class PricePolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = PricePolicy
        fields = '__all__'
