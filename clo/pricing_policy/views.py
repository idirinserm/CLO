from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .models import PricePolicy
from .serializers import PricePolicySerializer


class PricePolicyViewSet(viewsets.ModelViewSet):
    queryset = PricePolicy.objects.all()
    serializer_class = PricePolicySerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    search_fields = ['hotel', 'day_of_week', 'is_weekend', 'is_single_occupancy', 'price_adjustment']
    filterset_fields = ['hotel', 'day_of_week', 'is_weekend', 'is_single_occupancy', 'price_adjustment']
