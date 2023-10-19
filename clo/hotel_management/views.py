from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend

from .models import Hotel, Room
from .serializers import HotelSerializer, RoomSerializer


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    search_fields = ['id', 'name', 'address', 'phone_number']
    filterset_fields = ['id', 'name', 'address', 'phone_number']


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    search_fields = ['name', 'capacity', 'base_rate', 'hotel', 'services']
    filterset_fields = ['name', 'capacity', 'base_rate', 'hotel', 'services']

